---
topic_id: 19129
title: "Diffusion Brain Dicom To Nrrd Conversion"
date: 2021-08-09
url: https://discourse.slicer.org/t/19129
---

# Diffusion brain: DICOM to NRRD conversion

**Topic ID**: 19129
**Date**: 2021-08-09
**URL**: https://discourse.slicer.org/t/diffusion-brain-dicom-to-nrrd-conversion/19129

---

## Post #1 by @rahulpaul (2021-08-09 23:21 UTC)

<p>Operating system: MacOS<br>
Slicer version: 4.11</p>
<p>I am having little difficulty in converting the Dicom images to NRRD using DWIConvert. I believe something is not happening correctly during conversion as after conversion I can’t find any DWI components to choose. I am uploading the 24 sequences of DWI in Dicom. I can also upload the Dicom header info if anyone requires.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29f58cedf43f08ac81f702b3e0279c62a4ce9e28.jpeg" data-download-href="/uploads/short-url/5ZbFhpMzSakDoP4teaFDP2s9vG8.jpeg?dl=1" title="Screen Shot 2021-08-09 at 5.24.12 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29f58cedf43f08ac81f702b3e0279c62a4ce9e28_2_643x500.jpeg" alt="Screen Shot 2021-08-09 at 5.24.12 PM" data-base62-sha1="5ZbFhpMzSakDoP4teaFDP2s9vG8" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29f58cedf43f08ac81f702b3e0279c62a4ce9e28_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29f58cedf43f08ac81f702b3e0279c62a4ce9e28_2_964x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29f58cedf43f08ac81f702b3e0279c62a4ce9e28_2_1286x1000.jpeg 2x" data-dominant-color="1D1D1D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-09 at 5.24.12 PM</span><span class="informations">1434×1114 97.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any help will be really appreciated.</p>

---

## Post #2 by @Chris_Rorden (2021-08-10 12:56 UTC)

<p>You might want to choose the <code>Extension Manager</code> menu item from the <code>View</code> menu and install the SlicerDcm2nii module.<a class="mention" href="/u/ihnorton">@ihnorton</a> can provide more details. This will give you access to the DCM2niixGUI module where you can select an input folder and apply.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/081a3b869019d9933359023d51ac17a60cb8bad9.png" data-download-href="/uploads/short-url/19G1pbWNtO2kjMWocq9QXevjSUp.png?dl=1" title="dcm2niix" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/081a3b869019d9933359023d51ac17a60cb8bad9_2_690x158.png" alt="dcm2niix" data-base62-sha1="19G1pbWNtO2kjMWocq9QXevjSUp" width="690" height="158" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/081a3b869019d9933359023d51ac17a60cb8bad9_2_690x158.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/081a3b869019d9933359023d51ac17a60cb8bad9_2_1035x237.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/081a3b869019d9933359023d51ac17a60cb8bad9_2_1380x316.png 2x" data-dominant-color="CACED6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dcm2niix</span><span class="informations">1598×368 81.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There are two other options:</p>
<ol>
<li>Use <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage" rel="noopener nofollow ugc">dcm2niix</a> from the command line. Provide the <code>-e y</code> to export to NRRD (instead of NIfTI), so the minimal command line would be <code>dcm2niix -e y /path/to/DICOMs</code>
</li>
<li>Get <a href="https://www.nitrc.org/plugins/mwiki/index.php/mricrogl:MainPage" rel="noopener nofollow ugc">MRIcroGL</a> and choose <code>Convert DICOM to NIfTI</code> from the <code>Import</code> menu. This provides a nice graphical wrapper for the many options available with dcm2niix. The relevant one for you is to choose NRRD from the <code>Output Format</code> drop down.</li>
</ol>
<p>If you continue having issues, you may want to provide details regarding the scanner manufacturer (e.g. Bruker, Canon, GE, Philips, Siemens, UIH), as they each use different methods to define <a href="https://www.na-mic.org/wiki/NAMIC_Wiki:DTI:DICOM_for_DWI_and_DTI" rel="noopener nofollow ugc">DTI</a> parameters.</p>

---

## Post #3 by @rahulpaul (2021-08-12 11:44 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> Thank you for your response. But its not working still. I can post the dicom headers, if that helps.</p>

---

## Post #4 by @rahulpaul (2021-08-18 12:01 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> I sent you a google drive link with my data.</p>

---

## Post #5 by @Chris_Rorden (2021-08-18 12:45 UTC)

<p><a class="mention" href="/u/rahulpaul">@rahulpaul</a> your DICOM images are from a Siemens VB17 MRI system. Unfortunately, the images were overzealously anonymized, removing the crucial sequence details stored in the <a href="https://nipy.org/nibabel/dicom/siemens_csa.html" rel="noopener nofollow ugc">CSA header</a>. The gradient directions and many other parameters are stored in the <a href="https://github.com/rordenlab/dcm2niix/tree/master/Siemens" rel="noopener nofollow ugc">CSA header</a>. Without these details, it is impossible for any conversion tool to infer these properties. I suggest you check the provenance of these images. Images directly from the scanner will have the CSA header intact, and you need to chose an anonymization tool that preserves this. This is a limitation of your images, not the tools used to import DICOM data.</p>

---
