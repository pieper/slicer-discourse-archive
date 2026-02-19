---
topic_id: 17412
title: "General Registration Pre Cbct Postcbct"
date: 2021-05-03
url: https://discourse.slicer.org/t/17412
---

# General Registration（pre CBCT+postCBCT）

**Topic ID**: 17412
**Date**: 2021-05-03
**URL**: https://discourse.slicer.org/t/general-registration-pre-cbct-postcbct/17412

---

## Post #1 by @lili-yu22 (2021-05-03 09:42 UTC)

<p>hi，<br>
i have a problem with BRANS<br>
i want to do do the registration between PreCBCT and ProCBCT of a patient’s skull<br>
Operating systerm:windows<br>
Slicer version:4.11.20210226<br>
Parameter set:General Registration<br>
percentage samples:0.05<br>
output settings:slicer liner transform<br>
Registration phases:Rigid(6DOF)<br>
masking option:ROI(the masked area is the skull base )<br>
after apply,the reasult is below:<br>
General Registration (BRAINS) standard output:<br>
Original Fixed image origin[-384, -384, -72.5, 0]<br>
Error while reading in imageC:/Users/13151/AppData/Local/Temp/Slicer/BIGBC_vtkMRMLLabelMapVolumeNodeB.nrrd</p>

---

## Post #2 by @lassoan (2021-05-21 18:47 UTC)

<p>It seems that one of the masks are invalid (probably empty). If you are sure that the mask is correct then you can try SlicerElastix extension, too.</p>

---

## Post #3 by @lili-yu22 (2021-05-24 23:34 UTC)

<p>thank you very much.</p>

---
