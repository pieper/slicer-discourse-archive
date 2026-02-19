---
topic_id: 41493
title: "Pytorch 2 6 Seems To Break Totalsegmentor"
date: 2025-02-04
url: https://discourse.slicer.org/t/41493
---

# PyTorch 2.6 seems to break TotalSegmentor 

**Topic ID**: 41493
**Date**: 2025-02-04
**URL**: https://discourse.slicer.org/t/pytorch-2-6-seems-to-break-totalsegmentor/41493

---

## Post #1 by @Michael_Stuart (2025-02-04 16:28 UTC)

<p>I was using TotalSegmentor with significant effect for reviewing my spinal fusion surgeries, but the extension stopped working after recent PyTorch 2.6 update. Both on my laptop (fast mode) and Workstation (RTX 3070 GPU).</p>

---

## Post #2 by @jamesobutler (2025-02-04 16:38 UTC)

<p>The developer of nnUNetv2 (a dependency of TotalSegmentator) issued a fix earlier today. Please try going to the “nnUNet” module in Slicer and specifying to install nnUNet &gt;=2.5.2.</p>
<p>Let us know how it goes for you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cfbc59a338afec4e952b92e18e5e147a7c425d5.png" data-download-href="/uploads/short-url/hPECKV9NnJCZuYpehgnleYGg3FX.png?dl=1" title="{15F668A2-77BE-4F91-B30C-35B2D0AF80C6}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7cfbc59a338afec4e952b92e18e5e147a7c425d5.png" alt="{15F668A2-77BE-4F91-B30C-35B2D0AF80C6}" data-base62-sha1="hPECKV9NnJCZuYpehgnleYGg3FX" width="414" height="254"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{15F668A2-77BE-4F91-B30C-35B2D0AF80C6}</span><span class="informations">414×254 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
