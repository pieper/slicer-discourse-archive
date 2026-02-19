---
topic_id: 38540
title: "Lung Lobe Input Segment Is Missing"
date: 2024-09-25
url: https://discourse.slicer.org/t/38540
---

# Lung lobe input segment is missing

**Topic ID**: 38540
**Date**: 2024-09-25
**URL**: https://discourse.slicer.org/t/lung-lobe-input-segment-is-missing/38540

---

## Post #1 by @Daniel_Lo (2024-09-23 06:37 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27df21e0863819382c7316e2ae3945aa0373465e.png" data-download-href="/uploads/short-url/5GIGayfjdTWFG9TsWVyawsOpzgq.png?dl=1" title="Screenshot 2024-09-23 at 14.37.00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27df21e0863819382c7316e2ae3945aa0373465e_2_690x292.png" alt="Screenshot 2024-09-23 at 14.37.00" data-base62-sha1="5GIGayfjdTWFG9TsWVyawsOpzgq" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27df21e0863819382c7316e2ae3945aa0373465e_2_690x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27df21e0863819382c7316e2ae3945aa0373465e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27df21e0863819382c7316e2ae3945aa0373465e.png 2x" data-dominant-color="D6D4D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-09-23 at 14.37.00</span><span class="informations">836×354 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>how to solve this ? i was using AI mode</li>
<li>how to solve GPU issue with macos system, is this model only linked to pytorchCUDA?</li>
</ol>

---

## Post #2 by @Daniel_Lo (2024-09-25 19:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78290711f8e3a8ce59b6cf9f67a9bd5146d950a7.png" data-download-href="/uploads/short-url/h8Zcg2dtiW4F25uy3HS0aA0iQib.png?dl=1" title="Screenshot 2024-09-26 at 03.49.33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78290711f8e3a8ce59b6cf9f67a9bd5146d950a7_2_690x213.png" alt="Screenshot 2024-09-26 at 03.49.33" data-base62-sha1="h8Zcg2dtiW4F25uy3HS0aA0iQib" width="690" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78290711f8e3a8ce59b6cf9f67a9bd5146d950a7_2_690x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78290711f8e3a8ce59b6cf9f67a9bd5146d950a7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78290711f8e3a8ce59b6cf9f67a9bd5146d950a7.png 2x" data-dominant-color="DEDEDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-09-26 at 03.49.33</span><span class="informations">848×262 19.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
hi, any idea how to solve this ? i have tried to use interactive lobe segmentation, however doesnt solve this</p>

---

## Post #3 by @lassoan (2024-09-25 19:57 UTC)

<p>In general, macOS is still lagging behind in AI segmentation. CUDA is only available for NVIDIA GPUs, but macOS is not compatible with NVIDIA GPUs. If you use any AI models that require CUDA, they will not work on your macOS computer.</p>
<p>TotalSegmentator and MONAIAuto3DSeg works on all platforms. You can use these Slicer extensions to segment lung lobes. They work much faster with a discrete GPU, but they are usable without GPU, too.</p>

---

## Post #4 by @Daniel_Lo (2024-09-25 20:03 UTC)

<p>Thank you. my lung cases are generally pretty bad, consolidations and collapse are everywhere, even mediastinum are pulled over due to collapses. i wonder if those modules can sort it out. Let me try it out.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8c52a65f8734bdf08fecdeaf571df1b731a317a.jpeg" data-download-href="/uploads/short-url/qmyhm8nXLvrI8rsA3I74Vq0rNmW.jpeg?dl=1" title="Screenshot 2024-09-26 at 04.05.21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8c52a65f8734bdf08fecdeaf571df1b731a317a_2_690x222.jpeg" alt="Screenshot 2024-09-26 at 04.05.21" data-base62-sha1="qmyhm8nXLvrI8rsA3I74Vq0rNmW" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8c52a65f8734bdf08fecdeaf571df1b731a317a_2_690x222.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8c52a65f8734bdf08fecdeaf571df1b731a317a_2_1035x333.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8c52a65f8734bdf08fecdeaf571df1b731a317a_2_1380x444.jpeg 2x" data-dominant-color="D7D6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-09-26 at 04.05.21</span><span class="informations">2464×794 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> this happens for monai3Dautoseg<br>
total seg as well</p>

---

## Post #5 by @lassoan (2024-09-25 20:09 UTC)

<p>See trobleshooting instructions <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#troubleshooting">here</a>.</p>

---
