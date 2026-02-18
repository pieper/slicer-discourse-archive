# Virtual Fracture Reconstruction Extension

**Topic ID**: 10587
**Date**: 2020-03-07
**URL**: https://discourse.slicer.org/t/virtual-fracture-reconstruction-extension/10587

---

## Post #1 by @kt297 (2020-03-07 22:08 UTC)

<p>How do I install this Virtual Fracture reconstruction module into 3d Slicer? There doesn’t seem to be an extension for it within 3D slicer?</p>
<p>Here is the link: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/VirtualFractureReconstruction" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/VirtualFractureReconstruction</a></p>

---

## Post #2 by @lassoan (2020-03-08 05:15 UTC)

<p>The extension was not updated to Slicer-4.11. I’ve <a href="https://github.com/lassoan/VirtualFractureReconstructionSlicerExtension">fixed the build errors</a> now, but some more work would be needed to make the extension functional, due to some Slicer API changes (most notably, replacement of Model Hierarchy by Subject hierarchy).</p>
<p>To be able to make these changes, it would be necessary to have sample data set to test with. Can you provide sample reference image, reference labelmap, and fragment image?</p>
<p>Also, could you contact the authors (in particular Karl Fritscher) to get information about what the extension can do (to verify that the module does what you need)? It would be also nice to know if they are still willing to spend time with maintenance or even development of the extension.</p>

---

## Post #3 by @kt297 (2020-03-08 08:03 UTC)

<p>Thanks. I can provide you with a anonymised DICOM CT file with a fractured bone. However, I don’t know how from that dataset to provide a sample reference image, reference labelmap, and fragment image (willing to learn if there is a step by step tutorial or reference I can learn from?).</p>
<p>I have emailed (on 6th March) Karl Fritscher about the extension not being available on current version of 3D slicer but has not responded yet.</p>

---

## Post #4 by @kt297 (2020-04-11 08:26 UTC)

<p>No reply with Karl Fritscher although I have emailed again. Hopefully may have some time to work on this.</p>
<p>Any other ways to get this going in current version of 3D slicer?</p>

---

## Post #5 by @kt297 (2020-04-23 20:25 UTC)

<p>any luck with slicer API functionality?</p>

---

## Post #6 by @kt297 (2020-06-21 15:23 UTC)

<p>Anyway I can help this plugin to work?</p>

---
