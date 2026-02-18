# Add 1 cm thick layer on segmentation

**Topic ID**: 19839
**Date**: 2021-09-24
**URL**: https://discourse.slicer.org/t/add-1-cm-thick-layer-on-segmentation/19839

---

## Post #1 by @SlicerBP (2021-09-24 13:10 UTC)

<p>Hello everyone,</p>
<p>For a research project we need to add a 1 cm thick layer (in all spatial directions) to different segmentations. Is there any special function for this? Also gladly per script using vtk or itk.</p>
<p>Thank you very much!<br>
BP</p>

---

## Post #2 by @mikebind (2021-09-24 15:29 UTC)

<p>In Segment Editor, the “Margin” effect will allow you to do exactly this to segments.  Make sure that the “Modify other segments” setting is “Allow overlap” first, or else expanding one segment will eat into any adjacent segments.</p>

---
