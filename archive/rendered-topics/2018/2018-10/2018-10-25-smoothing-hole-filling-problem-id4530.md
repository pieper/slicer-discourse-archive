---
topic_id: 4530
title: "Smoothing Hole Filling Problem"
date: 2018-10-25
url: https://discourse.slicer.org/t/4530
---

# Smoothing/ Hole Filling problem

**Topic ID**: 4530
**Date**: 2018-10-25
**URL**: https://discourse.slicer.org/t/smoothing-hole-filling-problem/4530

---

## Post #1 by @kantzoul (2018-10-25 18:37 UTC)

<p>Hi all,</p>
<p>So I am having trouble fixing some holes on my Tympanic membrane model. After using the closing holes option for smoothing in the segmentation editor, whilst some holes where repaired some still persist. I have attached a screenshot of these persistent holes.<br>
(upload://aj7bgFRxRORkFpJ4WSQD4RHRwUa.jpeg) <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c184c1ded24ebf1c2c3520feb98f74adaaa7b170.jpeg" data-download-href="/uploads/short-url/rBWA96rjl7ftH9Iljzm6rhSs9G0.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c184c1ded24ebf1c2c3520feb98f74adaaa7b170_2_690x333.jpeg" alt="PNG" data-base62-sha1="rBWA96rjl7ftH9Iljzm6rhSs9G0" width="690" height="333" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c184c1ded24ebf1c2c3520feb98f74adaaa7b170_2_690x333.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c184c1ded24ebf1c2c3520feb98f74adaaa7b170_2_1035x499.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c184c1ded24ebf1c2c3520feb98f74adaaa7b170_2_1380x666.jpeg 2x" data-dominant-color="BECD20"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1871×903 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ca38091be9a018edf2839f1c7a8b0ed5fa50b6d.jpeg" data-download-href="/uploads/short-url/6mTjfWp4HM3S9szEZY1idcVDgp7.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ca38091be9a018edf2839f1c7a8b0ed5fa50b6d_2_624x500.jpeg" alt="Capture2" data-base62-sha1="6mTjfWp4HM3S9szEZY1idcVDgp7" width="624" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ca38091be9a018edf2839f1c7a8b0ed5fa50b6d_2_624x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ca38091be9a018edf2839f1c7a8b0ed5fa50b6d_2_936x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ca38091be9a018edf2839f1c7a8b0ed5fa50b6d_2_1248x1000.jpeg 2x" data-dominant-color="AFC036"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1455×775 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> ![Capture7|550x500]<br>
As well as the TM, other segments of the model have gaps inside the segmentations that need to be closed. I have attached screen shots as well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6655c4354715521b9844774a0a2efc254d85986c.png" data-download-href="/uploads/short-url/eBisfPC2IEygjSMK312yMDjgcTq.png?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6655c4354715521b9844774a0a2efc254d85986c.png" alt="PNG" data-base62-sha1="eBisfPC2IEygjSMK312yMDjgcTq" width="690" height="334" data-dominant-color="261511"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">837×760 2.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a9be8640a6da0407c264a888900570c8505b896.png" data-download-href="/uploads/short-url/8mtITEOaWfxkcAtDITrCWTwkLfU.png?dl=1" title="Capture8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a9be8640a6da0407c264a888900570c8505b896.png" alt="Capture8" data-base62-sha1="8mtITEOaWfxkcAtDITrCWTwkLfU" width="458" height="500" data-dominant-color="455B43"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture8</span><span class="informations">771×841 3.18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Any thoughts on how to close all these holes? As fore mentioned the closing holes function has improved the situation but seems to only be able to go so far.</p>

---

## Post #2 by @lassoan (2018-10-26 03:53 UTC)

<p>You may increase the kernel size in Smoothing effect to fill larger holes. If large kernel would alter the volume too much then you may need to fill those large holes manually (with Paint effect).</p>
<p>You may also try to slightly reduce smoothing factor that is used for creating closed surface representation from binary labelmap representation (you can access it by clicking the small down arrow button on “Show 3D” button then click on “Set surface smoothing” and adjust the value).</p>
<p>Reducing voxel size in segmentation node may help, too.</p>

---

## Post #3 by @Izere_Lys_Delicia (2023-12-04 08:55 UTC)

<p>Hi,<br>
i am currently segmenting cartilage of two bones and i am having a similar issue. To give context, i manually segmented the cartilage of the two bones and to get rid of overlapping between the two cartilages, i used the subtraction logical operator. It then left the segments with holes, which led me to use the smoothing method ‘closing holes’. However, some holes persisted, which then led me to manually fill them (as you suggested). My only issue is, filling them in manually cause overlapping between the cartilages which is undesirable, and when i reuse the subtraction logical operator, holes reappear . Any tips to fix that?</p>

---
