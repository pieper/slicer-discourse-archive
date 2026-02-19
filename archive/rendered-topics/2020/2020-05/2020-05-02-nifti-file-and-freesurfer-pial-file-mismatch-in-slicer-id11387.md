---
topic_id: 11387
title: "Nifti File And Freesurfer Pial File Mismatch In Slicer"
date: 2020-05-02
url: https://discourse.slicer.org/t/11387
---

# Nifti file and freesurfer pial file mismatch in slicer

**Topic ID**: 11387
**Date**: 2020-05-02
**URL**: https://discourse.slicer.org/t/nifti-file-and-freesurfer-pial-file-mismatch-in-slicer/11387

---

## Post #1 by @Tutu (2020-05-02 21:50 UTC)

<p>Hi slicers,<br>
I tried to view several files that were built from Freesurfer (brain.mgz, l/rh.pial,l/rh.white). However, I found the surface of the pial could not match the outline of raw MRI images. I checked online and found the tutorial of visualization of FreeSurfer data in Slicer. As was introduced in the tutorial, we need to center the volume. It works after the volume is centered.<br>
Does anyone know why we should center the volume and how to calculate the image origin related to the center?<br>
Many thanks<br>
Tutu</p>

---

## Post #2 by @lassoan (2020-05-02 22:04 UTC)

<p>We have received funding for improving brain image segmentation and FreeSurfer support in Slicer. As a result, lots of new features and improvements are coming for viewing and fixing FreeSurfer segmentations in the coming year.</p>
<p>As a first step, we have created new <a href="https://github.com/PerkLab/SlicerFreeSurfer">SlicerFreeSurfer extension</a>, which has just been published on the Slicer extensions manager yesterday Slicer Preview Release, but it has not been officially announced yet. It offers new, simplified FreeSurfer data import, which can import images and surfaces correctly. Please give it a try and let us know how it worked. Any feedback about existing features and suggestions for new features and improvements are welcome.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>

---

## Post #3 by @Tutu (2020-05-03 08:54 UTC)

<p>Dear Andras,<br>
Many thanks for your timely reply. I will try the nightly build version of Slicer.<br>
Kindly regards<br>
Tutu</p>

---

## Post #4 by @Kae1 (2023-03-08 05:34 UTC)

<p>Hi Andras, can you point me in the direction on information on how to add this SlicerFreeSurfer extension to 3DSlicer? I am new to 3dSlicer use and am not sure how to do this.  I have added other extensions for other software to 3DSlicer through Slicer&gt;edit/Applications &amp; Settings/ Modules/ &gt;add module. However this doesn’t seem to work for the SlicerFreeSurfer extension files I downloaded from Github.</p>
<p>My main issue to getting lh.pial and lh.white files created in FreeSurfer into 3dSlicer. Drag and drop just gives ‘unable to load’ error messages. So, any advice on this would also be great. I’m hoping that the SlicerFreeSurfer extension will help with this.</p>
<p>Thank in advance!</p>

---
