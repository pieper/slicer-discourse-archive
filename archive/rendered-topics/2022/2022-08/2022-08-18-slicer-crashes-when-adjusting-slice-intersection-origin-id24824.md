---
topic_id: 24824
title: "Slicer Crashes When Adjusting Slice Intersection Origin"
date: 2022-08-18
url: https://discourse.slicer.org/t/24824
---

# Slicer crashes when adjusting slice intersection origin

**Topic ID**: 24824
**Date**: 2022-08-18
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-adjusting-slice-intersection-origin/24824

---

## Post #1 by @connorh (2022-08-18 20:40 UTC)

<p>I repeatedly crash slicer when I try to place the origin of my slice intersections on top of markup point (Slicer 5.0.2). Does this happen to anyone else? It is because Slicer is trying to move my fiducial marker any my slice-view origin at the same time and gets confused?</p>
<p>To reproduce:</p>
<ol>
<li>Open dummy image set (e.g. CT Chest)</li>
<li>Place fiducial marker on image</li>
<li>Enable “show how the other slice planes interact” and enable “Interaction”</li>
<li>Click and drag the center of the slice-view origin to over top of the placed fiducial marker</li>
</ol>
<p>In this image below, I can get it close, but if I drag it right overtop it crashes for me every time.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3f0b809243acf34885394407e176c73383552f3.jpeg" data-download-href="/uploads/short-url/rXmQmyZYrvHTMP0EQmvvoKPYGdl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f0b809243acf34885394407e176c73383552f3_2_690x374.jpeg" alt="image" data-base62-sha1="rXmQmyZYrvHTMP0EQmvvoKPYGdl" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f0b809243acf34885394407e176c73383552f3_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f0b809243acf34885394407e176c73383552f3_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3f0b809243acf34885394407e176c73383552f3_2_1380x748.jpeg 2x" data-dominant-color="80818B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1041 87.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2022-08-18 21:29 UTC)

<p>I used Slicer 5.0.3 (latest stable) from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> and did not run into this issue. Please try upgrading from Slicer 5.0.2 to Slicer 5.0.3 as the new version includes the following bug fix which may solve your issue.</p>
<p>Let us know how it goes for you!</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/11dfe7ef9d7ed67fabc8a3e962d11335c0b5f3f0">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/11dfe7ef9d7ed67fabc8a3e962d11335c0b5f3f0" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/11dfe7ef9d7ed67fabc8a3e962d11335c0b5f3f0" target="_blank" rel="noopener nofollow ugc">BUG: Fix interactive slice intersection widget focus handling</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-07-08" data-time="05:19:05" data-timezone="UTC">05:19AM - 08 Jul 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 2 files with 7 additions and 2 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/11dfe7ef9d7ed67fabc8a3e962d11335c0b5f3f0" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+7</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">(cherry picked from commit 457016b3f)

When interactive slice intersection was d<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/11dfe7ef9d7ed67fabc8a3e962d11335c0b5f3f0" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ragged over a markup control point the dragging got interrupted.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
