---
topic_id: 36621
title: "How To Load 3Ddose File With Slicerrt Extensions"
date: 2024-06-06
url: https://discourse.slicer.org/t/36621
---

# How to load .3ddose file with SlicerRT extensions

**Topic ID**: 36621
**Date**: 2024-06-06
**URL**: https://discourse.slicer.org/t/how-to-load-3ddose-file-with-slicerrt-extensions/36621

---

## Post #1 by @JamsNeroc (2024-06-06 12:32 UTC)

<p>Hello everyone.<br>
﻿<br>
It could be found that many topics had successfully load 3ddose file with SlicerRT extensions, and <a class="mention" href="/u/cpinter">@cpinter</a> had also mentioned that “after you install the SlicerRT extension from the Extension Manager, you can load 3ddose files using drag&amp;drop or the load file menu”<br>
﻿<br>
However, error would occur when I tried to load 3ddose file by the ways mention above, as the snapshot shown.<br>
﻿<br>
Looking forward your help.<br>
Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f075aff10b3a6850fb4b73050845205ec336a61.png" data-download-href="/uploads/short-url/i7KoETwGsoClZglf5jVmTm8fr3P.png?dl=1" title="1717656818996" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f075aff10b3a6850fb4b73050845205ec336a61_2_690x375.png" alt="1717656818996" data-base62-sha1="i7KoETwGsoClZglf5jVmTm8fr3P" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f075aff10b3a6850fb4b73050845205ec336a61_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f075aff10b3a6850fb4b73050845205ec336a61_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f075aff10b3a6850fb4b73050845205ec336a61_2_1380x750.png 2x" data-dominant-color="B2B1BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1717656818996</span><span class="informations">1928×1048 84.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-06 12:32 UTC)

<p>Please use the latest Slicer Stable Release or latest Slicer Preview Release.</p>

---

## Post #3 by @JamsNeroc (2024-06-07 06:12 UTC)

<p>Thanks for your advice.</p>
<p>I re-install the latest stable Slicer (version 5.6.2) and then it could successfully load 3ddose file.</p>
<p>Although I have no idea why it would work but it doesn’t matter.</p>

---

## Post #4 by @cpinter (2024-06-07 09:16 UTC)

<p>Because we fixed it in January when other people had the same problem:</p><aside class="quote quote-modified" data-post="1" data-topic="34265">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sieunmiin96/48/67738_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-open-vff-file/34265">Unable to open vff file</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have Slicer 5.6.1, but I’m unable to open the vff file despite having the SlicerRT extension installed. The following is the error log: 
LoadVffFile: The values for the origin must each be greater than or equal to 0. 
LoadVffFile: Incorrect parameters or required parameters that were not set, vff file failed to load. The required parameters are: rank, type, format, bits, bands, size, spacing, origin, rawsize, data scale, data offset, and title. 
Warning: In vtkSlicerVffFileReaderLogic.cxx, lin…
  </blockquote>
</aside>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerRt/SlicerRT/commit/3fb93b870bf8f12cfb2b2e0062534e4045468253">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/commit/3fb93b870bf8f12cfb2b2e0062534e4045468253" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/commit/3fb93b870bf8f12cfb2b2e0062534e4045468253" target="_blank" rel="noopener">ENH: Relax condition for positive origin coordinates in Vff reading</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-02-16" data-time="11:42:56" data-timezone="UTC">11:42AM - 16 Feb 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener">
          <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>

      <div class="lines" title="changed 1 files with 0 additions and 5 deletions">
        <a href="https://github.com/SlicerRt/SlicerRT/commit/3fb93b870bf8f12cfb2b2e0062534e4045468253" target="_blank" rel="noopener">
          <span class="added">+0</span>
          <span class="removed">-5</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Re #241</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It’s always a good idea to search the forum first.</p>

---

## Post #5 by @JamsNeroc (2024-06-11 00:34 UTC)

<p>Thank you very much for the explanation.<br>
I will search the forum first if the problem come out.</p>

---
