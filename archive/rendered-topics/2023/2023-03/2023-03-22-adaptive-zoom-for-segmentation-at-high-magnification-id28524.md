---
topic_id: 28524
title: "Adaptive Zoom For Segmentation At High Magnification"
date: 2023-03-22
url: https://discourse.slicer.org/t/28524
---

# Adaptive zoom for segmentation at high magnification

**Topic ID**: 28524
**Date**: 2023-03-22
**URL**: https://discourse.slicer.org/t/adaptive-zoom-for-segmentation-at-high-magnification/28524

---

## Post #1 by @mohammed_alshakhas (2023-03-22 16:13 UTC)

<p>It just occurred to me during segmentation</p>
<p>wish to have an option that views readjust to center around the cursor</p>
<p>example for use: during segmenting at high magnification, and instead of needing to readjust view each time you move to a different slice, the view itself can automatically center around</p>
<p>for further clarification: during segmenting an orbit, I use maximum zoom at the medial wall (can’t see the floor ) so have to scroll the view down to see floor. then once I move to a different slive I have to repeat scrolling view</p>
<p>not an essential feature but it would really help when segmentation is needed at high magnification</p>

---

## Post #2 by @pieper (2023-03-22 18:18 UTC)

<p>If I understand what you are looking for, try switching to Jump slices - centered in the crosshair menu.  Then when you use the shift-mouse-move the other views will be visible at that point.  Also link the views so all three will zoom together.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b5ca56f448f24705733bc46240ecb062f6fd241.png" alt="image" data-base62-sha1="1CvKeSh8XGK3avpXljucGDgbh73" width="275" height="159"></p>

---

## Post #3 by @mohammed_alshakhas (2023-03-22 18:29 UTC)

<p>the one I was thinking of is, within the view is using ( NOT OTHER VIEWS) , when I point to the bottom of the view, the same view will center around the location of the cursor. like the center of view following the cursor</p>

---

## Post #4 by @lassoan (2023-03-27 17:28 UTC)

<blockquote>
<p>during segmenting at high magnification, and instead of needing to readjust view each time you move to a different slice, the view itself can automatically center around</p>
</blockquote>
<p>This is exactly what jump slices with the “centered” option does.</p>
<p>Can you post a screen capture video that shows why centered jump slices does not work well for you?</p>
<p>Zooming around the cursor could be problematic because the cursor may not be visible in the current slice view. Would you then jump to center the crosshair? Maybe zooming at the current mouse pointer position would be sufficient? That could be used to keep the current point of interest inside the slice view.</p>

---

## Post #5 by @mohammed_alshakhas (2023-03-27 17:42 UTC)

<p>what i meant is that centering occurs around the cursor in the same view.</p>
<p>like in the video when I point to the top left corner in the axial,  I want the view to be  centered  around that location in the axial view I’m working in</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4565ea43fb48788ba8b2cc36feca496fa3a01f24.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4565ea43fb48788ba8b2cc36feca496fa3a01f24.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4565ea43fb48788ba8b2cc36feca496fa3a01f24.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #6 by @lassoan (2023-03-27 18:11 UTC)

<p>You can move the mouse over to any other view and touch the point of interest with the Shift key to center it in thr current view. After that point the point is centered, so it is kept in the center at all zoom factors.</p>
<p>It could be possible to add a new keyboard shortcut or mouse gesture to make the current mouse pointer position the center. However, for a 3D center positioning you need to look at an orthogonal slice anyway (to ensure that you are on the right slice), so it may actually lead to worse result.</p>
<p>You can also drag-and-drop the point of interest into the center using middle-button or shift+Left-button drag-and-drop.</p>

---
