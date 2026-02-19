---
topic_id: 46175
title: "Endless Loading In The Dental Segmentator"
date: 2026-02-16
url: https://discourse.slicer.org/t/46175
---

# endless loading in the dental segmentator 

**Topic ID**: 46175
**Date**: 2026-02-16
**URL**: https://discourse.slicer.org/t/endless-loading-in-the-dental-segmentator/46175

---

## Post #1 by @Imran (2026-02-16 14:21 UTC)

<p>I installed the dental segmentator extension to automatically segment the cbct. I download the cbct, click apply, and the download begins, which lasts indefinitely. nvidia rtx 4070 gpu. then I entered this command (slicer.util.pip_install(“acvl_utils==0.2”) into phyton and now I have a new problem, the program does not see the cuda drivers. help me pls</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8172d84cce850b7a4f1ca3a6269a3d5b093f8ca.jpeg" data-download-href="/uploads/short-url/x7aqKb4oDQgGBerbFMXx7GOFKWK.jpeg?dl=1" title="Снимок экрана 2026-02-15 031146" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8172d84cce850b7a4f1ca3a6269a3d5b093f8ca_2_690x431.jpeg" alt="Снимок экрана 2026-02-15 031146" data-base62-sha1="x7aqKb4oDQgGBerbFMXx7GOFKWK" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8172d84cce850b7a4f1ca3a6269a3d5b093f8ca_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8172d84cce850b7a4f1ca3a6269a3d5b093f8ca_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8172d84cce850b7a4f1ca3a6269a3d5b093f8ca_2_1380x862.jpeg 2x" data-dominant-color="7A7A79"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Снимок экрана 2026-02-15 031146</span><span class="informations">1920×1200 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Esteban_Barreiro (2026-02-17 09:53 UTC)

<p>Hi Imran.</p>
<p>The Troubleshooting for Total Segmentator works also for Dental Segmentator, you can find it on the Lasso’s GitHub page, heres the link:</p>
<p><a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#troubleshooting" rel="noopener nofollow ugc">https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#troubleshooting</a><br>
Probably you should:</p>
<ul>
<li>Install Nvidia Drivers</li>
<li>Download CUDA for that Drivers</li>
<li>Install Pytorch for that CUDA Version</li>
<li>Use Pytorch Utils Module to get everything working on 3dSlicer (a few Restarts required)</li>
</ul>
<p>Hope it helps.</p>

---
