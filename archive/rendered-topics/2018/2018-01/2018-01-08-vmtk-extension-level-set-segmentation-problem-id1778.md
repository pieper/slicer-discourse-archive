---
topic_id: 1778
title: "Vmtk Extension Level Set Segmentation Problem"
date: 2018-01-08
url: https://discourse.slicer.org/t/1778
---

# VMTK extension- Level Set Segmentation problem

**Topic ID**: 1778
**Date**: 2018-01-08
**URL**: https://discourse.slicer.org/t/vmtk-extension-level-set-segmentation-problem/1778

---

## Post #1 by @Ella (2018-01-08 01:17 UTC)

<p>I have downloaded the SlicerVMTK extension and followed this tutorial: <a href="https://www.youtube.com/watch?v=DJ2032yo5Co" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=DJ2032yo5Co</a> to extract a model of the Trachea and Bronchi from my DICOM images.</p>
<p>However when I get up to the Level set segmentation it doesn’t seem to work, below is a screenshot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd2f15238aeeb0ae710764ef1d1096928d20522.jpeg" data-download-href="/uploads/short-url/keDgu7nvYr8zFD6GyXdbyXX7hZ0.jpeg?dl=1" title="forum screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd2f15238aeeb0ae710764ef1d1096928d20522_2_690x416.jpeg" alt="forum screenshot" data-base62-sha1="keDgu7nvYr8zFD6GyXdbyXX7hZ0" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd2f15238aeeb0ae710764ef1d1096928d20522_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd2f15238aeeb0ae710764ef1d1096928d20522_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8dd2f15238aeeb0ae710764ef1d1096928d20522_2_1380x832.jpeg 2x" data-dominant-color="96969E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">forum screenshot</span><span class="informations">1920×1160 325 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be greatly appreciated!</p>

---

## Post #2 by @lassoan (2018-01-08 03:49 UTC)

<p>You need to specify two seeds: one at the start and one at the end of the vessel part that you would like to segment. You can find description of the module user interface in tooltips (hover the mouse over a widget and keep it there for a few seconds to see them).</p>

---

## Post #3 by @Ella (2018-01-08 21:51 UTC)

<p>Thanks for your help, I have placed two seeds and it has produced a small part of the bronchi tree, however not in its entirety. Is there a way to obtain it all using just two points or do I have to do it seperately?</p>
<p>I have attempted to add another branch as shown below, but it doesn’t seem to work…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d63931a1028e8444a36dd130768b6ad977e75b4.jpeg" data-download-href="/uploads/short-url/1UrxM0CtOPYrOocLFkoHPPeD0xK.jpeg?dl=1" title="forum2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d63931a1028e8444a36dd130768b6ad977e75b4_2_690x417.jpeg" alt="forum2" data-base62-sha1="1UrxM0CtOPYrOocLFkoHPPeD0xK" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d63931a1028e8444a36dd130768b6ad977e75b4_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d63931a1028e8444a36dd130768b6ad977e75b4_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d63931a1028e8444a36dd130768b6ad977e75b4_2_1380x834.jpeg 2x" data-dominant-color="999B9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">forum2</span><span class="informations">1920×1161 356 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-01-09 03:02 UTC)

<p>There are a couple of things that probably should be done differently:</p>
<ul>
<li>Crop your volume (using Crop volume module). By keeping the full image, you just increase computation time.</li>
<li>Vesselness filtering: It seems that you have only computed “Preview” of vesselness filtering. If preview looks good, you need to click “Start”.</li>
<li>In “Level set segmentation” module, create a new fiducial list (use DiameterSeed fiducial list only for vesselness filtering diameter definition), place a fiducial at the beginning and end of the vessel part that you would like to segment. Level set segmentation will create a model between the two fiducial points. If they are not connected, then adjust Thresholding at the bottom.</li>
<li>If you need to segment a complete vessel tree, then don’t use “Level set segmentation”, but segment using Segment editor module (you can use Thresholding effect on vesselness filtering result), export segment to model using Segmentations module, then use “Centerline computation” module to compute the centerline of the vessel tree.</li>
</ul>

---
