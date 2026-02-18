# Reformat module keeps switching images back

**Topic ID**: 27691
**Date**: 2023-02-07
**URL**: https://discourse.slicer.org/t/reformat-module-keeps-switching-images-back/27691

---

## Post #1 by @scrmc (2023-02-07 21:53 UTC)

<p>Hi all,</p>
<p>I’m experiencing a somewhat strange issue with the Reformat module. Although I know it isn’t recommended, I unfortunately must read .mat files into Slicer. For some reason these are rotated when I first read them in, and I can’t seem to modify my MATLAB function to avoid this.</p>
<p>The reformat module lets me rotate them back to the way I would like them, but this never seems to last. So I will rotate one image, switch to view a different image, and when I come back to the original image it has “unrotated” and is back to the (bad) orientation it was first read in as. It admittedly isn’t a huge issue, but it is getting a bit tiresome having to rotate things a million times to view them properly.</p>
<p>Does anyone have a suggestion to avoid this, or has anyone else experienced this? Is this just an unavoidable thing that happens? Is reading in a mat file just a terrible idea and this is what I deserve for doing this?</p>
<p>Would be very grateful for anyone’s thoughts on this!</p>

---

## Post #2 by @lassoan (2023-02-07 21:59 UTC)

<p>You can disable automatic reset on view orientation by right-clicking on the eye icon in th Data module and uncheck automatic setting of orientation on show.</p>
<p>To fix the root cause of the issue, you can use nrrdwrite.m to write your matrix to file in NRRD file format. If you set the correct IJK to LPS matrix (it specifies origin, axis directions, and spacing) then the image will appear in Slicer at the correct position, size, and orientation.</p>

---
