---
topic_id: 12771
title: "2D Image Of Dcm File To 3D Volume"
date: 2020-07-29
url: https://discourse.slicer.org/t/12771
---

# 2D image of .dcm file to 3D Volume

**Topic ID**: 12771
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/2d-image-of-dcm-file-to-3d-volume/12771

---

## Post #1 by @Madelene_Habib (2020-07-29 16:34 UTC)

<p>Hi,<br>
I’ve received a .dcm file that only displays on the axial view as a 2D image of a sonogram. Is it possible to convert this into a 3D volume for segmentation? I’ve tried increasing the volumes using the Volumes module, as well as convert to DICOM module but I get the same thing.  If not, what type of file is preferred in 3DSlicer when wanting to segment fetal ultrasounds/sonograms. Attached is the screenshot of what I get when I uploaded the .dcm file onto 3DSlicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34e0bdfaed32ae5e170885353728398acba0731d.png" data-download-href="/uploads/short-url/7xMkQp5V4EQ2zsnOw9RfmxQ4XSt.png?dl=1" title="capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e0bdfaed32ae5e170885353728398acba0731d_2_665x500.png" alt="capture" data-base62-sha1="7xMkQp5V4EQ2zsnOw9RfmxQ4XSt" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e0bdfaed32ae5e170885353728398acba0731d_2_665x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e0bdfaed32ae5e170885353728398acba0731d_2_997x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34e0bdfaed32ae5e170885353728398acba0731d.png 2x" data-dominant-color="403E47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture</span><span class="informations">1090×819 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2020-07-29 17:58 UTC)

<p>This seems like a Secondary Capture, basically a 2D screenshot. This is a completely valid DICOM format, one of many types.</p>
<p>Do you have more files? If not, then it is not possible to have a 3D volume. Such volume renderings are usually done in the ultrasound workstation and saved as image. Real reconstructed 3D ultrasound volumes are very rare in current clinical settings.</p>

---

## Post #3 by @lassoan (2020-07-29 18:05 UTC)

<p>It is possible that standard DICOM fields only contain this 2D screenshot but there is a full 3D volume stored in private fields. <a href="https://github.com/SlicerHeart/SlicerHeart">SlicerHeart extension</a> can load many kinds of 3D/4D volumes.</p>

---

## Post #4 by @Madelene_Habib (2020-07-29 18:37 UTC)

<p>Thank you for your response! Do you know how (or where I can learn) to access/edit the private fields?</p>

---

## Post #5 by @lassoan (2020-07-29 18:50 UTC)

<p>You can view content of all DICOM fields in DICOM module (right-click on a series and choose “View DICOM metadata”). However, 3D ultrasound data is usually stored using complex encoding so you cannot trivially get the 3D volume out of it. That’s what SlicerHeart extension takes care of, for a number of ultrasound systems. See <a href="https://github.com/SlicerHeart/SlicerHeart#importing-dicom-files">DICOM import section</a> for more details.</p>
<p>If it is not clear enough how you can get the 3D volume then give us more information (brand and model of the ultrasound system, file size, maybe the whole DICOM metadata - with patient information excluded) and we can provide more specific advice.</p>

---

## Post #6 by @Madelene_Habib (2020-07-29 19:16 UTC)

<p>I understand. I will take a look at the section, and see if i can also get any more information to give you. Thanks again.</p>

---

## Post #7 by @fili_S_S (2024-04-23 18:35 UTC)

<p>hi, this seems to be a constant topic for … most of us.<br>
how to get the geometry from a DICOM file that seems to have only a screenshot.<br>
can you help me?<br>
i have a Mindray DC40  and a Mindray Renewa i9.</p>

---

## Post #8 by @lassoan (2024-04-23 21:21 UTC)

<p>The new <code>Ultrasound</code> extension (that will be officially announced soon but it is already available in the Extensions Manager) should retrieve all geometry data that is available in the DICOM header. <a class="mention" href="/u/ungi">@ungi</a>, developer of this new extension may provide more details if you tell a bit more about your project, what your end goal is, and how would you use the ultrasound images.</p>

---

## Post #9 by @ungi (2024-04-23 23:45 UTC)

<p>Hi <a class="mention" href="/u/fili_s_s">@fili_S_S</a>, have you tried to load you DICOM files in a recent preview version of Slicer? <a class="mention" href="/u/lassoan">@lassoan</a> recently updated how time series (ultrasound) are loaded in Slicer. I tested it with Mindray DICOM files and the pixel spacing was correct.</p>
<p>If you need the full geometry of the ultrasound (e.g. four corners of a fan shaped image), that is not stored in DICOM unfortunately. We needed those points and I added a module in the Ultrasound extension to manually annotate the corner points and save them in separate files besides the DICOMs.</p>
<p>There are other confusing features of Minday DICOM files. E.g., if you don’t change the imaging parameters on the machine, it stops saving image geometry in the DICOM headers. Instead, it keeps the same series ID, so all scans are loaded at the same time, and image geometry is loaded from the first file. That is bad  because we cannot throw out scans that we don’t need for a project. I’m planning to address these issues as much as possible in the Ultrasound extension, but it is a work-in-progress.</p>

---

## Post #10 by @fili_S_S (2024-05-02 00:50 UTC)

<p>Basically I’m trying to 3d print  fetal heads for NON COMERCIAL uses (gifts for patients in my private practice).  I’m trying go obtain fetus head models or early pregnancy embryo models</p>

---
