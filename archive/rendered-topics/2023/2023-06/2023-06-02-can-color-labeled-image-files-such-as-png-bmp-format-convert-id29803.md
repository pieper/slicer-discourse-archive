---
topic_id: 29803
title: "Can Color Labeled Image Files Such As Png Bmp Format Convert"
date: 2023-06-02
url: https://discourse.slicer.org/t/29803
---

# Can color-labeled image files such as png, bmp format convert into volume by marked labeling?

**Topic ID**: 29803
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/can-color-labeled-image-files-such-as-png-bmp-format-convert-into-volume-by-marked-labeling/29803

---

## Post #1 by @william1 (2023-06-02 14:46 UTC)

<p>Can color-labeled image files such as png, bmp format convert into volume by marked labeling?</p>
<p>All the best guys,</p>
<p>I wonder if I can convert the each colored label in the image files can be converted into volume rendering. since it is already colored and labeled, it does not need to segment again in Slicer.</p>
<p>Hope the pro can help me to figure out</p>
<p>Thanks</p>
<p>William Jung</p>

---

## Post #2 by @lassoan (2023-06-02 14:48 UTC)

<p>You can render RGB color images as is, both in 2D and 3D.</p>
<p>For analysis, I would recommend to convert to scalar volume using “Vector to scalar volume” module, or you can load it directly as a scalar volume if you enable the grayscale option in ImageStacks module (provided by SlicerMorph extension).</p>

---
