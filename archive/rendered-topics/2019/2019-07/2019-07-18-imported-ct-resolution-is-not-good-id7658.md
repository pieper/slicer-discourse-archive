# imported ct resolution is not good

**Topic ID**: 7658
**Date**: 2019-07-18
**URL**: https://discourse.slicer.org/t/imported-ct-resolution-is-not-good/7658

---

## Post #1 by @kisu_mang (2019-07-18 14:05 UTC)

<p>hi…i’m new to 3d slicer . i imported ct images but after imported resolution of R, Y window is not good.</p>
<p>how i can fix ?</p>
<p>i recorded video please help me.</p>
<p>thanks so much!</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1wkCFK_rU__zZdupxoE8MmlB-8xBZSbpO/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh3.googleusercontent.com/6F33K4mrJLxAxQIIIM0h2xstTSSnbv3wzlcLKQeodq2-UFa5EiASlIN6VUU=w1200-h630-p" class="thumbnail"></div>

<h3><a href="https://drive.google.com/file/d/1wkCFK_rU__zZdupxoE8MmlB-8xBZSbpO/view?usp=sharing" target="_blank" rel="nofollow noopener">ctprobelm.wmv (video)</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2019-07-18 15:31 UTC)

<p>Maybe you look at the different loaded volumes with the Data module to find the highest resolution one.</p>

---

## Post #3 by @lassoan (2019-07-19 04:10 UTC)

<p>The study contains 3 volumes, each one is low-resolution along a different axis. You cannot get a single high-resolution volume (<a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">see this topic for details</a>), but if you just want review 2D slices then you can choose to see the series in each of the orthogonal view that has the highest resolution in that particular orientation (click on the push-pin icon in the top-left corner of a slice view to see the volume selector).</p>

---
