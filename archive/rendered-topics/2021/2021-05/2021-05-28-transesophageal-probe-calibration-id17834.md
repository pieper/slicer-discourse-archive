# Transesophageal Probe calibration

**Topic ID**: 17834
**Date**: 2021-05-28
**URL**: https://discourse.slicer.org/t/transesophageal-probe-calibration/17834

---

## Post #1 by @Gerardo (2021-05-28 04:12 UTC)

<p>Dear 3D Slicer community,</p>
<p>I am wondering if the steps for freehand tracked ultrasound calibration (<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationfCal.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Freehand tracked ultrasound calibration application (fCal)</a>) apply for transesophageal echocardiography. Thank you.</p>
<p>Regards,<br>
Gerardo</p>

---

## Post #2 by @lassoan (2021-05-28 21:30 UTC)

<p>You can use fCal to calibrated transesophageal probes the same way as any other linear arrays. However, calibration is not the biggest challenge. It is harder to get the probe’s 3D position and get the current rotation angle and imaging depth. There are solutions to this that have been implemented with Slicer and Plus, such as attaching an electromagnetic tracking sensor near the probe tip (it required a custom sheath, as it was not possible to get the sensor wire into the probe) and use OCR to read angles from the ultrasound screen (that’s why the OCR feature was added to Plus). You can find more details in papers in Terry Peter’s group at Robarts and you can ask for more details on the data acquisition setup at the <a href="https://github.com/PlusToolkit/PlusLib/discussions">Plus toolkit’s repository</a>.</p>

---

## Post #3 by @Gerardo (2021-05-31 22:26 UTC)

<p>Thank you, Andras. I have been looking for more details on the data acquisition setup, but I could not find them. Could you please provide me with more information? Thank you.<br>
Regards,<br>
Gerardo</p>

---

## Post #4 by @lassoan (2021-05-31 23:20 UTC)

<p>I would need to know much more about your application to give more specific advice. What ultrasound brand&amp;model do you have and what probe do you use? Do you have real-time digital interface (software API) access to the images and metadata or do you plan to use a framegrabber? How do you plan to track the probe? How do you plan to get the image angle information? Would you like to acquire 2D+t image sequence of a single plane? Or biplane? Will the probe move during acquisition? Can the image rotation angle, imaging depth, or other image geometry parameters change during the acquisition? Do you plan to reconstruct 3D or 4D volumes? What is the clinical application? Guiding minimally invasive valve replacement? Do you need to integrate with other imaging modalities (fluoro, trans-thoracic echo, …)?</p>

---

## Post #5 by @Gerardo (2021-06-01 02:42 UTC)

<p>Thank you Andras for this opportunity to explain my project. The project intends to evaluate the effect of an electromagnetic measurement system (NDI Aurora V2) in the outcome of a perventricular intervention. The intervention is mainly guided by transesophageal echocardiography (TEE). A group of cardiologists will perform the intervention in heart phantoms. We would like to record the actions of the cardiologists during all the procedure, including the motion of the TEE probe and the respective ultrasound images. I would like to apply an appropriate calibration method for the TEE. I have experience with the calibration of a transthoracic probe using fCal, but TEE is new for me. We are working with an ultrasound machine GE Vivid E95 with a TEE pediatric probe. We plan to use a framegrabber. We plan to track the probe with the electromagnetic measurement system; however, I am still thinking about how to attach a sensor to the probe. For now, I do not know how to get the image angle information; in your previous answer, you mentioned OCR in the Plus toolkit to do that, but I could not find it. I would like to acquire 2D+t image sequence of a single plane. The probe moves during the acquisition. The image rotation angle and imaging depth could change during acquisition. I do not plan to reconstruct volumes. The clinical application is in cardiology, specifically in ventricular septal defects. I do not need to integrate with other imaging modalities.<br>
Please let me know if more information is required. Thank you.<br>
Regards,<br>
Gerardo</p>

---
