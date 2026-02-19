---
topic_id: 35755
title: "Broken Centerline Model With Continuous Voronoi Diagram"
date: 2024-04-26
url: https://discourse.slicer.org/t/35755
---

# Broken centerline model with continuous voronoi diagram

**Topic ID**: 35755
**Date**: 2024-04-26
**URL**: https://discourse.slicer.org/t/broken-centerline-model-with-continuous-voronoi-diagram/35755

---

## Post #1 by @ruili (2024-04-26 16:24 UTC)

<p>Hello,</p>
<p>I have been using the Extract Centerline module to extract the centerlines from some vessel segmentation. However, I have been struggling to get a fully connected centerline model even though the segmentation is all connected. In particular, I found on one vessel where the centerline model is broken even though the voronoi diagram seems all connected. I have attached a screenshot below, and you can find the mrb file of my scene here: <a href="https://drive.google.com/file/d/1UTtuBIo1IZPRGUIyXrbESuSGfNbuu9Uj/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">2024-04-26-Scene.mrb - Google Drive</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/165426fedc294e1290126e7a816750dc531baf3c.jpeg" data-download-href="/uploads/short-url/3bwNAJdTnx5rpVn3mM4kXDcD9fe.jpeg?dl=1" title="Screenshot 2024-04-26 at 17.09.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/165426fedc294e1290126e7a816750dc531baf3c_2_681x500.jpeg" alt="Screenshot 2024-04-26 at 17.09.27" data-base62-sha1="3bwNAJdTnx5rpVn3mM4kXDcD9fe" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/165426fedc294e1290126e7a816750dc531baf3c_2_681x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/165426fedc294e1290126e7a816750dc531baf3c_2_1021x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/165426fedc294e1290126e7a816750dc531baf3c.jpeg 2x" data-dominant-color="939BCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-26 at 17.09.27</span><span class="informations">1286×943 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone know why this is happening? I thought if the voronoi diagram seems to be connected, it means the centerline extraction algorithm can reach those regions and thus the centerline model should extend there as well. Many thanks in advance!</p>

---

## Post #2 by @chir.set (2024-04-27 08:23 UTC)

<p>Using ‘Smoothing / Fill holes’ with a kernel size of 0.3 mm, and using the sphere brush on the ignored part in 3D view, the centerline could be completely extracted, and the surface is not visually altered after smoothing.</p>

---

## Post #3 by @ruili (2024-04-27 11:11 UTC)

<p>Thanks! Do you mean using the “smoothing” tool from the segmentation editor as shown here:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ee6dcef76ed9f683bb11e4db1f19b76b6f484a.png" alt="Screenshot 2024-04-27 at 12.07.23" data-base62-sha1="exJ3tSX03jK8sKTJ5QN1Yl9CMCm" width="586" height="331"></p>
<p>You are right that after this smoothing, the surface is not visually altered, so it was diffitult to tell what I have done. I tried the setting shown in the screenshot, but I was still unable to extract that part. May I ask if you used a different setting?</p>

---

## Post #4 by @chir.set (2024-04-27 11:36 UTC)

<p>Click on ‘Edit in 3D views’ and use the brush in the 3D view to smooth only that part of the model with no centerline.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bc41574d28fed77a0bd871518d28ff1e653e172.png" data-download-href="/uploads/short-url/6faDBMUUCXdKRVvxRZZMvuZAhz4.png?dl=1" title="centerline_complete" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bc41574d28fed77a0bd871518d28ff1e653e172_2_648x500.png" alt="centerline_complete" data-base62-sha1="6faDBMUUCXdKRVvxRZZMvuZAhz4" width="648" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2bc41574d28fed77a0bd871518d28ff1e653e172_2_648x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bc41574d28fed77a0bd871518d28ff1e653e172.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bc41574d28fed77a0bd871518d28ff1e653e172.png 2x" data-dominant-color="0E180F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">centerline_complete</span><span class="informations">720×555 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
