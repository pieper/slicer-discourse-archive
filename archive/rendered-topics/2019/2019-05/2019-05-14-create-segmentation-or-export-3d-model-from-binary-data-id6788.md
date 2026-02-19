---
topic_id: 6788
title: "Create Segmentation Or Export 3D Model From Binary Data"
date: 2019-05-14
url: https://discourse.slicer.org/t/6788
---

# Create segmentation or export 3D model from binary data

**Topic ID**: 6788
**Date**: 2019-05-14
**URL**: https://discourse.slicer.org/t/create-segmentation-or-export-3d-model-from-binary-data/6788

---

## Post #1 by @GLA_mod (2019-05-14 17:14 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10<br>
Expected behavior: Segment and export as .obj file<br>
Actual behavior: Can’t segment. Also can’t load as binary labelmap.</p>
<p>I have some microscopy data which has effectively already been segmented into a binary TIFF stack. I want to export the fluorescent regions as an .obj file so I have a 3D model.</p>
<p>I’m not able to select any regions of the data for further segmentation (no threshold range can be selected). I have also tried importing the data as a binary labelmap, but it does not appear to work - I have looked in the Data and Segmentation modules but found no files there.</p>
<p>What am I doing wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd5525a79358c8a0e796b2c2ea0ff30928f2c6bb.jpeg" data-download-href="/uploads/short-url/A95e3ThrjbSCFqk3lG1v1AOlkfh.jpeg?dl=1" title="binary" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd5525a79358c8a0e796b2c2ea0ff30928f2c6bb_2_690x431.jpeg" alt="binary" data-base62-sha1="A95e3ThrjbSCFqk3lG1v1AOlkfh" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd5525a79358c8a0e796b2c2ea0ff30928f2c6bb_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd5525a79358c8a0e796b2c2ea0ff30928f2c6bb_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd5525a79358c8a0e796b2c2ea0ff30928f2c6bb_2_1380x862.jpeg 2x" data-dominant-color="808688"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">binary</span><span class="informations">1680×1050 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-05-14 19:40 UTC)

<p>If this is rgb data you can use the Vector to Scalar Volume module to convert it, then you should be able to use it with the Segment Editor.</p>

---
