# Quantifying Mouse Lung microCT Scans

**Topic ID**: 14170
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/quantifying-mouse-lung-microct-scans/14170

---

## Post #1 by @DeeMos (2020-10-20 19:51 UTC)

<p>Hello. I have a series of mouse lung microCT scans that I’ve obtained using a Perkin Elmer microCT scanner. Using the DICOM files from these scans I am trying to quantify different aspects of the mouse lung; specifically lung density, capacity/function, inflammation, and airway structures using 3D Slicer. I’m not quite sure how to go about doing so…</p>
<p>From the tutorials I’ve figured out how to threshold the lungs using segment editor. From there I use Segment Statistics to calculate volume, surface area, number of voxels, and mean HU’s.</p>
<p>I’ve tried using the Chest Imaging Platform (CIP) but I’ve had no success thus far, mainly because the mouse CT scans aren’t detailed enough to show lung lobe fissures (used for lung lobe segmentation &amp; parenchyma analysis) and there is no trachea present on the scan as well (used for airway quantifications).</p>
<p>Any guidance you can give would be very much appreciated! I’ve attached a screenshot of a mouse lung microCT scan so that you can visualize the level of detail.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b850e868d54378766891fae1f8264d354beb62b1.png" data-download-href="/uploads/short-url/qixckiZyZ6ykRCU0Qkz2Aba1Csp.png?dl=1" title="Mouse microCT Lung Scan" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b850e868d54378766891fae1f8264d354beb62b1_2_619x500.png" alt="Mouse microCT Lung Scan" data-base62-sha1="qixckiZyZ6ykRCU0Qkz2Aba1Csp" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b850e868d54378766891fae1f8264d354beb62b1_2_619x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b850e868d54378766891fae1f8264d354beb62b1_2_928x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b850e868d54378766891fae1f8264d354beb62b1.png 2x" data-dominant-color="0F0D0D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Mouse microCT Lung Scan</span><span class="informations">982×793 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-09-08 01:58 UTC)

<p>It seems that this message fell through the cracks. Let us know if you still need help with this.</p>

---

## Post #3 by @DeeMos (2021-09-10 19:22 UTC)

<p>Hello Mr. Lasso,</p>
<p>Thank you for reaching out! I’ve made pretty good progress on this over time, but I do have some questions that hopefully you can help with me.</p>

---

## Post #4 by @djrowland (2021-09-10 20:05 UTC)

<p>Hi. I was watching for some replies to this. I will be needing to do a similar analysis in the near future. It would be great to know your workflow DeeMos. Please update this thread if possible. Or message me.</p>
<p>Thanks.<br>
Doug</p>

---

## Post #5 by @Riley_Hannan (2025-08-18 20:52 UTC)

<p>I recognize mouse CT is not a high-volume topic here, but will ping this thread again - asking for example workflows, bonus points if anyone has had success with automatic lung / thoracic / heart segmentation tools with small animal uCT. Trying to avoid manually segmenting dozens of lungs.</p>

---

## Post #6 by @pieper (2025-08-18 20:56 UTC)

<p>Did you see this work? <a href="https://journals.biologists.com/bio/article/12/2/bio059698/287076/Deep-learning-enabled-multi-organ-segmentation-of">https://journals.biologists.com/bio/article/12/2/bio059698/287076/Deep-learning-enabled-multi-organ-segmentation-of</a></p>
<p>Nowadays segmenting a dozen or so cases should be enough to train a similar segmenter (if the anatomy is pretty consistent you may need even less).</p>

---
