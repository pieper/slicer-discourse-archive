# General Registration (Elastix/BRAINS) unable to handle large rotation

**Topic ID**: 7031
**Date**: 2019-06-05
**URL**: https://discourse.slicer.org/t/general-registration-elastix-brains-unable-to-handle-large-rotation/7031

---

## Post #1 by @blackfish (2019-06-05 01:02 UTC)

<p>Operating system: win 10<br>
Slicer version: 4.11.0 (nightly build)<br>
Expected behavior: input the fixed and moving volume to obtain a transformed volume and a transform matrix<br>
Actual behavior: the transformed volume would not be aligned with the fixed volume (in Elastix module using the generic preset). I’ve also tried tuning the parameters using the BRAINS module, but it doesn’t seem to like to rotate much, despite increasing the maximum step length and decreasing the transform scale.</p>
<p>I am certain that the two volumes overlap because the moving volume is a cropped and rotated version of the fixed volume. I am applying the modules to try and recover the transform.</p>
<p>In summary, my first question is am I using the modules wrong?<br>
Second question: can I recover the affine transform matrix when using the elastix module? Currently the transform file size is 2G for a 500x500x500 pixel volume… it seems too big for a 3x4 affine transform matrix.</p>
<p>Thank you in advance!</p>

---

## Post #2 by @lassoan (2019-06-05 01:24 UTC)

<p>Intensity-based automatic registration methods typically do not converge if the initial rotation error is more than 15-20 degrees. You can pre-align the images visually, or by specifying a few matching landmarks, or if the images have approximately the same contents then automatically, based on second degree central moments.</p>
<p>Unfortunately, Elastix uses its own transformation file format that only Elastix can read and Slicer not. It should not be too difficult to implement reading at least linear transformation (and maybe bspline) from the Elastix transform files in SlicerElastix module. See <a href="https://github.com/lassoan/SlicerElastix/issues/5" rel="nofollow noopener">issue on GitHub</a>. We plan to work on this at some point, but if you need it soon then probably your best bet is to implement it yourself (read the text file that Elastix generates, find the transform parameters, and set the matrix values into a transform node) and send a pull request. If you have any help for it then let us know.</p>

---

## Post #3 by @blackfish (2019-06-05 21:45 UTC)

<p>Thank you for the tip.</p>

---
