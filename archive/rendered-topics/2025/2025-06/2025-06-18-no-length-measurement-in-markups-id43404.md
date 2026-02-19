---
topic_id: 43404
title: "No Length Measurement In Markups"
date: 2025-06-18
url: https://discourse.slicer.org/t/43404
---

# No length measurement in markups

**Topic ID**: 43404
**Date**: 2025-06-18
**URL**: https://discourse.slicer.org/t/no-length-measurement-in-markups/43404

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-06-18 07:34 UTC)

<p>Hi to everyone. Today working with the markups module I wanted to measure some segments, but when I create the markups, they do not show the length property (see picture). In curves, other properties like curvature and torsion were computed fine.</p>
<p>My slicer version is 5.6.2 in windows 11.</p>
<p>PD: I have tried to uninstall the extensions related with markups and then re-install it but nothing happens.</p>

---

## Post #2 by @jamesobutler (2025-06-18 10:41 UTC)

<p>I suspect this was already fixed in the following commit which was originally included with the Slicer 5.8.0 stable release:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/39ff123f94df4b2600efe21a149a6e9dbb73d333">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/39ff123f94df4b2600efe21a149a6e9dbb73d333" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/39ff123f94df4b2600efe21a149a6e9dbb73d333" target="_blank" rel="noopener nofollow ugc">BUG: Fix copying of markup measurements</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-10-28" data-time="02:21:20" data-timezone="UTC">02:21AM - 28 Oct 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/39ff123f94df4b2600efe21a149a6e9dbb73d333" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When markup node content was copied, input node for measurements was not set cor<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/39ff123f94df4b2600efe21a149a6e9dbb73d333" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">rectly.

fixes #7239</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please try again with the latest stable which you can get at <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.</p>

---

## Post #3 by @jamesobutler (2025-06-18 10:51 UTC)

<p>SlicerMorph removed its undo enabled functionality for markup line nodes to avoid this missing measurement issue (see linked commit below), but it appears they no longer what have to do so. FYI <a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/commit/248235d5814e8cb91d709598658971d4753d35f9">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/commit/248235d5814e8cb91d709598658971d4753d35f9" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerMorph/SlicerMorph/commit/248235d5814e8cb91d709598658971d4753d35f9" target="_blank" rel="noopener nofollow ugc">Update undo function</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-09-21" data-time="16:27:41" data-timezone="UTC">04:27PM - 21 Sep 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/smrolfe" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/43060230?v=4" class="onebox-avatar-inline" width="20" height="20">
          smrolfe
        </a>
      </div>

      <div class="lines" title="changed 1 files with 0 additions and 6 deletions">
        <a href="https://github.com/SlicerMorph/SlicerMorph/commit/248235d5814e8cb91d709598658971d4753d35f9" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+0</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Only allow undo for point lists</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
