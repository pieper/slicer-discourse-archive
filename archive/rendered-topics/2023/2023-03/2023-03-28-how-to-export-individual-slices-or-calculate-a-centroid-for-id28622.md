---
topic_id: 28622
title: "How To Export Individual Slices Or Calculate A Centroid For"
date: 2023-03-28
url: https://discourse.slicer.org/t/28622
---

# How to export individual slices or calculate a centroid for each slice of a segmentation?

**Topic ID**: 28622
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/how-to-export-individual-slices-or-calculate-a-centroid-for-each-slice-of-a-segmentation/28622

---

## Post #1 by @Melanie (2023-03-28 12:37 UTC)

<p>I have some medical images, saved as .nrrd files. (segmented)</p>
<p>I would like to calculate the centroid for each slice along a single axis. (Entire segmnet is currently aligned)</p>
<p>Then create a line of best fit for this.</p>
<p>Any suggestions for this please,(I am very much a beginner  and not of engineering background.)</p>
<p>Alternatively if I can export single slices as .png I think there is some function in matlab to do that. I am not sure how to export  png files each slice. I use Mac with Mac OS 11.</p>
<p>Slicer 4.11</p>
<p>Thanks heaps</p>

---

## Post #2 by @lassoan (2023-03-28 14:00 UTC)

<p>You can get the segmentation as a 3D voxel array and access each slice using indexing. But most likely you will not need to deal with such low-level operations.</p>
<p>What is your overall goal? Would you like to extract the centerline of a segmented structure? Have you tried the <a href="https://github.com/vmtk/SlicerExtension-VMTK#the-vmtk-extension-for-3d-slicer">VMTK extension for this</a> or <a href="https://github.com/jmhuie/Slicer-SegmentGeometry#segmentgeometry">SegmentGeometry</a> extensions?</p>

---

## Post #3 by @Melanie (2023-03-29 07:01 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I think segment geometry extension has it,</p>
<p>Yes, I would lilke to extract the centreline of the structure,<br>
Based on centroid of every slice of the segmentation.</p>
<p>So I selcetd computations  as centroid (screenshot), I think Cx and Cy is the x and y coordinates of the centroid for each slice. Is that correct?</p>
<p>But I place a fiducialmarker the possible centroid, on a particlar slice, I get different coordinates for the marker,<br>
I think the module does what I want but I am not interpreting it correctly. Could  you pls advice.<br>
Also how can I draw a best fit line for the series of centroids pls</p>
<p>Thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0adefadc457c9c6e565a9cf0a75e574747c6187.png" data-download-href="/uploads/short-url/w3BBP67tKG8foAhyEW3CmApoWQT.png?dl=1" title="Screen Shot 2023-03-29 at 5.31.11 pm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0adefadc457c9c6e565a9cf0a75e574747c6187_2_690x396.png" alt="Screen Shot 2023-03-29 at 5.31.11 pm" data-base62-sha1="w3BBP67tKG8foAhyEW3CmApoWQT" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0adefadc457c9c6e565a9cf0a75e574747c6187_2_690x396.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0adefadc457c9c6e565a9cf0a75e574747c6187_2_1035x594.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0adefadc457c9c6e565a9cf0a75e574747c6187_2_1380x792.png 2x" data-dominant-color="C3C3C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-29 at 5.31.11 pm</span><span class="informations">1485×854 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-03-30 15:33 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="3" data-topic="28622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>So I selcetd computations as centroid (screenshot), I think Cx and Cy is the x and y coordinates of the centroid for each slice. Is that correct?</p>
</blockquote>
</aside>
<p>See <a href="https://github.com/jmhuie/Slicer-SegmentGeometry#output-details">documentation</a>:</p>
<blockquote>
<ul>
<li>Cx: Centroid x-coordinates that correspond to the resampled and cropped volume exported by SegmentGeometry. Presented in IJK format.</li>
<li>Cy: Centroid y-coordinates that correspond to the resampled and cropped volume exported by SegmentGeometry. Presented in IJK format.</li>
</ul>
</blockquote>
<p>IJK refers to voxels coordinates. You can compute world (RAS) coordinates from voxel coordinates of a volume as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-markup-control-point-ras-coordinates-from-volume-voxel-coordinates">this example</a>.</p>
<aside class="quote no-group" data-username="Melanie" data-post="3" data-topic="28622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Also how can I draw a best fit line for the series of centroids pls</p>
</blockquote>
</aside>
<p>You can compute best fit line using SVD (see example in <a href="https://github.com/SlicerHeart/SlicerHeart/blob/bb7a14a48f52dad67142ff14339e23761e1829aa/ValveAnnulusAnalysis/HeartValveLib/ValveModel.py#L1399-L1435">SlicerHeart</a>). You can draw the computed line using a line markup.</p>

---

## Post #5 by @Melanie (2023-04-01 03:48 UTC)

<p>Thanks very much <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Works well</p>

---
