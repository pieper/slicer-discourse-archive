# Is DICOM to NIFTI a fully anonymised file in Slicer?

**Topic ID**: 13347
**Date**: 2020-09-05
**URL**: https://discourse.slicer.org/t/is-dicom-to-nifti-a-fully-anonymised-file-in-slicer/13347

---

## Post #1 by @kt297 (2020-09-05 09:53 UTC)

<p>When saving a DICOM into NIFTI in slicer does the resultant NIFTI file fully anonymised to patient personal data?</p>

---

## Post #2 by @lassoan (2020-09-05 21:44 UTC)

<p>Research file formats, such as nrrd, metaimage, nifti do not contain patient health information in standard fields, only the minimum information needed for interpreting the image (image geometry and type). It is possible to store more information in custom fields, but 3D Slicer does not save any patient information in custom fields either.</p>
<p>However, anonymization is a really complicated topic and depending on your study protocol, removing patient health information might not be sufficient deidentification. For example, you may need to remove or blur the patient’s face (if visible in the image), modify image orientation and axis direction (to prevent easy matching with the original data set), etc.</p>
<p>Note that nifti file format is not a general-purpose file format: it is only intended for brain imaging. If you work with other kind of images, nrrd may be a more suitable format.</p>

---

## Post #3 by @lassoan (2020-09-06 17:45 UTC)

<p>A post was split to a new topic: <a href="/t/preserve-image-rescale-and-slope-when-saving-in-nrrd-file/13357">Preserve image rescale and slope when saving in NRRD file</a></p>

---

## Post #4 by @kt297 (2020-09-06 12:10 UTC)

<p>Thanks,</p>
<p>So I assume CT DICOM to NIFTI conversion sufficiently anonymise personalised patient data. Or would one recommend to anonymise the DICOM first then convert to NIFTI?</p>

---

## Post #5 by @lassoan (2020-09-06 17:43 UTC)

<aside class="quote no-group" data-username="kt297" data-post="4" data-topic="13347">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/a587f6/48.png" class="avatar"> kt297:</div>
<blockquote>
<p>I assume CT DICOM to NIFTI conversion sufficiently anonymise personalised patient data</p>
</blockquote>
</aside>
<p>For most study protocols, conversion to nifti or nrrd is enough. If anonymization requirements are very strict (for example require changing the image origin or blurring of patient face) then you need to do extra steps to fulfill those.</p>
<aside class="quote no-group" data-username="Chris_Rorden" data-post="1" data-topic="13357">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"><a href="https://discourse.slicer.org/t/preserve-image-rescale-and-slope-when-saving-in-nrrd-file/13357/1">Preserve image rescale and slope when saving in NRRD file</a></div>
<blockquote>
<p>one core problem with DICOM to NRRD conversion is that NRRD is unable to preserve <a href="https://blog.kitware.com/dicom-rescale-intercept-rescale-slope-and-itk/">rescale intercept (0028,1052) and slope (0028,1053)</a></p>
</blockquote>
</aside>
<p>This is a good point and it would be interesting to discuss it further. I’ll move your post to a new topic.</p>

---

## Post #6 by @Chris_Rorden (2020-09-06 18:39 UTC)

<p>@ <a href="/u/kt297">kt297</a> it is worth noting that Slicer includes several tools to convert DICOM to NIfTI (and NRRD). I think all will by default anonymize data. In theory, a tool could save personal details in the file name or a text field (e.g. NIfTI Intention, DataType, Description, DBName and AuxFile text fields).</p>
<p>Since dcm2niix is one of the extensions that support DICOM to NRRD/NIfTI conversion, I will say that dcm2niix will store the series time as the number of seconds since mid-night in the Description field (which allows you to synchronize physiological data like respiration and cardiac signals). From the command line, it is possible to get dcm2niix to store Patient Name (0010,0010), Patient ID (0010,0020) and Data;Time (0008,0020; 0008,0030) in the <a href="https://github.com/rordenlab/dcm2niix/blob/master/FILENAMING.md" rel="nofollow noopener">filename</a>. The command line option <code>-ba n</code> will also disable anonymization from the BIDS sidecar, storing these same attributes there.</p>

---

## Post #7 by @Saima (2023-06-15 04:52 UTC)

<p>Hi Andras,<br>
How can I convert multiple dicom images into multiple nrrd files. I have a folder with multiple dicom images for several MRIs.</p>
<p>Is there anything available in slicer for the conversion of all these dicom images into seperate nrrd files?</p>
<p>regards,<br>
saima</p>

---
