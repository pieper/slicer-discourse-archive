---
topic_id: 20653
title: "My Experiences With 3Dslicer In Radiotherapy Nuclear Medicin"
date: 2021-11-17
url: https://discourse.slicer.org/t/20653
---

# My experiences with 3Dslicer in radiotherapy, nuclear medicine and radiology

**Topic ID**: 20653
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/my-experiences-with-3dslicer-in-radiotherapy-nuclear-medicine-and-radiology/20653

---

## Post #1 by @shahrokh (2021-11-17 06:53 UTC)

<p>I would like to sincerely congratulate the development team of 3DSlicer. I really enjoy the modules/features that 3DSlicer has in general. I also sincerely thank the development team and programmers who provide excellent support to users.</p>
<p><strong>List of completed or ongoing projects since 2017</strong></p>
<p>In doing a project entitled <em>Automatic correction of geometric distortion in MRI images used in radiotherapy treatment planning</em>, CT and MRI scans was taken from the pelxiglass phantom containing thin rods of water. The prepared images were then transferred to 3DSlicer. Registration and extraction of centerlines of this phantom was done by <strong>3DSlicer</strong> modules and libraries in <strong>VMTK</strong>. The modules used in this research include the following: <strong>Transforms,</strong> <strong>Effects in</strong> <strong>Segment Editor,</strong> <strong>Segmentations,</strong> <strong>MergeModels, Scattered Transforms, libraries and tools in VMTK (Vascular Modeling Toolkit) used in Graphical mode, Python Interactor and basch shell</strong>. An article entitled <em>Detection and Correction of Geometric Distortion by a Novel Automated Method in Different Magnetic Resonance Images</em> is under review in <em>Radiologica</em> journal.</p>
<p>In doing a project entitled <em>Use of machine vision in determining the characteristics of pulmonary vessels in CT Scan images of COVID-19 patients</em>, we used the <strong>Chest Imaging Platform</strong> module (<strong>CLI</strong>). In this study, the pulmonary lobes of patients with COVID-19 disease were extracted by CLI on CT images. Then the properties of the vessels were sampled in the form of particles (Scale Space Particles) and finally the classification of these particles was done by a model based on deep learning in Keras. The research article is being written.</p>
<p>In doing a project entitled <em>Evaluation of Condylar surface morphology in images of CBCT and its relation to blood minerals in patients with Temporomandibular Joint disorders (RDC/TMDII)</em>, we used <strong>SPHRAM-PDM</strong> module. In this study, CBCT image relative to suffering Osteoarthritis and control people were recontructed to statistics analysis by using SPHARM.</p>
<p>In doing a project entitled <em>Determination of relationship between spinal cord atrophy and severity of disability in patients with multiple seleorsis</em>, we used <strong>Transforms</strong> and <strong>Volume Rendring</strong> modules to register and view 3D results of <em>Spinal Cord Toolbox</em> on T2 weighted MR images.</p>
<p>In doing a project entitled <em>Dose verification of intra-fraction in IMRT using EPID</em>, we used <strong>SlicerRT</strong> module to compute and display dose comparison metrics. In this study, we used <strong>Plastimatch</strong> in bash shell. An article entitled <em>Dosimetric verification of IMRT and 3D conformal treatment delivery using EPID</em> is under review in <em>Applied Radiation and Isotopes</em> journal.</p>
<p>In doing several projects to determine <em>patient specific dosimetry</em> in nuclear medicine using <a href="http://www.opengatecollaboration.org/" rel="noopener nofollow ugc">OpenGATE</a> Monte Carlo, we used the following modules to process CT and SPECT or PET images: <strong>Volumes, Volume Rendering, Mask Scalar Volume, Cast Scalar Volume,</strong> <strong>filters in ITK Simple Filters, Markups, Simple Region Growing Segmentation, Label Statistics,</strong> <strong>Resample Image (BRAINS), Crop Volumes, Forground Masking (BRAINS), Effects in Segment Editor,</strong> <strong>and</strong> <strong>Segmentation.</strong> The research articles are being written.</p>
<p>In doing a project entitled <em>Harmonization in Quantitative parameters of PET/CT Images for Assessment of Treatment response; A multi-center study on phantiom &amp; patient</em> , we used modules such as <strong>Volumes, Volume Rendering, Mask Scalar Volume, Cast Scalar Volume,</strong> <strong>filters in ITK Simple Filters,</strong> <strong>Markups,</strong> <strong>Create Models, Segment Statistics</strong> and <strong>Label Statistics.</strong></p>
<p>In doing a project entitled <em>Radiotherapy treatment planning based on magnetic resonance images</em>, we used thes modules: <strong>Fiducial Registration, Markups, Scattered Transform, Transform and filters in ITK Simple Filters (ScalarChanAndveseDenseLevelSetImageFilter and ShiftScaleImageFilter)</strong> .</p>
<p>In continue, I have a hypothesis about the possibility of converting DRR to two-dimensional absorbed dose distribution with using calibration DRRs from water phantoms synthesized in <strong>plastimatch</strong> based on practical results in our radiotherapy center equipped with LINAC. I shared this with Csaba Pintér and Greg Sharp in April 2021. Unfortunately, I was heavily involved in other projects and I could not continue working.</p>
<p>Also, I interest to develop module to do patient specific dosimetry with OpenGATE. As mentioned above, for doing it, it is necessary to preprocess CT/SPECT or CT/PET images (as attenuation/ source map) for using this data in the macrofiles in OpenGATE code. To do these calculations, most of the work is related to preparing these images.</p>
<p>Wishing you good health and good luck.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2021-11-17 17:51 UTC)

<p>Very impressive list of projects and accomplishments, thanks for sharing. It would be nice if you could also attach a few illustrative images.</p>

---

## Post #3 by @shahrokh (2021-11-27 12:07 UTC)

<p>Sorry… for not preparing illustrative images.  I have been very involved in life issues for some time. I will prepare these images as soon as possible.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #4 by @Alex_Vergara (2021-11-27 20:05 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="20653">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>In doing several projects to determine <em>patient specific dosimetry</em> in nuclear medicine using <a href="http://www.opengatecollaboration.org/" rel="noopener nofollow ugc">OpenGATE</a> Monte Carlo, we used the following modules to process CT and SPECT or PET images: <strong>Volumes, Volume Rendering, Mask Scalar Volume, Cast Scalar Volume,</strong> <strong>filters in ITK Simple Filters, Markups, Simple Region Growing Segmentation, Label Statistics,</strong> <strong>Resample Image (BRAINS), Crop Volumes, Forground Masking (BRAINS), Effects in Segment Editor,</strong> <strong>and</strong> <strong>Segmentation.</strong> The research articles are being written.</p>
</blockquote>
</aside>
<p>You may be interested in <a href="https://gitlab.com/opendose/opendose3d" rel="noopener nofollow ugc">OpenDose3D</a>, it is available inside the radiotherapy modules group <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>

---
