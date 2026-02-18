# Import labelmap and re-threshold

**Topic ID**: 7090
**Date**: 2019-06-08
**URL**: https://discourse.slicer.org/t/import-labelmap-and-re-threshold/7090

---

## Post #1 by @Dmitriy_Desser (2019-06-08 23:07 UTC)

<p>Hi guys,</p>
<p>I have some longitudinal brain mri data. I am wondering, if it is possible after segmenting (thresholded paint brush from segment editor) one file (e.g. ses-01) and saving the segmentation to a label map to load and apply it on the next file (e.g. ses-02) and “re-threshold” it within the segmentation?</p>
<p>I would apriciate any help very much!</p>
<p>Cheers,</p>
<p>Dima</p>

---

## Post #2 by @lassoan (2019-06-08 23:52 UTC)

<p>Yes, sure. 1. You can switch master volume any time. 2. To restrict an effect to operate only inside/outside selected segment(s), adjust masking settings near the bottom of the Segment Editor panel.</p>

---
