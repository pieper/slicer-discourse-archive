# .vtp to segmentation & load segmentation in Python

**Topic ID**: 2883
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/vtp-to-segmentation-load-segmentation-in-python/2883

---

## Post #1 by @trnhx001 (2018-05-22 17:37 UTC)

<p>Hi,</p>
<p>I saved my segmentation as .vtp. Is there anyway to convert it back to Segmentation (.nrrd probably) in python or using 3D Slicers existing tools.</p>
<p>Moreover, I am trying to load segmentation data into 3D matrix in Python for analysis with the volume I used to do the segmentation.</p>
<p>I wonder if these can be done. Thank you for all of your help.</p>

---

## Post #2 by @lassoan (2018-05-22 18:20 UTC)

<aside class="quote no-group" data-username="trnhx001" data-post="1" data-topic="2883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ed655f/48.png" class="avatar"> trnhx001:</div>
<blockquote>
<p>I saved my segmentation as .vtp. Is there anyway to convert it back to Segmentation (.nrrd probably) in python or using 3D Slicers existing tools.</p>
</blockquote>
</aside>
<p>You can use Import section of Segmentations module. You can specify spacing, axis direction, and origin position by choose a reference volume (click on Representations / Binary labelmap / Update, then click the conversion path, and click “Set geometry from volume”; you may enter oversampling factor &gt; 1 to increase resolution).</p>
<aside class="quote no-group" data-username="trnhx001" data-post="1" data-topic="2883">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ed655f/48.png" class="avatar"> trnhx001:</div>
<blockquote>
<p>I am trying to load segmentation data into 3D matrix in Python for analysis with the volume I used to do the segmentation.</p>
</blockquote>
</aside>
<p>You can get voxels of a segment as a numpy array using <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L810-L815"><code>slicer.util.arrayFromSegment</code></a>. You can also export the entire segmentation to a labelmap volume and access its voxels using <code>slicer.util.arrayFromVolume</code>.</p>

---
