---
topic_id: 19102
title: "Brain Image Registration For Radiotherapy Treatment Planning"
date: 2021-08-06
url: https://discourse.slicer.org/t/19102
---

# Brain image registration for radiotherapy treatment planning

**Topic ID**: 19102
**Date**: 2021-08-06
**URL**: https://discourse.slicer.org/t/brain-image-registration-for-radiotherapy-treatment-planning/19102

---

## Post #1 by @Eman_Showkatian (2021-08-06 12:40 UTC)

<p>Operating system: Windows 10 x64<br>
Slicer version: 4.11.0</p>
<p>Hi slicer team,</p>
<p>I exported one patient data from the radiotherapy treatment planning system and tried to register the CT images with corresponding MRI T1w of the brain. I want to overlay these two images and try to segment the tumor on ct images with the guide of MR images. after that I want to use the SlicerRT Extention to deploy some radiation field and calculated the dose-volume histogram. I used the Elastic registration and general registration modules to register these two modaliteis. but the results were not satisfactory at all. the coordination and dimensions of MR images are completely different from CT images and I have no idea how to register these to volumes. I would be appreciated for any help in advance.  you can find these  images alongside with RT files here <em>(link removed due to potentially containing patient information)</em>.</p>

---

## Post #2 by @lassoan (2021-08-07 18:46 UTC)

<p>Before registration, you need to crop the input volumes so that they approximately contain the same anatomical region as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">here</a>.</p>
<p>After cropping, I got reasonable results using both Elastix and ANTs, but ANTs looked slightly better:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81beb40a7e9e319d0c8af37355a8312e2b045cda.jpeg" data-download-href="/uploads/short-url/ivMaLhPpon3OqCboWmbyUX0glCO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81beb40a7e9e319d0c8af37355a8312e2b045cda_2_690x420.jpeg" alt="image" data-base62-sha1="ivMaLhPpon3OqCboWmbyUX0glCO" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81beb40a7e9e319d0c8af37355a8312e2b045cda_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81beb40a7e9e319d0c8af37355a8312e2b045cda_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81beb40a7e9e319d0c8af37355a8312e2b045cda_2_1380x840.jpeg 2x" data-dominant-color="8A8A8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1169 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Eman_Showkatian (2021-08-09 14:57 UTC)

<p>Hi Lassoan,</p>
<p>Thanks for the quick response, I have a question:</p>
<p>which of the volumes did you crop? CT or MRI or both? (any screenshot from the crop process would be appreciated) and did you used the corresponding RT structure file?</p>

---

## Post #4 by @lassoan (2021-08-09 15:25 UTC)

<p>The CT covers a much larger area than the MRI, so I only cropped the CT, using Crop volume module.</p>
<p>I only used the RT structure set for visualization of the end result.</p>

---

## Post #5 by @SogolSadeghi (2021-08-17 08:33 UTC)

<p>Hi Lassoan,<br>
I have the same question and I tried your solution for cropping the CT. As a beginner( in using slicer I mean) actually, I don’t know how to crop the CT scans. I wondered if you could take a screenshot from the process and share it with me or guide me in a way that you are happy with.<br>
thanks</p>

---

## Post #6 by @lassoan (2021-08-17 18:10 UTC)

<p>You can find lots of Slicer tutorial videos on YouTube. Check out <a href="https://www.youtube.com/results?search_query=slicer+crop+volume">these</a> and let us know if something is not clear or does not work as you expect.</p>

---

## Post #7 by @Eman_Showkatian (2021-08-20 08:49 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Hope you are doing well. I have a question. assume that we have a CT volume and MRI volume. Also, we have a CT_segmentation structure that contains the corresponding structure of CT volume and we have an MRI_segmentation structure that contains the corresponding structure of MRI volume. how can I transfer the MRI_segmentation structures to CT_segmentation structure so I can see the labels drawn using MRI on CT images.</p>

---

## Post #8 by @cpinter (2021-08-23 09:46 UTC)

<p>See this extension: <a href="https://github.com/SlicerRt/SegmentRegistration" class="inline-onebox">GitHub - SlicerRt/SegmentRegistration: 3D Slicer extension for segment registration (aka fusion, conto</a></p>
<p>It has two modules. If you are doing it for prostate brachytherapy then you can use the module <code>Prostate MRI-US Contour Propagation</code> otherwise you can use the generic <code>Segment Registration</code> one. Note that there is a paper cited in the readme of the extension, you may want to read it to see how it was used originally.</p>

---

## Post #9 by @Zahra_Rezaei (2024-07-12 15:44 UTC)

<p>Hi , I want register CTand MRIin brain , and after that I want to make equal slice for CT and MRI , means find reslice CT and MR for cycle Gan<br>
for registration I want to crop image before registration and after registration for find reslice ؟ how to crop and then register and find equal slice ؟</p>

---
