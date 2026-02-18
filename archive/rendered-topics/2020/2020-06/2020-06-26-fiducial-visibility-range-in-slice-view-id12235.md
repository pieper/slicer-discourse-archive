# Fiducial visibility range in slice view

**Topic ID**: 12235
**Date**: 2020-06-26
**URL**: https://discourse.slicer.org/t/fiducial-visibility-range-in-slice-view/12235

---

## Post #1 by @gcsharp (2020-06-26 15:19 UTC)

<p>When I am in slice view, how close does a fiducial need to be in order to be visible?<br>
Is there a way to control this and make more of the nearby fiducials visible?</p>

---

## Post #2 by @lassoan (2020-06-26 15:25 UTC)

<p>If fiducial projection is disabled then you always see the fiducial on the current slice, i.e., within +/- slice spacing distance. You can adjust slice spacing manually if you want to show more fiducials.</p>

---

## Post #3 by @gcsharp (2020-06-26 15:39 UTC)

<p>I’m not sure I follow.  Doesn’t changing the slice spacing mean that the fiducials don’t match the anatomy?</p>

---

## Post #4 by @lassoan (2020-06-26 15:42 UTC)

<p>I meant changing the slice spacing in the slice viewer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4952f05eb44fff6af7129a71905c73f3a7883821.png" data-download-href="/uploads/short-url/asEyaRvCRCcQRBvUsMUe2enWrm1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4952f05eb44fff6af7129a71905c73f3a7883821_2_690x190.png" alt="image" data-base62-sha1="asEyaRvCRCcQRBvUsMUe2enWrm1" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4952f05eb44fff6af7129a71905c73f3a7883821_2_690x190.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4952f05eb44fff6af7129a71905c73f3a7883821_2_1035x285.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4952f05eb44fff6af7129a71905c73f3a7883821.png 2x" data-dominant-color="D1D1E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×322 28.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @gcsharp (2020-06-26 15:53 UTC)

<p>Got it.  Thanks!  (need 20 characters)</p>

---

## Post #6 by @muratmaga (2020-06-26 15:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, this had been a confusion for us a while, and now I understand the issue. If the ‘interpolation’ option in the volume setting has been unset (no interpolation), this spacing has no effect. You can try with MRHead and set the slice spacing to 0.2mm and then see that for 4-5 slice increments no change in the slice is visible, even though the sliders shows move.</p>
<p>We do disable the interpolation quite a bit to be able to follow voxel boundaries in manual segmentations.</p>
<p>I think this needs to be somehow disabled if the interpolation option is not used.</p>

---

## Post #7 by @lassoan (2020-06-26 16:04 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="12235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think this needs to be somehow disabled if the interpolation option is not used.</p>
</blockquote>
</aside>
<p>What would need to be disabled?</p>

---

## Post #8 by @muratmaga (2020-06-26 16:30 UTC)

<p>Setting the slice spacing something different than the image spacing.</p>

---

## Post #9 by @lassoan (2020-06-26 18:24 UTC)

<p>The slice offset slider certainly needs improvement. Most importantly, it needs a “snap to slice” mode (see for example discussion here <a href="https://discourse.slicer.org/t/how-slice-selection-slider-should-work/496" class="inline-onebox">How slice selection slider should work?</a>), but it is a complex issue. For example, markups still need to be placed at arbitrary locations (not just at voxel centers), but then what would you display when the user wants to jump to a markup point location? A potential solution could be to add a “snap” button, which would jump to nearest slice and would probably override manual slice spacing. When slice position is set to a non-center voxel, or slice spacing is adjusted manually, or the slice view is rotated, then then “snap” mode could be automatically deactivated.</p>
<p>Disabling interpolation of grayscale images leads to many subtle problems. One of them is what you noted, but things even get worse when you have non-axis-aligned views, overlay model intersections, markups, etc. that I would not recommend anyone to use it.</p>
<p>Did you disable interpolation because you wanted to see voxel boundaries? For that, a proper solution would be to show a grid when you zoom in a lot - as it was done in Slicer-3.x. Unfortunately, this feature has not yet ported over to Slicer-4.x. It would not be hard to implement it, especially if you only need it for non-rotated views.</p>
<p>In your workflow, why did you adjusted the slice view spacing manually?</p>

---
