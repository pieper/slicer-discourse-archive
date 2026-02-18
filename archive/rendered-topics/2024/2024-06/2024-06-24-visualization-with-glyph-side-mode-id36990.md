# Visualization with Glyph Side mode

**Topic ID**: 36990
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/visualization-with-glyph-side-mode/36990

---

## Post #1 by @capucinelab (2024-06-24 20:31 UTC)

<p>Hello,<br>
I would like to have more details about the use of the color map visualization with the Glyph Side mode, on human skull scans. Is there a way to reduce the number of arrows, and choose to have them localized only on my region of interest (in this case the maxilla, on almost the entire scan)?</p>
<p>Thanks in advance for your feedback!</p>

---

## Post #2 by @muratmaga (2024-06-24 20:35 UTC)

<p>Most, if not, all of this is possible. Have you look in the details of Transforms module?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a11df7c6724712ff3ef2761041078306e6b3b30.png" data-download-href="/uploads/short-url/azfCMvoE2cj89KJlpjnwdLw2yXe.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a11df7c6724712ff3ef2761041078306e6b3b30_2_409x500.png" alt="image" data-base62-sha1="azfCMvoE2cj89KJlpjnwdLw2yXe" width="409" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a11df7c6724712ff3ef2761041078306e6b3b30_2_409x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a11df7c6724712ff3ef2761041078306e6b3b30_2_613x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a11df7c6724712ff3ef2761041078306e6b3b30_2_818x1000.png 2x" data-dominant-color="E0E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">896×1094 81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @capucinelab (2024-06-25 09:05 UTC)

<p>I’ve taken a closer look at the Transform module.</p>
<p>I can reduce the number of arrows, but I can’t choose which ones to remove. I’d like to remove the superfluous arrows around the skull and keep only those present on the maxilla, but the module removes as many on the maxilla as around the skull …</p>
<p>Do you know how to interpret these arrows?</p>
<p>Thanks a lot!</p>
<p>Capucine</p>

---

## Post #4 by @capucinelab (2024-06-25 09:39 UTC)

<p>for greater visibility, I’ve taken a screenshot. It’s the arrows around the skull that I’d like to remove, while keeping the ones on the skull. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d942f15460838030fe7539ed8e7ef8ecaf3a65d0.jpeg" data-download-href="/uploads/short-url/uZZ2b6ABBAntVjcrEElu1Zdxh4I.jpeg?dl=1" title="Capture d’écran 2024-06-25 à 11.37.25.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d942f15460838030fe7539ed8e7ef8ecaf3a65d0_2_410x256.jpeg" data-base62-sha1="uZZ2b6ABBAntVjcrEElu1Zdxh4I" alt="Capture d’écran 2024-06-25 à 11.37.25.png" width="410" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d942f15460838030fe7539ed8e7ef8ecaf3a65d0_2_410x256.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d942f15460838030fe7539ed8e7ef8ecaf3a65d0_2_615x384.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d942f15460838030fe7539ed8e7ef8ecaf3a65d0_2_820x512.jpeg 2x" data-dominant-color="B3B5D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-06-25 à 11.37.25.png</span><span class="informations">2880×1800 473 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2024-06-25 16:02 UTC)

<aside class="quote no-group" data-username="capucinelab" data-post="3" data-topic="36990">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ecccb3/48.png" class="avatar"> capucinelab:</div>
<blockquote>
<p>Do you know how to interpret these arrows?</p>
</blockquote>
</aside>
<p>Please read this section carefully:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html</a></p>
<p>You can create a ROI markup, and have the visualization constrain to its contents.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50c5ad77c505e4de0958cb42172e0affd59ff8ab.png" data-download-href="/uploads/short-url/bwxIDwvlRLBNN4Lh2x1M0R2Rr5N.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50c5ad77c505e4de0958cb42172e0affd59ff8ab_2_690x340.png" alt="image" data-base62-sha1="bwxIDwvlRLBNN4Lh2x1M0R2Rr5N" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50c5ad77c505e4de0958cb42172e0affd59ff8ab_2_690x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50c5ad77c505e4de0958cb42172e0affd59ff8ab_2_1035x510.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50c5ad77c505e4de0958cb42172e0affd59ff8ab_2_1380x680.png 2x" data-dominant-color="B4AEBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2458×1214 472 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @capucinelab (2024-07-08 12:12 UTC)

<p>Sorry for the late reply</p>
<p>My 3D Slicer doesn’t offer me to create my ROI, it only offers me that, knowing that 15FEMME and 15HOMME correspond to my initial scans, and 15_volume_carte to the use of registration just before.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e2ef112510d05c96bf71e94b7e01584be2dac82.jpeg" data-download-href="/uploads/short-url/fIJ5OKqCJQ9iwAlYb7qMIaZKVXQ.jpeg?dl=1" title="Capture d’écran 2024-07-08 à 14.09.41.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2ef112510d05c96bf71e94b7e01584be2dac82_2_690x431.jpeg" alt="Capture d’écran 2024-07-08 à 14.09.41.jpg" data-base62-sha1="fIJ5OKqCJQ9iwAlYb7qMIaZKVXQ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2ef112510d05c96bf71e94b7e01584be2dac82_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2ef112510d05c96bf71e94b7e01584be2dac82_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e2ef112510d05c96bf71e94b7e01584be2dac82_2_1380x862.jpeg 2x" data-dominant-color="AFAFAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-08 à 14.09.41.jpg</span><span class="informations">2880×1800 674 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @capucinelab (2024-07-08 12:23 UTC)

<p>I can set up an ROI, but through the converses module, I don’t know if that’s what you meant.</p>
<p>However, I still have arrows that aren’t really on my region of interest.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/633cac7a583524460fc460f85861f5c96a0f0e4b.jpeg" data-download-href="/uploads/short-url/e9TggVbIbQzTTRftNcfrTRo44ht.jpeg?dl=1" title="Capture d’écran 2024-07-08 à 14.21.05.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633cac7a583524460fc460f85861f5c96a0f0e4b_2_690x431.jpeg" alt="Capture d’écran 2024-07-08 à 14.21.05.jpg" data-base62-sha1="e9TggVbIbQzTTRftNcfrTRo44ht" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633cac7a583524460fc460f85861f5c96a0f0e4b_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633cac7a583524460fc460f85861f5c96a0f0e4b_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633cac7a583524460fc460f85861f5c96a0f0e4b_2_1380x862.jpeg 2x" data-dominant-color="AEAFC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-08 à 14.21.05.jpg</span><span class="informations">2880×1800 526 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2024-07-08 15:18 UTC)

<p>Notice that arrows are now only inside he ROI. You can adjust the ROI to match where you would like those glyphs to be displayed.</p>

---
