---
topic_id: 20380
title: "Convert Vtk Model To Stl While Maintaining Groupids"
date: 2021-10-27
url: https://discourse.slicer.org/t/20380
---

# Convert VTK model to STL while maintaining GroupIds

**Topic ID**: 20380
**Date**: 2021-10-27
**URL**: https://discourse.slicer.org/t/convert-vtk-model-to-stl-while-maintaining-groupids/20380

---

## Post #1 by @ames (2021-10-27 10:07 UTC)

<p>Dear all,</p>
<p>I am processing a surface model of the LIMA-LAD bypass in VMTK. I managed to split the domain in separate regions using VMTKBranchExtractor and VMTKBranchClipper, as shown in the figure. In the VTK file format the GroupIds are conserved, but when writing a STL file as output of the VMTKBranchClipper, this information gets lost.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4.png" data-download-href="/uploads/short-url/xs7mkPQY6XSd8sHnEIdXGrJNwm8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4_2_601x500.png" alt="image" data-base62-sha1="xs7mkPQY6XSd8sHnEIdXGrJNwm8" width="601" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4_2_601x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7572ce8d6f17f2e37cf39fa96486e5705074c4.png 2x" data-dominant-color="F7F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">683×568 48.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am trying to get a STL file of this domain (including the caps at the outlets) where each region has a different ID, so this would mean that each region becomes a solid in the STL file format? I would get 9 different regions, 4 for the endscaps and 5 for the different arteries. I can use VMTKThreshold to write seperate STL files by thresholding based on the GroupId number, but that is not very efficient.</p>
<p>Does someone have any experience with creating one STL file containing different solids for each region from a VTK?</p>

---

## Post #2 by @ames (2021-10-27 14:25 UTC)

<p>Besides, if I want to compute the length and average radius throughout each segment, how can I accomplish that?</p>

---

## Post #3 by @pieper (2021-10-27 16:42 UTC)

<p>STL is a very simple format.  You probably need to make each group into a separate STL file and keep track of the groups another way.</p>

---
