---
topic_id: 46632
title: "Urgent (Thesis project): Thresholding Impossible due to High Noise Levels in CT Reconstruction"
date: 2026-04-01
url: https://discourse.slicer.org/t/46632
last_bumped: 2026-04-06T16:11:19.378Z
---

# Urgent (Thesis project): Thresholding Impossible due to High Noise Levels in CT Reconstruction

**Topic ID**: 46632
**Date**: 2026-04-01
**URL**: https://discourse.slicer.org/t/urgent-thesis-project-thresholding-impossible-due-to-high-noise-levels-in-ct-reconstruction/46632

---

## Post #1 by @Yaren_Cetin (2026-04-01 19:59 UTC)

<p>To Whom It May Concern,<br>
I am experiencing a critical technical issue with my CT scan data that is preventing me from proceeding with my thesis analysis.<br>
The primary problem is that the Signal-to-Noise Ratio (SNR) is so low that I cannot perform a reliable thresholding/segmentation process. The bone tissue is indistinguishable from the background noise and artifacts.<br>
Key issues I am facing:</p>
<ul>
<li>Threshold Inconsistency: It is impossible to select a Hounsfield Unit (HU) or grayscale range that captures the bone structure without including massive amounts of noise.</li>
<li>Loss of Connectivity: When I attempt to isolate the bone, the structural integrity breaks down, resulting in a “fragmented” or “moth-eaten” appearance that does not reflect the actual anatomy.</li>
<li>Boundary Blur: The interface between the cortical bone and surrounding tissue is too blurred for manual or automatic segmentation tools to function correctly.<br>
Since this data is vital for my thesis and I am working against a strict deadline, I urgently need your guidance on:</li>
<li>Which reconstruction filters or denoising algorithms should be applied to the raw data to clean up this noise?</li>
<li>Are there specific artifact reduction settings you recommend to stabilize the image for thresholding?<br>
I have attached a representative slice and dicom showing the severity of the noise. I look forward to your immediate technical feedback.<br>
Best regards,</li>
</ul>
<p><a href="https://drive.google.com/file/d/1JJtti3CZZ4L9Sbs_pKPWSbngoom14H9y/view?usp=sharing" rel="noopener nofollow ugc">Dıcom</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18a620e9fae8cfa2bd5f017cf3cb326713b0a0ba.jpeg" data-download-href="/uploads/short-url/3w3o3TIOG8j3JjaTtUkVm5CfLfk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18a620e9fae8cfa2bd5f017cf3cb326713b0a0ba.jpeg" alt="image" data-base62-sha1="3w3o3TIOG8j3JjaTtUkVm5CfLfk" width="660" height="444"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×444 25.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2026-04-01 22:24 UTC)

<p>You could try <a href="https://www.openrtk.org/" rel="noopener nofollow ugc">https://www.openrtk.org/</a> for reconstruction, I have never used it myself. Maybe also learn if there are some new AI reconstruction methods published</p>
<p>If you have control of the CT scanner you could increase the radiation and the scanning-time to have better images</p>

---

## Post #3 by @Deep_Learning (2026-04-02 10:45 UTC)

<p>Use the nninteractive.  There is an extension.  Expecting an ack in your thesis….</p>

---

## Post #4 by @Dieter_Rosch (2026-04-03 10:25 UTC)

<p>I doubt you’ll have much success with traditional image processing like thresholding, connectivity, watershed etc.</p>
<p>I think your best bet is an ML approach, such as training an nnU-Net, or one of the existing trained segmenters. I’d give TotalSegmentator to see if it gives you a reasonable starting point. If it seems to work, you could then focus in your specific use-case.</p>

---

## Post #5 by @N-Van (2026-04-06 16:11 UTC)

<p>Your problem is not strictly one of noise or artifacts, but of lack of spatial resolution and sensitivity to the different tissues.<br>
Provided that you cannot re-scan you specimen at lower voltage, higher acquisition time, higher resolution and with contrastive agent, you can try ML methods like nninteractive, as written above. Biomedisa can be of help, too.<br>
You can also try to first enhance the dynamics of the scan, then denoise it. I usually use CLAHE for the contrast and <a href="https://imagej.net/plugins/non-local-means-denoise/" rel="noopener nofollow ugc">Non-local means</a> for the noise. All with Fiji. Non local means is very powerful at removing noise while keeping structures, but requires a long processing time. Try first on a few slices with different parameters.<br>
And if all of that doesn’t work: manual segmentation! (be patient)</p>

---
