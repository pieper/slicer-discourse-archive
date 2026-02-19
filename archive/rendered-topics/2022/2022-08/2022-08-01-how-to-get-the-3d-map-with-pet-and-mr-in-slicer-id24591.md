---
topic_id: 24591
title: "How To Get The 3D Map With Pet And Mr In Slicer"
date: 2022-08-01
url: https://discourse.slicer.org/t/24591
---

# How to get the 3D map with PET and MR in Slicer

**Topic ID**: 24591
**Date**: 2022-08-01
**URL**: https://discourse.slicer.org/t/how-to-get-the-3d-map-with-pet-and-mr-in-slicer/24591

---

## Post #1 by @slicer365 (2022-08-01 13:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6eba7d04d37ab1039b087a56ba51fb3ea289f61.jpeg" data-download-href="/uploads/short-url/zemlxfbFrNDV1XmekCIDQ1Ys50d.jpeg?dl=1" title="微信图片_20220731214903" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6eba7d04d37ab1039b087a56ba51fb3ea289f61_2_516x192.jpeg" alt="微信图片_20220731214903" data-base62-sha1="zemlxfbFrNDV1XmekCIDQ1Ys50d" width="516" height="192" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6eba7d04d37ab1039b087a56ba51fb3ea289f61_2_516x192.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6eba7d04d37ab1039b087a56ba51fb3ea289f61_2_774x288.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6eba7d04d37ab1039b087a56ba51fb3ea289f61_2_1032x384.jpeg 2x" data-dominant-color="414330"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20220731214903</span><span class="informations">1206×450 68.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How  to use  slicer get the result like the above picture,it  used PET-CT.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/195b6e8c7d292bfe57d0881a8c76022d0db4bf94.png" data-download-href="/uploads/short-url/3CjPmY7sBvaGS2sKFdgAfeQCut6.png?dl=1" title="1659275425770" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/195b6e8c7d292bfe57d0881a8c76022d0db4bf94_2_517x200.png" alt="1659275425770" data-base62-sha1="3CjPmY7sBvaGS2sKFdgAfeQCut6" width="517" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/195b6e8c7d292bfe57d0881a8c76022d0db4bf94_2_517x200.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/195b6e8c7d292bfe57d0881a8c76022d0db4bf94_2_775x300.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/195b6e8c7d292bfe57d0881a8c76022d0db4bf94.png 2x" data-dominant-color="5E535E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1659275425770</span><span class="informations">1013×392 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-08-01 17:14 UTC)

<p>This module should do what you are asking for:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/probevolumewithmodel.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/probevolumewithmodel.html</a></p>

---

## Post #3 by @slicer365 (2022-08-01 22:11 UTC)

<p>Thank you very much for your answer, yes, I know about this module, but this model just adjusts the surface of the brain, when I use Easy Clip to crop the brain, the inside of it doesn’t change very well.</p>

---

## Post #4 by @pieper (2022-08-02 15:22 UTC)

<p>you probably need to re-run after clipping to sample the volume at the new coordinates.  The clipped surface may have few vertices though so it may not work well, is that what you mean?  maybe a picture would help explain.</p>

---

## Post #5 by @slicer365 (2022-08-03 05:36 UTC)

<p>Thank you !  As you see,this picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520cbf424a203c9ce0b9657cff362a3e74acb889.jpeg" data-download-href="/uploads/short-url/bHQsIfnNfk44g8aGWwSMBZK3Dv3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520cbf424a203c9ce0b9657cff362a3e74acb889_2_345x172.jpeg" alt="image" data-base62-sha1="bHQsIfnNfk44g8aGWwSMBZK3Dv3" width="345" height="172" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520cbf424a203c9ce0b9657cff362a3e74acb889_2_345x172.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520cbf424a203c9ce0b9657cff362a3e74acb889_2_517x258.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/520cbf424a203c9ce0b9657cff362a3e74acb889_2_690x344.jpeg 2x" data-dominant-color="CCACCC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1851×927 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This color is not very smooth!<br>
Difficulty identifying abnormal metabolic structures</p>

---

## Post #6 by @slicer365 (2022-08-03 05:37 UTC)

<p>Is it because my model is not standard enough?</p>

---

## Post #7 by @pieper (2022-08-03 13:39 UTC)

<p>I see - yes, if you go to the Models module Display section you can turn on display of the edges and you’ll see those are large polygons in the cut part so the volume is not sampled well.</p>
<p>There may be other options, but one approach could be to import the clipped model into a segmentation (right click on model in data module), then re-export it as a model (right click on segmentation or use the Segmentations module) and the re-run the Probe module.  Converting the segmentation back to a model should have more vertices on the cut plane, but they may get optimized out so you might have to adjust the advanced parameters.</p>

---
