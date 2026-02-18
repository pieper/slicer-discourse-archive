# Can I reproduction of change in body shape

**Topic ID**: 29579
**Date**: 2023-05-22
**URL**: https://discourse.slicer.org/t/can-i-reproduction-of-change-in-body-shape/29579

---

## Post #1 by @sotarad (2023-05-22 13:36 UTC)

<p>Hi all. I want to transform OAR volume into smaller in order to reproduct of change in body shape.<br>
Finaly, I want to get DVFs that shrink some OARs.<br>
I think if I could get DVF from contour base DIR, the challenge will be solved.<br>
But, in the first place I don’t know how to do contour base DIR in the 3Dslicer.<br>
If you have other way to reproduct of change in body shape, please tell me that.</p>

---

## Post #2 by @lassoan (2023-05-23 03:17 UTC)

<p>You can compute displacement vector field from shape change of a segmented structure using <a href="https://github.com/SlicerRt/SegmentRegistration#segment-registration">SegmentRegistration</a> extension.</p>
<p>If you want to simulate shape change then you can also prescribe displacement at specific point positions and compute a dense displacement vector field using Fiducial Registration Wizard module in SlicerIGT extension:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="GfDDQykH1iY" data-video-title="Soft tissue deformation simulation" data-video-start-time="0" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=GfDDQykH1iY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/GfDDQykH1iY/maxresdefault.jpg" title="Soft tissue deformation simulation" width="" height="">
  </a>
</div>


---

## Post #3 by @sotarad (2023-05-24 00:18 UTC)

<p>Thanks for comment, Mr. Lasso.<br>
I can do what I want with Segment Registration.<br>
And I hadn’t installed untill you teach me about SliceIGT.<br>
So,I think that very interesting tool.<br>
I make an effort using this for my study.</p>

---
