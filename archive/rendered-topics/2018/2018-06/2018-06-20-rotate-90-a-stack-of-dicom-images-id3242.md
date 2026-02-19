---
topic_id: 3242
title: "Rotate 90 A Stack Of Dicom Images"
date: 2018-06-20
url: https://discourse.slicer.org/t/3242
---

# Rotate 90° a stack of DICOM images

**Topic ID**: 3242
**Date**: 2018-06-20
**URL**: https://discourse.slicer.org/t/rotate-90-a-stack-of-dicom-images/3242

---

## Post #1 by @Tommaso_Di_Noto (2018-06-20 08:47 UTC)

<p>Hi everyone!</p>
<p>I have a stack of DICOM images which I would like to rotate 90° counterclockwise. Any suggestion?</p>
<p>Thanks a lot in advance!</p>

---

## Post #2 by @pieper (2018-06-20 12:40 UTC)

<p>You can do that by adding a linear transform and setting the rotation.  Then you can harden that transform and export the data in whatever format you need.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms</a></p>

---
