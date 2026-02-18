# Edges in 3d volume

**Topic ID**: 4921
**Date**: 2018-11-30
**URL**: https://discourse.slicer.org/t/edges-in-3d-volume/4921

---

## Post #1 by @sarvpriya1985 (2018-11-30 23:05 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.10<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,<br>
Would appreciate thoughts on how to deal with edges in 3d volume after segmentation. I have seen these on few cases of mine now and don’t know how to get rid of them.</p>
<p>Attaching a sample here.</p>
<p>Thanks,<br>
Sarv<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca11618d0742a662af03e00fa5c46c8746db9778.jpeg" data-download-href="/uploads/short-url/sPzGDOiJjHBQ12a0HXX1fDqU4xG.jpeg?dl=1" title="Edges" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca11618d0742a662af03e00fa5c46c8746db9778_2_463x500.jpeg" alt="Edges" data-base62-sha1="sPzGDOiJjHBQ12a0HXX1fDqU4xG" width="463" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca11618d0742a662af03e00fa5c46c8746db9778_2_463x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ca11618d0742a662af03e00fa5c46c8746db9778_2_694x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca11618d0742a662af03e00fa5c46c8746db9778.jpeg 2x" data-dominant-color="999490"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Edges</span><span class="informations">740×799 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-11-30 23:20 UTC)

<p>You see the stripes because your volume has highly anisotropic spacing. I would recommend to crop and resample your volume to have isotropic spacing using <em>Crop volume</em>  module.</p>

---

## Post #3 by @sarvpriya1985 (2018-12-01 14:33 UTC)

<p>Thanks a lot. I fixed that and it came perfect.</p>
<p>Will keep posted.</p>
<p>Sarv</p>

---
