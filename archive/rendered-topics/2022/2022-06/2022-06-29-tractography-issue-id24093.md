# Tractography issue

**Topic ID**: 24093
**Date**: 2022-06-29
**URL**: https://discourse.slicer.org/t/tractography-issue/24093

---

## Post #1 by @massimo (2022-06-29 04:40 UTC)

<p>Operating system: Mac OSX Monterey<br>
Slicer version:5.0.2<br>
Expected behavior: Tractography visualization<br>
Actual behavior: Errors in data import</p>
<p>Dear Community,</p>
<p>I’m trying to create a 3d model of a tractography to view the that i just received.</p>
<p>I followed the various tutorial provided by this community but as soon as i try to import the DICOM’s set, i notice a serie of errors.</p>
<p>The DICOM files that i received are without extension .dcm, .nii, nifti, nrrd</p>
<p>I installed the UKFTractography, SlicerDMRI and SlicerDcm2nii</p>
<p>Following the link of the DICOM’s set.</p>
<p>I think I’m doing something wrong so I hope someone with more experience could indicate me the right process to follow.</p>
<p>Best regards</p>
<p>Massimo</p>
<p>https://…</p>

---

## Post #2 by @massimo (2022-06-29 06:55 UTC)

<p>Following the errors track</p>
<p>Could not load: Design - as DWI Volume as a Diffusion Volume (please see DWIConvert module for advanced options and help)</p>
<p>Could not load: ep2d_diff_mddw_20_p2_TRACEW - as DWI Volume as a Diffusion Volume (please see DWIConvert module for advanced options and help)</p>
<p>Could not load: 15: ep2d_diff_mddw_20_p2_TENSOR as a Scalar Volume</p>
<p>Could not load: ep2d_diff_mddw_20_p2_ColFA - as a 40 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume</p>

---

## Post #3 by @pieper (2022-06-30 14:17 UTC)

<p><a class="mention" href="/u/massimo">@massimo</a> you will need to install SlicerDMRI and make sure the dicom diffusion plugin is enabled.<br>
From there you can load the <code>ep2d_diff_mddw_20_p2</code> series and load it as DWI.  From there you can do interactive and whole brain tractography and other SlicerDMRI operations.  Most of the other diff series are pre-calculated from the DWI on the scanner.</p>

---

## Post #4 by @massimo (2022-06-30 17:57 UTC)

<p>Thanks for your kind reply,<br>
I already installed SlicerDMRI<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3b09b298ae66761b84ce19d5afe24c273fca7c7.jpeg" data-download-href="/uploads/short-url/nm4cG9btsH96Qi6q1TP1ayzxB5l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3b09b298ae66761b84ce19d5afe24c273fca7c7_2_539x500.jpeg" alt="image" data-base62-sha1="nm4cG9btsH96Qi6q1TP1ayzxB5l" width="539" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3b09b298ae66761b84ce19d5afe24c273fca7c7_2_539x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3b09b298ae66761b84ce19d5afe24c273fca7c7_2_808x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3b09b298ae66761b84ce19d5afe24c273fca7c7_2_1078x1000.jpeg 2x" data-dominant-color="514F5D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1508×1398 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To be more accurate, i do the following:<br>
Menu/Diffusion/Import And Export/ Tractography DICOM load</p>
<p>Unfortunately, during the import, I notice these serie of errors:<br>
Could not load: Design - as DWI Volume as a Diffusion Volume (please see DWIConvert module for advanced options and help)<br>
Could not load: ep2d_diff_mddw_20_p2_TRACEW - as DWI Volume as a Diffusion Volume (please see DWIConvert module for advanced options and help)<br>
Could not load: 15: ep2d_diff_mddw_20_p2_TENSOR as a Scalar Volume<br>
Could not load: ep2d_diff_mddw_20_p2_ColFA - as a 40 frames MultiVolume by ImagePositionPatient+AcquisitionTime as a MultiVolume</p>
<p>So cannot proceed.<br>
Did you try to import the same serie? In case, any errors?<br>
Thanks again<br>
Massimo</p>

---

## Post #5 by @pieper (2022-06-30 18:21 UTC)

<p>I was able to load and do tractography via the DICOM module from the <code>ep2d_diff_mddw_20_p2</code> series, so focus on that one and you should be able to load it too.  The other series are derived data that cannot be used for tractography.</p>
<p>Specifically:</p>
<ul>
<li>import the study into the DICOM database</li>
<li>select only the <code>ep2d_diff_mddw_20_p2</code>
</li>
<li>in the DICOM Plugins tab be sure DICOMDiffusionVolumePlugin is select and turn off the others</li>
<li>clicking Load should load data as a diffusion volume</li>
<li>you will see the baseline volume, but if you go to the Volumes module you can scroll through the diffusion directions</li>
<li>you can then use any of the SlicerDMRI operations (tensor estmation, interactive tractography, UKF, etc)</li>
</ul>

---
