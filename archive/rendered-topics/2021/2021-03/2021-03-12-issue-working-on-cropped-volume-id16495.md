---
topic_id: 16495
title: "Issue Working On Cropped Volume"
date: 2021-03-12
url: https://discourse.slicer.org/t/16495
---

# Issue working on cropped volume

**Topic ID**: 16495
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/issue-working-on-cropped-volume/16495

---

## Post #1 by @mohammed_alshakhas (2021-03-12 14:44 UTC)

<p>when i crop volume i have the issue of including part of the cropped area<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c1e40cecf4ed3a60fb4a885086ecfbe6d61247d.jpeg" data-download-href="/uploads/short-url/d8UK9lPwZGACch2eUqKS4F0hoIt.jpeg?dl=1" title="Screen Shot 2021-03-12 at 17.42.09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c1e40cecf4ed3a60fb4a885086ecfbe6d61247d_2_690x388.jpeg" alt="Screen Shot 2021-03-12 at 17.42.09" data-base62-sha1="d8UK9lPwZGACch2eUqKS4F0hoIt" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c1e40cecf4ed3a60fb4a885086ecfbe6d61247d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c1e40cecf4ed3a60fb4a885086ecfbe6d61247d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c1e40cecf4ed3a60fb4a885086ecfbe6d61247d_2_1380x776.jpeg 2x" data-dominant-color="67595A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-12 at 17.42.09</span><span class="informations">1920×1080 394 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>so i end up with this segment</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/169c663380ba3292da34ec50b1594e70bc9de801.jpeg" data-download-href="/uploads/short-url/3e1AsOmymc7KKoQ2Ty4qhMCjDqh.jpeg?dl=1" title="Screen Shot 2021-03-12 at 17.41.34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/169c663380ba3292da34ec50b1594e70bc9de801_2_690x388.jpeg" alt="Screen Shot 2021-03-12 at 17.41.34" data-base62-sha1="3e1AsOmymc7KKoQ2Ty4qhMCjDqh" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/169c663380ba3292da34ec50b1594e70bc9de801_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/169c663380ba3292da34ec50b1594e70bc9de801_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/169c663380ba3292da34ec50b1594e70bc9de801_2_1380x776.jpeg 2x" data-dominant-color="6C675B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-12 at 17.41.34</span><span class="informations">1920×1080 405 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>any idea how can i get rid of this issue ?</p>

---

## Post #2 by @lassoan (2021-03-27 18:34 UTC)

<p>The segmentation extents and resolution are defined by the <em>first</em> selected master volume. You selected the full volume first, which was larger than the cropped volume. When you switched to the cropped volume as master the region of the segmentation that was outside the image assigned 0 intensity value by default, so that’s why thresholding with [-23; 32700] highlighted it.</p>
<p>An easy fix is to delete the segmentation node and create a new one, for that you choose the cropped volume as first master node.</p>
<p>I’ve also made a small fix in the Segment Editor, so by default a cropped volume is padded not with 0 anymore but with the value that is found in the image corners (in a CT image it is typically around -1000). This fix is available in Slicer Preview Releases downloaded tomorrow or later.</p>

---
