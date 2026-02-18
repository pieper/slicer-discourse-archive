# can one make transforms graphically rather than using Transforms Module?

**Topic ID**: 21944
**Date**: 2022-02-13
**URL**: https://discourse.slicer.org/t/can-one-make-transforms-graphically-rather-than-using-transforms-module/21944

---

## Post #1 by @asdf (2022-02-13 03:21 UTC)

<p>Operating system: MacOS Catalina<br>
Slicer version: 4.13<br>
Expected behavior: I know one can use the Transforms module to rotate, translate, and make other transforms on segmentations (ie, an object in .nrrd format). But this is not very user-friendly.<br>
Question: Is there a way within Slicer to move, rotate, etc the segmentation using the mouse within the Segment Editor?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-02-13 13:59 UTC)

<p>You can also shift and rotate the transform in 3D views by enabling “Interaction in 3D view”:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="bbikx7Edv4g" data-video-title="Transforming objects using Data module in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=bbikx7Edv4g" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/bbikx7Edv4g/hqdefault.jpg" title="Transforming objects using Data module in 3D Slicer" width="" height="">
  </a>
</div>

<p>However, editing transforms visually is an iterative process (translate then rotate in different views multiple times) which takes a long time and less accurate than using <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">semi-automatic registration tools</a>. Semi-automatic registration tools can directly compute the optimal transform from matching landmark points that you specified.</p>

---

## Post #3 by @asdf (2022-02-23 05:08 UTC)

<p>Thank you, this is helpful – using the Data module I can now rotate and translate the segmentation graphically.<br>
However, I still cannot understand how to rescale or deform the segmentation graphically (I believe this would be the graphical equivalent of editing the Transform matrix in the Transform module). With your example above, I would want to make the yellow cylinder larger or smaller, fatter or thinner. Can you help?</p>

---

## Post #4 by @asdf (2022-02-26 02:42 UTC)

<p>Hello, I’m re-pasting my follow-up question, because I’m not sure if I replied to you before, or if I accidentally replied only to myself?<br>
Please see below and thank you</p>
<p>Thank you, this is helpful – using the Data module I can now rotate and translate the segmentation graphically.<br>
However, I still cannot understand how to rescale or deform the segmentation graphically (I believe this would be the graphical equivalent of editing the Transform matrix in the Transform module). With your example above, I would want to make the yellow cylinder larger or smaller, fatter or thinner. Can you help?</p>

---

## Post #5 by @muratmaga (2022-02-26 05:25 UTC)

<p>If expand the Display and enable interactions, particularly scaling, you can modify your models scaling by manipulating each axis independently (drag the handle on the axis vectors).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3f272ad0e5aed64b9d270a9bc7f52d3789e6c63.jpeg" data-download-href="/uploads/short-url/nolgJZ1xEKI7qARKrRQhNVyL0xt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3f272ad0e5aed64b9d270a9bc7f52d3789e6c63_2_654x500.jpeg" alt="image" data-base62-sha1="nolgJZ1xEKI7qARKrRQhNVyL0xt" width="654" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3f272ad0e5aed64b9d270a9bc7f52d3789e6c63_2_654x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3f272ad0e5aed64b9d270a9bc7f52d3789e6c63_2_981x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3f272ad0e5aed64b9d270a9bc7f52d3789e6c63_2_1308x1000.jpeg 2x" data-dominant-color="D3D4DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1467 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
