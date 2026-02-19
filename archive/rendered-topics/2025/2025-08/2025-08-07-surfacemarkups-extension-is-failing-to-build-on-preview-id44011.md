---
topic_id: 44011
title: "Surfacemarkups Extension Is Failing To Build On Preview"
date: 2025-08-07
url: https://discourse.slicer.org/t/44011
---

# surfaceMarkups extension is failing to build on Preview

**Topic ID**: 44011
**Date**: 2025-08-07
**URL**: https://discourse.slicer.org/t/surfacemarkups-extension-is-failing-to-build-on-preview/44011

---

## Post #1 by @muratmaga (2025-08-07 19:23 UTC)

<p>Seems across all the platforms. We do rely on that for a functionality in SlicerMorph, so I wanted to see if this is related to latest python changes.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @pieper (2025-08-07 19:55 UTC)

<p>Should be just a matter of fixing the overloaded virtual method.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/builds/3887623">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://slicer.cdash.org/builds/3887623" target="_blank" rel="noopener">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/builds/3887623" target="_blank" rel="noopener">SlicerPreview - Build Summary</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/559dce8b1fb10ad3b9e664b56a96355ac3ad16b3">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/559dce8b1fb10ad3b9e664b56a96355ac3ad16b3" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/559dce8b1fb10ad3b9e664b56a96355ac3ad16b3" target="_blank" rel="noopener">ENH: Create node type display name for GUI usage</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-12-10" data-time="22:56:32" data-timezone="UTC">10:56PM - 10 Dec 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="changed 15 files with 42 additions and 13 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/559dce8b1fb10ad3b9e664b56a96355ac3ad16b3" target="_blank" rel="noopener">
          <span class="added">+42</span>
          <span class="removed">-13</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">GetMarkupTypeDisplayName has been generalized to GetTypeDisplayName so any node <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/559dce8b1fb10ad3b9e664b56a96355ac3ad16b3" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">type can be given a more appropriate and translatable name for use in the GUI.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @cpinter (2025-08-08 09:00 UTC)

<p>I pushed a fix, the extension should be back in the next preview.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerHeart/SlicerSurfaceMarkup/commit/7b4b4d5c39b06f2ab512c728db04b73a473749b7">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup/commit/7b4b4d5c39b06f2ab512c728db04b73a473749b7" target="_blank" rel="noopener">github.com/SlicerHeart/SlicerSurfaceMarkup</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup/commit/7b4b4d5c39b06f2ab512c728db04b73a473749b7" target="_blank" rel="noopener">COMP: Fix build that failed due to Slicer API changes</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2025-08-08" data-time="09:00:07" data-timezone="UTC">09:00AM - 08 Aug 25 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>

      <div class="lines" title="changed 2 files with 3 additions and 7 deletions">
        <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup/commit/7b4b4d5c39b06f2ab512c728db04b73a473749b7" target="_blank" rel="noopener">
          <span class="added">+3</span>
          <span class="removed">-7</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Re https://discourse.slicer.org/t/surfacemarkups-extension-is-failing-to-build-o<span class="show-more-container"><a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup/commit/7b4b4d5c39b06f2ab512c728db04b73a473749b7" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">n-preview/44011</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @muratmaga (2025-08-09 20:28 UTC)

<p>Confirmed the fix. Thank you <a class="mention" href="/u/cpinter">@cpinter</a></p>

---
