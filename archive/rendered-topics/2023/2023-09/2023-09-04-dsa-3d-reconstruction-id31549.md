---
topic_id: 31549
title: "Dsa 3D Reconstruction"
date: 2023-09-04
url: https://discourse.slicer.org/t/31549
---

# DSA 3D reconstruction

**Topic ID**: 31549
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/dsa-3d-reconstruction/31549

---

## Post #1 by @Murillo_Cunegatto_Br (2023-09-04 14:51 UTC)

<p>Hi</p>
<p>I wonder how to reconstruct a rotational cerebral angiography run to 3D with Slicer. The DICOM file contains 120 frames but loads in Slicer in the same position. I tried to transform each frame position but did not succeed.<br>
tried to use Sequence Registration but it ends with Error: Command ‘elastix’ died with &lt;Signals.SIGABRT: 6&gt;.<br>
Is there a way out ?</p>
<p>Thank you.</p>

---

## Post #2 by @kopachini (2023-09-05 15:51 UTC)

<p>You have to import 3d data (cbct), not angiography runs.<br>
It worked for me.</p>

---

## Post #3 by @lassoan (2023-09-05 16:31 UTC)

<p>You can use the <a href="https://iopscience.iop.org/article/10.1088/1742-6596/489/1/012079/meta">RTK toolkit</a> (pip-installable in Slicer) to reconstruct a 3D volume from 2D projections. The main challenge is to figure out how to get the geometry of each projection accurately.</p>
<p>I would recommend to reconstruct the 3D volume using the angio system’s built-in 3D reconstruction feature. The angio system’s volume reconstruction software performs sophisticated gantry calibration that measures rotation axis positions, takes into account deformation of the C-arm due to gravity, compensates for small calibration inaccuracies of the rotational encoders, etc. This information is not recorded in the DICOM images. If you don’t perform such calibration (and almost certainly you don’t, as it would take several years of effort) then the quality of the reconstructed 3D volumes will be much worse than what the angio system’s built-in software provides.</p>

---
