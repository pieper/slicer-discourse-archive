# SegmentationUNet Logic Module

**Topic ID**: 25433
**Date**: 2022-09-26
**URL**: https://discourse.slicer.org/t/segmentationunet-logic-module/25433

---

## Post #1 by @Isabella_Romero (2022-09-26 08:23 UTC)

<p>Hi,</p>
<p>Does anyone have an example using the SegmentationUNet Logic Module in Python to recreate the segmentation of an image?</p>
<p>Thank you.</p>

---

## Post #2 by @ungi (2022-09-27 03:19 UTC)

<p>Hi, the widget of this module is probably the only example of using the logic. I don’t know of other modules using it.<br>
Trained models usually expect specific input format. Unless your trained model uses exactly the same format for input and output, you probably need to modify the SegmentationUNet module, keep it backwards compatible, and submit a pull request. Or implement your own module based on this one.</p>

---
