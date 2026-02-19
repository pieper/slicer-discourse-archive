---
topic_id: 25968
title: "Slicer Doesnt Load"
date: 2022-10-29
url: https://discourse.slicer.org/t/25968
---

# Slicer doesn't load

**Topic ID**: 25968
**Date**: 2022-10-29
**URL**: https://discourse.slicer.org/t/slicer-doesnt-load/25968

---

## Post #1 by @scorpo_901 (2022-10-29 20:18 UTC)

<p>Hello, my slicer was working very well with blender, now I double click on the slicer.exe and it isn’t working.<br>
I tried to uninstall and reinstall it, it worked for a day, then the same problem recurred.<br>
Did any one face a similar issue and how to resolve it.</p>

---

## Post #2 by @lassoan (2022-10-29 20:21 UTC)

<p>Do you have multiple displays? Is this a Dell PC?</p>
<p>It sounds like this display driver issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6568">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6568" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6568" target="_blank" rel="noopener">Application hang at startup in multi-monitor configuration on Windows</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-10-07" data-time="17:54:53" data-timezone="UTC">05:54PM - 07 Oct 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

A few users reported over the years that on Windows computers with<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> multiple displays, Slicer suddenly does not start (does not appear or hangs at startup). 

## Steps to reproduce

It is not clear what steps are needed to reproduce the issue. Having multiple displays connected (at least at some point) is involved.

## Workaround

Deleting Slicer.ini fixes the issue. It may return after changing Slicer position or connecting/disconnecting displays.

## Environment
- Slicer version: observed as early as Slicer-4.11, happens with latest Slicer-5.1 release, too
- Operating system: Windows only</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2022-10-30 12:02 UTC)

<p>5 posts were split to a new topic: <a href="/t/slow-application-start-if-recently-used-file-is-on-unavailable-network/25970">Slow application start if recently used file is on unavailable network</a></p>

---
