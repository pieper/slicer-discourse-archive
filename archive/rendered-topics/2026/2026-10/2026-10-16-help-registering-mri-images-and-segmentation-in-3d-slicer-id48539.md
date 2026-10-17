---
topic_id: 48539
title: "Help Registering MRI Images and Segmentation in 3D Slicer"
date: 2026-10-16
url: https://discourse.slicer.org/t/48539
last_bumped: 2026-10-16T15:50:06.554Z
---

# Help Registering MRI Images and Segmentation in 3D Slicer

**Topic ID**: 48539
**Date**: 2026-10-16
**URL**: https://discourse.slicer.org/t/help-registering-mri-images-and-segmentation-in-3d-slicer/48539

---

## Post #1 by @cv24 (2026-10-16 15:27 UTC)

<p>I am trying to register two shoulder MRI images acquired from the same participant. One image has a manually segmented region of cartilage, while the other image does not have a segmentation. I need to align the two images (and segmeentation) and transfer the existing segmentation to the second image.</p>
<p>My goal is to register the images, apply the transformation to the segmentation, and export it as a binary mask (.nrrd) aligned with the second image for analysis in MATLAB.</p>
<p>I have tried using Landmark Registration with corresponding anatomical landmarks and affine registration. However, the transformed image either appears black or does not seem to align correctly with the fixed image.</p>
<p>I have successfully done this in 3D Slicer before, but I cannot seem to replicate the process and am unsure where I am going wrong.</p>
<p>Does anyone have suggestions for troubleshooting this or a recommended workflow for registering the images while keeping the segmentation aligned?</p>
<p>Any and all help would be greatly appreciated! Thank you!</p>

---

## Post #2 by @mikebind (2026-10-16 15:50 UTC)

<p>Your general plan sounds good.  Try the Fiducial Registration Wizard module.  If the images do not line up well under an affine transformation, check how well your corresponding landmark points line up (after transforming the moving ones by the same transformation).  If the points don’t line up well, then the transformation may not be well-represented by an affine transform.  Lots of things can move nonlinearly around the shoulder joints. If a linear transform is not able to align the images, I would move on to a nonlinear registration approach.  If there are big changes between images, I would crop both the fixed and moving images to just the region around the area of interest and do a nonlinear registration (via ANTs or Elastix).  If that aligns the images well, you can apply the nonlinear transform to your segmentation, change the segmentation geometry of the transformed segmentation to match your second image, and then export the transformed segment to a binary labelmap.</p>

---
