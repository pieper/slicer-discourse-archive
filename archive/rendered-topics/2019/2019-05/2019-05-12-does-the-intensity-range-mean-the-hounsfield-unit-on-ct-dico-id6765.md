# Does the " intensity range" mean the "Hounsfield unit" on CT dicom image?

**Topic ID**: 6765
**Date**: 2019-05-12
**URL**: https://discourse.slicer.org/t/does-the-intensity-range-mean-the-hounsfield-unit-on-ct-dicom-image/6765

---

## Post #1 by @markyang19 (2019-05-12 08:25 UTC)

<p>I am trying the segmentation editor by intensity range on my CT dicom image.<br>
Does the " intensity range" mean the “Hounsfield unit” on CT dicom image???<br>
I compare the same dicom image on the 3D slicer and other dicom viewer. It seems the " intensity range" on 3D slicer equal to Hounsfield unit. But I am not sure about this point.</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior: segmentation by intensity range<br>
Actual behavior:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a79be0494bfd728b348f4ffa2f50dbad0e9817b.jpeg" data-download-href="/uploads/short-url/jL0INjiak0RKs1Dxen0pa2M7U4r.jpeg?dl=1" title="intensity%20range" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a79be0494bfd728b348f4ffa2f50dbad0e9817b_2_689x351.jpeg" alt="intensity%20range" data-base62-sha1="jL0INjiak0RKs1Dxen0pa2M7U4r" width="689" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a79be0494bfd728b348f4ffa2f50dbad0e9817b_2_689x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a79be0494bfd728b348f4ffa2f50dbad0e9817b_2_1033x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a79be0494bfd728b348f4ffa2f50dbad0e9817b.jpeg 2x" data-dominant-color="868483"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">intensity%20range</span><span class="informations">1344×685 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-05-12 12:16 UTC)

<aside class="quote no-group" data-username="markyang19" data-post="1" data-topic="6765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/45deac/48.png" class="avatar"> markyang19:</div>
<blockquote>
<p>Does the " intensity range" mean the “Hounsfield unit” on CT dicom image???</p>
</blockquote>
</aside>
<p>Yes, voxel values of a CT volume is in HU.</p>

---

## Post #3 by @markyang19 (2019-05-12 14:33 UTC)

<p>Dear Andras Lasso:<br>
Thank you for your kindly replay.</p>
<p>Regards,<br>
Mark</p>

---

## Post #4 by @kookoo9999 (2021-11-08 14:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Hi ,while searching for the House Field unit, I have a question here.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, voxel values of a CT volume is in HU.</p>
</blockquote>
</aside>
<p>According to this comment, is it correct to indicate the segmented HA value in the segment editor in the picture?</p>

---

## Post #5 by @lassoan (2021-11-08 14:58 UTC)

<p>Yes, in clinical CT images, voxel values are in HU and the threshold range is defined in HU.</p>

---
