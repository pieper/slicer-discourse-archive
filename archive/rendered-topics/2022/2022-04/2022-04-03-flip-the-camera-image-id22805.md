# Flip the camera image

**Topic ID**: 22805
**Date**: 2022-04-03
**URL**: https://discourse.slicer.org/t/flip-the-camera-image/22805

---

## Post #1 by @jgc2155338150 (2022-04-03 13:10 UTC)

<p>Hello, after my 3DSlicer is connected to the camera, the image displayed is upside down, and clicking the center button next to R is just adapt to the center display of the screen, which is still upside down.  How do I flip it? Or the flip caused by my configuration file parameters not being correct</p>

---

## Post #2 by @lassoan (2022-04-03 13:19 UTC)

<p>You have two main options:</p>
<ul>
<li>A. Set the correct physical directions (which images axis corresponds to which physical axis) in the volume node using <code>SetIJKToRASDirections</code>. If you use PlusToolkit for image streaming then then you can set the image orientation using the M/U/N/F codes.</li>
<li>B. Set the desired orientation (what physical direction corresponds to which directions on the screen) in the slice node using <code>SetSliceToRAS</code>.</li>
</ul>

---
