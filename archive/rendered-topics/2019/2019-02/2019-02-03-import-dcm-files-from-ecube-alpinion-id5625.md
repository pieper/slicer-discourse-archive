# Import DCM files from Ecube Alpinion

**Topic ID**: 5625
**Date**: 2019-02-03
**URL**: https://discourse.slicer.org/t/import-dcm-files-from-ecube-alpinion/5625

---

## Post #1 by @jhonny422 (2019-02-03 05:18 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.1</p>
<p>Hello, I successfully obtained a 3D design of a complete denture tomography, I used a folder with more than 100 dcm files that all made up a 3D model.<br>
I wanted to repeat the process with an ultrasound that was done with an Alpinion Ecube8, but this time it was only possible to export 1 image that in the cd is represented with 1 dcm file, but when I entered that image in the echograph I could see all the 3D model, and in Slicer I can not see the 3D model, I can only see a photo, I assume that I must have more than 100 dcm files the same as the denture, I am correct? what should I do? Thank you.</p>

---

## Post #2 by @pieper (2019-02-03 08:10 UTC)

<p>If nobody here has experience with that machine (I don’t) you may need to contact the vendor to figure out what export options are available.  If you can share anonymized sample data maybe we can help.</p>
<p>In general try the suggestions here:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM</a></p>

---

## Post #3 by @jhonny422 (2019-02-04 19:07 UTC)

<p>Hello, Thanks for answering, I want to know if it is possible to make a 3D model from 1 dcm image, or if I need more than 100 dcm images? Is it possible to export that amount of data from the ecograph ??</p>

---

## Post #4 by @lassoan (2019-02-05 04:21 UTC)

<p>You need at least tens but preferably hundreds of 2D image slices to reconstruct a 3D volume. The slices may be stored in one file, but in DICOM still the most typical is to store a single slice per file.</p>
<p>Some further details are available in the answers given to your other question here: <a href="https://discourse.slicer.org/t/echograph-for-3d-model/5639" class="inline-onebox">Echograph for 3d model</a></p>

---
