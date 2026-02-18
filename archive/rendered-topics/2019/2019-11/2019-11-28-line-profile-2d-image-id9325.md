# Line Profile - 2D image

**Topic ID**: 9325
**Date**: 2019-11-28
**URL**: https://discourse.slicer.org/t/line-profile-2d-image/9325

---

## Post #1 by @ycpan (2019-11-28 14:37 UTC)

<p>Hello,</p>
<p>I have been using Dr. Lasso’s Line Profile and it has worked well for a 3D CT volume. However, when analyzing a 2D image, I kept getting a line of zeros. I am wondering if this is because each coordinate of the line/ruler is three-dimensional and there might be a mismatch in the third direction perpendicular to the image plane?</p>
<p>Also, I think Line Profile is a useful tool that should be included in Kitware. Please let me know how I can help with this process!</p>
<p>Thank you,</p>
<p>Preston</p>

---

## Post #2 by @lassoan (2019-11-28 14:52 UTC)

<p>There are a few implementations of this module. Did you use the one in the “Sandbox” extension?</p>

---

## Post #3 by @lassoan (2019-11-28 22:04 UTC)

<p>VTK has trouble probing a single-slice volume. I’ve <a href="https://discourse.vtk.org/t/bounding-box-of-vtkimagedata/2178">asked for advice on the VTK forum</a>.</p>

---

## Post #4 by @ycpan (2019-12-09 21:34 UTC)

<p>Yes, I am using the Sandbox extension. I am reading through the vtk forum you linked to. I am a beginning to vtk, so would you mind directing me to the right function to look at/modify if I were to get profiles of individual slices?</p>

---

## Post #5 by @uwo27 (2020-01-21 18:32 UTC)

<p>Hi -</p>
<p>Were you able to find a solution? I am encountering the same problem.</p>

---

## Post #7 by @lassoan (2020-01-22 02:24 UTC)

<p>This problem turned out to be caused by a fundamental error in VTK (in how image boundaries are misinterpreted by vtkProbeFilter). I’ve <a href="https://github.com/PerkLab/SlicerSandbox/commit/c6aba38d5701ed0abbf7e6c81e05197b7f039b98">made point probing more robust</a>, which should fix this issue in releases downloaded tomorrow or later.</p>

---

## Post #8 by @uwo27 (2020-01-22 02:37 UTC)

<p>Hi Andras - I’m using the “Sandbox” extension, if I re-download the extension tomorrow or later it should be okay?</p>

---

## Post #9 by @lassoan (2020-01-22 09:25 UTC)

<p>Yes. The extension is updated each night, so you can wait a day and update (or uninstall and install) it. If you don’t want to wait a day then you can <a href="https://github.com/PerkLab/SlicerSandbox/commit/c6aba38d5701ed0abbf7e6c81e05197b7f039b98">modify LineProfile.py</a> on your computer manually right now.</p>

---
