---
topic_id: 26054
title: "Image Quality Decreased When Loading Into 3D Slicer"
date: 2022-11-03
url: https://discourse.slicer.org/t/26054
---

# Image quality decreased when loading into 3D slicer

**Topic ID**: 26054
**Date**: 2022-11-03
**URL**: https://discourse.slicer.org/t/image-quality-decreased-when-loading-into-3d-slicer/26054

---

## Post #1 by @LIE_CAI (2022-11-03 16:03 UTC)

<p>When I use other image viewer of a mammography image, it shows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db1f37b766c75481aa829ee0731f32fa34bc59c3.jpeg" data-download-href="/uploads/short-url/vgrrRWOqeJEOnukAEMFlbZzyfMD.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db1f37b766c75481aa829ee0731f32fa34bc59c3_2_285x500.jpeg" alt="捕获" data-base62-sha1="vgrrRWOqeJEOnukAEMFlbZzyfMD" width="285" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db1f37b766c75481aa829ee0731f32fa34bc59c3_2_285x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db1f37b766c75481aa829ee0731f32fa34bc59c3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db1f37b766c75481aa829ee0731f32fa34bc59c3.jpeg 2x" data-dominant-color="333333"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">304×533 16.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
But when loading the same image into 3D slicer, it shows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d10ff87f04a6c1cdc00fcd52548f23d8c517b50.jpeg" data-download-href="/uploads/short-url/6qFU5c4K8lAWyYS3QQrPWAoe5DW.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d10ff87f04a6c1cdc00fcd52548f23d8c517b50_2_259x500.jpeg" alt="2" data-base62-sha1="6qFU5c4K8lAWyYS3QQrPWAoe5DW" width="259" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d10ff87f04a6c1cdc00fcd52548f23d8c517b50_2_259x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d10ff87f04a6c1cdc00fcd52548f23d8c517b50.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d10ff87f04a6c1cdc00fcd52548f23d8c517b50.jpeg 2x" data-dominant-color="757575"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">277×533 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This would obviously have negative influence on doing segmentation.<br>
Any solutions?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @pieper (2022-11-03 16:08 UTC)

<p>The pixel data should be identical even if the initial display is not the same.  You can zoom to see the resolution of the data and you can change the lookup table to Inverted Gray in the Volumes module and adjust window/level and you should get identical results.  If you still see differences share some (deidentified) data that demonstrates your concerns.</p>

---
