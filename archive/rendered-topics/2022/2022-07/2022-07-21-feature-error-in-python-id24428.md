---
topic_id: 24428
title: "Feature Error In Python"
date: 2022-07-21
url: https://discourse.slicer.org/t/24428
---

# Feature Error in python

**Topic ID**: 24428
**Date**: 2022-07-21
**URL**: https://discourse.slicer.org/t/feature-error-in-python/24428

---

## Post #1 by @Van_Tran_Sang_Huynh (2022-07-21 08:56 UTC)

<p>I use python pyrradiomics to extract features for .nrrd images. And I got an error…<br>
how can i fix it. Please help!!!<br>
Respect<br>
Sang<br>
I use code<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/777318878b6693695a64b1eb8b5ea3c5b3d63ec8.png" data-download-href="/uploads/short-url/h2HpsueJyKoCFmcvbe82VsvYkQg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777318878b6693695a64b1eb8b5ea3c5b3d63ec8_2_690x388.png" alt="image" data-base62-sha1="h2HpsueJyKoCFmcvbe82VsvYkQg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777318878b6693695a64b1eb8b5ea3c5b3d63ec8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777318878b6693695a64b1eb8b5ea3c5b3d63ec8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/777318878b6693695a64b1eb8b5ea3c5b3d63ec8_2_1380x776.png 2x" data-dominant-color="FAF9F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
And error…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61a824f1f0d84736c7ae7d61f35980a20656a704.png" data-download-href="/uploads/short-url/dVUyQZ14BD1fDVfkumEiSCXOPT6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61a824f1f0d84736c7ae7d61f35980a20656a704_2_690x388.png" alt="image" data-base62-sha1="dVUyQZ14BD1fDVfkumEiSCXOPT6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61a824f1f0d84736c7ae7d61f35980a20656a704_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61a824f1f0d84736c7ae7d61f35980a20656a704_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61a824f1f0d84736c7ae7d61f35980a20656a704_2_1380x776.png 2x" data-dominant-color="FDFCFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @edwardwang1 (2022-07-21 17:23 UTC)

<p>Hi Sang,</p>
<p>It looks to me like you are trying to assign a single file path (Lung-001.nrrd) to both imagePath and maskPath. What is your the path to your mask?</p>
<p>imagePath, maksPath  = “C:/Users/Admin/Downloads/LUNG1-001.nrrd”, PATH_TO_MASK</p>

---
