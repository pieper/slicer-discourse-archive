# How can I add an axis of rotation about the center of mass to the model?

**Topic ID**: 27599
**Date**: 2023-02-02
**URL**: https://discourse.slicer.org/t/how-can-i-add-an-axis-of-rotation-about-the-center-of-mass-to-the-model/27599

---

## Post #1 by @q2577040659 (2023-02-02 10:28 UTC)

<p>How can I add an axis of rotation about the center of mass to the model?</p>

---

## Post #2 by @pieper (2023-02-02 13:44 UTC)

<p>These links may help - you can get the center of mass from the statistics and make a transform around it.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#quantifying-segments" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#quantifying-segments</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point</a></p>

---

## Post #3 by @q2577040659 (2023-02-03 02:06 UTC)

<p>Thank youfor the reply, but I’m going to add an action axis to the model like this, what do I do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93daeded781696728e28d8723568c4edd233f309.png" data-download-href="/uploads/short-url/l5Zf1b9ixKAKhNuk1ueJqr1qnnX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93daeded781696728e28d8723568c4edd233f309_2_690x379.png" alt="image" data-base62-sha1="l5Zf1b9ixKAKhNuk1ueJqr1qnnX" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93daeded781696728e28d8723568c4edd233f309_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93daeded781696728e28d8723568c4edd233f309_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93daeded781696728e28d8723568c4edd233f309.png 2x" data-dominant-color="060605"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1353×744 25.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2023-02-03 08:15 UTC)

<p>That should still be possible if you set up nested transforms.  Study transform hierarchies and you can center the model around it’s center of mass and even align it to the principle axes (moments) and harden the transform if you want for convenience.</p>

---

## Post #5 by @q2577040659 (2023-02-06 01:40 UTC)

<p>Thanks, but I still want to use the action axis.</p>

---
