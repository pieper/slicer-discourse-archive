---
topic_id: 33151
title: "Issue With Dicom To Nifti Conversion"
date: 2023-11-30
url: https://discourse.slicer.org/t/33151
---

# Issue with DICOM to Nifti Conversion

**Topic ID**: 33151
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/issue-with-dicom-to-nifti-conversion/33151

---

## Post #1 by @Shovon_Ahmed (2023-11-30 20:14 UTC)

<p>I am trying to convert Dicom files to Nifti. But after conversion, I see a huge change in intensity (2nd image). I have also tried SimpleITK library bias correction. But the outcomes are the same.</p>
<p>Would anyone explain why it happened and how to fix this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5046459c035ee79677237b73bcdeab81c64e2934.jpeg" data-download-href="/uploads/short-url/bs8KMlujvfjdeEuSKL35FRgOw4I.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5046459c035ee79677237b73bcdeab81c64e2934_2_468x500.jpeg" alt="image" data-base62-sha1="bs8KMlujvfjdeEuSKL35FRgOw4I" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5046459c035ee79677237b73bcdeab81c64e2934_2_468x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5046459c035ee79677237b73bcdeab81c64e2934_2_702x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5046459c035ee79677237b73bcdeab81c64e2934.jpeg 2x" data-dominant-color="6C6C6C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">718×766 90 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Dicom</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94b50c14b91ec9e89a99c36ad0a2008f06079358.jpeg" data-download-href="/uploads/short-url/ldwyyOG1AF6qwEpJ12QztJv5soM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94b50c14b91ec9e89a99c36ad0a2008f06079358_2_524x500.jpeg" alt="image" data-base62-sha1="ldwyyOG1AF6qwEpJ12QztJv5soM" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94b50c14b91ec9e89a99c36ad0a2008f06079358_2_524x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94b50c14b91ec9e89a99c36ad0a2008f06079358_2_786x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94b50c14b91ec9e89a99c36ad0a2008f06079358.jpeg 2x" data-dominant-color="6C6C6C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">885×844 42.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Nifti (after conversion)</p>

---

## Post #2 by @pieper (2023-11-30 21:26 UTC)

<p>DICOM files can contain window/level information to indicated how they should be displayed, but nii files do not have that, so viewers just guess how best to display.  Try different window/level settings to confirm that the data was transferred correcty.</p>

---

## Post #3 by @Shovon_Ahmed (2023-12-09 07:56 UTC)

<p>I have tried to apply the same windowing and leveling using sitk while converting DICOM to NIFTI. But still, it doesn’t look the same. Any idea what would be the best conversion method to keep the visual information intact?</p>

---

## Post #4 by @Chris_Rorden (2023-12-27 15:00 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> the <a href="https://nifti.nimh.nih.gov/pub/dist/src/niftilib/nifti1.h" rel="noopener nofollow ugc">NIfTI header</a> does provide <code>cal_min</code> and <code>cal_max</code>. While these NIfTI fields are not often used, they would provide you a mechanism to retain the DICOM <a href="https://dicom.innolitics.com/ciods/digital-x-ray-image/dx-image/00281050" rel="noopener nofollow ugc">Window Center	(0028,1050)</a> and <a href="https://dicom.innolitics.com/ciods/nm-image/voi-lut/00281051" rel="noopener nofollow ugc">Window Width (0028,1051)</a> tags. Specifically:</p>
<pre><code class="lang-auto"> cal_min = WC - (WW/2)
 cal_max = WC + (WW/2)
</code></pre>
<p><a class="mention" href="/u/shovon_ahmed">@Shovon_Ahmed</a> have you tried converting your DICOMs to NIfTI and loading the resulting NIfTI allows you apply the original window values? This would help you trouble shoot at what stage the problem is occurring. My first thought might be to make sure that the DICOM <a href="https://www.kitware.com/dicom-rescale-intercept-rescale-slope-and-itk/" rel="noopener nofollow ugc">Rescale intercept, (0028,1052), and rescale slope (0028,1053) </a> have been correctly converted to the NIfTI scl_inter and scl_slope fields.</p>

---

## Post #5 by @pieper (2023-12-27 18:18 UTC)

<p>Thanks for the heads up on that <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> - perhaps we should add support for these cal_min/max fields in our nifti readers and writers.  It wouldn’t be a hard task if someone wants to take it on.</p>

---

## Post #6 by @Shovon_Ahmed (2023-12-31 06:54 UTC)

<p>Thank you <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a>. Normalizing WW and WC gives the same visual result as DICOM.</p>

---
