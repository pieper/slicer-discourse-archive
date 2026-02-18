# Segmentation inside a ROI

**Topic ID**: 12588
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/segmentation-inside-a-roi/12588

---

## Post #1 by @Jaswant (2020-07-17 00:17 UTC)

<p>My question is somewhat similar to ongoing discussion on ROI to segmentation topic.<br>
I am working on a whole body CT with contrast of a dog to segment bones, muscles and blood vessels of thoracic and pelvic limbs, axial skeleton and head&amp;neck. In order to do so, I created ROI for each of these regions and have to create sub-volumes to do region-specific segmentations. Is there a direct way for me use only one master volume (whole body) and perform segmentation within a specific ROI. I am a novice, so please re-direct me an example, if available. Thank you very much in advance.</p>

---

## Post #2 by @timeanddoctor (2020-07-17 02:10 UTC)

<p>You can create a croped volume as the ROI volume for the master volume of segment editor.</p>

---

## Post #3 by @lassoan (2020-07-17 19:21 UTC)

<p>You can also use masking settings to restrict editing to a certain region, or extract part of a segment that is in a certain region (using Logical operators effect).</p>

---
