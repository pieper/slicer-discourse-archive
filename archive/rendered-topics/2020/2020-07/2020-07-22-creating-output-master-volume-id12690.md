# Creating Output Master Volume

**Topic ID**: 12690
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/creating-output-master-volume/12690

---

## Post #1 by @vertebrae (2020-07-22 14:23 UTC)

<p>Hello,</p>
<p>When I run my local threshold segmentation code, 3D Slicer automatically creates an output master volume for my code. Instead, I would like to create a new master volume that could be my output volume after the segmentation. How would I do this?</p>

---

## Post #2 by @lassoan (2020-07-22 14:30 UTC)

<p>You can find the examples in script repository for creating empty volume. However, master volume is an input for thresholding, so an empty input volume will not work as input.</p>

---

## Post #3 by @vertebrae (2020-07-22 14:34 UTC)

<p>Thank you for the help <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
