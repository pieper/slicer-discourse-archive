---
topic_id: 5802
title: "Dti Image Visualization"
date: 2019-02-16
url: https://discourse.slicer.org/t/5802
---

# DTI image visualization

**Topic ID**: 5802
**Date**: 2019-02-16
**URL**: https://discourse.slicer.org/t/dti-image-visualization/5802

---

## Post #1 by @Vinny (2019-02-16 21:39 UTC)

<p>Hi,</p>
<p>I have constructed a DTI color FA map in Dipy and exported it to 3d Slicer for visualization.  This file is a 3 volume nifti file that was imported and viewed using Slicer’s MultiVolume Support module.  Each of the FA nifti volumes appear in greyscale and, I presume, they represent the 3 orthogonal vectors since the greyscale intensities vary between volumes.  Is it possible to convert this multiple volume file into a single VectorVolume file that is RGB colorized?</p>
<p>Thanks for your help,</p>
<p>Vinny</p>

---

## Post #2 by @ljod (2019-02-16 23:23 UTC)

<p>Hi Vinny. I don’t know how to convert or load it as a vector volume. Others on the forum may know. But if you simply want to look at DTI in this way you could use the SlicerDMRI extension to view the DTI data.</p>

---

## Post #3 by @Vinny (2019-02-17 01:57 UTC)

<p>Hi Lauren, thanks for your suggestion.  I am not sure how to view the 3 Nifti Volume DTI file in SlicerDMRI.  I downloaded the sample data and was able view the sample DTI data using the SlicerDMRI extension.  Do I need to convert my multivolume DTI data into DiffusionTensorVolume format?</p>

---

## Post #4 by @ljod (2019-02-17 08:13 UTC)

<p>For many nifti volumes, the dwiconvert module in SlicerDMRI can be used to read them. Do you have image data plus bvecs and bvals?</p>

---

## Post #5 by @Vinny (2019-02-17 12:24 UTC)

<p>I had converted the DICOM to nifti using MRIcroGL and then had preprocessed using FSL eddy.  I used NiftiFSL To Nrrd Conversion Parameters within the DWIconvert module using the input image plus bvecs and bvals but get the following error message:  Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p><em>Error: the output file type is not supported currently</em></p>
<p><em>Missing output volume name</em></p>
<p>I’m using Slicer version 4.10.0<br>
Windows 10</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #6 by @ljod (2019-02-17 13:39 UTC)

<p>Hi this usually means the output needs to be specified in the user interface before you hit apply. There is a tutorial on this module at <a href="http://dmri.slicer.org/docs/" rel="nofollow noopener">http://dmri.slicer.org/docs/</a><br>
(Tutorial may cover other use cases but hopefully is helpful.)</p>

---

## Post #7 by @Vinny (2019-02-17 14:08 UTC)

<p>Thanks, this is very helpful.</p>

---
