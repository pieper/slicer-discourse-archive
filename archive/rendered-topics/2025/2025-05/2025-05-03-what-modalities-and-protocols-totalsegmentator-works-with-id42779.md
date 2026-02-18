# What modalities and protocols TotalSegmentator works with?

**Topic ID**: 42779
**Date**: 2025-05-03
**URL**: https://discourse.slicer.org/t/what-modalities-and-protocols-totalsegmentator-works-with/42779

---

## Post #1 by @angeek (2025-05-03 07:04 UTC)

<p>Hello, is there any specific recommendations concerning the modality.<br>
Does TotalSegmentator work well on CT Scans with/without injection, and for MRI, which kind is prefered (T1,T2,STIR,Flair,inPhase) ?<br>
Thanks</p>

---

## Post #2 by @lassoan (2025-05-03 14:42 UTC)

<p>TotalSegmentator models were trained on images acquired with a wide variety of imaging protocols, with/without contrast agent, etc. and the models are expected to generalize well enough to work beyond the exact protocols used in the training data. So, in general, the models should work on anything. Probably the best you can do is to try it on all your images to see what gives you the best performance.</p>
<p>That said, it is likely that you get better results on images that are more similar to the <a href="https://arxiv.org/pdf/2405.19492">training data sets</a>. For example, for MRI:</p>
<blockquote>
<p>The dataset contained a wide variety of MRI<br>
examinations, with differences in contrast, section thickness, field strength, pulse sequences (e.g. T1-weighted, T2-weighted, Proton Density), echo time, repetition time, resolution, and contrast agent.</p>
</blockquote>

---

## Post #3 by @lassoan (2025-05-04 22:27 UTC)

<p>A post was split to a new topic: <a href="/t/3d-print-shoulder-muscles-based-on-mri/42788">3D print shoulder muscles based on MRI</a></p>

---
