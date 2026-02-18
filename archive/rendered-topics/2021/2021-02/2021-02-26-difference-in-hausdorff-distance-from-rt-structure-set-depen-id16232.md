# Difference in Hausdorff distance from RT structure set dependent on Version

**Topic ID**: 16232
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/difference-in-hausdorff-distance-from-rt-structure-set-dependent-on-version/16232

---

## Post #1 by @Matt_B (2021-02-26 10:30 UTC)

<p>I was originally using V4.10.2 and have now changed to V4.11.20200930 and noticed difference in the Hausdorff distance (and DICE) metrics.<br>
In the earlier version importing an RT structure set would allow calculation of the HD however the later version required creation of binary label map in the segmentation module to allow calculation (otherwise an error in ITK conversion is shown).</p>
<p>Is it now not possible to compute HD directly from the RTstructure set without conversion?<br>
Which should be considered the correct value?<br>
The attached image shows calculation results in both versions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d3f95924678717eb3f30ed3bf31c29bf445713f.png" data-download-href="/uploads/short-url/diUDgOJsa404iIFE1pa9ApP8vLh.png?dl=1" title="HD dif" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d3f95924678717eb3f30ed3bf31c29bf445713f_2_690x444.png" alt="HD dif" data-base62-sha1="diUDgOJsa404iIFE1pa9ApP8vLh" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d3f95924678717eb3f30ed3bf31c29bf445713f_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d3f95924678717eb3f30ed3bf31c29bf445713f_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d3f95924678717eb3f30ed3bf31c29bf445713f_2_1380x888.png 2x" data-dominant-color="9DDDA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">HD dif</span><span class="informations">2160×1390 464 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
