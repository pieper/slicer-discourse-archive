# Best way to flip entire scene

**Topic ID**: 36822
**Date**: 2024-06-16
**URL**: https://discourse.slicer.org/t/best-way-to-flip-entire-scene/36822

---

## Post #1 by @evaherbst (2024-06-16 10:32 UTC)

<p>Hello,</p>
<p>I am having some trouble with incorrect orientations of a scan.</p>
<p>We received a CT scan of the upper body in .IMA format (unfortunately not DICOM). Therefore to load the CT data I converted to .nrrd in ImageJ, then loaded in Slicer.</p>
<p>I noticed that the left and right axes are flipped in the scan - I assume it has to do with something going wrong in the IJK to RAS transformation because the scan was “upside down”, ie when I load it in slicer, superior and inferior are also flipped.</p>
<p>In my original image volume the transform is as follows which seems to be the standard IFK to RAS.<br>
IJKToRASDirections:<br>
-1 0 0<br>
0 -1 0<br>
0 0 1</p>
<p>Maybe the image was already in RAS and that caused the issues?</p>
<p>Since the last axis is not flipped in the IJK to RAS transform, I created a linear transform and applied it to everything in the scene:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1df3143122056777c1d2d3c40352c4a14d39ca0.png" data-download-href="/uploads/short-url/pnwHocA0JqtDk0uQSoI3ajOTba0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1df3143122056777c1d2d3c40352c4a14d39ca0.png" alt="image" data-base62-sha1="pnwHocA0JqtDk0uQSoI3ajOTba0" width="690" height="204" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1503×445 8.05 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This gives me the correct orientations for superior inferior, left right etc, and the bones are not mirrored incorrectly anymore.</p>
<p>I just wanted to confirm:<br>
-Do you recommend applying the transform to everything in the scene and continuing working on that scene? Or exporting the transformed image and segmentation data and importing into a new scene?</p>
<p>I already did some segmentation so would like to avoid re-starting from scratch.</p>
<p><strong>Should I also transform the camera or no?</strong></p>
<p>Thank you,<br>
Eva</p>

---

## Post #2 by @lassoan (2024-06-16 13:16 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="1" data-topic="36822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>Do you recommend applying the transform to everything in the scene and continuing working on that scene?</p>
</blockquote>
</aside>
<p>Applying and hardening the transform would make sense, because by hardening you permanently fix the position/orientation of the objects.</p>
<p>You don’t have to transform the camera or modify views - they are all good, just the pose of the objects were incorrect.</p>

---

## Post #3 by @evaherbst (2024-06-21 10:09 UTC)

<p>Thank you so much Andras.</p>
<p>Best,<br>
Eva</p>

---
