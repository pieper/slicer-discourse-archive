# Convert voxels to grayscale

**Topic ID**: 12376
**Date**: 2020-07-05
**URL**: https://discourse.slicer.org/t/convert-voxels-to-grayscale/12376

---

## Post #1 by @talmazov (2020-07-05 01:12 UTC)

<p>Hey,<br>
I am using<br>
slicer.util.arrayFromVolume<br>
to obtain an array of my slice widget view. However, the array contains voxel data, how can i convert that to RGB grayscale?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-07-05 01:56 UTC)

<p>I don’t know what you mean by “RGB grayscale”.</p>
<p>If your volume is a scalar volume (i.e., each voxel of the volume is a scalar, not a vector) then <code>slicer.util.arrayFromVolume</code> returns a 3D array.</p>
<p>If you want the displayed slice, with current window/level, opacity settings, all the overlays then you can get the 24-bit RGB image using <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">Screen Capture module’s logic</a>. This is intended for presentations, slide shows, etc., not for computation, because all the display settings (window/level, overlays, etc.) are burnt into the displayed image.</p>

---

## Post #3 by @talmazov (2020-07-30 21:57 UTC)

<p>the screen capture module is what i needed!<br>
Thanks!</p>

---
