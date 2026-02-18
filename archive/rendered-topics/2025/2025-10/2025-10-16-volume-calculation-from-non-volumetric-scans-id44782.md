# Volume Calculation From Non-Volumetric Scans

**Topic ID**: 44782
**Date**: 2025-10-16
**URL**: https://discourse.slicer.org/t/volume-calculation-from-non-volumetric-scans/44782

---

## Post #1 by @erencan (2025-10-16 12:05 UTC)

<p>Hello, I’m a newbie to the community. I wanted to ask if trying to calculate pituitary adenoma volumes from routine scans that are not volumetric is feasible. Does slicer take slice gaps and thickness and other parameters which may impact the calculation into account? Is the volume reliable? Thanks so much for the help.</p>

---

## Post #2 by @pieper (2025-10-16 13:53 UTC)

<p>In general if the image data is acquired with well defined spatial information then it’s possible to segment the structure of interest and calculate reasonably accurate volumes.  The exact type of acquisition is less important than the geometric information.</p>
<p>What modality are you referring to?</p>

---

## Post #3 by @erencan (2025-10-16 14:13 UTC)

<p>Hello, thank you for your answer. I intend to do volumetric calculations on pituitary MRI’s with coronal and sagittal T2, pre and post contrast T1 sequences and coronal dynamic contrast enhanced T1 sequences. I’ll likely use the coronal T2 sequences.</p>

---

## Post #4 by @pieper (2025-10-16 14:33 UTC)

<p>Generally yes, you should be able to calculate volumes accurately from those.  The exact accuracy will depend on the imaging parameters (in-slice pixel spacing and the spacing between the slices, which should both be as small as possible) and how well the image contrast relates to the actual tissue type (i.e. how well you can see the adenoma).</p>

---
