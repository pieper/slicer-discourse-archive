---
topic_id: 48929
title: "Can we skip registration in the OpenDose3D dosimetry workflow?"
date: 2026-11-16
url: https://discourse.slicer.org/t/48929
last_bumped: 2026-11-26T15:24:47.987Z
---

# Can we skip registration in the OpenDose3D dosimetry workflow?

**Topic ID**: 48929
**Date**: 2026-11-16
**URL**: https://discourse.slicer.org/t/can-we-skip-registration-in-the-opendose3d-dosimetry-workflow/48929

---

## Post #1 by @nicolas.chouin (2026-11-16 16:59 UTC)

<p>Dear OpenDose3D developers,</p>
<p>first, thank you for all the developments around OpenDose3D: it’s a very interesting tool.</p>
<p>I am a beginner with OpenDose3D so I do want to apologize if my questions are not fully relevant or already discussed elsewhere in a forum. I have performed my first dosimetry on patient data and I have noticed that the “registration” step is mandatory to get the absorbed dose to the organs I am interested in. I am usually not keen on registering the different time-points images on a reference image since to me, it’s a source of uncertainty on the final absorbed dose. This uncertainty can be avoided if we want to carry out organ-scale dosimetry (especially since we have access to automated segmentation nowadays). I was wondering if there was a way with OpenDose3D to skip this registration step: i.e. segmenting images at <strong>each</strong> time-point and then deriving absorbed-dose rate for the different tissues and eventually absorbed dose by integration, as it is already done in OpenDose3D?</p>
<p>Thank you for your answer.</p>
<p>Best regards,</p>
<p>Nicolas Chouin</p>

---

## Post #2 by @Alex_Vergara (2026-11-17 08:07 UTC)

<p>Hello Nicolas</p>
<p>Yes, you can skip registration with the cost of having to segment EVERY time point, otherwise you cannot propagate the segments from reference point. Registration is not mandatory, just open the next tab and you can do your convolution.</p>
<p>Regards<br>
Alex</p>

---

## Post #3 by @nicolas.chouin (2026-11-26 15:24 UTC)

<p>Hello Alex,</p>
<p>thank you for your answer.</p>
<p>To me the cost of segmenting every time-point is almost negligible since TotalSegmentator carries out this task within a few minutes without supervision. If this reduces the uncertainty on the absorbed dose (but this has to be verified), it is worth it.</p>
<p>Registration is indeed not mandatory but if I skip this step, I can indeed perform the convolution but then I need to carry out the next steps “by hand”. I can launch total segmentator 4 times (I have four time points) but then, do we agree that OpenDose3D is not able to quantify the SPECT images with the right segmentation and thus is not able to perform the time-activity curve fitting?</p>
<p>Best regards,</p>
<p>Nicolas</p>

---
