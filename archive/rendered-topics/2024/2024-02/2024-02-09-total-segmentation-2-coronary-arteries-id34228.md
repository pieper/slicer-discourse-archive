# Total segmentation 2 coronary arteries

**Topic ID**: 34228
**Date**: 2024-02-09
**URL**: https://discourse.slicer.org/t/total-segmentation-2-coronary-arteries/34228

---

## Post #1 by @Caterina (2024-02-09 16:11 UTC)

<p>Dear support, is it possibile to have a example file of total segmentation results (including dicom images) for coronary arteries?<br>
Thanks</p>

---

## Post #2 by @Matteboo (2024-02-09 16:36 UTC)

<p><a href="https://drive.google.com/drive/folders/1ggrQn4UFK2_SIJxIrg-cVeqiUXDOgmCr?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1ggrQn4UFK2_SIJxIrg-cVeqiUXDOgmCr?usp=sharing</a></p>
<p>I did this quickly on some sample data, I hope it helps</p>

---

## Post #3 by @lassoan (2024-02-10 17:30 UTC)

<p>I exported videos of the result for easier viewing:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/343b2ea87bda4c68f36a66d9710ee3913db9202e.mp4">
  </div><p></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dafffa980bd772baa8654a5b8d8e6f9ec10458c.mp4">
  </div><p></p>
<p>The CT scan is an old one and not very good resolution (1.15 x 1.15 x 2mm), so probably on a more modern CT you would get much finer details.</p>

---

## Post #4 by @Caterina (2024-02-11 21:56 UTC)

<p>Thank you very much. I also followed this video (<a href="https://www.youtube.com/watch?v=aeOFl19fh_c" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=aeOFl19fh_c</a>) for coronary vessel segmentation on cardiac CT images. Volume rendering model does not update interactively with ROI. At 1.16’, the volume in my case is not updated. can you please suggest me a solution?Thanks</p>

---

## Post #5 by @lassoan (2024-02-12 12:16 UTC)

<p>To make the output of mask volume effect visible in 3D, you need to hide volume rendering of the original (non-masked) volume and show volume rendering of the new masked volume.</p>

---

## Post #6 by @Pawel_Zakrzewski (2025-01-07 08:05 UTC)

<p>Hi, is this automatic segmentation? I don’t see such an option in Total Segmentator.<br>
Valve leaflets can also be automated?<br>
Amazing Plugin <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2025-01-07 15:25 UTC)

<p>Yes, it is automatic segmentation. As far as I remember both TotalSegmentator and MONAIAuto3DSeg can segment coronaries. They are not great, but may be usable for some applications if the scan quality is good enough.</p>
<p>Leaflet segmentation could be automated as well, but basic 3D segmentation would probably only work on good quality scans and only on those frames where the leaflet does not move fast. If you have training data (maybe a few dozens of CTs are sufficient) then you can do the training using MONAI or nn-UNet and use it in the MONAIAuto3DSeg or NNUNet Slicer extensions.</p>

---
