# OutOfMemoryError: CUDA out of memory TotalSegmentator

**Topic ID**: 28697
**Date**: 2023-03-31
**URL**: https://discourse.slicer.org/t/outofmemoryerror-cuda-out-of-memory-totalsegmentator/28697

---

## Post #1 by @NicoV (2023-03-31 13:57 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.2.2<br>
Expected behavior: TotalSegmentator full resolution segmentation with GPU 8Gb (NVIDIA)<br>
Actual behavior: semgmentation fails due to “OutOfMemoryError: CUDA out of memory”, seems to result from preprocessing crop of CT images (509 in that case). Lower croping makes the process succeed (around 250).<br>
How does it work and is it possible to edit this parameter in TotalSegmentator.<br>
One 16 Gb GPU is best but we can read that 8Gb is also sufficient (our IT dept did not offer the first one…).<br>
Thank you for your help,<br>
nicolas</p>

---

## Post #2 by @rbumm (2023-04-02 13:03 UTC)

<p>Does it work with the CTs from the Sample datasets?</p>

---

## Post #3 by @NicoV (2023-04-04 10:48 UTC)

<p>Hi Rudolf,</p>
<p>Yes ! thanks for the tip.</p>
<p>As consequence, the resolution is lowered with this CT (2.2 vs 0.9 mm). With the high resolution of segmentation (1.5mm vs 3mm), it could be worth being quantified, nevertheless.</p>
<p>Anyway, we are not blocked anymore and that is the most important, I would say!</p>
<p>Nevertheless, do you have any clue on how the resampling operate within TotalSegmentator?</p>
<p>Thank a lot for your help and answering,</p>
<p>Best regards,</p>
<p>Nicolas</p>

---

## Post #4 by @lassoan (2023-04-04 13:06 UTC)

<p>You can crop and/or resample the volume on the CPU using <strong>Crop volume</strong> module before you run Total Segmentator on it.</p>

---

## Post #5 by @NicoV (2023-04-04 14:29 UTC)

<p>Thanks Andras,</p>
<p>It works pretty well and ensure to perform TotalSegmentator on the high-resolution CT (relatively).</p>
<p>And this remains a quick pre-processing step.</p>
<p>Best regards,</p>
<p>nicolas</p>

---

## Post #6 by @NicoV (2023-04-04 14:59 UTC)

<p>Concerning TotalSegmentator, just a quick wondering, any idea why the sternum is not included?</p>
<p>BR,</p>
<p>NV</p>

---

## Post #7 by @rbumm (2023-04-04 16:10 UTC)

<p>There is a preview circulating with sternum already, it will probably soon be integrated.<br>
Best, r</p>

---

## Post #8 by @lassoan (2023-04-04 16:16 UTC)

<p>The latest TotalSegmentator model includes the sternum, but I don’t think it has been publicly released yet.</p>

---
