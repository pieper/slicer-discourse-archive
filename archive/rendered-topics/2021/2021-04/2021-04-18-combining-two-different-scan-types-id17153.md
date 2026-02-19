---
topic_id: 17153
title: "Combining Two Different Scan Types"
date: 2021-04-18
url: https://discourse.slicer.org/t/17153
---

# Combining two different scan types

**Topic ID**: 17153
**Date**: 2021-04-18
**URL**: https://discourse.slicer.org/t/combining-two-different-scan-types/17153

---

## Post #1 by @arif (2021-04-18 03:53 UTC)

<p>Hi everyone!</p>
<p>Is it possible to combine two different scan types(PET/CT and MpMRI) in one dicom file?</p>
<p>Have a nice day.</p>

---

## Post #2 by @lassoan (2021-04-18 04:00 UTC)

<p>A fused PET/CT could be only exported in DICOM as secondary capture, which could not be used for much. What would you like to achieve?</p>

---

## Post #3 by @arif (2021-04-19 14:13 UTC)

<p>Thank you for your answer.</p>
<p>I am modeling mpMRI as 3D with Segment editor module of slicer. I would like to add PET/CT findings(segmented and modeled in slicer with PET-IndiC) of the same patient to the model generated from mpMRI. The reasoning behind this is mpMRI gives clear anatomical structure that PET PSMA lacks. So I need to fuse them to achieve greater understanding of the patient.</p>
<p>Best Regards</p>

---

## Post #4 by @lassoan (2021-04-19 17:27 UTC)

<p>If you mean you want to see multiple volumes while you are segmenting, you can choose display one volume as background (by clicking the eye icon in Data module) and the other module as foreground (by right-clicking on the eye icon and choosing “Show in slice views as foreground”). You can adjust view settings as described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#interacting-with-views">user guide</a>.</p>
<p>In Segment Editor you can switch to a different “Master volume” anytime. The master volume is used editor effects that perform operations guided by an underlying volume.</p>

---

## Post #5 by @arif (2021-04-20 12:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/207d50f0f0842eb2cd308b926462c396a35a8ed8.png" data-download-href="/uploads/short-url/4DpLB89Xbt3yFcR4tvio6qcaCeI.png?dl=1" title="sad" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/207d50f0f0842eb2cd308b926462c396a35a8ed8_2_517x274.png" alt="sad" data-base62-sha1="4DpLB89Xbt3yFcR4tvio6qcaCeI" width="517" height="274" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/207d50f0f0842eb2cd308b926462c396a35a8ed8_2_517x274.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/207d50f0f0842eb2cd308b926462c396a35a8ed8_2_775x411.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/207d50f0f0842eb2cd308b926462c396a35a8ed8_2_1034x548.png 2x" data-dominant-color="CBCFD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sad</span><span class="informations">1365×725 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello Andras;<br>
I have tried your suggestion and as shown in the image the two series did not overlapped. Do you have any suggestion on overlapping the two series better ?</p>
<p>Best Regards</p>

---

## Post #6 by @lassoan (2021-04-20 12:52 UTC)

<p>You can register images to each other using various <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">registration techniques</a>. Probably the most common method for PET-CT to MRI registration is to compute the CT to MRI transform and use that to align the PET image, too. But if you don’t have the CT you can align the images manually or by specifying matching anatomical landmarks.</p>

---

## Post #7 by @Pavel_Pakhomov (2024-09-15 13:05 UTC)

<p>can you help - how save that fusion in Dicom?</p>

---
