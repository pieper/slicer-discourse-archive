# 3D Slicer for segmentation of LIMA-LAD Bypass with severe calcification

**Topic ID**: 19820
**Date**: 2021-09-23
**URL**: https://discourse.slicer.org/t/3d-slicer-for-segmentation-of-lima-lad-bypass-with-severe-calcification/19820

---

## Post #1 by @ames (2021-09-23 05:59 UTC)

<p>Hi all,</p>
<p>I am using 3D Slicer with the VMTK extension for the segmentation of contrast-enhanced CCTA images. I was provided with 3 CCTA data sets from patients with a LIMA-LAD bypass 1 year post-surgery. For CFD simulations I want to segment the left coronary artery tree including LMCA, LAD, LCx and the main side branches and the LIMA.</p>
<p>I am using the level set segmentation in the VMTK extension. I keep the parameters to the default values, but I also need to define a threshold range. For the lower threshold I use 180 HU, to exclude soft tissue. For the upper threshold I am in doubt. As you can see in the images below, there are large calcifications in the LAD and LCx. A too high upper value will lead to calcification classified as lumen and a too low upper value will lead to undersegmentation of the lumen. Besides these calcifications lead to gaps in the segmentation and in some cases the level set method does not output any segmentation at all.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d9054d4cbe6c2f6708bf3da1184b1a31c0a7e5.jpeg" data-download-href="/uploads/short-url/3xOqhVDGlRtvgiNNryXTizDwyhL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18d9054d4cbe6c2f6708bf3da1184b1a31c0a7e5_2_529x499.jpeg" alt="image" data-base62-sha1="3xOqhVDGlRtvgiNNryXTizDwyhL" width="529" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18d9054d4cbe6c2f6708bf3da1184b1a31c0a7e5_2_529x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18d9054d4cbe6c2f6708bf3da1184b1a31c0a7e5_2_793x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d9054d4cbe6c2f6708bf3da1184b1a31c0a7e5.jpeg 2x" data-dominant-color="2A2A2A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×807 62.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e63a1819d44a21c670d84a698309ae12e5a408d6.jpeg" data-download-href="/uploads/short-url/wQGhCYws3w1Yho7Y9OY3mCggwiW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e63a1819d44a21c670d84a698309ae12e5a408d6_2_482x500.jpeg" alt="image" data-base62-sha1="wQGhCYws3w1Yho7Y9OY3mCggwiW" width="482" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e63a1819d44a21c670d84a698309ae12e5a408d6_2_482x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e63a1819d44a21c670d84a698309ae12e5a408d6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e63a1819d44a21c670d84a698309ae12e5a408d6.jpeg 2x" data-dominant-color="373737"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">644×668 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Does anyone have experience with segmentation of CCTA images with severly calcified coronary arteries or any tips/suggestions for defining the threshold range + obtaining a segmentation of the entire left coronary tree?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @suculent (2025-05-04 12:06 UTC)

<p>Hi Ames,</p>
<p>It’s been 4 years, but have you found a solution to this problem you are experiencing? I am currently working on modeling coronary arteries and calcification.</p>
<p>Thank you.</p>

---
