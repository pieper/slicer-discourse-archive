# Ankle Osteotomy

**Topic ID**: 42143
**Date**: 2025-03-14
**URL**: https://discourse.slicer.org/t/ankle-osteotomy/42143

---

## Post #1 by @JuMaLe (2025-03-14 19:04 UTC)

<p>Hello!<br>
I’m looking for a tool or a set of tools to approach osteotomy planning. The Osteotomy Planner module appears to be useless for this.</p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2025-03-15 15:37 UTC)

<p>Slicer has been improved a lot since the Osteotomy Planner module was introduced and probably you can fulfill most needs only using Slicer core modules.</p>
<p>For example, you can place a markup plane using Markups module, and then simulate bone cuts using <code>Dynamic modeler</code> module.</p>
<p>If you describe what you need eactly then we can give further suggestions.</p>

---

## Post #3 by @JuMaLe (2025-03-15 16:39 UTC)

<p>I would like to plan a surgery and create surgical guides for deformity correction. For the first step, Dynamic Modeler’s tools allow me to create all the references I need to determine the CORA or another required reference, but I guess I need to set the lines and planes manually. What about the second step?</p>
<p>Thanks for your answer!</p>

---

## Post #4 by @lassoan (2025-03-17 20:46 UTC)

<p>You can validate your workflow using general-purpose manual tools. Then you can gradually automate your workflow by Python scripting. The <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner?tab=readme-ov-file#bonereconstructionplanner">BoneReconstructionPlanner</a> extension is a nice example that implements mandible fibula flap reconstruction planning workflow and automatic 3D-printable guide generation.</p>

---
