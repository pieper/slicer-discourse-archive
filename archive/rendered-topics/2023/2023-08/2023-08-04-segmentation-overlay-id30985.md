# Segmentation overlay

**Topic ID**: 30985
**Date**: 2023-08-04
**URL**: https://discourse.slicer.org/t/segmentation-overlay/30985

---

## Post #1 by @Alra2000 (2023-08-04 19:13 UTC)

<p>Hello everyone,</p>
<p>I am segmenting laser ablation tissue on brain MRI, and I am trying to overlay the segmentations for volume comparison. Is there an option for that in 3D slicer, please?</p>

---

## Post #2 by @ebrahim (2023-08-04 19:47 UTC)

<p>I think you can just toggle both of your segmentations to be visible and they will be overlaid in the slice views.</p>
<p>Assuming they are segmentation nodes</p>
<p>If you are talking about the closed surface representation in the 3D view, then you can just lower the opacity in order to see both segmentations</p>

---

## Post #3 by @Alra2000 (2023-08-05 15:37 UTC)

<p>Thank you for your reply Ebrahim. To clarify, I am having two segments one from intraop and the other from post-op. These two segments are from a DICOM series each. So the segments are not done on the same series. And I was wondering if 3D Slicer has an option to link these two series in a way that makes the segments comparable side by side or through an overlay for volume comparison.</p>

---
