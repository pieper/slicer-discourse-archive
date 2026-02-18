# Markups - fiducial - keep the moved point visible in all views

**Topic ID**: 30088
**Date**: 2023-06-16
**URL**: https://discourse.slicer.org/t/markups-fiducial-keep-the-moved-point-visible-in-all-views/30088

---

## Post #1 by @hortakc (2023-06-16 22:44 UTC)

<p>Hello!<br>
I need to change the position of some markups (fiducial or landmarks). I am use to do it with ITK Snap because it shows me the lines of the axes crossing my markup to have them as references.<br>
More importantly, if I move one markup, it simultaneously shows me the movement in the other axes jumping through slices. For example, while moving my landmark in Axial plane, it will show me simultaneously the movement in Sagittal and Coronal slices, by moving the slices while the markup is static in these axes.<br>
At the moment, in Slicer, if I move my markup in axial, the markup disappear in sagittal and coronal axes (my slices do not move, only my markup, eventually it disappear in these axes). If I double click on it will show me where are them in all axes, but I lost the reference and complicated the exact location of my markup.</p>
<p>Is there any way to have the reference lines (which represent the intersection of axes) crossing the markups?<br>
Can I move the markup in one axes (plane) and have the movement reflected in the other planes associated with the slices movement?</p>
<p>Operating system: Windows<br>
Slicer version: 5.2.2<br>
Expected behavior: moving markups trough slices in all axes simultaneously (slices in axial, coronal and sagittal planes) showing the movement in the slices of all planes<br>
Actual behavior: movement of the markup only not movement of the slices in the remaining planes</p>

---

## Post #2 by @hortakc (2023-06-16 22:50 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be.jpeg" data-download-href="/uploads/short-url/wBb9WqSy5COOs4zMM9YAkut00vI.jpeg?dl=1" title="ITK - feducial - reference axis1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_690x373.jpeg" alt="ITK - feducial - reference axis1.PNG" data-base62-sha1="wBb9WqSy5COOs4zMM9YAkut00vI" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_1380x746.jpeg 2x" data-dominant-color="4A4A4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ITK - feducial - reference axis1.PNG</span><span class="informations">1920×1040 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Image in ITK Snap</p>

---

## Post #3 by @lassoan (2023-06-28 03:30 UTC)

<aside class="quote no-group" data-username="hortakc" data-post="1" data-topic="30088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hortakc/48/76987_2.png" class="avatar"> hortakc:</div>
<blockquote>
<p>At the moment, in Slicer, if I move my markup in axial, the markup disappear in sagittal and coronal axes</p>
</blockquote>
</aside>
<p>We call this “track mode” and we don’t enable is generally for all markups manipulations but only in specific modules. For example, <code>Landmark Registration</code> module in Slicer uses this. If you think this should be a generic markups feature then please create a topic in the <a href="https://discourse.slicer.org/c/support/feature-requests/9">Feature requests</a> category.</p>
<aside class="quote no-group" data-username="hortakc" data-post="1" data-topic="30088">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hortakc/48/76987_2.png" class="avatar"> hortakc:</div>
<blockquote>
<p>Is there any way to have the reference lines (which represent the intersection of axes) crossing the markups?</p>
</blockquote>
</aside>
<p>You can show slice intersections or crosshair to see the current slice or cursor position in all views. To move all slice views while moving the mouse, you can hold down the Shift key. I usually just click on a markup point after moving it to show it in all views.</p>

---
