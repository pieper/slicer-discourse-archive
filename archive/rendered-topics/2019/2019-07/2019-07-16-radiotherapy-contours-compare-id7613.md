# Radiotherapy Contours compare

**Topic ID**: 7613
**Date**: 2019-07-16
**URL**: https://discourse.slicer.org/t/radiotherapy-contours-compare/7613

---

## Post #1 by @zeinebnaimi (2019-07-16 16:17 UTC)

<p>Hi everyone, I am radiotherapy resident doctor. In order to study the feasability of coronary arteries’ contouring using a reference atlas, we aim to use 3D slicer RT to compare contours. Unfortunately, we are having some difficulties with the software. We didn’t figure out how to match the two DICOM files to compare. As a consequence we are having great values of Hausdorff distance. Hope to get some yo<br>
help with this issue.</p>

---

## Post #2 by @lassoan (2019-07-16 16:26 UTC)

<p>Before computing differences, you need to register the images or segmentations. There is a chance that you register the segments using Segment Registration module (in Segment Registration extension). If that does not work well enough then you can define matching anatomical landmarks in the atlas and in your data set and register them using Fiducial registration wizard module (in SlicerIGT extension).</p>

---

## Post #3 by @cpinter (2019-07-16 17:00 UTC)

<p>If you have the CTs for both the structure sets you want to compare, then I suggest registering the CTs and use the transformation to propagate the structure set for comparison.</p>
<p>Similarly to how it’s done in the World Congress tutorial:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials</a></p>

---
