---
topic_id: 9856
title: "Manual Segmentation Of Interpolated Mri Images"
date: 2020-01-17
url: https://discourse.slicer.org/t/9856
---

# Manual segmentation of interpolated (MRI) images

**Topic ID**: 9856
**Date**: 2020-01-17
**URL**: https://discourse.slicer.org/t/manual-segmentation-of-interpolated-mri-images/9856

---

## Post #1 by @Dmitriy_Desser (2020-01-17 19:08 UTC)

<p>Hi guys,</p>
<p>in the Volumes module it is possible to check/uncheck interpolation of the image/voxels right?</p>
<p>So not interpolated image looks like e.g. :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d4cefefa7ed120ce239c0fdbe20b2fab534aed6.png" alt="not_interpolated" data-base62-sha1="4bcGp4AemtMI26vJH6AEUsUr96m" width="483" height="405"></p>
<p>Interpolated image looks like:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8543f423f6ec955c964367bcb1d4ddffe0b695bb.png" alt="interpolated" data-base62-sha1="j0V5NY48Dht33WR6QOyPDRUzdLt" width="641" height="434"></p>
<p>But the label/segmentation looks not interpolated…</p>
<p>Is it possible to edit interpolated image?<br>
I mean, I have already tried both ways:</p>
<ol>
<li>Load Volume with checked interpolation first and edit with paint brush<br>
and</li>
<li>Load Volume with unchecked interpolation and edit with paint brush</li>
</ol>
<p>the segmentation looks same way…</p>
<p>Thank you very much!</p>
<p>Best,</p>
<p>Dima</p>

---

## Post #2 by @lassoan (2020-01-17 19:32 UTC)

<p>The “Interpolate” checkbox in Volumes module’s Display section only affects how that particular node is visualized. It does not affect how that volume is processed, segmented, etc. It does not affect any other nodes, e.g., a segmentation node that it is used with.</p>
<p>If the input volume’s resolution is too low to represent all the details you want to segment then you can use “Crop volume” module before segmentation to resample the volume at a finer grid with interpolation (and usually you also want to reduce the extents of the volume to the minimum size, to improve processing speed). Alternatively, you can keep the original volume intact and oversample the segmentation by using the segmentation geometry button on the right side of the master volume node selector in Segment Editor module.</p>

---
