---
topic_id: 912
title: "Comparing Label Maps Nrrd Nii And Mat"
date: 2017-08-21
url: https://discourse.slicer.org/t/912
---

# Comparing Label maps: nrrd, nii and .mat

**Topic ID**: 912
**Date**: 2017-08-21
**URL**: https://discourse.slicer.org/t/comparing-label-maps-nrrd-nii-and-mat/912

---

## Post #1 by @mwelch (2017-08-21 16:02 UTC)

<p>Hi!<br>
I would like to qualitatively compare binary label maps generated from RTStruct files by visualizing them in 3D Slicer. I have three different formats: .nrrd, .nii and .mat. The .nrrd and .nii files were generated in 3D Slicer, and the .mat file was generated in Matlab.</p>
<p><strong>Is there a way to load a .mat label mask to 3D Slicer without having to re-write it to an .nrrd?</strong></p>
<p>The Matlab Commander: img = load(’…\mask.mat’) completes and knows that the file is a logical volume, but I can’t figure out how to visualize it.</p>
<p>Thanks for any help or guidance you can give!</p>

---

## Post #2 by @lassoan (2017-08-21 16:07 UTC)

<p>In Matlab, save the voxel array as a .nrrd file using nrrdwrite.m. You should be able to write a function using a few lines of code that iterates through all the .mat files in a directory structure and saves them as .nrrd.</p>
<p>In general, it is fine to use any file format for temporary storage, but better for archiving, long-term storage, sharing, and analysis it is always better to use standard, open, widely supported file formats (DICOM, NRRD, MetaIO, etc) instead of proprietary/application-specific formats (such as Matlab’s .mat).</p>

---

## Post #3 by @mwelch (2017-08-22 20:27 UTC)

<p>Thank you, Andras!<br>
Not exactly what I was looking for, but it will do the trick.</p>

---
