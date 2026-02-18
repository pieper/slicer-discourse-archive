# How can I export a brain tumor 3d model with brains opacity?

**Topic ID**: 21625
**Date**: 2022-01-25
**URL**: https://discourse.slicer.org/t/how-can-i-export-a-brain-tumor-3d-model-with-brains-opacity/21625

---

## Post #1 by @Vinesh13 (2022-01-25 15:24 UTC)

<p>I used the segmentation for making the brain and tumor…later after exporting as an object file with merging both the segments as a single file,I opened this obj file in 3d viewer…but the output doesn’t has the brains opacity…</p>
<p>Can anyone help me out??</p>

---

## Post #2 by @lassoan (2022-01-27 03:53 UTC)

<p>OBJ is an export format for segmentation (for exchanging data with other software), not a saving format (for saving data to be reloaded later).</p>
<p>If you want to save the segmentation to disk without losing any information then save it as a .seg.nrrd (if labelmap is the master representation) or .seg.vtm (if closed surface is the master representation).</p>
<p>Slicer’s OBJ reader only reads the .obj file (mesh geometry and material IDs) and not the .mat file (that contains the colors and opacities).</p>

---

## Post #3 by @drnoorfatima (2026-02-17 09:29 UTC)

<p>Hi!</p>
<p>This is actually a pretty common issue when exporting merged segments as OBJ, the opacity/transparency you see in Slicer’s 3D viewer is a rendering property that lives inside Slicer itself, not in the geometry file. So when you export, that information doesn’t travel with it.</p>
<p>Getting it to look right in an external viewer depends on a couple of things that aren’t immediately obvious from the export side.</p>
<p>What are you trying to achieve with it ?visualization, 3D printing, or something else? And which 3D viewer are you using? DM me if you’d like, happy to help.</p>

---
