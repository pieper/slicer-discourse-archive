# TotalSegmentator indicates that GTX 1060 GPU has not enough memory

**Topic ID**: 28766
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/totalsegmentator-indicates-that-gtx-1060-gpu-has-not-enough-memory/28766

---

## Post #1 by @kopachini (2023-02-22 17:18 UTC)

<p>Hello everyone,</p>
<p>first of all I must say that Total Segmentor is a game changer with it’s fast segmentation. GREAT JOB!!!</p>
<p>Second, I have a question… I have NVidia GTX 1060 graphic card with GPU memory 13.9 GB as in the pic1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e54d1fc5d8a995d159bd7676491ade5b9bca1df.jpeg" data-download-href="/uploads/short-url/mAFalxp6n46HkHeqXBapxJ2LovR.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e54d1fc5d8a995d159bd7676491ade5b9bca1df_2_560x500.jpeg" alt="1" data-base62-sha1="mAFalxp6n46HkHeqXBapxJ2LovR" width="560" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e54d1fc5d8a995d159bd7676491ade5b9bca1df_2_560x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e54d1fc5d8a995d159bd7676491ade5b9bca1df.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e54d1fc5d8a995d159bd7676491ade5b9bca1df.jpeg 2x" data-dominant-color="F4F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">768×685 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But when I start the segmentation it says that I need to change to “fast” mode because my computer has less than 7 GB GPU, although the integrated card has memory of 7.9 GB GPU, also.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8949ff83d4f648d17dea19df630a488d775bcc2b.jpeg" data-download-href="/uploads/short-url/jAvX7S7ZflXNUpJb0ku5wPdpdQT.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8949ff83d4f648d17dea19df630a488d775bcc2b_2_634x499.jpeg" alt="2" data-base62-sha1="jAvX7S7ZflXNUpJb0ku5wPdpdQT" width="634" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8949ff83d4f648d17dea19df630a488d775bcc2b_2_634x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8949ff83d4f648d17dea19df630a488d775bcc2b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8949ff83d4f648d17dea19df630a488d775bcc2b.jpeg 2x" data-dominant-color="66656A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">839×661 88.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What I have to change? I tried to set my settings that the Slicer app uses GPU and the same note showed…</p>

---

## Post #2 by @rbumm (2023-02-22 17:30 UTC)

<p>Hello,</p>
<p>The GTX 1060 has in fact  <a href="https://www.techpowerup.com/gpu-specs/geforce-gtx-1060-6-gb.c2862#:~:text=NVIDIA%20has%20paired%206%20GB,MHz%20(8%20Gbps%20effective).">6 GB VRAM</a> so the message is true. It´s also in your screenshot - see dedicated video memory.</p>
<p>You can check it with the NVIDIA Control Panel.</p>

---
