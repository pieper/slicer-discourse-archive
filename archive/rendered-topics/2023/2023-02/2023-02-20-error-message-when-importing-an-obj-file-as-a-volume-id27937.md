---
topic_id: 27937
title: "Error Message When Importing An Obj File As A Volume"
date: 2023-02-20
url: https://discourse.slicer.org/t/27937
---

# Error message when importing an .obj file as a volume 

**Topic ID**: 27937
**Date**: 2023-02-20
**URL**: https://discourse.slicer.org/t/error-message-when-importing-an-obj-file-as-a-volume/27937

---

## Post #1 by @Lily_Armstrong-Davie (2023-02-20 20:05 UTC)

<p>Operating system: macOS<br>
Slicer version: 5.2.1<br>
Expected behavior: I’d like my 3D skull .obj thats been edited in C4D to be imported into 3D Slicer as a volume so that I can threshold it and then use WrapSolidify to extrapolate the inside<br>
Actual behavior: When I upload the .obj through Add Data it imports as a Segmentation but when I try to import as a volume it gives me an Error Message with no information.</p>

---

## Post #2 by @pieper (2023-02-20 22:26 UTC)

<p>You should be able to export your segmentation to a binary labelmap volume and then convert that to a scalar volume if needed.  But if it’s started as a surface model you won’t be able to threshold it since there’s not continuous tone values, just inside/outside the model.  WrapSolidify should work though.</p>

---
