# Straightening 3D dataset

**Topic ID**: 36325
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/straightening-3d-dataset/36325

---

## Post #1 by @tweagles94 (2024-05-22 13:37 UTC)

<p>Hello!</p>
<p>I have a dataset composed by single plane tif images of a cleared spinal cord. Overall size is about 40-50GB. Is there a way I can import them altogether, straighten the object and export it as a sequence of images from another view (say, rostral to caudal)?<br>
I am very new to this software but I could not find  another option<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2024-05-22 13:39 UTC)

<p>If you have enough memory (virtual memory is fine too, but it can be slow) then it should be no problem at all.</p>
<p>It could make sense to load the image tightly cropped around the spine to reduce memory usage - using ImageStacks module in SlicerMorph extension.</p>

---
