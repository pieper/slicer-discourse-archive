---
topic_id: 33479
title: "Using Monailabel On Masks Not Created Using Monailabel"
date: 2023-12-21
url: https://discourse.slicer.org/t/33479
---

# Using monailabel on masks not created using monailabel

**Topic ID**: 33479
**Date**: 2023-12-21
**URL**: https://discourse.slicer.org/t/using-monailabel-on-masks-not-created-using-monailabel/33479

---

## Post #1 by @Vineet_Saravanan (2023-12-21 00:11 UTC)

<p>Hello. I am trying to use the train feature of monailabel using a dataset with masks that were created outside 3dslicer. Would I need to create a datastore_v2 file for this case?<br>
For the folder structure, I have a folder with the mra data, and in that folder, I have a folder called labels in which there is a folder called final with all the masks.<br>
Is this correct?</p>

---

## Post #2 by @Vineet_Saravanan (2023-12-23 03:37 UTC)

<p>Hello.</p>
<p>I tried running that, and I got a torch size error. Here is the error I am getting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16d30d55dafb6ae7c2913f3bb6b5258c70249ca9.png" data-download-href="/uploads/short-url/3fUGfbz5Zxc7tsKbUrjKxrAHR0d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16d30d55dafb6ae7c2913f3bb6b5258c70249ca9.png" alt="image" data-base62-sha1="3fUGfbz5Zxc7tsKbUrjKxrAHR0d" width="690" height="410" data-dominant-color="181918"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1641×976 62.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ec641bdaa411e835e25d64283e4ed0b53e35d2.png" data-download-href="/uploads/short-url/coXwJqFwefS5bniPz5USsuIx0Zk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ec641bdaa411e835e25d64283e4ed0b53e35d2.png" alt="image" data-base62-sha1="coXwJqFwefS5bniPz5USsuIx0Zk" width="690" height="88" data-dominant-color="191919"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1581×203 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there something wrong with the data I am giving?</p>

---

## Post #3 by @rbumm (2023-12-23 22:35 UTC)

<p>Sorry for the error, I am not officially in the commercial MONAILabel NVIDIA team, but try to help support ML in the Slicer forum, which is a secondary help source. There is also a MONAI GitHub and the GitHub of MONAILabel, which you could feed with an “issue”.<br>
But let us first look at your system. Please provide system information including your GPU data. And please invest some patience and endurance.</p>
<p>You could also start with the “spleen” segmentation model to get experience with the process of MONAILabel.</p>
<p>A good Youtube linke of <a class="mention" href="/u/diazandr3s">@diazandr3s</a>  <a href="https://www.youtube.com/watch?v=-HAryYAO5J4">is here</a>.</p>

---

## Post #4 by @Vineet_Saravanan (2023-12-24 08:20 UTC)

<p>I am using a 2070 GPU with an i7 8700k CPU. I was able to run and train MONAILabel before on a different dataset, but I am only having an issue now, so I am confused on what the issue is.</p>

---

## Post #5 by @rbumm (2023-12-24 12:04 UTC)

<p>Please compare the file sizes of your both datasets, maybe reduced file numbers of your new dataset. What is the file format of the single files ? NIFTI or MRB or NRRD or somehow importing DICOM ?<br>
Also compare a not working data file when opening “Volumes” and “Volume Information” in 3D Slicer.<br>
Make a screenshot like this and post it here. Take care not to include any non-anonymized data when you post things on 3D Slicer discourse.<br>
An example of the sample dataset of 3D Slicer is here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a464576bec8a2975ed4d38bb6d54313ba054545.png" data-download-href="/uploads/short-url/61YBMBbDV6vIAGhMyOTEHy2uyxf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a464576bec8a2975ed4d38bb6d54313ba054545.png" alt="image" data-base62-sha1="61YBMBbDV6vIAGhMyOTEHy2uyxf" width="577" height="500" data-dominant-color="F4F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">618×535 25.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please provide one screenshot from working and one from not working dataset.</p>

---

## Post #6 by @Vineet_Saravanan (2023-12-25 01:58 UTC)

<p>Hello, just to clarify the new dataset I was trying to train is bigger than the one that worked. The files are NIFTI files with .nii.gz endings.</p>
<p>Here is a screenshot from the dataset that is working:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671cabea7862736636664393905cfe9cbc56d0f9.png" data-download-href="/uploads/short-url/eIaBH0cdVbCKLq0iHHO6fnIZq3v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671cabea7862736636664393905cfe9cbc56d0f9.png" alt="image" data-base62-sha1="eIaBH0cdVbCKLq0iHHO6fnIZq3v" width="690" height="472" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1246×853 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is a screenshot from the dataset that is not working:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b64c247e672f6ab4381959be7805da54963ca3e6.png" data-download-href="/uploads/short-url/q0G27Os9zmia8qP3EWaGcW3ypaS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b64c247e672f6ab4381959be7805da54963ca3e6.png" alt="image" data-base62-sha1="q0G27Os9zmia8qP3EWaGcW3ypaS" width="689" height="465" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1237×835 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for assisting me.</p>

---

## Post #7 by @rbumm (2023-12-25 14:45 UTC)

<p>This may cause the problem, and the IJK to RAS matrix and the image spacings are different in the non-working files. Your 8 GB video RAM is on the lower end of system requirements for training. We recommend 12 - 24 GB video RAM.<br>
But great technical experience have <a class="mention" href="/u/diazandr3s">@diazandr3s</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, who may also comment on the problem. But please accept a possible delay of their response due to the holiday season. I will experiment a bit and if I find something new I will post it here.</p>

---

## Post #8 by @rbumm (2023-12-25 14:49 UTC)

<p>And please describe the way you installed MONAILabel. Have you followed <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">this How-To</a> ? Are you using Windoes (which) or Linux or WSL on Windows ?</p>

---

## Post #9 by @Vineet_Saravanan (2023-12-26 04:28 UTC)

<p>Hello.<br>
I am running this on Windows 10. For the matrices, shouldn’t it be fine as long as the image and the mask match?</p>

---

## Post #10 by @diazandr3s (2024-01-01 21:55 UTC)

<p>This discussion is being moved to the MONAI Label repo. Here: <a href="https://github.com/Project-MONAI/MONAILabel/issues/1613" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel torchsize error when training with 3d slicer · Issue #1613 · Project-MONAI/MONAILabel · GitHub</a></p>

---
