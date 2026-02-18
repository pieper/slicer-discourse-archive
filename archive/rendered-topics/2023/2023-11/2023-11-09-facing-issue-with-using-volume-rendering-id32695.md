# Facing issue with using Volume Rendering

**Topic ID**: 32695
**Date**: 2023-11-09
**URL**: https://discourse.slicer.org/t/facing-issue-with-using-volume-rendering/32695

---

## Post #1 by @Tondup_Dolkar (2023-11-09 16:38 UTC)

<p>Operating System: Windows<br>
Slicer version: 5.2.2</p>
<p>Hello Everyone,</p>
<p>I am new to 3D Slicer. I am trying to obtain an ROI by using crop function of volume rendering. Whenever I click the show volume button, the 3D object appears outside the cubical frame box. I used center view feature as well but nothing changes. Further, when I click the enable button or Display ROI button for cropping purpose, the 3D object totally disappears. What is the issue and how can I rectify it? Any assistance would be greatly appreciated.</p>
<p>Following are other details:<br>
Preset: CT-Coronary-Arteries-3<br>
Rendering: VTK GPU Ray Casting</p>

---

## Post #2 by @lassoan (2023-11-09 16:43 UTC)

<p>Most likely your volume is under a non-linear transform because it was loaded from a DICOM series that required regularization (tilted-gantry acquisition, missing slices, etc). Volume rendering ignores non-linear transform (in current Slicer version, we disable volume rendering in this case to avoid confusion).</p>
<p>You can harden the transform on the volume to avoid all the other unexpected behavior you described.</p>

---

## Post #3 by @Tondup_Dolkar (2023-11-11 21:50 UTC)

<p>Hardening the transform worked. Thank you for your help.</p>

---

## Post #4 by @Davide_Punzo (2023-11-13 08:28 UTC)

<p>NOTE: Support for regularization transform hardening in DICOM Scalar plugin has been added. See <a href="https://discourse.slicer.org/t/enh-support-regularization-transform-hardening-in-dicom-scalar-plugin/32772">link</a>.</p>

---
