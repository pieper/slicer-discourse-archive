# Vtk streamlines not aligning with reference image

**Topic ID**: 12367
**Date**: 2020-07-03
**URL**: https://discourse.slicer.org/t/vtk-streamlines-not-aligning-with-reference-image/12367

---

## Post #1 by @Vinny (2020-07-03 23:46 UTC)

<p>Hi,</p>
<p>I am using 3D Slicer 4.11.0-2020-06-06 and noticed that the imported vtk streamlines do not align with the corresponding reference scan; however, for 3D Slicer version 4.10.2, the streamlines do align.</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2020-07-04 03:51 UTC)

<p>If you load old model files (that do not have embedded coordinate system information) then you may need to manually select “RAS” coordinate system in the “Add data” window.</p>
<p>See explanation here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default</a></p>

---

## Post #3 by @Vinny (2020-07-04 12:58 UTC)

<p>Thank you Andras, this worked great.</p>

---
