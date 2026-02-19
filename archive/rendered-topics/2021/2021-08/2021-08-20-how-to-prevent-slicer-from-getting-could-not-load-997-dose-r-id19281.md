---
topic_id: 19281
title: "How To Prevent Slicer From Getting Could Not Load 997 Dose R"
date: 2021-08-20
url: https://discourse.slicer.org/t/19281
---

# How to prevent Slicer from getting "Could not load: 997 Dose record as a scalar volume" error and having black screen with white dots?

**Topic ID**: 19281
**Date**: 2021-08-20
**URL**: https://discourse.slicer.org/t/how-to-prevent-slicer-from-getting-could-not-load-997-dose-record-as-a-scalar-volume-error-and-having-black-screen-with-white-dots/19281

---

## Post #1 by @geonse (2021-08-20 12:39 UTC)

<p>Hi everyone,</p>
<p>I was trying to get Brain CT images from our hospital server in Slicer preview version to annotate them via Nvidia extension. Until I fetched them everything was fine, however, when I loaded them it pops out a warning message named  “Could not load: 997 Dose record as a scalar volume”. Then screen got black with some white dots so can not navigate to the slices. How can I prevent that? Am I doing something wrong?</p>
<p>Kind regards.</p>
<p>(Link of the video which reproduce the error and screenshots are provided)</p>
<p>Link: <a href="https://wetransfer.com/downloads/285b2e611a07994cd53e87566e8c98af20210820074818/13393951ae586e587679d120e1b0ed6620210820074845/476083" rel="noopener nofollow ugc">https://wetransfer.com/downloads/285b2e611a07994cd53e87566e8c98af20210820074818/13393951ae586e587679d120e1b0ed6620210820074845/476083 </a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82a34e3a03ad6237262428059d79aa897164e4e2.png" data-download-href="/uploads/short-url/iDFX0sW2UuMuMD51R8KZFqxNO0i.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82a34e3a03ad6237262428059d79aa897164e4e2_2_690x373.png" alt="image" data-base62-sha1="iDFX0sW2UuMuMD51R8KZFqxNO0i" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82a34e3a03ad6237262428059d79aa897164e4e2_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82a34e3a03ad6237262428059d79aa897164e4e2_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82a34e3a03ad6237262428059d79aa897164e4e2_2_1380x746.png 2x" data-dominant-color="E1EBF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1039 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55174410d43f61f3e599a408aa6d935438af95a0.png" data-download-href="/uploads/short-url/c8KqMgfwtZPRengPSiV97ESMPzW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55174410d43f61f3e599a408aa6d935438af95a0_2_690x363.png" alt="image" data-base62-sha1="c8KqMgfwtZPRengPSiV97ESMPzW" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55174410d43f61f3e599a408aa6d935438af95a0_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55174410d43f61f3e599a408aa6d935438af95a0_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55174410d43f61f3e599a408aa6d935438af95a0_2_1380x726.png 2x" data-dominant-color="67676F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1010 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-08-20 13:01 UTC)

<p>The dose record is a structured report that records the patient’s exposure to radiation so you can ignore that for the purposes of image processing (just don’t select that series to load).</p>
<p>For the images, you can see in the Data module that volumes are being split by acquisition number which is an artifact of how your dicom data is structured and probably not what you want.  Unfortunately when this happens it can be hard to narrow down to the best load strategy, but basically you should focus on one series, probably 2,3, or 4 that is the best set of images and then enable Advanced mode in the DICOM module and try the different load options for that series.  If you can’t find a good way to load you might try the DICOMPatcher module.</p>

---

## Post #3 by @geonse (2021-08-20 13:39 UTC)

<p>Thanks Steve, will do.</p>
<p>Actually I’ve another question.<br>
(I’ve added screen recorder video which reproduces the process and screenshot)</p>
<p>Why am I getting 8bit-like display? Not sure if our machines causes this. Slicer, as you know, has very good sample images but I can not make radiologists to annotate tumors in such low resolution images. I’d like to ask that is there any options or settings in Slicer to make it better?</p>
<p>Kind regards.</p>
<p>Screen Recorder:<br>
<a href="https://we.tl/t-aorFfksuSC" rel="noopener nofollow ugc">https://we.tl/t-aorFfksuSC </a><br>
1 öge</p>
<p>Screenshot: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/187f0725b688bac197b0e2624e9b80ff4ec1673a.jpeg" data-download-href="/uploads/short-url/3uHC9pJm2fjo5VcnnzJBLAVCS14.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187f0725b688bac197b0e2624e9b80ff4ec1673a_2_690x361.jpeg" alt="image" data-base62-sha1="3uHC9pJm2fjo5VcnnzJBLAVCS14" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187f0725b688bac197b0e2624e9b80ff4ec1673a_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187f0725b688bac197b0e2624e9b80ff4ec1673a_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/187f0725b688bac197b0e2624e9b80ff4ec1673a_2_1380x722.jpeg 2x" data-dominant-color="7A7981"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1007 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2021-08-20 13:53 UTC)

<p>What you are seeing is normal.  In fact that’s a pretty nice image.  The in-plane image, the axial in the red viewer (upper-left) is typically what the radiologist would review for this kind of scan.  The slice spacing is fairly wide compared to the in-plane resolution so you see some blurring in the sagittal and coronal views.</p>
<p>You have a number of different volumes in your study so probably best is for you to talk with a radiologist who can explain why they acquire each one and what they learn from it.  There’s always a tradeoff between time in the scanner (which costs money) vs clinical value of the images acquired, so you need to understand that in order to make use of the data.</p>

---
