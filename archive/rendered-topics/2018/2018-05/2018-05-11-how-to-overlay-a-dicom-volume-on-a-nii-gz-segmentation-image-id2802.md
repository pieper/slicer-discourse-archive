# How to overlay a DICOM volume on a nii.gz segmentation image for editing in segment editor?

**Topic ID**: 2802
**Date**: 2018-05-11
**URL**: https://discourse.slicer.org/t/how-to-overlay-a-dicom-volume-on-a-nii-gz-segmentation-image-for-editing-in-segment-editor/2802

---

## Post #1 by @Fuessinger (2018-05-11 11:22 UTC)

<p>Operating system: MAC<br>
Slicer version: 4.81.<br>
Hallo,</p>
<p>I want to edit my segmentation which is saved as nii.gz on basis of a dicom file.<br>
How I can modify the dicim and the nii.gz to edit the segmentation?<br>
Thanks for your help.</p>

---

## Post #2 by @lassoan (2018-05-11 16:22 UTC)

<p>Load the DICOM volume using Slicer’s DICOM module. Load the nii.gz file using Add data function - and in the Add data dialog, click Show Options, scroll to the right, and make sure that LabelMap checkbox is selected.</p>

---

## Post #3 by @Stweie (2018-11-18 11:09 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>. I want to achieve the same result but using python script. Can you please give me idea or example code to achieve that. I used pydicom to load dcm series and nibabel module to read nii.gz file.</p>
<p>Thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lassoan (2018-11-18 15:21 UTC)

<p>See examples in the script repository:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file">Load volume from file</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images">Select what is shown in slice viewers</a></li>
</ul>

---

## Post #5 by @Stweie (2018-11-19 08:57 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>.  But When 3D slicer overlay nifti file over .dcm files, does it convert dicom series to nifti ? Otherwise how does the overlay transformation happens? can you please explain the principal/way this nifti on dicom series overlay ?</p>

---

## Post #6 by @lassoan (2018-11-19 13:07 UTC)

<p>Slicer can load images from a wide variety of file formats, including DICOM, nifti, nrrd, metaimage. Once an image is loaded, it can be displayed in slice viewer layers. Images can be saved in any file format, regardless of what format they were loaded from.</p>

---
