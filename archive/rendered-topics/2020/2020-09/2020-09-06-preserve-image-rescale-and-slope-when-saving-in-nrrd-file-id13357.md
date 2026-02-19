---
topic_id: 13357
title: "Preserve Image Rescale And Slope When Saving In Nrrd File"
date: 2020-09-06
url: https://discourse.slicer.org/t/13357
---

# Preserve image rescale and slope when saving in NRRD file

**Topic ID**: 13357
**Date**: 2020-09-06
**URL**: https://discourse.slicer.org/t/preserve-image-rescale-and-slope-when-saving-in-nrrd-file/13357

---

## Post #1 by @Chris_Rorden (2020-09-06 11:19 UTC)

<p>@ <a href="/u/lassoan">lassoan</a> I would argue that NRRD and NIfTI are very similar from a user perspective, but one core problem with DICOM to NRRD conversion is that NRRD is unable to preserve <a href="https://blog.kitware.com/dicom-rescale-intercept-rescale-slope-and-itk/" rel="nofollow noopener">rescale intercept (0028,1052) and slope (0028,1053) </a>. In contrast, NIfTI has a direct translation in <a href="https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/scl_slopeinter.html" rel="nofollow noopener">scl_inter and scl_slope</a>.</p>
<p>Consider the typical DICOM storage of <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Computed_Tomography_.28CT.2C_CAT.29" rel="nofollow noopener">CT scans</a>, where the raw data is stored as a 12-bit unsigned integer (0…4095) and the rescale intercept/slope translates this to Hounsfield units:</p>
<pre><code>(0028,0101) US 12       #   2, 1 BitsStored
(0028,1052) DS [-1024]  #   6, 1 RescaleIntercept
(0028,1053) DS [1]      #   2, 1 RescaleSlope
</code></pre>
<p>In this situation, a DICOM-to-NRRD converter must make a difficult decision:</p>
<ol>
<li>Keep original data format. In this example values will appear to be 0…4096 rather than -1024…3072.</li>
<li>Save image data as FLOAT32, requiring twice the disk space (and depending on the viewer, float vs int performance penalties).</li>
<li>Recognize that in this case both the rescale slope and intercept are integers, so losslessly apply the intensity transform and save data as signed 16-bit integer.</li>
</ol>
<p>While the final approach is attractive, I do not think it is common. Further, it will not work in situations like MRI-based arterial spin labeling where the slope and intercept values are not integers. Likewise, it will not work when one wants to use NRRD to create a detached header for a DICOM image.</p>
<p>In general, I am an advocate of NRRD, but as the developer of DICOM to NIfTI/NRRD converter (dcm2niix), the lack of a slope/intercept in NRRD keeps me up at night. I am not sure if all users are aware of the consequences of converting to NRRD.</p>

---

## Post #2 by @Chris_Rorden (2020-09-06 18:29 UTC)

<p>Issue also discussed <a href="https://discourse.slicer.org/t/nrrd-scale-factor/10232/3">here</a>.</p>

---
