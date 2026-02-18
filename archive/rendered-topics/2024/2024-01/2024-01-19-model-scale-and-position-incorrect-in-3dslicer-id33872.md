# Model Scale and Position Incorrect in 3DSlicer

**Topic ID**: 33872
**Date**: 2024-01-19
**URL**: https://discourse.slicer.org/t/model-scale-and-position-incorrect-in-3dslicer/33872

---

## Post #1 by @ebf (2024-01-19 15:03 UTC)

<p>My models (from photogrammetry) have correct scale and position in Metashape but when I open them in 3DSlicer, they do not retain their scale or x, y, z position. Has anyone else encountered this issue? How was it resolved?</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2024-01-19 16:07 UTC)

<p>3D surface formats often do not explicit units, so the values written in them is open to interpretation. Slicer in that case interprets those values as millimeters, which is the default unit in Slicer. I would check what units metashape is saving the coordinates (meters, centimeters, inches) first. If you figure that out, it is often a simple linear transform.</p>

---

## Post #3 by @ebf (2024-01-26 09:37 UTC)

<p>Thank you, this is helpful!</p>

---
