# 3D binary mask from both sagittal frontal axial segments

**Topic ID**: 13414
**Date**: 2020-09-10
**URL**: https://discourse.slicer.org/t/3d-binary-mask-from-both-sagittal-frontal-axial-segments/13414

---

## Post #1 by @Ndzimbong_William_Br (2020-09-10 00:06 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: obtain one 3D binary mask<br>
Actual behavior: three 3D masks, each by segment<br>
Imaging Modality: 3D US</p>

---

## Post #2 by @lassoan (2020-09-10 00:19 UTC)

<p>What kind of ultrasound images do you work with: cardiovascular, ob/gyn, musculoskeletal? Are they acquired by 3D probe or position-tracked 2D probe? What is the brand/model of your ultrasound system? How did you import the images?</p>

---

## Post #3 by @Ndzimbong_William_Br (2020-09-11 09:42 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a><br>
I got the answer.<br>
These are 3D US kidney volumes. The probe used is a 3D.<br>
According to the expert who did the scans, it’s almost impossible to get complete kidney segmentations on living beings.<br>
3D slicer offers the possibility to transform the 3 very partial segmentations into a single binary volume which is also partial. And that’s all we can do, apparently.</p>

---
