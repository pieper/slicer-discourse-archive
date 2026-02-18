# Cranial Bone flap Thickness Measurement

**Topic ID**: 16393
**Date**: 2021-03-05
**URL**: https://discourse.slicer.org/t/cranial-bone-flap-thickness-measurement/16393

---

## Post #1 by @Antonio_Giulio_Genna (2021-03-05 17:11 UTC)

<p>Operating system: Windows 8 version 6.3<br>
Slicer version: 4.10.2<br>
Expected behavior: Generating a centerline and analyzing segment thickness<br>
Actual behavior: None</p>
<p>Hello, I am a new Slicer user struggling with an old, debated problem.<br>
I generated a segmentation, defining the craniotomy bone flap in patients who underwent neurosurgical procedures, using T1 weighted MRI images.<br>
I saved the segmentation, using both .seg.nrrd and .stl extensions. Then I tried to follow the “How to analyze the thickness of the model” tutorial, but I am stuck. I tried loading the .seg.nrrd segmentation together with the T1 volume. After that, as suggested, I searched the Simple Filters module and used the BinaryThinningImageFilter, using the T1 volume as input volume and creating a new volume as output. However, after clicking the apply button I waited 40 minutes, but the progress line still remained at 0%. I thought the problem was the extension of the file, so I used the same segmentation generating a .stl file. Then I repeated the same process, ending with similar results.<br>
Theoretically speaking, analyzing the bone flap thickness should easily to compute. However, I am struggling with it, how do you suggest proceeding?</p>
<p>Kind regards</p>

---

## Post #2 by @lassoan (2021-03-05 17:14 UTC)

<p>You need to apply the filter not to the T1 volume but to the segmentation (exported to a labelmap). Make sure to crop the segmentation to the minimum necessary size (e.g., using Scissors tool). After this, computation should take a few seconds.</p>

---

## Post #3 by @Antonio_Giulio_Genna (2021-03-06 11:33 UTC)

<p>Dear Andreas,</p>
<p>Thank you for your reply. I tried to implement your suggestion, and it worked partially.<br>
At the moment, I am worried I did something wrong in the first passages, which is flawing my result. So, I will try to explain what I did and maybe you can help me fix it.<br>
I loaded a T1 volumetric image in Slicer, then used the Segment Editor to paint out the bone flap. Afterward, I smoothed the created ROI and saved it through the save button using both the .seg.nrrd and .stl extensions. I think this is the passage that is generating my problems. Although I created an ROI it seems to rely on the native volume for dimensions, volumes, etc.</p>
<p>So, as you suggested I cropped the native volume around the ROI, then I created a lablemap and applied the passages in the “How to analyze the thickness of the model” tutorial. Although the process functioned, my results were not similar to the ones in the tutorial and I did not have the green and red outline of my ROI.</p>
<p>Maybe I am struggling with really complex tasks for a beginner user, but I really hope you can help me.</p>
<p>Many thanks in advance,<br>
Antonio</p>

---

## Post #4 by @lassoan (2021-03-06 12:53 UTC)

<p>Can you share your seg.nrrd file (upload somewhere and post the link here)?</p>

---

## Post #5 by @Antonio_Giulio_Genna (2021-03-06 14:06 UTC)

<p>Sure, could you suggest me somewhere to upload the file?</p>

---

## Post #6 by @Antonio_Giulio_Genna (2021-03-06 14:16 UTC)

<p>Also, I created the ROI segmenting a Nifti T1 volumetric image. Is it correct that NIfti images do not store any patient’s information?</p>

---

## Post #7 by @lassoan (2021-03-06 14:16 UTC)

<p>Anything works - Dropbox, OneDrive, Google drive…</p>
<p>Nifti does not store patient health information. In theory, somebody could inject some patient information into some fields, so if you want then you can open the file in a text editor and have a look at the first few hundred bytes of the file to check if you see anything about the patient there, but it is highly unlikely.</p>

---

## Post #8 by @Antonio_Giulio_Genna (2021-03-08 08:49 UTC)

<p>Dear Andreas,</p>
<p>Sorry for the late reply. Underneath you can find the segmentation link:</p>
<p><a href="https://drive.google.com/file/d/1EKKORh0UWQnwK7mhIqVOSy4N6Kr5I_2A/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1EKKORh0UWQnwK7mhIqVOSy4N6Kr5I_2A/view?usp=sharing</a></p>
<p>Thank you for helping me,</p>
<p>Antonio</p>

---

## Post #9 by @Antonio_Giulio_Genna (2021-03-12 09:16 UTC)

<p>Dear Andreas,</p>
<p>I think I came closer to the result. After cropping the image, applying the Bunary thinning and Danielsson mapping distance filters this is the result. However, to me, it seems that Slicer is sampling the whole volume rather than the segment. How can I try to fix this problem? Did you manage to look at the file I sent you earlier?</p>
<p>All the best,<br>
Antonio</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cfb6a12477682038096e9e2a9bc2636e3a2cfb4.png" data-download-href="/uploads/short-url/k7buUDyI8tGcn7SS9PNMuAMossY.png?dl=1" title="Schermata 2021-03-12 alle 10.07.57.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfb6a12477682038096e9e2a9bc2636e3a2cfb4_2_565x499.png" alt="Schermata 2021-03-12 alle 10.07.57.png" data-base62-sha1="k7buUDyI8tGcn7SS9PNMuAMossY" width="565" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfb6a12477682038096e9e2a9bc2636e3a2cfb4_2_565x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfb6a12477682038096e9e2a9bc2636e3a2cfb4_2_847x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8cfb6a12477682038096e9e2a9bc2636e3a2cfb4_2_1130x998.png 2x" data-dominant-color="7A776F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermata 2021-03-12 alle 10.07.57.png</span><span class="informations">1824×1614 536 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @Antonio_Giulio_Genna (2021-03-15 15:01 UTC)

<p>Dear Andras,</p>
<p>I tried the Skeleton module, and I was able to define the segmentation’s center-line. Therefore, I am wondering what I did wrong. Did you manage to look at the segmentation I send you a week ago?</p>
<p>All the best,</p>
<p>Antomnio</p>

---
