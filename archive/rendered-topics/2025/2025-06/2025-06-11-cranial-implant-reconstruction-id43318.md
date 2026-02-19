---
topic_id: 43318
title: "Cranial Implant Reconstruction"
date: 2025-06-11
url: https://discourse.slicer.org/t/43318
---

# Cranial Implant Reconstruction

**Topic ID**: 43318
**Date**: 2025-06-11
**URL**: https://discourse.slicer.org/t/cranial-implant-reconstruction/43318

---

## Post #1 by @Alina_Abbas (2025-06-11 15:59 UTC)

<p>Hello everyone,</p>
<p>I hope this message finds you well.</p>
<p>I am new to 3D Slicer and am using it for cranial implant reconstruction. I have attempted to utilize the scissor and mirror techniques on my image, but I have not achieved the desired results.</p>
<p>I would greatly appreciate any guidance on how to approach this problem and which features would be most effective. Thank you in advance for your assistance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19767f57a3d881575dc78b7aae6782d117aba9b1.jpeg" data-download-href="/uploads/short-url/3DfOBZNTitzAa7y0FnrvKvIQH7j.jpeg?dl=1" title="Screenshot 2025-06-11 125902" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19767f57a3d881575dc78b7aae6782d117aba9b1_2_575x500.jpeg" alt="Screenshot 2025-06-11 125902" data-base62-sha1="3DfOBZNTitzAa7y0FnrvKvIQH7j" width="575" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19767f57a3d881575dc78b7aae6782d117aba9b1_2_575x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19767f57a3d881575dc78b7aae6782d117aba9b1_2_862x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19767f57a3d881575dc78b7aae6782d117aba9b1.jpeg 2x" data-dominant-color="A39CA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-11 125902</span><span class="informations">1010×877 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-06-11 21:00 UTC)

<p>You can try the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/BafflePlanner.md">BafflePlanner</a></p>
<div class="youtube-onebox lazy-video-container" data-video-id="AigTwMYRI1Y" data-video-title="Design surface patches using new Baffle Planner module" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=AigTwMYRI1Y" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/AigTwMYRI1Y/maxresdefault.jpg" title="Design surface patches using new Baffle Planner module" width="690" height="388">
  </a>
</div>


---

## Post #3 by @lassoan (2025-06-13 14:19 UTC)

<p>To get some guidance for defining your baffle surface, you can mirror and align the original segmentation:</p>
<ul>
<li>In Data module, Clone the segmentation</li>
<li>In Transforms module: create a new linear transform (right-click in the “Node” section and select “Create new transform”), set the top-left value to -1 to mirror along the R axis, apply and harden this transform on the segmentation</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0355bd7802576d6c1d734dd0077742127a15ce1a.png" data-download-href="/uploads/short-url/tv82MgiQ2TDESjqmt5lqiUiN2G.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0355bd7802576d6c1d734dd0077742127a15ce1a_2_690x156.png" alt="image" data-base62-sha1="tv82MgiQ2TDESjqmt5lqiUiN2G" width="690" height="156" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0355bd7802576d6c1d734dd0077742127a15ce1a_2_690x156.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0355bd7802576d6c1d734dd0077742127a15ce1a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0355bd7802576d6c1d734dd0077742127a15ce1a.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1004×228 10.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>In Data module, enable transformation handles for the mirrored segmentation by right-clicking on the eye icon and enable the “Interaction” checkbox; then use the handles to align the mirrored segmentation to the original segmentation</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b0792b4b29df286a1f869d7642fb27967d0001b.jpeg" data-download-href="/uploads/short-url/3R77ftuXPd1TqQjNhp0RluKyLTZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0792b4b29df286a1f869d7642fb27967d0001b_2_690x318.jpeg" alt="image" data-base62-sha1="3R77ftuXPd1TqQjNhp0RluKyLTZ" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0792b4b29df286a1f869d7642fb27967d0001b_2_690x318.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0792b4b29df286a1f869d7642fb27967d0001b_2_1035x477.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b0792b4b29df286a1f869d7642fb27967d0001b_2_1380x636.jpeg 2x" data-dominant-color="9E9D9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×886 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
