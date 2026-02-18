# SlicerMorph failed to load DICOM

**Topic ID**: 13684
**Date**: 2020-09-24
**URL**: https://discourse.slicer.org/t/slicermorph-failed-to-load-dicom/13684

---

## Post #1 by @lv_xiao (2020-09-24 03:53 UTC)

<p>Operating system: Win10<br>
Slicer version: 1.5<br>
Expected behavior: Load DICOM images<br>
Actual behavior: SlicerMorph crashed</p>
<p>Hello, I am new to SlicerMorph. I followed the tutorial <a href="https://spujol.github.io/SlicerDICOMTutorial/" rel="noopener nofollow ugc">https://spujol.github.io/SlicerDICOMTutorial/</a> and tried to load TorsoCT into SlicerMorph1-5. After importing the data, when I click “Examine” or “Load”, the software carshes. The message before the software automatically exits is as below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6f732525c956145080a6a39f20df5ecc9a13242.png" alt="Snipaste_2020-09-24_11-24-05" data-base62-sha1="nP2SkvcuwuyeY5wxmkk6KLi1v8u" width="414" height="224"></p>
<p>I noted that <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a> suggests that “See if the SlicerDcm2nii extension will convert your images” . I am not sure if I am missiing the Dcm2nii extension. I tried to install SlicerDcm2nii extension in Extension Manager but I did not find any plugin related to Dcm2nii. BTW, the sample DICOM file from the link above could not be successfully loaded either.</p>
<p>I am confused how I can load DICOM images into my data. I am using laptop with a RAM of 16 GB.</p>

---

## Post #2 by @lassoan (2020-09-24 03:54 UTC)

<p>Please try with the very latest Slicer Preview Release (that you download today) and let us know if it works well.</p>

---

## Post #3 by @muratmaga (2020-09-24 04:00 UTC)

<p>DCM2NIIX plugin sometimes causes a crash. Disable the plugin as shown here: <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/DICOM/Disable_dcm2niix_plugin.png" rel="noopener nofollow ugc">https://github.com/SlicerMorph/S_2020/blob/master/Day_1/DICOM/Disable_dcm2niix_plugin.png</a><br>
then re-try the import</p>

---

## Post #4 by @lv_xiao (2020-09-24 04:53 UTC)

<p>Disabling DCM2NIIX solved the issue. Thank you.</p>

---

## Post #5 by @lassoan (2020-09-24 11:15 UTC)

<p>The crash is due to this known issue: <a href="https://github.com/Slicer/Slicer/issues/5078">https://github.com/Slicer/Slicer/issues/5078</a></p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> is this supposed to be fixed in latest Slicer Preview Release?</p>

---

## Post #6 by @muratmaga (2020-09-24 14:40 UTC)

<p>This might have been fixed in the nightly, but we maintain a prepackaged version of SlicerMorph that is a few weeks stale, in case people cannot download it from the main Slicer site. That’s what <a class="mention" href="/u/lv_xiao">@lv_xiao</a> was using.</p>

---

## Post #7 by @Sam_Horvath (2020-09-25 00:07 UTC)

<p>Yes, this should be fixed in the current Preview</p>

---
