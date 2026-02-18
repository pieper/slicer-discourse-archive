# How to reveal jaw with teeth over skull

**Topic ID**: 19194
**Date**: 2021-08-14
**URL**: https://discourse.slicer.org/t/how-to-reveal-jaw-with-teeth-over-skull/19194

---

## Post #1 by @Fatih_Hamircu (2021-08-14 17:27 UTC)

<p>Hello,<br>
From the skull, I want to reveal the lower jaw together with the teeth. I want to see 3D. I want to reveal it in Stl format and make a model from a 3D printer.<br>
I saw the videos on YouTube. I do the tissue together with the bones every time. I couldn’t quite uncover the bone.<br>
How can I do that?</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2021-08-14 17:37 UTC)

<p>Segmenting bone and teeth in CT is usually quite easy, using Thresholding effect.</p>
<p>Separating lower and upper jaw may not be trivial if the image is acquired with teeth in contact. “Grow from seeds” effect can be used for this separation, but might require additional seeds at the tip of the teeth or some manual touchup of the end result.</p>

---

## Post #3 by @Fatih_Hamircu (2021-08-15 09:14 UTC)

<p>I did a Google search, to decipher grow from seed tutorials. But I couldn’t find it, do you have it?</p>

---

## Post #4 by @Fatih_Hamircu (2021-08-15 10:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8de13b7ee48d58eb4c93919855b721a0a1cf990f.jpeg" data-download-href="/uploads/short-url/kf7SECA27qm9fPxecZU3aqF03Uz.jpeg?dl=1" title="16290247759972535040114712170859" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de13b7ee48d58eb4c93919855b721a0a1cf990f_2_666x500.jpeg" alt="16290247759972535040114712170859" data-base62-sha1="kf7SECA27qm9fPxecZU3aqF03Uz" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de13b7ee48d58eb4c93919855b721a0a1cf990f_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de13b7ee48d58eb4c93919855b721a0a1cf990f_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8de13b7ee48d58eb4c93919855b721a0a1cf990f_2_1332x1000.jpeg 2x" data-dominant-color="A9A59C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">16290247759972535040114712170859</span><span class="informations">1920×1440 358 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I have this image. Noise around teeth. How to take clean lower jaw?</p>

---

## Post #5 by @lassoan (2021-08-16 23:16 UTC)

<p>We’re you able to figure out how to segment multiple regions using Grow from seeds? To help others with similar needs in the future, can you share what you learned?</p>

---
