# Fly-through rendering

**Topic ID**: 1947
**Date**: 2018-01-26
**URL**: https://discourse.slicer.org/t/fly-through-rendering/1947

---

## Post #1 by @nirotu (2018-01-26 18:12 UTC)

<p>Hello:<br>
I am trying to use mesh file in MAYA software to create fly-though anatomic image.  BTW, is it possible to create fly-though within 3D Slicer itself?  Trying to avoid going to MAYA.</p>
<p>The mesh tile was created using slicer tools and save as .obj (MAYA can open this).</p>
<p>Thanks<br>
A.</p>

---

## Post #2 by @lassoan (2018-01-26 20:42 UTC)

<p>Yes, you can define trajectory and fly through with the camera using Endoscopy module.</p>

---

## Post #3 by @pieper (2018-01-26 20:46 UTC)

<p>And you can record it with the ScreenCapture module</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/Endoscopy" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/Endoscopy</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/ScreenCapture" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/ScreenCapture</a></p>

---

## Post #4 by @mikebind (2018-03-10 01:18 UTC)

<p>It doesn’t look like the Screen Capture module can record an Endoscopy fly through. The only animation mode is 3D Rotation, and the only way to play the fly-through is from the Endoscopy module. I’d love to get one recorded, but I don’t see how to do it from within 3D Slicer. Any other suggestions?</p>

---
