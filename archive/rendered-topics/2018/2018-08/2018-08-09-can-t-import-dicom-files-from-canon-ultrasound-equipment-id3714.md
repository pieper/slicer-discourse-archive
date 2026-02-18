# Can’t import dicom files from Canon ultrasound equipment

**Topic ID**: 3714
**Date**: 2018-08-09
**URL**: https://discourse.slicer.org/t/can-t-import-dicom-files-from-canon-ultrasound-equipment/3714

---

## Post #1 by @ksksbs (2018-08-09 08:26 UTC)

<p>Dear</p>
<p>I could not import dicom files from Canon ultrasound equipment. Canon’s dicom format seems to be not suitable to Slicer software.</p>
<p>Using SlicerHeart extension, but I could not import.</p>
<p>My operating system is Win 7 and Slicer version is 4.8.1.</p>
<p>Please, let me your comment.</p>
<p>Best regards,</p>
<p>Seonkyu Kim</p>

---

## Post #2 by @lassoan (2018-08-09 08:31 UTC)

<p>Is it a time sequence of 2D image frames or 3D image volumes?</p>

---

## Post #3 by @ksksbs (2018-08-10 02:39 UTC)

<p>Dear</p>
<p>As you mentioned, test file seems to be 3D images volumes.</p>
<p>There is a Dicom loading massage in dicom Browser as follows.</p>
<p>Could not load: test - as a 2 frames Volume Sequence by ImagePositionPatient+AcquisitionTime as a MultiVolume<br>
Could not load: 1: test as a Scalar Volume<br>
Could not load: test - as a 2 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume</p>
<p>Can it be solved?</p>

---

## Post #4 by @lassoan (2018-08-12 00:45 UTC)

<p>Can your share a sample data set (non-human or anonymized)?</p>

---

## Post #5 by @ksksbs (2018-08-13 01:52 UTC)

<p>Dear Andras Lasso</p>
<p>Thank you for your reply.</p>
<p>I attached dicom file for you.</p>
<p>Please, let me know your comment.</p>
<p>Best regards,</p>
<p>Seonkyu Kim.</p>
<p><a href="https://drive.google.com/file/d/1QK9vr6tPqwZIXKJ1-nFt4WAZpIUZ8Gvx/view?usp=drive_web" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/b/bcec071d2daf94f074e0d45f573498975b42d6b0.png" width="16" height="16"> 135751.zip</a></p>

---

## Post #6 by @lassoan (2018-08-13 09:44 UTC)

<p>Most data are stored in two large private DICOM tags. One of them seem to be uncompressed, so there is a chance that it can be decoded with some small software development. Are you familiar with Python scripting or can you ask someone at your or at a collaborating institution to help out? We can give advice how to get started.</p>
<p>Are there any export modes/options on your ultrasound system? Maybe if you export the data in a different format then it can be read directly.</p>

---
