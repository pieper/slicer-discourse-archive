---
topic_id: 4298
title: "Merging Overlaying Ct And Mri Dicom Into One File"
date: 2018-10-05
url: https://discourse.slicer.org/t/4298
---

# Merging/Overlaying CT and MRI DICOM into one file

**Topic ID**: 4298
**Date**: 2018-10-05
**URL**: https://discourse.slicer.org/t/merging-overlaying-ct-and-mri-dicom-into-one-file/4298

---

## Post #1 by @DrWatson (2018-10-05 13:46 UTC)

<p>Operating system:Mac<br>
Slicer version:4.9</p>
<p>Hi, I’m trying to merge an MRI DICOM with a CT for targeted irradiation.  Our irradiator uses CT images for targeting, but the position of brain lesions can’t be seen by CT.  The goal is to produce a single CT file that has the lesion from the MRI visible in the correct location. So we basically want merge the volumes with comparable pixel values so that we can see both in a single image. Image quality isn’t really important, we just need the position of the lesion and the position of skull features that can be used for targeting.</p>
<p>So far we’ve been able to properly align the files using registration, and resample them (because we have far fewer MRI slices than CT slices), but we’re struggling with merging them together so that features from both are visible.</p>
<p>Does anyone know a method to do this?</p>
<p>Thanks!</p>

---

## Post #2 by @Python_Pros (2021-05-01 22:04 UTC)

<p>hi,<br>
what i understand is you want to merge an mri scan with a ct scan.<br>
well i have found a way doing so using python if you are interested please contact me for more details.<br>
thank you.</p>

---
