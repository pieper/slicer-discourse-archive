---
topic_id: 33714
title: "1 Scissors Can T Conduct On 3D Model 2 How To Fill A Hollow"
date: 2024-01-10
url: https://discourse.slicer.org/t/33714
---

# 1-Scissors can’t conduct on 3D model. 2-how to fill a hollow vessel to solid

**Topic ID**: 33714
**Date**: 2024-01-10
**URL**: https://discourse.slicer.org/t/1-scissors-can-t-conduct-on-3d-model-2-how-to-fill-a-hollow-vessel-to-solid/33714

---

## Post #1 by @Cathy123 (2024-01-10 04:30 UTC)

<p>Hi everyone. I encountered some problem when i deal with the 3D vessel binary(mask) images. I try to use scissors to remove some part vessel. When I threshold it first, for the 2D images, the 1value parts have been selected(green parts in the 2D images below) However,in the 3D image the object was not shown green(it is the original one) it hasn’t been selected, so I can’t conduct scissor operation. I don’t know the reason and could you please give me some advice?<br>
2- the vessel is hollow and is there any quick method to fill it to solid?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a326bd09f2396ce6ccb06d96410298808ccc52d.jpeg" data-download-href="/uploads/short-url/m05yy8RtjzTfoqrJb3o0PfWayyV.jpeg?dl=1" title="IMG_0822" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a326bd09f2396ce6ccb06d96410298808ccc52d_2_619x500.jpeg" alt="IMG_0822" data-base62-sha1="m05yy8RtjzTfoqrJb3o0PfWayyV" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a326bd09f2396ce6ccb06d96410298808ccc52d_2_619x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a326bd09f2396ce6ccb06d96410298808ccc52d_2_928x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a326bd09f2396ce6ccb06d96410298808ccc52d_2_1238x1000.jpeg 2x" data-dominant-color="6C728B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0822</span><span class="informations">2776×2240 1.58 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2024-01-10 23:57 UTC)

<p>I suspect that you have a model shown in 3D rather than a representation of a segmentation.  Therefore, when you edit the segmentation, the segmentation is changed, but the model is unaffected.</p>
<p>To solidify the model, here are a few different segment editor approaches you could try to see which works best for you: Local Threshold, Wrap Solidify, and Smoothing → Close Holes.</p>

---
