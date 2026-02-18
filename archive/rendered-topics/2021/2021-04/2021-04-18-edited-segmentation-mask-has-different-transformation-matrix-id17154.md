# Edited segmentation mask has different transformation matrix to original segmentation

**Topic ID**: 17154
**Date**: 2021-04-18
**URL**: https://discourse.slicer.org/t/edited-segmentation-mask-has-different-transformation-matrix-to-original-segmentation/17154

---

## Post #1 by @yizhwan (2021-04-18 03:53 UTC)

<p>Hi all,</p>
<p>I have a segmentation (brain tumour) derived from a deep learning pipeline. It shares the same transformation matrix as the T1/T2/FLAIR scans for the subject.</p>
<p>I imported the segmentation into Slicer as a label map, converted it into a segmentation node and edited it to correct the segmentation. I then converted the edited segmentation into a volume via Slicer and saved it as a nifti.</p>
<p>My goal is to use this mask for further processing of the T1 scan using other tools including SPM. This requires the mask to be in the space as the T1 image. However, after opening the scan and edited segmentation in FSLview, I found that the original mask and the edited mask no longer have the same transformation matrix (although visually both are aligned together on the T1 scan).</p>
<p>Is there any way to ensure that the edited segmentation is saved in the same space as the original segmentation?</p>
<p>Thanks,</p>
<p>Yizhou</p>

---

## Post #2 by @lassoan (2021-04-18 03:58 UTC)

<p>You can choose the segmentation to match geometry of any volume, by <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">choosing that volume as “reference volume” when you export the segmentation</a>.</p>

---

## Post #3 by @yizhwan (2021-04-20 14:39 UTC)

<p>Perfect, thanks, that is very helpful!</p>

---
