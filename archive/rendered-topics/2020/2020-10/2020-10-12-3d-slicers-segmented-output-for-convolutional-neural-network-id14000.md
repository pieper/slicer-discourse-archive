---
topic_id: 14000
title: "3D Slicers Segmented Output For Convolutional Neural Network"
date: 2020-10-12
url: https://discourse.slicer.org/t/14000
---

# 3D slicer's segmented output for convolutional neural network training 

**Topic ID**: 14000
**Date**: 2020-10-12
**URL**: https://discourse.slicer.org/t/3d-slicers-segmented-output-for-convolutional-neural-network-training/14000

---

## Post #1 by @Abdulrahman (2020-10-12 14:28 UTC)

<p>Hi all,<br>
I’m working on the field of brain segmentation using convolutional neural network CNN. I have already segmented the brain regions on Slicer, so now I want to export the input images(DICOM) and its corresponding outputs  as 3D  for CNN training.<br>
How I can perform that ?</p>
<p>Any idea will be appreciated</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-10-12 14:33 UTC)

<p>I would recommend saving both the CT and segmentation into nrrd or nifti format that you can easily read into numpy array and use in your network.</p>

---

## Post #3 by @Abdulrahman (2020-10-12 23:17 UTC)

<p>Thanks Mr Lassoan,<br>
Is there any tool or module can export/save the files into nifti format in Slicer. By the way, I’m using Matlab.</p>
<p>Secondly, Should I perform registration for the MRI and its corresponding segmentation ?</p>
<p>Kind regards</p>

---

## Post #4 by @lassoan (2020-10-12 23:33 UTC)

<aside class="quote no-group" data-username="Abdulrahman" data-post="3" data-topic="14000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> Abdulrahman:</div>
<blockquote>
<p>Is there any tool or module can export/save the files into nifti format in Slicer</p>
</blockquote>
</aside>
<p>No need for a module, you can run <code>slicer.util.saveNode</code> to save an image in nifti format.</p>
<aside class="quote no-group" data-username="Abdulrahman" data-post="3" data-topic="14000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> Abdulrahman:</div>
<blockquote>
<p>By the way, I’m using Matlab.</p>
</blockquote>
</aside>
<p>I’m not sure this is the best idea: you cannot implement complete applications in Matlab, it is only affordable for academic use, and in general you just make your life harder by not using the same toolsets that most machine learning experts . For example, if you use tensorflow, pytorch, etc. then you can run training or inference directly within Slicer’s Python environment. You can interface Slicer with Matlab, too, but there are several additional layers and inconveniences.</p>
<aside class="quote no-group" data-username="Abdulrahman" data-post="3" data-topic="14000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> Abdulrahman:</div>
<blockquote>
<p>Should I perform registration for the MRI and its corresponding segmentation ?</p>
</blockquote>
</aside>
<p>If you segment an image then the resulting segmentation will be spatially aligned with it in physical space (and in most cases, you choose the segmentation to have the exact same geometry as the input image). Therefore, there should be no need for any additional registration step.</p>

---

## Post #5 by @Abdulrahman (2020-10-12 23:57 UTC)

<p>Thanks you so much for your perfect explanation.</p>

---

## Post #6 by @Abdulrahman (2020-10-14 05:22 UTC)

<p>[No need for a module, you can run <code>slicer.util.saveNode</code> to save an image in nifti format.]</p>
<p>Sorry Mr Lassoan for keep asking, Can I save only the visible segments into nifti file?.<br>
If yes, Is it like what I’ve attached.</p>
<p>Thanks again<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/622a5e82683da71fd8ad34aabd958402a9612aba.jpeg" alt="Picture1" data-base62-sha1="e0pzc2ncXJB69yc7rQ9LPyhDSkO" width="661" height="394"></p>

---

## Post #7 by @lassoan (2020-10-15 05:25 UTC)

<p>You can use “Export to files…” feature in Segment Editor module (“Segmentations…” button’s dropdown menu). Use latest Slicer Stable Release.</p>

---
