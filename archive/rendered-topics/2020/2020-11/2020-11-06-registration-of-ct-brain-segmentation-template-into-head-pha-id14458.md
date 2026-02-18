# Registration of CT brain segmentation template into head phantom in 3D Slicer

**Topic ID**: 14458
**Date**: 2020-11-06
**URL**: https://discourse.slicer.org/t/registration-of-ct-brain-segmentation-template-into-head-phantom-in-3d-slicer/14458

---

## Post #1 by @hajarzuber (2020-11-06 06:57 UTC)

<p>Hi, I am developing a head phantom made of wood (all HU represent soft tissue), thus the image in CT shows only homogenous grayscale with no bone. However, I need to delineate OAR (parotid gland, lens and brain) for measurement of absorbed dose in treatment planning for radiotherapy. May I know if there is any available brain delineation template or is there any better ways to delineate the invisible area, due to the condition of the phantom?<br>
Thank you so much Sir.</p>

---

## Post #2 by @lassoan (2020-11-06 16:26 UTC)

<p>Can your treatment planning system import DICOM RT structure sets created in other software? If yes, then you warp an existing segmentation (RT structure set) to your phantom by following these steps:</p>
<ul>
<li>import any head&amp;neck segmentation from TCIA (using TCIA browser module) that has RT structure set</li>
<li>register the patient CT to the CT scan of your wooden phantom using landmarks (for example, using “Fiducial registration wizard” module)</li>
<li>apply the transform to the RT structure set</li>
<li>export the RT study (CT and structure set) to DICOM using export type “RT”</li>
<li>import the exported study into your treatment planning system</li>
</ul>
<p>Before you start, you need to install SlicerRT, TCIABrowser, and SlicerIGT extensions. If you get stuck at any point then let us know.</p>

---
