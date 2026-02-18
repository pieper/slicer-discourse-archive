# Change focus of camera in 3D view

**Topic ID**: 15545
**Date**: 2021-01-15
**URL**: https://discourse.slicer.org/t/change-focus-of-camera-in-3d-view/15545

---

## Post #1 by @LuckyLuke (2021-01-15 22:11 UTC)

<p>Hello everyone!</p>
<p>I have one silly question: how to change focus of the camera in 3D.</p>
<p>from what I understood, camera is always looking at exactly &gt;&gt;1 position.</p>
<p>I can indeed pan the camera back and forth but when I rotate the model, I see that the camera is still not looking at the model.</p>
<p>In other words when I rotate camera around a model, center of rotation is let’s say left arm. I pan the entire CT scan to the left (or camera to the right) so that the center of rotation is torso.</p>
<p>However, that does not happen. IT seems to me while panning camera to the right (meaning torso to the left) somehow torget of camera remains&gt;&gt; the left arm.</p>
<p>This when rotating the model it ssems like body is spinning around an anxis and I can not move that axis to the middle of the scanned body.</p>
<p>Hmm…</p>

---

## Post #2 by @NoobForSlicer (2021-01-15 22:18 UTC)

<p>Okay I am stupid… I actually don’t know what you want again</p>

---

## Post #3 by @LuckyLuke (2021-01-15 22:25 UTC)

<p>I just tried it again and the target of camera remains always at the same position, but the body does move and shift around the target. In other words by moving the scan to the center, rotation is nice and is indeed rotation rather than orbitning around his own forearm</p>

---

## Post #4 by @lassoan (2021-01-15 23:28 UTC)

<p>Focal point of the camera is the 3D position that remains at the same position on the screen display when the camera is rotated.</p>
<p>Focal point is set to the center of the displayed 3D content when you press <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view">Reset field of view button</a>. This is the most common way to set the focal point position.</p>
<p>You translate the focal point along the view plane when you <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-views">pan (translate) the 3D view</a>. To translate the focal point along the view normal there are several options, see details <a href="https://discourse.slicer.org/t/move-3d-focal-point-using-mouse-or-keyboard/15468/2">here</a>.</p>
<p>Can you tell a bit about your application? What are you visualizing and what would be the ideal way of setting the focal point?</p>

---
