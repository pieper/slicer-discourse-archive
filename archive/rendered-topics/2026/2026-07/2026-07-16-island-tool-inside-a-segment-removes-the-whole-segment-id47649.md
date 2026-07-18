---
topic_id: 47649
title: "Island tool inside a segment removes the whole segment"
date: 2026-07-16
url: https://discourse.slicer.org/t/47649
last_bumped: 2026-07-17T15:57:11.042Z
---

# Island tool inside a segment removes the whole segment

**Topic ID**: 47649
**Date**: 2026-07-16
**URL**: https://discourse.slicer.org/t/island-tool-inside-a-segment-removes-the-whole-segment/47649

---

## Post #1 by @muratmaga (2026-07-16 23:02 UTC)

<p>I want to remove these small specs left after a boolean. So I restricted the editable area to inside that specific segment, and then tried to use the island tools remove small islands with really small island size (like 10 voxel). It removed the whole segment.</p>
<p>Is this normal? What’s the combination of options for me to do that?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a.jpeg" data-download-href="/uploads/short-url/2Bktzqf6sbjfrOjYRxqjZH5jXBw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_690x416.jpeg" alt="image" data-base62-sha1="2Bktzqf6sbjfrOjYRxqjZH5jXBw" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/123c9f494042fa3e5759143c75b88036297f681a_2_1380x832.jpeg 2x" data-dominant-color="60605E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-07-17 02:37 UTC)

<p>This feels like a bug to me. Because when I used the “Keep Selected Island” with the same masking options it completed successfully.</p>

---

## Post #3 by @hherhold (2026-07-17 12:34 UTC)

<p>I have noticed this type of behavior too, but wasn’t really able to nail down exactly what was happening. I wound up just doing keep selected island as well, or making a new segment and adding large islands by clicking on them using “add island”. I’m glad you noticed it too, I kinda felt like it was a bug but figured it was my masking settings or something.</p>

---

## Post #4 by @lassoan (2026-07-17 15:26 UTC)

<p>I could reproduce the problem (it is due to the input segment is deleted at the beginning of the splitting, which invalidates the editable area). I have a fix (reorder the operations to keep the original segment around until the end) and will submit a pull request soon.</p>
<p>Until the fix is ready, you can use “Remove small islands”, setting “Editable area” to the current segment is redundant, as only the current segment is modified by this operation anyway.</p>

---

## Post #5 by @lassoan (2026-07-17 15:41 UTC)

<p>Here is the pull request with the fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9292">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9292" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9292" target="_blank" rel="noopener">BUG: Fix Islands effect clearing whole segment with editable area masking (#9292)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:fix-islands-editable-area-masking</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-07-17" data-time="15:41:03" data-timezone="UTC">03:41PM - 17 Jul 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 61 additions and 54 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9292/files" target="_blank" rel="noopener">
            <span class="added">+61</span>
            <span class="removed">-54</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Problem: Islands effect cleared the current segment when editable area was set t<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9292" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">o the current segment (https://discourse.slicer.org/t/island-tool-inside-a-segment-removes-the-whole-segment/47649).

Root cause: The Islands effect operations (Remove small islands, Keep largest island, Split islands to segments) erased the selected segment first and then added the surviving islands back. When the editable area was restricted to the current segment, the editable mask is regenerated from that segment on every modification, so once the segment was erased the editable area became empty and the islands could no longer be written back - clearing the entire segment.

Fix: Do not erase the segment up front. For the split operation, fill the new per-island segments first (while the selected segment still defines a full editable area), then replace the selected segment content last with a single Set operation. The empty result case (e.g. all islands smaller than the minimum size) is handled explicitly.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @muratmaga (2026-07-17 15:57 UTC)

<p>Thanks Andras. I use masking and editable area quite often, because even as a veteran user I get confused about which effects are global vs which ones are segment specific.</p>

---
