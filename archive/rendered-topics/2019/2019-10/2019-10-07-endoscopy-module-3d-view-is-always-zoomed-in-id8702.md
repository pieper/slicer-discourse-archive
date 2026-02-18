# Endoscopy module: 3D view is always zoomed in

**Topic ID**: 8702
**Date**: 2019-10-07
**URL**: https://discourse.slicer.org/t/endoscopy-module-3d-view-is-always-zoomed-in/8702

---

## Post #1 by @aptirumalai (2019-10-07 23:23 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Set the 3D view to a desired zoom setting so that I can see the slice traversing along the defined trajectory when I hit the Play button<br>
Actual behavior: As soon as I hit the Play button or advance a frame using the Frame Up/Down arrow, the 3D view zooms in. Is there a way to fix the zoom setting?</p>

---

## Post #2 by @lassoan (2019-10-07 23:51 UTC)

<p>It might look like the camera is zoomed in, but it is actually not. The module just places the camera on the trajectory and so you are probably very close to objects that you are interested in.</p>
<p>If you use perspective camera (default) then objects that are close to you appear larger. Objects that are very close to you appear very large. When you “zoom out” then the camera is moved farther.</p>
<p>You can switch the camera to parallel projection (this is available in the 3D view controller - when you click the push-pin icon in the top-left corner) or change the field of view of your perspective camera (you can only do this by using the Python console - see how to get access to the camera in examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras" rel="nofollow noopener">script repository</a>).</p>

---

## Post #3 by @aptirumalai (2019-10-08 16:00 UTC)

<p>Andras,<br>
Thanks for the tip. So all I had to do was to create a second camera which allows me to observe how the slice is generated as it traverses the path.</p>
<p>-Arun</p>

---
