---
topic_id: 8047
title: "Import Dti Nifti"
date: 2019-08-15
url: https://discourse.slicer.org/t/8047
---

# Import DTI nifti

**Topic ID**: 8047
**Date**: 2019-08-15
**URL**: https://discourse.slicer.org/t/import-dti-nifti/8047

---

## Post #1 by @DTI (2019-08-15 19:39 UTC)

<p>Hi,<br>
Is it possible to load tensor data into slicer directly? I had problems with diffusion orientation using the dwi import tool, so I calculated the tensors outside slicer with fsl. Now I would like to import the tensor data (nifti) to perform streamline tractography.<br>
is this possible?<br>
Thank you!</p>

---

## Post #2 by @ljod (2019-08-15 22:12 UTC)

<p>Hi! Did you try DICOM import using the new DCM2nii module? This will be the preferred way to load DWI data moving forward. It will replace DWIConvert.</p>

---

## Post #3 by @DTI (2019-08-16 14:27 UTC)

<p>Hi<br>
Thank you, that worked very well for DICOM (that was acquired in coronal fashion)!</p>
<p>Can it also handle nifti files?</p>
<p>Thank you, Lorenz</p>

---

## Post #4 by @ljod (2019-08-16 14:41 UTC)

<p>Awesome!!! Are you the Lorenz Epprecht that I know? I was optimistic this fix would work for your data. Glad you’ve tried it out now!</p>
<p>Technically the dcm2nii program can output nifti files. The current implementation in Slicer uses dcm2nii in order to convert DICOM to nrrd. Future work could ideally leverage better nifti file loading.</p>
<p>Can your project work using DICOM instead of nifti?</p>

---

## Post #5 by @DTI (2019-08-16 14:56 UTC)

<p>Hi Lauren. Yes, it’s me!<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Just thought the topic might be of interest to a wider readership.</p>
<p>Thanks for the fix! I don’t have DICOM for all subjects, but will try to convert nifti back to DICOM for importing to Slicer!</p>
<p>I think the nifti import feature would be interesting for everyone working with HCP data for example.</p>
<p>This is a great step forward, really! I’m very happy this works!</p>
<p>Thank you! Lorenz</p>

---

## Post #6 by @ljod (2019-08-16 15:01 UTC)

<p>I agree about nifti import being important. There is nifti import in DWIConvert that may work with the correct options selected. I believe we are converting HCP data outside of Slicer to nrrd and that script is something developed by the PNL: <a href="https://github.com/pnlbwh" rel="nofollow noopener">https://github.com/pnlbwh</a></p>
<p>Nice to hear from you, Lorenz!</p>

---

## Post #7 by @amymanson (2019-09-12 09:15 UTC)

<p>Hi! Where can I find this dcm2nii module for Slicer, please?<br>
Thank you</p>

---

## Post #8 by @pieper (2019-09-12 14:24 UTC)

<p>It’s an extension</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/479c08867250b01ab65ae71fa7408d2cf18a2108.jpeg" data-download-href="/uploads/short-url/aducpBiRAsrIZcMSdkIoa9BL4UM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/479c08867250b01ab65ae71fa7408d2cf18a2108_2_690x361.jpeg" alt="image" data-base62-sha1="aducpBiRAsrIZcMSdkIoa9BL4UM" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/479c08867250b01ab65ae71fa7408d2cf18a2108_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/479c08867250b01ab65ae71fa7408d2cf18a2108_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/479c08867250b01ab65ae71fa7408d2cf18a2108_2_1380x722.jpeg 2x" data-dominant-color="ECEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1682×882 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @amymanson (2019-09-12 15:23 UTC)

<p>Is this only available for a specific operating system or Slicer version? I can’t seem to find it in my Extensions Manager.</p>

---

## Post #10 by @Sam_Horvath (2019-09-12 15:36 UTC)

<p>We are having some issues with build system today (<a href="https://discourse.slicer.org/t/extensions-will-be-late-today-update-on-build-system/8404" class="inline-onebox">Extensions will be late today - update on build system</a>).   Extensions will be available later than usual for today’s preview, and preview builds from the last week or so may be missing extensions.  You can use the installer linked here: <a href="https://discourse.slicer.org/t/slicerigt-extenstion/8369/2" class="inline-onebox">SlicerIGT Extenstion</a>  which has the full extension set.</p>

---
