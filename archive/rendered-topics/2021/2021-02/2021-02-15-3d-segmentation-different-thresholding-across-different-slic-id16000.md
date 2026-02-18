# 3D-segmentation + different thresholding across different slices

**Topic ID**: 16000
**Date**: 2021-02-15
**URL**: https://discourse.slicer.org/t/3d-segmentation-different-thresholding-across-different-slices/16000

---

## Post #1 by @lekremer (2021-02-15 16:14 UTC)

<p>hello,</p>
<p>I want to do a 3d volume of a structure (e.g. kidney) of an image volume, but I need to threshold across the kidney at different threshold intensities. unfortunately, the threshold applies to the 3d volume the same intensity across all slides. is there a way to do this in an efficient manner, versus making a different segmentation for each image slice?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2021-02-15 18:40 UTC)

<p>Indeed, simple global thresholding only works well in a few special cases (such as bone segmentation in CT). That is why we added several other semi-automatic segmentation methods that rely on local intensity changes only. The most commonly used is <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#grow-from-seeds">Grow from seeds</a>, but you can also try Local threshold, Fast marching, Watershed, or Flood filling methods (in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/#slicersegmenteditorextraeffects">SegmentEditorExtraEffects extension</a>).</p>

---
