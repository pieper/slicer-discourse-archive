#!/usr/bin/env python3
"""
Fetch Discourse forum content via the REST API and archive as JSON + Markdown.

Outputs:
  archive/posts/{topic_id}.json         - raw topic JSON
  archive/rendered-topics/YYYY/YYYY-MM/YYYY-MM-DD-slug-idNNN.md - rendered markdown

Usage:
  python scripts/fetch_discourse.py --url https://discourse.slicer.org \
      --api-key YOUR_KEY --api-username YOUR_USERNAME \
      --target-dir ./archive [--since-days 7] [--debug]
"""

import argparse
import json
import re
import time
import os
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import urllib.request
    import urllib.error
    import urllib.parse
    HAS_REQUESTS = False


def make_request(url, api_key=None, api_username=None, debug=False, retry_count=5):
    """Make an HTTP GET request, handling rate limits and retries."""
    headers = {"Accept": "application/json"}
    if api_key:
        headers["Api-Key"] = api_key
        headers["Api-Username"] = api_username or "system"

    for attempt in range(retry_count):
        if debug:
            print(f"  GET {url}", flush=True)
        try:
            if HAS_REQUESTS:
                resp = requests.get(url, headers=headers, timeout=30)
                if resp.status_code == 429:
                    wait = int(resp.headers.get("Retry-After", 60)) + 5
                    print(f"Rate limited, waiting {wait}s...", flush=True)
                    time.sleep(wait)
                    continue
                if resp.status_code == 404:
                    return None
                resp.raise_for_status()
                return resp.json()
            else:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=30) as r:
                    return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            if HAS_REQUESTS and hasattr(e, "response") and e.response is not None:
                if e.response.status_code == 404:
                    return None
            print(f"  Attempt {attempt+1}/{retry_count} failed for {url}: {e}", flush=True)
            if attempt < retry_count - 1:
                time.sleep(5 * (attempt + 1))
    return None


def fetch_topic_with_all_posts(topic_id, base_url, api_key, api_username, debug):
    """Fetch a topic and all its posts (handling pagination)."""
    url = f"{base_url}/t/{topic_id}.json"
    topic = make_request(url, api_key, api_username, debug)
    if not topic:
        return None

    # Discourse returns the first ~20 posts; fetch the rest via post IDs
    stream_ids = topic.get("post_stream", {}).get("stream", [])
    fetched_ids = {p["id"] for p in topic.get("post_stream", {}).get("posts", [])}
    remaining = [sid for sid in stream_ids if sid not in fetched_ids]

    # Batch-fetch remaining posts (up to 300 IDs per request)
    for i in range(0, len(remaining), 300):
        batch = remaining[i : i + 300]
        ids_qs = "&".join(f"post_ids[]={pid}" for pid in batch)
        posts_url = f"{base_url}/t/{topic_id}/posts.json?{ids_qs}"
        posts_data = make_request(posts_url, api_key, api_username, debug)
        if posts_data:
            topic["post_stream"]["posts"].extend(
                posts_data.get("post_stream", {}).get("posts", [])
            )
        time.sleep(0.3)

    return topic


def render_topic_to_markdown(topic):
    """Convert Discourse topic JSON to a Markdown document.

    Emits a YAML frontmatter block including `last_bumped`, which the main
    loop reads on subsequent runs to skip topics whose upstream `bumped_at`
    hasn't changed since they were last fetched.
    """
    title = topic.get("title", "Unknown")
    topic_id = topic.get("id", 0)
    slug = topic.get("slug", f"topic-{topic_id}")
    created_at = topic.get("created_at", "")
    bumped_at = topic.get("bumped_at") or topic.get("last_posted_at") or ""
    try:
        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        date_str = dt.strftime("%Y-%m-%d")
    except Exception:
        date_str = "2000-01-01"

    # Escape double quotes in title for valid YAML.
    yaml_title = title.replace("\"", "\\\"")

    lines = [
        "---",
        f"topic_id: {topic_id}",
        f"title: \"{yaml_title}\"",
        f"date: {date_str}",
        f"url: https://discourse.slicer.org/t/{topic_id}",
        f"last_bumped: {bumped_at}",
        "---",
        "",
        f"# {title}",
        "",
        f"**Topic ID**: {topic_id}",
        f"**Date**: {date_str}",
        f"**URL**: https://discourse.slicer.org/t/{slug}/{topic_id}",
        "",
        "---",
        "",
    ]

    posts = topic.get("post_stream", {}).get("posts", [])
    # Sort by post_number to ensure chronological order
    posts = sorted(posts, key=lambda p: p.get("post_number", 0))

    for post in posts:
        username = post.get("username", "unknown")
        post_num = post.get("post_number", "?")
        post_created = post.get("created_at", "")
        try:
            pdt = datetime.fromisoformat(post_created.replace("Z", "+00:00"))
            post_date = pdt.strftime("%Y-%m-%d %H:%M UTC")
        except Exception:
            post_date = ""
        # Prefer raw markdown source; fall back to HTML cooked content
        body = post.get("raw") or post.get("cooked") or ""
        lines += [
            f"## Post #{post_num} by @{username} ({post_date})",
            "",
            body,
            "",
            "---",
            "",
        ]

    return "\n".join(lines)


def topic_output_paths(topic, target_dir):
    """Return (json_path, md_path) for a topic."""
    topic_id = topic.get("id")
    slug = topic.get("slug", f"topic-{topic_id}")
    created_at = topic.get("created_at", "")
    try:
        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        date_str = dt.strftime("%Y-%m-%d")
        year = dt.strftime("%Y")
        year_month = dt.strftime("%Y-%m")
    except Exception:
        date_str = "2000-01-01"
        year = "2000"
        year_month = "2000-01"

    safe_slug = re.sub(r"[^\w-]", "-", slug)[:60].strip("-")
    filename = f"{date_str}-{safe_slug}-id{topic_id}.md"

    json_path = Path(target_dir) / "posts" / f"{topic_id}.json"
    md_path = Path(target_dir) / "rendered-topics" / year / year_month / filename
    return json_path, md_path


_LAST_BUMPED_RE = re.compile(r"^last_bumped:\s*(\S+)\s*$", re.MULTILINE)
_POST_HEADER_RE = re.compile(r"^## Post #\d+ ", re.MULTILINE)


def local_is_current(md_path, upstream_bumped, upstream_post_count):
    """Return True if the local .md already reflects upstream's latest state.

    Two independent signals, either is sufficient:
      1. last_bumped frontmatter field equals upstream bumped_at. Cheap
         (only the file head matters), and accurate going forward — but
         only works for files written by a version of this script that
         emits last_bumped.
      2. Number of "## Post #N" headers in the local file is >= upstream
         posts_count. Works on legacy files written before last_bumped
         existed, so the first full sweep after introducing this check
         can still skip the ~95% of topics that haven't been bumped since
         they were originally archived.

    Either match means there's nothing new to fetch. If neither matches,
    we don't know the local file is current, so fetch and re-render.
    """
    try:
        content = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False

    if upstream_bumped:
        m = _LAST_BUMPED_RE.search(content[:1024])
        if m and m.group(1) == upstream_bumped:
            return True

    if upstream_post_count and upstream_post_count > 0:
        local_count = sum(1 for _ in _POST_HEADER_RE.finditer(content))
        if local_count >= upstream_post_count:
            return True

    return False


def save_topic(topic, target_dir, save_json=False):
    """Save rendered markdown (and optionally raw JSON).

    Always re-renders when called: the previous "skip if .md exists" check
    silently dropped new replies on bumped topics during incremental runs.
    The API fetch is the expensive step and has already happened by the
    time we reach here — the file write is cheap and idempotent, so just
    do it.
    """
    json_path, md_path = topic_output_paths(topic, target_dir)

    md_path.parent.mkdir(parents=True, exist_ok=True)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(render_topic_to_markdown(topic))

    if save_json:
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(topic, f, ensure_ascii=False, indent=2)


def get_all_topic_ids(base_url, api_key, api_username, _since_dt, debug):
    """
    Page through ALL topics sorted by creation (ascending). Only used for
    true full archives with no date cutoff — use get_recently_updated_topic_ids
    whenever a date window is available, since it stops early.
    """
    page = 0
    seen = set()
    while True:
        url = f"{base_url}/latest.json?order=created&ascending=true&page={page}"
        data = make_request(url, api_key, api_username, debug)
        if not data:
            break

        topic_list = data.get("topic_list", {})
        topics = topic_list.get("topics", [])
        if not topics:
            break

        for t in topics:
            tid = t.get("id")
            if tid in seen:
                continue
            seen.add(tid)
            yield t

        if not topic_list.get("more_topics_url") and len(topics) < 30:
            break

        page += 1
        time.sleep(0.5)


def get_recently_updated_topic_ids(base_url, api_key, api_username, since_dt, debug):
    """
    For incremental updates: page through /latest.json sorted by activity
    and collect topics bumped since since_dt.
    """
    page = 0
    seen = set()
    stop = False
    while not stop:
        url = f"{base_url}/latest.json?page={page}"
        data = make_request(url, api_key, api_username, debug)
        if not data:
            break

        topic_list = data.get("topic_list", {})
        topics = topic_list.get("topics", [])
        if not topics:
            break

        for t in topics:
            tid = t.get("id")
            if tid in seen:
                continue
            seen.add(tid)
            bumped_at = t.get("bumped_at") or t.get("last_posted_at") or ""
            try:
                dt = datetime.fromisoformat(bumped_at.replace("Z", "+00:00"))
            except Exception:
                dt = datetime.min.replace(tzinfo=timezone.utc)

            if dt < since_dt:
                stop = True  # rest of list is older
                break
            yield t

        if not topic_list.get("more_topics_url") and len(topics) < 30:
            break
        page += 1
        time.sleep(0.5)


def load_state(target_dir):
    """Load last-run state from disk."""
    state_file = Path(target_dir) / ".archive_state.json"
    if state_file.exists():
        try:
            return json.loads(state_file.read_text())
        except Exception:
            pass
    return {}


def save_state(target_dir, state):
    """Persist state to disk."""
    state_file = Path(target_dir) / ".archive_state.json"
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Archive a Discourse forum via API")
    parser.add_argument("--url", default="https://discourse.slicer.org",
                        help="Base URL of the Discourse instance")
    parser.add_argument("--api-key", default=os.environ.get("DISCOURSE_API_KEY"),
                        help="Discourse API key (or set DISCOURSE_API_KEY env var)")
    parser.add_argument("--api-username", default=os.environ.get("DISCOURSE_API_USERNAME", "system"),
                        help="Discourse API username (or set DISCOURSE_API_USERNAME env var)")
    parser.add_argument("--target-dir", default="./archive",
                        help="Directory to write archive files into")
    parser.add_argument("--since-days", type=int, default=None,
                        help="Only fetch topics active in the last N days "
                             "(omit for full archive on first run, then auto-incremental)")
    parser.add_argument("--full", action="store_true",
                        help="Force a full re-archive (ignore previous state)")
    parser.add_argument("--save-json", action="store_true",
                        help="Also save raw topic JSON to archive/posts/ "
                             "(adds ~800 MB for a full archive; markdown-only is the default)")
    parser.add_argument("--debug", action="store_true",
                        help="Print each API request URL")
    args = parser.parse_args()

    base_url = args.url.rstrip("/")
    target_dir = Path(args.target_dir)

    if not args.api_key:
        print("WARNING: No API key provided. Requests will be anonymous and rate-limited.")
        print("Set --api-key or DISCOURSE_API_KEY env var for better performance.")

    # Determine date cutoff
    state = load_state(target_dir)
    last_run_str = state.get("last_run")

    if args.since_days is not None:
        # Explicit date window always wins
        since_dt = datetime.now(timezone.utc) - timedelta(days=args.since_days)
        print(f"Fetching topics active in the last {args.since_days} day(s) (since {since_dt.date()})")
    elif not args.full and last_run_str:
        # Incremental: resume from last run with a 1-hour buffer
        last_run = datetime.fromisoformat(last_run_str)
        since_dt = last_run - timedelta(hours=1)
        print(f"Incremental fetch: topics updated since {since_dt.isoformat()}")
    else:
        since_dt = None
        print("Full fetch mode: fetching ALL topics (this may take a long time)")

    run_start = datetime.now(timezone.utc)

    # Choose iteration strategy:
    # - Any date cutoff → scan descending from latest and stop early (efficient)
    # - No date cutoff  → full ascending scan of every page (true full archive)
    if since_dt is not None:
        topic_iter = get_recently_updated_topic_ids(
            base_url, args.api_key, args.api_username, since_dt, args.debug
        )
    else:
        topic_iter = get_all_topic_ids(
            base_url, args.api_key, args.api_username, since_dt, args.debug
        )

    saved = 0
    skipped = 0
    errors = 0

    for topic_summary in topic_iter:
        tid = topic_summary["id"]
        title = topic_summary.get("title", "")

        # Cheap skip: if local already reflects upstream's latest state,
        # avoid the per-topic API call entirely. /latest.json gives us
        # bumped_at and posts_count in the summary, so this works for both
        # newly-rendered files (via last_bumped frontmatter) and legacy
        # files (via post-header count). Massive speedup on full-archive
        # runs since ~95% of topics haven't been bumped recently.
        upstream_bumped = topic_summary.get("bumped_at")
        upstream_post_count = topic_summary.get("posts_count")
        _, md_path = topic_output_paths(topic_summary, target_dir)
        if md_path.exists() and local_is_current(
            md_path, upstream_bumped, upstream_post_count
        ):
            skipped += 1
            continue

        print(f"Fetching topic {tid}: {title[:60]}", flush=True)

        try:
            topic = fetch_topic_with_all_posts(
                tid, base_url, args.api_key, args.api_username, args.debug
            )
            if not topic:
                print(f"  Skipped (not found or private)")
                skipped += 1
                continue

            save_topic(topic, target_dir, save_json=args.save_json)
            saved += 1
            print(f"  Saved ({len(topic.get('post_stream',{}).get('posts',[]))} posts)")

        except Exception as e:
            print(f"  ERROR: {e}", flush=True)
            errors += 1

        time.sleep(0.5)  # polite delay between topics

    # Update state
    state["last_run"] = run_start.isoformat()
    save_state(target_dir, state)

    print(f"\nDone. Saved: {saved}, Skipped: {skipped}, Errors: {errors}")
    if errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
