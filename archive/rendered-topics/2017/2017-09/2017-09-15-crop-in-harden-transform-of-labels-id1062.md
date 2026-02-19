---
topic_id: 1062
title: "Crop In Harden Transform Of Labels"
date: 2017-09-15
url: https://discourse.slicer.org/t/1062
---

# Crop in harden transform of labels

**Topic ID**: 1062
**Date**: 2017-09-15
**URL**: https://discourse.slicer.org/t/crop-in-harden-transform-of-labels/1062

---

## Post #1 by @pwang (2017-09-15 16:27 UTC)

<p>Operating system: Windows7<br>
Slicer version:4.7.0<br>
The label is transformed normally by Transforms function. However, when it is hardened, the bottom part of the label is cut off. Please see the pictures of before the hardening and after. Thanks. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9066c2aad8460d44a98efbbb6fae86fb324ebe3e.jpeg" alt="image" data-base62-sha1="kBqUYme8ZQ3VygKYGHS0lTErAQe" width="287" height="218"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82d75f9215b81bbcca66a357e2b591ae9653c3e2.jpeg" alt="image" data-base62-sha1="iFtvovcyw0wP5fgmTBjYmWAN1g6" width="249" height="237"></p>

---

## Post #2 by @lassoan (2017-09-15 17:52 UTC)

<p>Voxel grid of the volume is not changed when you harden the transform, so deformation moves out structures from the original extent of the volume then it’ll be cropped. I’ve added a feature request to automatically extend the volume (<a href="https://issues.slicer.org/view.php?id=4433">https://issues.slicer.org/view.php?id=4433</a>).</p>
<p>Until this new feature is implemented, you can use the crop volume to define a region that includes the deformed volume entirely module and apply the transform.</p>

---

## Post #3 by @pwang (2017-09-15 22:35 UTC)

<p>Thank you. I expanded the contours and it should solve my problem.</p>

---
