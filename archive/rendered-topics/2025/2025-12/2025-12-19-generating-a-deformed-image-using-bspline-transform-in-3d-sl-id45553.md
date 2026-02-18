# Generating a Deformed Image Using BSpline Transform in 3D Slicer

**Topic ID**: 45553
**Date**: 2025-12-19
**URL**: https://discourse.slicer.org/t/generating-a-deformed-image-using-bspline-transform-in-3d-slicer/45553

---

## Post #1 by @A_Eskandari (2025-12-19 12:48 UTC)

<p>Hello everyone,</p>
<p>I need to obtain CT images of a phantom (e.g., a Rando phantom) in two different states:<br>
Fixed Image: The initial, undeformed state of the phantom.<br>
Moving Image: The same phantom with a known and pre-defined deformation applied to it.<br>
Since the Rando phantom is inherently rigid, I plan to use 3D Slicer to artificially introduce a non-rigid deformation into the phantom’s CT image to create the second (Moving) image.</p>
<p>My question is: How can I apply a BSpline Transform with specific and controlled parameters (to serve as my Ground Truth) in 3D Slicer to generate the corresponding deformed image?<br>
Is this functionality available in 3D Slicer? If so, could you please guide me through the necessary steps to achieve this?<br>
Thank you very much for your assistance</p>

---

## Post #2 by @cpinter (2026-01-14 14:31 UTC)

<p>Sorry for the late reply.</p>
<p>If you want reproducibility, then what I’d suggest is either generate a deformation vector field image, or use landmarks to create the deformation. To generate an image, you could register two real patient images and use that vector field to transform your phantom. However, you won’t really have control over the deformation itself, and you’ll probably need to adjust volume geometry afterwards (e.g. the origin). To define a deformation with landmarks, you could try the LANDWARP module in the SlicerRT extension.</p>

---
