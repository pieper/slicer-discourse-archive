---
topic_id: 17820
title: "Problem While Processing Dwi Images In Slicer"
date: 2021-05-26
url: https://discourse.slicer.org/t/17820
---

# Problem while processing DWI images in Slicer

**Topic ID**: 17820
**Date**: 2021-05-26
**URL**: https://discourse.slicer.org/t/problem-while-processing-dwi-images-in-slicer/17820

---

## Post #1 by @benxa (2021-05-26 20:23 UTC)

<p>Dear experts, I am interested in learning how to use Slicer but I encounter a problem. When I have to indicate the inputs for the processes necessary to carry out the tractography (e.g create a brain mask), my images do not appear as an alternative in the input tab of slicer, although I manage to load and visualize my images with slicer. However, I do not have this problem when I work with the example data provided by slicer. My DWI images were acquired on a Philips Achieva 3T, they are composed of 32 diffusion images (bval=1000) and one non-diffusion image (b=0). Could my problem be related to the type of acquisition? My images are in .nii format, but I have managed to convert them to .nrrd by loading them in slicer and then saving them with .nrrd extension from slicer (I am not able to transform my images with DWIconvert tool because I cannot insert my images as inputs).</p>
<p>Regards and thank you very much in advance.</p>
<p>Benxa.</p>

---

## Post #2 by @pieper (2021-05-27 19:00 UTC)

<p>Yes, as you have seen loading DWI data can be a very challenging task given the variations in scanner and software.  If you have the dicom data, you should try <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Introduction">dcm2niix</a>, which also works with SlicerDMRI.</p>
<p>If you only have nii files you can also explore <a href="https://github.com/pnlbwh/conversion">these utilities</a>.</p>

---
