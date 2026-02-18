# Displaying CAD Model in Slicer3D

**Topic ID**: 20814
**Date**: 2021-11-28
**URL**: https://discourse.slicer.org/t/displaying-cad-model-in-slicer3d/20814

---

## Post #1 by @sziselman4c (2021-11-28 03:48 UTC)

<p>Hi All! I am new to working with 3D Slicer, so I’m looking to the forum for some guidance. I am working on a project where I am developing my own python module. I’d like to be able to display a STEP file (for example, of a self-designed mechanical component) in 3D Slicer, and manipulate it’s configuration. What is the best way to approach displaying this model? I’ve found a couple sources/tutorials that allude to this being possible, but nothing that goes in-depth well enough for me to follow. Thank you for your help! I can provide more information or clarification if necessary.</p>

---

## Post #2 by @lassoan (2021-11-28 05:34 UTC)

<p>You can export a polygonal mesh (ply, stl, obj, vtk, vtp, …) file from your CAD software and read that into Slicer.</p>

---

## Post #4 by @sziselman4c (2021-12-03 16:59 UTC)

<p>Hi Andras,</p>
<p>Thank you for your help, I realize I wasn’t using a compatible file type and once I did load a STL file, I didn’t zoom out far enough. Is it possible to manipulate parts of the CAD model via a custom-written python module?</p>

---

## Post #5 by @lassoan (2021-12-03 17:25 UTC)

<p>Yes, all features that are available on the GUI are available via Python scripting, too.</p>
<p>What manipulation would you like to do? Combine the part with bone or skin surface extracted from a patient’s image?</p>

---
