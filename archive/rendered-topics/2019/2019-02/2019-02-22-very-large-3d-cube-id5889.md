# very large 3D cube ?

**Topic ID**: 5889
**Date**: 2019-02-22
**URL**: https://discourse.slicer.org/t/very-large-3d-cube/5889

---

## Post #1 by @meduser (2019-02-22 14:40 UTC)

<p>Operating system: Mac<br>
Slicer version: 4.10.1<br>
Please help: Working on segmentation. The 3D cube that is seen surrounding the 3D volume renderings is shown  as a very tall rectangle, with my actual CT volume data and segmentation occupying just a fraction of it, at the very top of the long rectangle. What is causing this, and how can I make the 3D cube be normally sized again, so as to surround my cropped working volume ? I looked at my data in the data module and nothing is so large.  Thanks for any help !!!</p>

---

## Post #2 by @pieper (2019-02-22 19:57 UTC)

<p>Are you able to reproduce this behavior and share a scene?</p>

---

## Post #3 by @meduser (2019-02-23 03:07 UTC)

<p>Steve,  Thank you for your interest in responding. I figured it out: there were several extra “Annotation ROI” items, one of which was at the bottom of the tall volume I described. Not sure how it was part of the data. Anyways, I deleted it and the problem is solved.  Thank you again,</p>
<p>Andres</p>

---
