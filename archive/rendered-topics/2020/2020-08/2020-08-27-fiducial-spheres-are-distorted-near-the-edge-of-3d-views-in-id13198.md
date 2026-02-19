---
topic_id: 13198
title: "Fiducial Spheres Are Distorted Near The Edge Of 3D Views In"
date: 2020-08-27
url: https://discourse.slicer.org/t/13198
---

# Fiducial spheres are distorted near the edge of 3D views in orthographic display

**Topic ID**: 13198
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/fiducial-spheres-are-distorted-near-the-edge-of-3d-views-in-orthographic-display/13198

---

## Post #1 by @ungi (2020-08-27 16:36 UTC)

<p>I just noticed an interesting optical feature. I’m not sure if this is a bug or normal. For context, I display CT images with volume rendering in orthographic mode. I need to zoom out a lot to see whole image. I noticed that markup fiducial spheres look distorted near the edges of views, when the camera distance is large (meters). Markups look like an eggs, instead of a spheres.<br>
Orthographic views do not distort the images near the edges, that’s why I’m using that option. E.g. in the screenshot below, the skeleton looks undistorted. It seems like the fiducial spheres are not rendered using the same method as the volume.<br>
Would there be a way to make markup points always look like spheres in orthographic mode, regardless of camera position and zoom?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/164fc8d734e723315d24618f65eedbeb6c08b7e3.png" alt="image" data-base62-sha1="3bnroL8RWFrhFMjnxB0v3OXkLFF" width="332" height="276"></p>

---

## Post #2 by @lassoan (2020-08-27 20:55 UTC)

<p>It should not be possible to adjust field of view by adjusting camera distance in parallel projection mode. Maybe if you set the camera distance to extremely large values then numerical issues start to change size of rendered objects as a side effect (effectively it breaks the rendering).</p>
<p>You need to use <a href="https://vtk.org/doc/nightly/html/classvtkCamera.html#ad0054858ddff1c0b142ebe289d7f4c43">SetParallelScale</a> to change field of view in parallel projection mode.</p>
<p>Nevertheless, markups should not be rendered using perspective projection (which seems to be the case) if the view is in parallel projection mode. Do you have a script that reproduces this behavior?</p>

---

## Post #3 by @ungi (2020-08-27 23:28 UTC)

<p>Here are the steps to reproduce:</p>
<ul>
<li>Open Slicer (optionally switch to 3D-only layout, so you see better)</li>
<li>Add one or more fiducials near the center of the 3D view</li>
<li>Set orthographic view in the 3D view</li>
<li>In Markups display, set large glyph sizes so you can see them as spheres from far</li>
<li>Scroll your mouse wheel to create some distance between the camera and the fiducials</li>
<li>Pan the 3D view (shift+drag) so the fiducials get to the edge of the 3D view.<br>
At this point you will see that the fiducial spheres turn into eggs.</li>
</ul>
<p>You only need roll your mouse wheel 2-3 times (about 1 meter in RAS) to reproduce very distorted spheres.</p>
<p>Here is a screen recording: <a href="https://1drv.ms/v/s!AhiABcbe1DByg9ABrKXWeinra6u56g" rel="nofollow noopener">https://1drv.ms/v/s!AhiABcbe1DByg9ABrKXWeinra6u56g</a></p>

---

## Post #4 by @ungi (2020-08-27 23:34 UTC)

<p>I’m sure the problem is that markups are not rendered with the same method as other objects in the 3D view. As a workaround, I can set camera position (in Python) to very far from my markups. In parallel projection, camera position does not matter anyway. Increasing camera-fiducial distance doesn’t change anything in the rendered CT volume, but it reduces the distortion of markups. So it’s a good way to work around this bug (in parallel/orthographic projection at least).</p>

---

## Post #5 by @lassoan (2020-08-28 03:30 UTC)

<p>I’ve managed to fix the issue.</p>
<p>It was quite tricky - see <a href="https://github.com/Slicer/Slicer/commit/d31576db7802e99772e589ade784f769ed735d4f">here</a>. vtkGlyph3D’s glyph orienting feature only supports facing “towards a point”. To achieve parallel direction, we need to move the reported camera position to a distant point.</p>

---
