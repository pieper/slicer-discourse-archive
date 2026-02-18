# Feature extraction in 2D image

**Topic ID**: 23828
**Date**: 2022-06-11
**URL**: https://discourse.slicer.org/t/feature-extraction-in-2d-image/23828

---

## Post #1 by @Rohini_Gaikar (2022-06-11 12:30 UTC)

<p>I have image and mask in float64.<br>
When I try to cast mask in INT32vit gives me error.<br>
sitk_mask = sitk.Cast(sitk_mask, sitk.sitkInt32)</p>
<p>Error is as:<br>
sitk::ERROR: Filter does not support casting from casting 64-bit float to 32-bit signed integer</p>
<p>how to correct this? Please help. Thanks.</p>

---

## Post #2 by @lassoan (2022-06-12 01:20 UTC)

<p>Have you tried a web search for this error?</p>
<p>Does this help? <a href="https://github.com/SimpleITK/SimpleITK/issues/592" class="inline-onebox">SimpleITK not working with any data type, be it 3D or 2D · Issue #592 · SimpleITK/SimpleITK · GitHub</a></p>

---
