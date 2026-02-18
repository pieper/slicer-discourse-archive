# Export File as bug for markup control points

**Topic ID**: 26188
**Date**: 2022-11-10
**URL**: https://discourse.slicer.org/t/export-file-as-bug-for-markup-control-points/26188

---

## Post #1 by @muratmaga (2022-11-10 21:19 UTC)

<p>This replicates in the latest preview (and current stable).</p>
<p>Create a pointList object with some markups in. Set the interaction lock for the control point addition (so that no new control points can be added to the pointList).</p>
<p>Save the pointList as a mrk.json via regular save as menu, and also a second time via Export File As under a different filename.</p>
<p>Reset the scene and load both mrk.json files into the scene. Observe the lock state is preserved in normal save as, but not in export file as.</p>
<p>This breaks our functionality (and tutorials) for landmark templates, when the template is saved via export file as.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2022-11-11 02:29 UTC)

<p>Good catch, fixed - <a href="https://github.com/Slicer/Slicer/commit/38d8d9911dcf0a72df73bec658cf2e985c95c049" class="inline-onebox">BUG: Fix fixedNumberOfControlPoints property value in exported markup… · Slicer/Slicer@38d8d99 · GitHub</a></p>

---
