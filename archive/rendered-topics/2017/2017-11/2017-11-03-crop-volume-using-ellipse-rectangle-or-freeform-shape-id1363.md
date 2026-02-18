# Crop volume using ellipse, rectangle, or freeform shape

**Topic ID**: 1363
**Date**: 2017-11-03
**URL**: https://discourse.slicer.org/t/crop-volume-using-ellipse-rectangle-or-freeform-shape/1363

---

## Post #1 by @AndFor (2017-11-03 11:48 UTC)

<p>Hello<br>
I’m new on Slicer, I work on 3D dicom MRI Data</p>
<p>In my philips workspace I can manually crop  direct from volume (using ellipse, rectangle, or manual shape)</p>
<p>I can I do this on 3DSlicer?<br>
Thanks</p>

---

## Post #2 by @lassoan (2017-11-03 15:43 UTC)

<p>If you consider cropping your volume to exclude areas during segmentation then you don’t need to actually modify your volume. You can use Scissors effect in Segment Editor module to draw rectangular/circular/freeform regions in 2D or 3D and use that as mask during segmentation.</p>
<p>If you actually want to mask out regions from your volume (e.g., as a pre-processing for volume rendering) then install <code>SegmentEditorExtraEffects</code> extension and use <code>Mask volume</code> effect to blank areas inside/outside the segment.</p>

---
