---
topic_id: 24701
title: "How To Fill Small Holes In Segmentations"
date: 2022-08-09
url: https://discourse.slicer.org/t/24701
---

# How to fill small holes in segmentations

**Topic ID**: 24701
**Date**: 2022-08-09
**URL**: https://discourse.slicer.org/t/how-to-fill-small-holes-in-segmentations/24701

---

## Post #1 by @tomdillon97 (2022-08-09 22:37 UTC)

<p>Hi,</p>
<p>I’m having trouble filling the small voids in this model. I’ve tried using the “closing” operation as visualized in the photo, though it seems to have no effect. Does anyone know of alternative tools I could use here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e34e3c602f6b02fe4ef805845ea3252ed11ae87.jpeg" data-download-href="/uploads/short-url/4jdDFCm7NuGiMyIwL0WAcdrRnjF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e34e3c602f6b02fe4ef805845ea3252ed11ae87_2_690x370.jpeg" alt="image" data-base62-sha1="4jdDFCm7NuGiMyIwL0WAcdrRnjF" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e34e3c602f6b02fe4ef805845ea3252ed11ae87_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e34e3c602f6b02fe4ef805845ea3252ed11ae87_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e34e3c602f6b02fe4ef805845ea3252ed11ae87_2_1380x740.jpeg 2x" data-dominant-color="C1C0D9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks so much<br>
Tom</p>

---

## Post #2 by @lassoan (2022-08-09 22:38 UTC)

<p>Smoothing effect’s “closing” operation should work well, just make sure to reset masking settings (allow editing everywhere by turning off editable intensity range, etc.).</p>

---

## Post #3 by @jay1987 (2022-08-10 01:57 UTC)

<p>you can try margin effect , [shrink] and [grow]</p>

---

## Post #4 by @lassoan (2022-08-10 09:44 UTC)

<p>It’s true that morphological closing is closely related to shrinking and growing, but their order matters.</p>
<p>Closing: dilation (growing) followed by erosion (shrinking) - it fills holes. Opening: erosion followed by shrinking - it removes small extrusions.</p>

---

## Post #5 by @jay1987 (2022-08-10 11:42 UTC)

<p>you are right lasso<br>
if only for exhibition,can use margin effect<br>
it’s not appropriate for caculation</p>

---

## Post #6 by @chir.set (2022-08-10 11:51 UTC)

<p>Try with greater kernel size… 12 … 18…</p>
<p>It will be a lengthy processing; you could save time using the sphere brush in slice views or 3D views. It should be doable.</p>

---

## Post #7 by @lassoan (2022-08-11 20:46 UTC)

<p>You’ve raised a very good point. If you want to use a very large kernel (20-30 pixels) then Smoothing effect’s Closing operation will be very slow. However, if you perform Margin effect’s grow operation and then shrink operation as <a class="mention" href="/u/jay1987">@jay1987</a> suggested then you’ll get the same output as from a closing operation; but it will be hundreds of times faster (because margin effect uses a distance map instead of a kernel to dilate and erode).</p>

---

## Post #8 by @chir.set (2022-08-12 08:36 UTC)

<p>The speed benefit of Margin’s Grow/Shrink is indeed confirmed.</p>
<p>However, the final result is less precise, please compare the second and third images below :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f448b47488525df304a6603c852578f33dd3d03.png" data-download-href="/uploads/short-url/i9RuBP4Sdb0SD3Ch61Apqkl6TXZ.png?dl=1" title="holes_0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f448b47488525df304a6603c852578f33dd3d03_2_501x500.png" alt="holes_0" data-base62-sha1="i9RuBP4Sdb0SD3Ch61Apqkl6TXZ" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f448b47488525df304a6603c852578f33dd3d03_2_501x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f448b47488525df304a6603c852578f33dd3d03.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f448b47488525df304a6603c852578f33dd3d03.png 2x" data-dominant-color="222522"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">holes_0</span><span class="informations">627×625 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02a2d3cfd0867eda47b7480c81b73a3ef506868.png" data-download-href="/uploads/short-url/mQSL1wjAEQQWnubRr8HX1T36Ms0.png?dl=1" title="holes_grow_shrink" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02a2d3cfd0867eda47b7480c81b73a3ef506868_2_501x500.png" alt="holes_grow_shrink" data-base62-sha1="mQSL1wjAEQQWnubRr8HX1T36Ms0" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02a2d3cfd0867eda47b7480c81b73a3ef506868_2_501x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02a2d3cfd0867eda47b7480c81b73a3ef506868.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02a2d3cfd0867eda47b7480c81b73a3ef506868.png 2x" data-dominant-color="222622"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">holes_grow_shrink</span><span class="informations">627×625 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5d6e1a58f1ddcc27fff7071a0cd55826a8aabb.png" data-download-href="/uploads/short-url/kjpYnt6kk2WQ1quxDvDMIVjkLvd.png?dl=1" title="holes_smoothing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5d6e1a58f1ddcc27fff7071a0cd55826a8aabb_2_501x500.png" alt="holes_smoothing" data-base62-sha1="kjpYnt6kk2WQ1quxDvDMIVjkLvd" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5d6e1a58f1ddcc27fff7071a0cd55826a8aabb_2_501x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5d6e1a58f1ddcc27fff7071a0cd55826a8aabb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5d6e1a58f1ddcc27fff7071a0cd55826a8aabb.png 2x" data-dominant-color="222522"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">holes_smoothing</span><span class="informations">627×625 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2022-08-13 20:57 UTC)

<p>The result should be about the same (maybe the boundary may differ by 1-2 voxels). Note that margin size (it is a radius) is half of the closing kernel size (it is a diameter).</p>

---
