---
topic_id: 12824
title: "Centerline Problem"
date: 2020-08-03
url: https://discourse.slicer.org/t/12824
---

# Centerline problem

**Topic ID**: 12824
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/centerline-problem/12824

---

## Post #1 by @Romeo_Guevara (2020-08-03 01:24 UTC)

<p>Good evening, I wanted to report that the “extract centerline” module is not working properly, it is not recognizing the “endpoints” well, sometimes it recognizes them and sometimes not, this did not happen a few days ago, please help<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfb17d3ae775e0b60184261cf65707efecb57871.png" data-download-href="/uploads/short-url/tDl6wnuL7tpESQp8wnC70zbZk9b.png?dl=1" title="2020-08-02 (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfb17d3ae775e0b60184261cf65707efecb57871_2_690x369.png" alt="2020-08-02 (2)" data-base62-sha1="tDl6wnuL7tpESQp8wnC70zbZk9b" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfb17d3ae775e0b60184261cf65707efecb57871_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfb17d3ae775e0b60184261cf65707efecb57871_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfb17d3ae775e0b60184261cf65707efecb57871_2_1380x738.png 2x" data-dominant-color="B9BCD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-08-02 (2)</span><span class="informations">1920×1027 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-08-03 02:35 UTC)

<p>There has not been any change in VMTK extension recently, so most likely the issues are due to the data. In the screenshots above, the segmentation contains a couple of noisy non-vessel regions, which may prevent the algorithm from working properly. If you use Local thresholding method for vessel extraction then increase minimum diameter and/or lower threshold value. If you still have issues then share the segmentation that you think should work well but it does not.</p>

---
