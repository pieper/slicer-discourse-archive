---
topic_id: 32345
title: "Segmentation Not Working With 2 Sets Of Dicom Images"
date: 2023-10-20
url: https://discourse.slicer.org/t/32345
---

# Segmentation not working with 2 sets of DICOM images

**Topic ID**: 32345
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/segmentation-not-working-with-2-sets-of-dicom-images/32345

---

## Post #1 by @Ben_Fong (2023-10-20 14:11 UTC)

<p>Operating system: Mac Big Sur<br>
Slicer version: 4.11.20210226</p>
<p>Hi,</p>
<p>I have little experience with 3D Slicer. I managed simple work with one set of DICOM.<br>
When I worked with two sets of DICOMs (CT &amp; MRI).<br>
After I imported the second DICOM, segmentation only worked on the first set (CT or MRI, only can work on the first set).<br>
After linear transformation +/- rigid (6DOF) registration, segmentation did not work on either set (e.g. could not paint, already checked editable intensity range is off, could not adjust threshold limit).<br>
I had changed the order of import, the result was the same.<br>
I must missed some steps.<br>
Please advise on the reason and how to fix it.<br>
Thanks.</p>
<p>Ben</p>

---

## Post #2 by @lassoan (2023-10-20 14:12 UTC)

<p>See instructions for resolving this <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>.</p>
<p>I would recommend to upgrade to the current Slicer version. The one that you are using is more than 2 years old, therefore missing hundreds of important fixes and improvements.</p>

---

## Post #3 by @Ben_Fong (2023-10-20 15:17 UTC)

<p>Thanks for your advice. Will update and see how it is going.</p>

---

## Post #4 by @Ben_Fong (2023-10-20 16:28 UTC)

<p>I Updated the software, but the condition is the same.<br>
I loaded CT, then MRI, and can only work with Segment Editor with CT images, not the MRI one.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d371cdc108a094e08fd53a6a9eafac5b5258174.jpeg" data-download-href="/uploads/short-url/diCtXz1dz5wSwVME31tE23vWcx6.jpeg?dl=1" title="Screenshot 2023-10-21 at 12.21.02 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d371cdc108a094e08fd53a6a9eafac5b5258174_2_690x431.jpeg" alt="Screenshot 2023-10-21 at 12.21.02 AM" data-base62-sha1="diCtXz1dz5wSwVME31tE23vWcx6" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d371cdc108a094e08fd53a6a9eafac5b5258174_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d371cdc108a094e08fd53a6a9eafac5b5258174_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d371cdc108a094e08fd53a6a9eafac5b5258174_2_1380x862.jpeg 2x" data-dominant-color="63666A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-21 at 12.21.02 AM</span><span class="informations">1920×1200 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the data screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e48ed1c7b28f207eb425f07eab99884ee2904bb7.jpeg" data-download-href="/uploads/short-url/wBUQR7MKtD2ALqzRPPoq1jbeDRB.jpeg?dl=1" title="Screenshot 2023-10-21 at 12.21.23 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48ed1c7b28f207eb425f07eab99884ee2904bb7_2_690x431.jpeg" alt="Screenshot 2023-10-21 at 12.21.23 AM" data-base62-sha1="wBUQR7MKtD2ALqzRPPoq1jbeDRB" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48ed1c7b28f207eb425f07eab99884ee2904bb7_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48ed1c7b28f207eb425f07eab99884ee2904bb7_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e48ed1c7b28f207eb425f07eab99884ee2904bb7_2_1380x862.jpeg 2x" data-dominant-color="616468"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-21 at 12.21.23 AM</span><span class="informations">1920×1200 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How can I do segmentation also on the second set of DICOM?<br>
Please advise.<br>
Thanks.</p>

---

## Post #5 by @Ben_Fong (2023-10-20 17:14 UTC)

<p>Thanks for the advice.<br>
I updated the software.<br>
It is the same.<br>
But after some more work, I found that segmentation only works in the 1st set DICOM area, so I need to transform and register the 2nd set DICOM to the 1st set, then it will work. This solved my problem.<br>
Thanks.</p>

---

## Post #6 by @lassoan (2023-10-21 14:30 UTC)

<p>In each imaging study, the patient coordinate system origin is chosen differently and the patient is positioned on the table slightly differently. Therefore, if you want to use multiple images (e.g., CT and MRI) for creating a single segmentation then you need to align them first. You can use the spatial registration methods described <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">here</a>.</p>

---
