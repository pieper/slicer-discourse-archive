# Function for surface registration

**Topic ID**: 1776
**Date**: 2018-01-07
**URL**: https://discourse.slicer.org/t/function-for-surface-registration/1776

---

## Post #1 by @shellyverde (2018-01-07 21:14 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8</p>
<p>Hi,<br>
I have patient data in CT Dicom space and I am capturing points in tracker space on patient. So I need to register the patient in tracker space (with captured points) to the CT Dicom space. I couldn’t find the function for this type of registration (surface points in tracker space to model in Dicom space). Could you please advise if there is already such function?<br>
Thanks,<br>
-Shelly</p>

---

## Post #2 by @shellyverde (2018-01-07 22:09 UTC)

<p>Can I use SlicerIGT ‘Fiducials-model Registration’ for it?<br>
Thanks,<br>
-Shelly</p>

---

## Post #3 by @lassoan (2018-01-08 02:15 UTC)

<p>Usually you register the patient using landmark-based registration, using Fiducial registration wizard module (in SlicerIGT extension). In special cases, when you cannot identify landmarks clearly then you may follow up on that with a surface-to-pointset registration, using Fiducials-Model registration module. See detailed step-by-step tutorials at <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT user training page</a>.</p>

---

## Post #4 by @shellyverde (2018-01-08 02:48 UTC)

<p>Got it and thanks a lot for the quick reply.<br>
-Shelly</p>

---
