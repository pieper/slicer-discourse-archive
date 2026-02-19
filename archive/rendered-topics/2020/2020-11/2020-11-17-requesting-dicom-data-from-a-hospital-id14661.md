---
topic_id: 14661
title: "Requesting Dicom Data From A Hospital"
date: 2020-11-17
url: https://discourse.slicer.org/t/14661
---

# Requesting DICOM Data from a Hospital

**Topic ID**: 14661
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/requesting-dicom-data-from-a-hospital/14661

---

## Post #1 by @Brandon_Holt (2020-11-17 12:07 UTC)

<p>Hello everyone, I am no Radiologist so I am constantly learning new vocabulary in the field of DICOM.</p>
<p>I need help understanding the correct way to request DICOM data from a Hospital. I don’t need help writing the email, I just need help requesting the correctly formatted data so that it will load smoothly into 3D Slicer.</p>
<p>Any tips would be highly appreciated!</p>

---

## Post #2 by @pieper (2020-11-17 13:00 UTC)

<p>What kind of data do you need (anatomy, modality) and what do you need to do with it?</p>

---

## Post #3 by @Brandon_Holt (2020-11-17 13:13 UTC)

<p>We are working with several Hospitals, they have all sent us Chest CT data. Every dataset seems to load differently into 3D Slicer. Our goal is to Segment out the lungs and create a 3D Model for each data set provided.</p>
<p>Our Client originally sent us a sample data set from the NHS England and everything loaded and segmented easily.</p>

---

## Post #4 by @pieper (2020-11-17 13:23 UTC)

<p>Thanks for the context.  In this case yes, there’s some variability expected from hospital to hospital due to differences in scanners and local practices but Slier should be able to handle most if not all variables.  What kind of variations are causing problems for you?  Do you mean they have different contrast?  Resolution?  Sometimes you can control this by requesting certain acquisition or reconstruction parameters, but sometimes it’s not justified to give the patient a higher radiation dose so image quality can be limited.</p>

---

## Post #5 by @Brandon_Holt (2020-11-17 13:35 UTC)

<p>Thank you so much for the response. The data is all over the place. Some consist of only a few slices, some look like they are being squashed in the axial plane, some will not show anything in the volume rendering module, Some look like they have a ton of noise. So far, none of the datasets provided by the hospitals are behaving normally and we just want to make sure that we can properly communicate with the hospital in order to get exactly what we need. That being a relatively high resolution data set that allows us to create an accurate 3D Model of the lungs. I really appreciate your help on this.</p>

---

## Post #6 by @pieper (2020-11-17 13:45 UTC)

<p>Probably the best is to develop a short protocol description so they can try to match.  You can find this in the literature.  Find papers about CT studies of the kind of lung disease you are studying and look at the methods section.  You’ll see information about kVp, current, table speed, reconstruction kernels, slice spacing, collimation, etc.  Typically you may need no more than half a page to summarize the variables.  This should help you get consistent data that will be easier to analyze.</p>

---

## Post #7 by @Brandon_Holt (2020-11-17 13:48 UTC)

<p>Thank you so much Steve, I will look into that and let you know if I have anymore questions.</p>
<p>Regards,</p>
<p>Brandon</p>

---
