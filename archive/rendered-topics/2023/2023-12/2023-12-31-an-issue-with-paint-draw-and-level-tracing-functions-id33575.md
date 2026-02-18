# An issue with (Paint), (Draw), and (Level tracing) functions

**Topic ID**: 33575
**Date**: 2023-12-31
**URL**: https://discourse.slicer.org/t/an-issue-with-paint-draw-and-level-tracing-functions/33575

---

## Post #1 by @MZA (2023-12-31 18:10 UTC)

<p>Problem report for Slicer 5.6.1 win-amd64: [please describe expected and actual behavior]</p>
<p>Greetings support team,</p>
<p>I am encountering an issue while utilizing functions such as (Paint), (Draw), or (Level tracing) for manual segmentation, where the functionality ceases at one cut – no drawing is permitted. However, it resumes working on the subsequent cut with the same drawing applied to the previous one. Any insights or suggestions would be greatly appreciated.</p>
<p>::UPDATE::</p>
<p>I’ve observed that the software treats two consecutive cuts as a single cut, meaning that whatever I draw in one cut also applies to the other.</p>
<p>Thank you in advance,</p>

---

## Post #2 by @lassoan (2023-12-31 21:48 UTC)

<p>Probably the slice spacing of the segmentation does not match the slice spacing of the current background volume. You can change the segmentation geometry to the current background volume as described in “Source volume” section of the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options">Segment Editor module documentation</a>.</p>

---

## Post #3 by @MZA (2024-03-07 19:05 UTC)

<p>That fixed the issue, thanks!</p>

---
