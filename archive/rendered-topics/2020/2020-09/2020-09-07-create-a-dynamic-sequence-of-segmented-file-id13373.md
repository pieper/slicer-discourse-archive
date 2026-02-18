# create a dynamic sequence of segmented file 

**Topic ID**: 13373
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/create-a-dynamic-sequence-of-segmented-file/13373

---

## Post #1 by @ponchan0 (2020-09-07 14:04 UTC)

<p>Good afternoon,</p>
<p>Im wondering if there is a tool allowing a rapid segmentation of a dynamic structure (heart ventricles contracting) ?<br>
As demonstrated in the youtube video sequence recording, a dynamic mesh is visualized in the 3D view, from a segment that seems to cover atrioventricular bloodpool. I tried to segment with threshold, but when applied the segment freezed.</p>
<p>We’d like to import a dynamic mesh in a visualizer for aacdemic educational purpose.</p>
<p>At your dispostion for more infos, thanks in advance for time and answers</p>
<p>Kevin Ponchant</p>

---

## Post #2 by @lassoan (2020-09-07 15:02 UTC)

<p>It should be no problem to segment a cardiac volume sequence. If you describe specific steps that lead to too long computation time then we can give advice about how to avoid that.</p>
<p><a class="mention" href="/u/sarvpriya1985">@sarvpriya1985</a> could you describe what workflow did you end up using for 4D cardiac data segmentation?</p>

---

## Post #3 by @ponchan0 (2020-09-07 18:32 UTC)

<p>thanks for your answer. is there a tool allowing an extrapolation of segment like a « dynamic » grow form seed ?</p>
<p>that stick with the moving blood pool</p>

---

## Post #4 by @lassoan (2020-09-07 20:06 UTC)

<p>Yes, there are several ways to automate the process. For example, you can define seeds at one time point, compute seeds for all other frames using Sequence registration module, then get complete segmentation using “Grow from seeds” effect. Depending on the image quality and clinical requirements, you may need some smoothing and manual corrections. We have discussed this on this forum earlier, so you may find more details by searching here.</p>

---
