# Bone segmentation on 2d slices

**Topic ID**: 612
**Date**: 2017-07-01
**URL**: https://discourse.slicer.org/t/bone-segmentation-on-2d-slices/612

---

## Post #1 by @mag (2017-07-01 17:13 UTC)

<p>Hi,</p>
<p>I am working on CTA scans for my research and I was wondering if it is possible in 3D Slicer to create a segmentation on the 2D slices and then remove the bones from the 2D slices. I know this is possible in the 3D viewer, but I was not able to figure out how I can show the scan without the bone segment in the 2D viewers.</p>
<p>I hope my question is clear.<br>
I need to visualize blood vessels on MIP in the axial view and when the vessels are very close to the skull they are sometimes covered from bone in upper or lower slices because of the MIP.</p>
<p>Thank you very much,</p>
<p>Marta</p>

---

## Post #2 by @lassoan (2017-07-01 17:19 UTC)

<p>Use the <code>Segment Editor</code> module for segmentation. Segments can be individually shown/hidden in 2D and 3D.</p>
<p>If you have already segmented your volume using the legacy <code>Editor</code> module then go to Segmentations module Import/Export section and convert the labelmap volume to a segmentation.</p>

---
