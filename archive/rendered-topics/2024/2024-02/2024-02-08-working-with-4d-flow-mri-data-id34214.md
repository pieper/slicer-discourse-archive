---
topic_id: 34214
title: "Working With 4D Flow Mri Data"
date: 2024-02-08
url: https://discourse.slicer.org/t/34214
---

# Working with 4D flow MRI data

**Topic ID**: 34214
**Date**: 2024-02-08
**URL**: https://discourse.slicer.org/t/working-with-4d-flow-mri-data/34214

---

## Post #1 by @sannpeterson (2024-02-08 18:07 UTC)

<p>I’ve never worked with 4D flow MRI data (head) before and am wondering if it is possible to perform flow analysis in 3D Slicer. I’ve also attempted to segment the brain vessels but cannot capture any vessels apart from the ICA and even those are quite hard to make out. Any tips would be greatly appreciated.</p>

---

## Post #2 by @roeg (2024-02-09 12:59 UTC)

<p>These topics have my attention too. They are 2 of my prime work related activities in 3D. I am currently working my way through the software, but the online tutorials are for an older software version.<br>
cheers<br>
john roeger<br>
3D Reconstruction<br>
VIR/INR Medical Radiation Technologist<br>
University Health Network</p>

---

## Post #3 by @lassoan (2024-02-09 15:01 UTC)

<p>We have developed a Slicer module for importing Siemens CS 4D flow images from DICOM, visualize it as a flow field, sample the speed with a plane (e.g., to get speed across a cross-section to be used as CFD simulation input), and experimenting with flow simulations. We plan to release the module publicly when corresponding paper is published (maybe in a couple of months).</p>
<p>If you have any specific questions then let us know.</p>

---

## Post #4 by @sannpeterson (2024-02-09 18:04 UTC)

<p>The data files for a study consists of these series: a 2D dataset, a 3D dataset (can’t figure out what this is in relation to other datasets), 3 magnitude datasets (3D), 3 phase datasets (3D). I don’t even really know what I’m looking at. I’ve gone through the metadata for the files but still having a hard time deciphering the images. I’m familiar with vessel segmentation for TOF MRA but cannot figure out how to do this for the files I have. Can you guide me please?</p>
<p><a href="https://www.dropbox.com/scl/fi/tnkn5nsn0ylhxm69w1gzq/Archive.zip?rlkey=vkdlb4y4qdbgv2j631bygv5r9&amp;dl=0" rel="noopener nofollow ugc">files here</a></p>

---

## Post #5 by @lassoan (2024-02-10 16:51 UTC)

<p>These NRRD files do not contain all the metadata that is necessary to interpret the data. If you have Siemens CS 4D flow images then I can give advice on how to load them (maybe share some code in private before we publish). For other vendors or acquisition types you can dig into the specification and/or search for existing readers on github. We can also help with some advice here if you have specific questions.</p>

---

## Post #6 by @sannpeterson (2024-02-12 17:22 UTC)

<p>What do you mean about the files not containing all the metadata? Would it be better if I upload the original dicom files?</p>

---

## Post #7 by @lassoan (2024-02-12 17:25 UTC)

<p>The exported NRRD files only contain the voxel values and the position, orientation, spacing of the voxel grid of each component, which is not sufficient to reconstruct the 5D flow fields. Make sure to use phantom/animal data set or anonymize the DICOM data before sharing.</p>

---

## Post #8 by @sannpeterson (2024-02-12 17:47 UTC)

<p>Can you take a look?</p>
<p><a href="https://www.dropbox.com/scl/fi/3nn3rrotf74xxiz8diqgc/dicom-anonymized.zip?rlkey=sxe722fzx6zng4i66oacogkef&amp;dl=0" rel="noopener nofollow ugc">files here</a></p>

---

## Post #9 by @klns23 (2024-06-07 16:39 UTC)

<p>Hi, I’m curious whether the Slicer module for working with 4D flow images has been released? The available commercial software does not seem very useful beyond visualization, and I would really like the ability to work with this type of data in Slicer.</p>

---

## Post #10 by @klns23 (2024-08-14 16:07 UTC)

<p>Any news on the Slicer module for importing Siemens CS 4D flow images from DICOM? Is it now available via an extension? Thanks!</p>

---

## Post #11 by @lassoan (2024-09-12 14:42 UTC)

<p>We have the Siemens CS 4D flow image importer Slicer module and it works well. We’ll release it as soon as we get it published, which may take several months. You can check back here/comment on this topic later to get an update.</p>

---

## Post #12 by @Onyxazure (2025-07-04 19:07 UTC)

<p>Hi Andras,</p>
<p>I wanted to ask if you have published this plugin / paper by now? I would be really interested to use it. Thanks a lot.</p>

---

## Post #13 by @lassoan (2025-07-04 19:24 UTC)

<p>We have made significant progress with the implementation (added bias correction, velocity phase unwrapping, motion compensation, flow metrics computation, etc.) but have not started writing the paper. So, publishing the software is probably still at least a few months away. Maybe we can share with you privately - you can contact me in private message to discuss.</p>

---
