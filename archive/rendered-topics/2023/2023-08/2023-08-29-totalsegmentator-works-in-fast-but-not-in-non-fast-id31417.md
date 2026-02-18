# Totalsegmentator works in fast but not in non-fast

**Topic ID**: 31417
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/totalsegmentator-works-in-fast-but-not-in-non-fast/31417

---

## Post #1 by @Ylim (2023-08-29 06:53 UTC)

<p>if fast is not selected -<br>
Slicer/__SlicerTemp__2023-08-29_16+39+14.764/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.<br>
under apply button<br>
.totalsegmentator\nnunet\results\nnUNet\3d_fullres\Task251_TotalSegmentator_part1_organs_1139subj\nnUNetTrainerV2_ep4000_nomirror__nnUNetPlansv2.1\fold_0\model_final_checkpoint.model.pkl’</p>
<p>Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000001833E38FDC0&gt;</p>
<p>AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>if fast is selected</p>
<ul>
<li>solution is achieved.</li>
</ul>
<p>slicer 5.2.2, pytorch 2.0.1, ndivia 536.67<br>
Please advise.</p>

---

## Post #2 by @Ylim (2023-08-31 07:55 UTC)

<p>Can someone please help?</p>

---
