# Hi everyone, i'm new on Slicer. I really need some help

**Topic ID**: 19762
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/hi-everyone-im-new-on-slicer-i-really-need-some-help/19762

---

## Post #1 by @alanpontes (2021-09-20 14:52 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.202</p>
<p>How can i segment ribs cartilages?</p>
<p>I’m ok with bone of chest. Sternum and ribs. But i really need cartilages.</p>
<p>I’m Thoracic Surgeon and need that for my pectus excavatum patients.</p>
<p>Thank you for the help</p>

---

## Post #2 by @lassoan (2021-09-21 17:07 UTC)

<p>You can use “Grow from seeds” effect with intensity masking to segment structures that have similar intensity, similar to this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="8Nbi1Co2rhY" data-video-title="Femur segmentation using masked region growing in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=8Nbi1Co2rhY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/8Nbi1Co2rhY/maxresdefault.jpg" title="Femur segmentation using masked region growing in 3D Slicer" width="" height="">
  </a>
</div>

<p>The difference for bone+cartilage segmentation are the followings:</p>
<ul>
<li>Set the editable intensity range (using Threshold effect) to include cartilage but exclude soft tissues as much as possible (to avoid the segmentation leaking too much into soft tissues).</li>
<li>Use “bone”, “cartilage”, and “other” segments. You would put small seeds in bone and cartilage. You would use the “other” segment to paint seeds into soft tissues that are within the intensity range that you specified (to prevent them to be added to the the cartilage segment).</li>
</ul>

---

## Post #3 by @alanpontes (2021-09-24 20:14 UTC)

<p>Thx so much!.<br>
I did my first real model. It’s not perfect, but it is a start.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/397dc5287d650af71720cd3b1295c7149557f6ae.jpeg" data-download-href="/uploads/short-url/8cAFYPZYpNHdz6oxKhlFAzFpzlA.jpeg?dl=1" title="3D PECTUS DC" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/397dc5287d650af71720cd3b1295c7149557f6ae_2_540x500.jpeg" alt="3D PECTUS DC" data-base62-sha1="8cAFYPZYpNHdz6oxKhlFAzFpzlA" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/397dc5287d650af71720cd3b1295c7149557f6ae_2_540x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/397dc5287d650af71720cd3b1295c7149557f6ae_2_810x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/397dc5287d650af71720cd3b1295c7149557f6ae.jpeg 2x" data-dominant-color="9C9BAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D PECTUS DC</span><span class="informations">922×853 77.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-09-25 03:56 UTC)

<p>Thanks for the update. It seems that you are on the right track.</p>
<p>You can try lowering the editable intensity range value to have less holes in the cartilage (of course that may bring in more noise from surrounding soft tissues).</p>
<p>You may also try to disable editable intensity range when you are done with the region growing and apply smoothing to fill in small holes.</p>

---
