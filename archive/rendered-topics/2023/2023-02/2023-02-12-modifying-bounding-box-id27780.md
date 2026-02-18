# Modifying bounding box

**Topic ID**: 27780
**Date**: 2023-02-12
**URL**: https://discourse.slicer.org/t/modifying-bounding-box/27780

---

## Post #1 by @Hannnonk (2023-02-12 14:35 UTC)

<p>Slicer version 4.13.0</p>
<p>Created a segmentation, but the bounding box is not centered nor orientated with the object<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08cd792fcf8ce4ac96775d657d67906b5372ec4.jpeg" data-download-href="/uploads/short-url/yk0lqOOn0ERbyP1mxPqqNqv70gI.jpeg?dl=1" title="2023-02-12_9-21-35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f08cd792fcf8ce4ac96775d657d67906b5372ec4_2_563x500.jpeg" alt="2023-02-12_9-21-35" data-base62-sha1="yk0lqOOn0ERbyP1mxPqqNqv70gI" width="563" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f08cd792fcf8ce4ac96775d657d67906b5372ec4_2_563x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08cd792fcf8ce4ac96775d657d67906b5372ec4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08cd792fcf8ce4ac96775d657d67906b5372ec4.jpeg 2x" data-dominant-color="9CA0CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-12_9-21-35</span><span class="informations">761×675 47.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>.</p>
<p>Makes it difficult to scale, etc. in Transforms. Is there any way to correct this?<br>
thanks</p>

---

## Post #2 by @lassoan (2023-02-15 06:06 UTC)

<p>This transform interactor is just for quick approximate visual alignment. I would recommend to use <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">landmark point based registration</a> modules to get accurate alignment.</p>

---
