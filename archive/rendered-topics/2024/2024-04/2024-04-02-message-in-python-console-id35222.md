---
topic_id: 35222
title: "Message In Python Console"
date: 2024-04-02
url: https://discourse.slicer.org/t/35222
---

# Message in python console

**Topic ID**: 35222
**Date**: 2024-04-02
**URL**: https://discourse.slicer.org/t/message-in-python-console/35222

---

## Post #1 by @DR.DHARAM_SINGH_RATH (2024-04-02 10:23 UTC)

<p>[FD] 2024-04-02 15:49:30.859 Slicer[707:5598] WARNING: Secure coding is not enabled for restorable state! Enable secure coding by implementing NSApplicationDelegate.applicationSupportsSecureRestorableState: and returning YES.<br>
[Qt] Populating font family aliases took 109 ms. Replace uses of missing font family “.AppleSystemUIFont” with one that exists to avoid this cost.</p>
<p>please explain what to enable in easy language as I’m not able to understand.</p>

---

## Post #2 by @pieper (2024-04-02 11:02 UTC)

<p>As far as I know these are just warnings you can ignore.  They should get sorted out in future versions.</p>

---

## Post #3 by @lassoan (2024-04-02 18:16 UTC)

<p>My understanding is that via this message Qt toolkit warns application developers that the application startup could be 0.1 second faster. So, yes, it can be ignored. See some more discussion here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7261">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7261" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7261" target="_blank" rel="noopener">Qt warning about missing font family</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-03" data-time="03:44:03" data-timezone="UTC">03:44AM - 03 Oct 23 UTC</span>
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
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Since the factory machine updates, Slicer-5.4.0 reports this warni<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ng every time Slicer is started:

    Populating font family aliases took 86 ms. Replace uses of missing font family ".AppleSystemUIFont" with one that exists to avoid this cost. 

This was [noticed when the update was done](https://github.com/Slicer/DashboardScripts/pull/53#issuecomment-1396980186), but there was no follow-up.

## Steps to reproduce

Start Slicer-5.4.0 on macOS.

## Expected behavior

No warning should be logged.

## Environment
- Slicer version: Slicer-5.4.0
- Operating system: Mac</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
