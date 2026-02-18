# Missing module: Hausdorff distances, Dice similarity metrics

**Topic ID**: 22159
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/missing-module-hausdorff-distances-dice-similarity-metrics/22159

---

## Post #1 by @Young_Wang (2022-02-24 15:27 UTC)

<p>Hi there, I’m tyring to calculate the Hausdorff distances, Dice similarity metrics to quantify registration results. However I noticed that <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison" rel="noopener nofollow ugc">SegmentComparison</a> module here is missing. I wonder is there an alternative or replacement for this module?</p>

---

## Post #2 by @cpinter (2022-02-25 09:36 UTC)

<p>You need to install the SlicerRT extension.</p>

---

## Post #3 by @Young_Wang (2022-02-25 12:41 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> thanks for getting back to me. I am using slicer version 4.13.0 revision 30643 built 2022-02-24.<br>
I can’t find the SlicerRT extension in the extension manager.</p>

---

## Post #4 by @Young_Wang (2022-02-25 16:17 UTC)

<p>hi <a class="mention" href="/u/cpinter">@cpinter</a> I just realized that the SlicerRT extension can only be found in the extension manager for the stable release. i.e. version 4.11.20210226 revision 29738 built 2021-02-28.</p>
<p>After I switched slicer to the stable release I was able to install the SlicerRT extension.</p>

---

## Post #5 by @cpinter (2022-02-25 20:23 UTC)

<aside class="quote no-group" data-username="Young_Wang" data-post="4" data-topic="22159">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>can only be found in the extension manager for the stable release</p>
</blockquote>
</aside>
<p>It has failed only in the past two days on Windows and Mac. So you can download the SlicerRT extension on those platforms for the nightly that are older than two days:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://download.slicer.org/?offset=-3">
  <header class="source">
      <img src="https://slicer.org/assets/favicons/favicon-32x32.png?v=Gv63MLlwnz" class="site-icon" width="" height="">

      <a href="https://download.slicer.org/?offset=-3" target="_blank" rel="noopener">3D Slicer</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://slicer.org/assets/img/3d-slicer-128x128.png" class="thumbnail">

<h3><a href="https://download.slicer.org/?offset=-3" target="_blank" rel="noopener">Download 3D Slicer</a></h3>

  <p>3D Slicer is a free, open source software for visualization, processing, segmentation, registration, and analysis of medical, biomedical, and other 3D images and meshes; and planning and navigating image-guided procedures.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
