# Lung Vessel using CIP module

**Topic ID**: 28327
**Date**: 2023-03-12
**URL**: https://discourse.slicer.org/t/lung-vessel-using-cip-module/28327

---

## Post #1 by @Marcelinus_Raymond (2023-03-12 12:07 UTC)

<p>Hi,<br>
Im a med student and pretty new about 3D Slicer.<br>
I want to calculate lung vessel BV5/TBV and PA:A.<br>
Recently i have been read this journal, <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7173739/" rel="noopener nofollow ugc">Radiographic Pulmonary Vessel Volume, Lung Function, and Airways Disease in the Framingham Heart Study - PMC</a> as a reference, but i still don’t know how to do it.</p>
<p>Can you help me explain step by step how to generate 3d model of lung vessel using CIP module, then calculate BV5/TBV and PA:A?</p>
<p>Many thanks.</p>

---

## Post #2 by @rbumm (2023-03-12 18:14 UTC)

<p>Unfortunately, this can not be done out of the box with the current implementation of 3D Slicer CIP. <a class="mention" href="/u/raul">@raul</a>, cited in the above reference, most probably used specialized vessel segmentation software for his project in 2013.</p>
<p>You can, however, dig into the Lung CT Analyzer extension and create a vessel segmentation like this in 240 s on an appropriate hardware (no mouse clicks, with TotalSegmentator extended AI, using “lung_vessel” subtask ,  <a href="https://www.sciencedirect.com/science/article/pii/S0720048X22001097">cite</a> and <a href="https://academic.oup.com/bjs/article/108/Supplement_4/znab202.077/6287437">cite</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5d95b7cc393f51aee27e17345824defd3dc1c9e.jpeg" data-download-href="/uploads/short-url/wNl1EQD1Jb6rxZtEYbeP9MSofoO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5d95b7cc393f51aee27e17345824defd3dc1c9e_2_690x342.jpeg" alt="image" data-base62-sha1="wNl1EQD1Jb6rxZtEYbeP9MSofoO" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5d95b7cc393f51aee27e17345824defd3dc1c9e_2_690x342.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5d95b7cc393f51aee27e17345824defd3dc1c9e_2_1035x513.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5d95b7cc393f51aee27e17345824defd3dc1c9e.jpeg 2x" data-dominant-color="4A4748"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1320×655 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hope that gets you started.</p>

---
