---
topic_id: 32916
title: "Remove Unwanted Areas Hip And Knee Joint Model"
date: 2023-11-20
url: https://discourse.slicer.org/t/32916
---

# Remove Unwanted Areas - Hip and Knee Joint Model

**Topic ID**: 32916
**Date**: 2023-11-20
**URL**: https://discourse.slicer.org/t/remove-unwanted-areas-hip-and-knee-joint-model/32916

---

## Post #1 by @hd00561 (2023-11-20 23:03 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/256912f8fad9db58a60d5615f89c78e3a2f920b9.png" alt="image" data-base62-sha1="5kWMLTkhfSBaNKcosWGEF1DOPgd" width="150" height="383"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c27e1ef604c63fc2b889d7821ecc451fc9e31751.jpeg" data-download-href="/uploads/short-url/rKyQdb3pQdA1DfuIgQNDGg3s9sl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27e1ef604c63fc2b889d7821ecc451fc9e31751_2_690x353.jpeg" alt="image" data-base62-sha1="rKyQdb3pQdA1DfuIgQNDGg3s9sl" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27e1ef604c63fc2b889d7821ecc451fc9e31751_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27e1ef604c63fc2b889d7821ecc451fc9e31751_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c27e1ef604c63fc2b889d7821ecc451fc9e31751_2_1380x706.jpeg 2x" data-dominant-color="909199"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1874×961 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi there,</p>
<p>I am required to create a 3D model of the hip and knee joint with the bones as different segments. I have used a threshold range of 99 to 242 but it includes unwanted areas of soft tissue (arteries and capillaries).</p>
<p>I have tried the following to remove the unwanted material:</p>
<ul>
<li>Scissors tool which doesn’t work to remove the unwanted areas</li>
<li>Island tool to keep the largest islands but none of the smaller islands remove - I have tried changing the voxels size as well</li>
<li>Creating another segmentation and painting the unwanted region then hid the segment however this is nor as accurate and I still have material close to the bone</li>
<li>Decreasing the threshold range to 107 to 242 but then I get holes in the tibia:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/548dcb88617c21bdd17d70b172d59f05eaeded9b.jpeg" data-download-href="/uploads/short-url/c3ZTVkpJb5YsWqLg71IyHgvyGGD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/548dcb88617c21bdd17d70b172d59f05eaeded9b.jpeg" alt="image" data-base62-sha1="c3ZTVkpJb5YsWqLg71IyHgvyGGD" width="690" height="422" data-dominant-color="8C6E70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">698×427 43.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would be so grateful if anyone could advise me on how to remove the unwanted soft tissue.</p>
<p>Many thanks,<br>
Heather</p>

---

## Post #2 by @muratmaga (2023-11-21 03:35 UTC)

<aside class="quote no-group" data-username="hd00561" data-post="1" data-topic="32916">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/ed8c4c/48.png" class="avatar"> hd00561:</div>
<blockquote>
<p>I have tried the following to remove the unwanted material:</p>
</blockquote>
</aside>
<p>Can you explain what didn’t work? First two methods are very robust and should work. Couple quick checks:</p>
<ol>
<li>If you are using the scissors tool after you split your segments, make sure the selected segment matches the area you are using the scissors on (e.g., if you are cleaning femur, femur needs to be the active segment).</li>
<li>If you run a median smoothing with a small kernel size (e.g.,  2x2x2 voxels) before the island tool, some of those small cluster may disappear or get disconnected from the rest creating islands for the tool to work.</li>
<li>When you start with the higher threshold and end up with holes, you can either use the closing filter in smoothing function to fill those holes, or use the SurfaceWrap effect (available as a separate extension), to fill them in.</li>
</ol>
<p>These are all generic segmentation recipes that should work well for your use case. If they are not working, it is often there is a mismatch with the active segment and where the edit is applied. You should also pay attention to the masking settings below the tools.</p>
<p>Alternatively you can try the total segmentator extension and use its deep-learning based segmentation model to obtain your segments automatically in a few minutes.</p>

---
