---
topic_id: 32407
title: "3D View Rendering Order Issue"
date: 2023-10-25
url: https://discourse.slicer.org/t/32407
---

# 3D view rendering order issue

**Topic ID**: 32407
**Date**: 2023-10-25
**URL**: https://discourse.slicer.org/t/3d-view-rendering-order-issue/32407

---

## Post #1 by @ffr (2023-10-25 04:24 UTC)

<p>Hello,</p>
<p>Please see the two ‘gif’ videos attached. The rendering order is wrong in the first video. They are showing the same content. May I ask how to reset the 3D view? What may cause this issue? Thank you.</p>
<p>Best,<br>
Ray</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fcd96cd8d122547ceeaaefe75f017dd28b7bf66.gif" alt="SlicerCapture" data-base62-sha1="kw8KycHzAmtKqEbtgAH3I9nVWXI" width="690" height="302" class="animated"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c49074f0a43378a7b327ccec1efaca4749b507e7.gif" alt="SlicerCapture2" data-base62-sha1="s2T53a6eq6JgVF3NyHYkx65OeTt" width="690" height="303" class="animated"></p>

---

## Post #2 by @muratmaga (2023-10-25 04:37 UTC)

<p>First one looks like the multivolume rendering bug in default GPURaycasting. But these are slice views, and I cannot replicate what you are seeing with sample data.</p>
<p>Can you tell us how you made the first one?</p>

---

## Post #3 by @ffr (2023-10-25 05:01 UTC)

<p>Thank you Murat, I also don’t know how this happened. I have been using 3D Slicer for a while and this is the first time I encountered this issue. I have tried to delete this problematic 3D view and reopen it but it did not fix it. The screenshot below is the dual 3D layout with the problematic 3D view on the left. The newly created 3D view does not have the issue. May I ask how to reset a 3D view setting?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a747c5aad440e4e7b01d15014ace14788c711fa6.jpeg" data-download-href="/uploads/short-url/nRPvxidvLaG75oimOB0YgTlds90.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a747c5aad440e4e7b01d15014ace14788c711fa6_2_690x314.jpeg" alt="Screenshot" data-base62-sha1="nRPvxidvLaG75oimOB0YgTlds90" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a747c5aad440e4e7b01d15014ace14788c711fa6_2_690x314.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a747c5aad440e4e7b01d15014ace14788c711fa6_2_1035x471.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a747c5aad440e4e7b01d15014ace14788c711fa6_2_1380x628.jpeg 2x" data-dominant-color="65667F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1920×876 73.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @ffr (2023-10-25 18:58 UTC)

<p>I deleted the current camera of this view in the camera module and it fixed the issue.</p>

---
