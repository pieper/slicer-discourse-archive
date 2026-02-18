# Slicer compatible and 3D capable PACS Viewer in clinical setting?

**Topic ID**: 16827
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/slicer-compatible-and-3d-capable-pacs-viewer-in-clinical-setting/16827

---

## Post #1 by @rbumm (2021-03-29 18:38 UTC)

<p>Hi,</p>
<p>we are looking for a new system-wide PACS Viewer in a hospital setting.<br>
Is there any advice on a Slicer-compatible 3D-capable product? Does anyone have experience with the Sectra viewer or other recommendations?</p>
<p>Thank you,</p>
<p>Best regards<br>
Rudolf</p>

---

## Post #2 by @pieper (2021-03-29 19:03 UTC)

<p>Hi Rudolf -</p>
<p>I’m not sure of any products that are particularly Slicer-compatible.  We have been encouraging the vendors to adopt DICOM standard segmentation object, structured report, and parametric map formats with mixed success (this <a href="https://dicom4qi.readthedocs.io/en/latest/participants/">list of participants</a> will give you an idea).  You can at least ask the vendors for a conformance statement about the information objects they support.</p>
<p>It also depends on what you want to achieve.  For many projects we’ve wanted to let radiologists annotate using their clinical systems, but exporting the results has been a challenge with all systems.  For other projects we want to load external calculations for therapy guidance and the navigation systems always seem to have some non-standard back door or other.</p>
<p>-Steve</p>

---
