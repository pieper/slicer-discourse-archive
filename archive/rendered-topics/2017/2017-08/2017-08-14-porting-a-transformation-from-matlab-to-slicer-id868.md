# Porting a transformation from Matlab to Slicer

**Topic ID**: 868
**Date**: 2017-08-14
**URL**: https://discourse.slicer.org/t/porting-a-transformation-from-matlab-to-slicer/868

---

## Post #1 by @Prashant_Pandey (2017-08-14 19:49 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.7<br>
Expected behavior: Transformation to match registered and transformed image in Matlab<br>
Actual behavior: Transformation is off</p>
<p>Hi, I am trying to double check the results of image registration (developed in Matlab) by copying the linear transformation matrix into slicer and applying it to the image. However, I do not get the same result. In matlab I use the affine3d() function to apply a homogenous transformation to an image.</p>
<p>I know that there is a difference between coordinate system definitions in Matlab and Slicer (IJK to RAS), but I still can’t seem to match the registration output when trying to compensate for this. What is the correct way of porting matlab affine3d() transformations to slicer?</p>

---

## Post #2 by @lassoan (2017-08-15 02:24 UTC)

<p>Slicer works in RAS coordinate system, but transform files are written as LPS, so you need a base transform between them: multiply from left and right by <code>diag([-1,-1,1,1])</code>.<br>
You might also need to invert the matrix, depending on what you need: transform <em>to</em> or <em>from</em> parent.</p>

---

## Post #3 by @Prashant_Pandey (2017-08-15 03:56 UTC)

<p>Thanks, I just realised shortly after posting that the transforms are in LPS, and the above base transform works correctly!</p>

---
