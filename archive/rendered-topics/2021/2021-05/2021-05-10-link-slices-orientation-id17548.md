---
topic_id: 17548
title: "Link Slices Orientation"
date: 2021-05-10
url: https://discourse.slicer.org/t/17548
---

# Link slices orientation

**Topic ID**: 17548
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/link-slices-orientation/17548

---

## Post #1 by @fabbard (2021-05-10 18:46 UTC)

<p>Is there a way to link the orientation of the slices to keep them orthogonal when I change the orientation of one of them using an axis?<br>
In other words: I want to change the plane orientation of one slice keeping a 90 degree angle with the other two.</p>
<p>thanks.</p>

---

## Post #2 by @lassoan (2021-05-11 03:07 UTC)

<p>You can rotate slice intersections (they remain orthogonal) by enabling slice intersections and use <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">Ctrl+Alt+Left-click-and-drag</a> or two-finger pinch-and-rotate gesture (on a Windows touchscreen or a mac touchpad).</p>
<p>Once you have set up your view directions, you can use “Valve View” module in SlicerHeart extension to rotate the views. This is useful if you want to draw valve annulus contours (or segment any other closed curves in images that are best recognizable on cross-sections).</p>

---

## Post #3 by @fabbard (2021-06-03 08:58 UTC)

<p>Dear Andras,<br>
thank you for your quick reply.<br>
Unfortunately, I had time to try your suggestion only now and it appears that it doesn’t work for me: when I try to move one of the intersections by dragging its axis with Ctrl+Alt+Left-click pressed, the intersection still moves independently from the others and they don’t remain orthogonal. Am I missing something?<br>
thank you,<br>
Fabrizio.</p>

---

## Post #4 by @lassoan (2021-06-03 12:52 UTC)

<p>I can confirm that this works well in latest Slicer Stable Release and latest Slicer Preview Release. Notes:</p>
<ul>
<li>slice view rotation preserves relative slice angles, so if you have non-orthogonal slice views then they will remain non-orthogonal</li>
<li>on macOS “Alt” button is labeled as “Option”</li>
</ul>
<p>If you want to rotate slice views to segment circular structures (such as heart annulus or valves) then you can use <strong>Valve View</strong> module (from SlicerHeart extension)</p>
<p>You can also use touchscreen or touchpad if that is more convenient than a triple-key combination:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="7lsN93iPmbg" data-video-title="3D Slicer - touchscreen and trackpad interaction" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=7lsN93iPmbg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/7lsN93iPmbg/maxresdefault.jpg" title="3D Slicer - touchscreen and trackpad interaction" width="" height="">
  </a>
</div>

<p>If you still have any problems with this then please record a screen capture video of what you do.</p>

---

## Post #5 by @fabbard (2021-06-03 18:45 UTC)

<p>Dear Andras,<br>
thank you again for your reply. I downloaded the latest version and using ctrl+alt+left-click&amp;drag works fine to move two intersections together. However, I was wondering if it is possible to move all three toghether (as it was a Cartesian axes system).<br>
My problem is that I have a porous materials with straight channels, and it is difficult to align the intersections to match the axes of the channels if they move independently, even when two of them are linked.<br>
thank you again,<br>
Fabrizio.</p>

---

## Post #6 by @lassoan (2021-06-03 19:04 UTC)

<p>All the coordinate system move together, the plane normals acting as a Cartesian coordinate system (as long as you did not rotate just a selected plane using reformat module or the reformat widget).</p>
<p>It should be actually very easy to align the views to channels:</p>
<ul>
<li>in the <strong>red</strong> slice view (we will make this the cross-sectional view): move the slice intersection into a middle of a channel (by moving the mouse while holding down “Shift” key) in the red slice view</li>
<li>in the <strong>yellow</strong> slice view: rotate the views until the <strong>green</strong> intersection line gets approximately aligned with the channel direction</li>
<li>in the <strong>green</strong> slice view: rotate the views until the <strong>yellow</strong> intersection line gets aligned with the channel direction</li>
</ul>
<p>You may repeat these steps to make the alignment even more accurate.</p>

---

## Post #7 by @fabbard (2021-06-04 13:55 UTC)

<p>It worked like charm!<br>
Thank you Andras!</p>

---
