# Linear transform documentation clarification?

**Topic ID**: 16229
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/linear-transform-documentation-clarification/16229

---

## Post #1 by @mikebind (2021-02-26 07:21 UTC)

<p>On <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html</a>, which I believe is the current documentation page for slicer transforms, it is a little unclear which form is displayed in the Transforms module: resampling or modeling.  It is clear the Slicer uses and displays RAS matrices, but the documentation seems inconsistent about whether the displayed matrix is the “resampling” or “modeling” direction for the transform. One part of the documentation says that <em>“Transform nodes in Slicer can store transforms in both modeling (when “to parent” transform is set) and resampling way (when “from parent” transform is set).”</em> and the Transforms module says that it is showing the “to parent” matrix.  Together, that would imply that the displayed matrix is the “modeling” direction.  However, just a bit further down, another part of the documentation page says <em>“Transforms module in Slicer shows linear transform matrix values in RAS coordinate system, according to resampling convention”</em>, which states directly that the Transforms module shows the “resampling” direction.  One of these two must be incorrect. I suspect the second statement is incorrect, but I have enough trouble with keeping this convention straight that I’m not entirely sure.  Could someone clarify?</p>

---

## Post #2 by @lassoan (2021-09-03 00:28 UTC)

<p>Good catch, yes, as you suspected, in the second statement “according to resampling convention” should read “according to modeling convention”. I’ve fixed it <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html#transform-files">here</a>.</p>

---
