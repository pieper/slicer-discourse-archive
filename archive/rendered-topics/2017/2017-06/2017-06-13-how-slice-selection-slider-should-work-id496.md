---
topic_id: 496
title: "How Slice Selection Slider Should Work"
date: 2017-06-13
url: https://discourse.slicer.org/t/496
---

# How slice selection slider should work?

**Topic ID**: 496
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/how-slice-selection-slider-should-work/496

---

## Post #1 by @lassoan (2017-06-13 19:33 UTC)

<p>Currently slice selector slider at the top of each slice view always moves with about 1/10th of slice spacing, rounded to nearest power of 10 (1.0mm, 0.1mm, …) increments when dragged with the mouse (or clicked with the mouse and then moved with the arrow button). This allows free browsing between slices (e.g., markups can be easily placed off-center from a slice), but results in almost always showing interpolated slices.</p>
<p>If the slider is moved all the way to one slide, the slice view is positioned to the edge of the last voxel. After this, if the user clicks in the view are (not in the selection slider) and browses between slices using the arrow keys, the slice view will be kept positioned at the boundary of slice views - causing suboptimal display (always interpolation between two slices are shown) and some unpredictability in displayed content (e.g., binary labelmap is not interpolated, therefore when the slice viewer is right at the boundary between two slices, the label for a slice may or may not appear).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c15782bad612965ad09d9bff0a366345e8a631b.png" alt="image" data-base62-sha1="jZeQjR9SVMwvZVNlG23ZLd73Bvd" width="294" height="373"></p>
<p>What is the preference of our users?</p>
<ul>
<li>Should the current slice view slider behavior be kept - allowing to <em>browse anywhere between slices</em>, or should the slider move slices so that the <em>slice viewer position is snapped to slice center positions</em>?</li>
<li>When the slice selector slider is moved to the all the way to the left/right, should it position the slice viewer to the <em>center</em> or <em>outer edge</em> of the first/last volume slice?</li>
</ul>

---

## Post #2 by @gcsharp (2017-06-13 20:00 UTC)

<p>For ordinary usage, I prefer snap to center of voxel, and increment voxel by voxel.<br>
But the question of sub-voxel placement of markups is interesting.<br>
If I jump to markup, would you still snap to center?</p>

---

## Post #3 by @lassoan (2017-06-13 22:20 UTC)

<p>Markup is placed on the slice view plane - not necessarily in the center of any volume slice. Jump to markup goes to that position and does not snap to center.</p>

---

## Post #4 by @pieper (2017-06-13 23:01 UTC)

<p>A related issue that we could sort out at the same time: <a href="https://github.com/Slicer/Slicer/blob/ff4a605ef55fdda4fbd8c20cee41e4b184461f72/Modules/Loadable/Markups/MRMLDM/vtkMRMLMarkupsDisplayableManager2D.cxx#L932-L1019">there is a tolerance</a> for when a markup is visible on a Slice.  But when you grab the markup it snaps to the middle of the plane.  I think the fiducial should move parallel to the current slice plane so the offset remains the same.</p>

---

## Post #5 by @fedorov (2017-06-13 23:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is the preference of our users?</p>
</blockquote>
</aside>
<p>Would it be too much of a hassle to make this a configurable setting of the application? We may not get sufficient response here, and we can’t anticipate all possible use cases.</p>

---

## Post #6 by @gcsharp (2017-06-13 23:03 UTC)

<p>This seems reasonable.  It preserves workflow for iterative sub-voxel adjustment of a fiducial location.</p>
<p>Presumably snap to center only affects viewing in the original orientation.  What is the proposed behavior when viewing images are reformatted to cardinal axes?</p>

---

## Post #7 by @cpinter (2017-06-14 07:58 UTC)

<p>+1 on snap to slice center<br>
+1 on adding the option to application settings</p>
<p>One thing I noticed that I’m not sure is related to this issue is that when I use the mouse wheel to scroll the slices, then after a bit of scrolling, a “dummy” position seems to appear. Same thing seems to happen with the touch pad scroll. Let me explain. When I first scroll with mouse wheel, one up, one down, it works fine, it switches slice at every scroll. Then I make a bigger scroll with the wheel, and then when I want to go back up one, it doesn’t move. Then down one, nothing happens. It is quite annoying, as 1) behavior changed 2) I need to scroll twice to scroll one slice, makes it counterintuitive to review a volume carefully.<br>
If this is related to the 1/10th of slice spacing steps, then this will need to be fixed as well if we make this an option and keep the current mode as well.</p>

---

## Post #8 by @fedorov (2017-06-14 17:38 UTC)

<p>Related to this issue, I could never understand why when I scroll to the end of the slice slider to the right (not to the left!), I am able to get outside of the volume field of view, and see black? How is this helpful? Would be great if this issue was fixed too.</p>

---

## Post #9 by @lassoan (2017-06-15 03:03 UTC)

<p>There is already a slice spacing settings in the slice view controller. Could we just use that to control the step size. Maybe we could add another checkbox there: “snap to background volume slice center”?</p>
<p>If there is a higher-resolution foreground or labelmap volume, should we still just snap to the background volume’s slice centers?</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>when I scroll to the end of the slice slider to the right (not to the left!), I am able to get outside of the volume field of view, and see black</p>
</blockquote>
</aside>
<p>Yes, it is the issue that I mentioned that in slider end positions are now mapped to the edge of the volume. If we change this so that slider end positions correspond to first/last slice center then we would always stay in the volume.</p>
<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I make a bigger scroll with the wheel, and then when I want to go back up one, it doesn’t move</p>
</blockquote>
</aside>
<p>I think this may be a mouse driver “feature” (maybe can be controlled by changing acceleration and smooth scroll settings), but we would need to add a breakpoint into the slider’s event callback function to confirm.</p>

---

## Post #10 by @cassiegriffin (2018-09-28 16:17 UTC)

<p>I have same issued like you but It is with my laptop.I hardly scroll with my touch pad. I have searched with keyword <a href="https://babasupport.org/hp/hp-laptop-touchpad-not-working/" rel="nofollow noopener">hp laptop touchpad not working</a>. I ask them about issue and they say to check your touchapd driver. Where I download driver for touchapd?</p>

---

## Post #11 by @stephan (2018-09-28 17:03 UTC)

<p>+1 for user-configurable.<br>
For most use-cases, snapping the slice to the voxel center makes sense.<br>
However, I do for example have one use-case (hard to explain in short, but it is about registering a stack of photographed gross pathology slices to an MRI) where it is very helpful to have the slice view snap to one border of the volume slices.<br>
So, if one could make this a per-viewer (or per-volume) user configurable setting, it would be perfect.</p>

---

## Post #12 by @lassoan (2018-09-29 20:26 UTC)

<p>Note that instead of mouse wheel/scroll, a much faster and more direct way of slicing through a volume is to simply move the mouse pointer over a view while holding down Shift key (no need to click). It works in both slice and 3D views.</p>

---
