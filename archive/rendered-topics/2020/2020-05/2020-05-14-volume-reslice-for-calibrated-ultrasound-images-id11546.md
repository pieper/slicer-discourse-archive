---
topic_id: 11546
title: "Volume Reslice For Calibrated Ultrasound Images"
date: 2020-05-14
url: https://discourse.slicer.org/t/11546
---

# Volume Reslice for Calibrated Ultrasound Images

**Topic ID**: 11546
**Date**: 2020-05-14
**URL**: https://discourse.slicer.org/t/volume-reslice-for-calibrated-ultrasound-images/11546

---

## Post #1 by @Winona_Richey (2020-05-14 20:07 UTC)

<p>Operating system: Windows 7 and MacOS 10.14.6<br>
Slicer version: 4.10.1<br>
Expected behavior: 1. Set the incoming tracked image as the driver for the corresponding 2D viewer.<br>
2. Find the appropriate mode from the Mode list that keeps your full tracked image in the 2D viewer. (All mode settings tried).<br>
3 (expected behavior). Visualize the whole US image in the 2D viewer in the 3D viewer by activating the “eye” icon in the header of the 2D viewer.</p>
<p>Actual behavior: 3. Only thin line visible in 2D viewer (and therefore in 3D view).</p>
<p>Additional Info: I can view the ultrasound image using the volume reslice driver when just applying the probe transform without a calibration transform (which is what the IGT instructions show). However, this shows the ultrasound in image space (with units = pixels), while all other scene information is in physical space (units =mm). The ultrasound calibration has a relatively large scaling aspect (e.g. 414 pixels -&gt; 40 mm). The scaling can be accurately applied, but the image volume cannot be viewed after the calibration rotation is applied. Models, segmentations and points designated in the US images are properly transformed by the applied transforms, but the image always disappears when transformed. This leads me to believe that the calibration is not faulty, and this is a volume visualization problem.</p>
<p>Unsuccessful fixes (a short list):  I believe it should work with the Transverse mode applied and the US image volume as the driver, but I also tried all combinations of reslice modes and drivers. I tried separating scaling and rotation matrices, with various combinations of hardened transforms so that the volume reslice driver was only accounting for one transform at a time.</p>
<p><a href="https://drive.google.com/drive/folders/1IhIy4-eHZGecZITXX67LKmGS3NJ37Ud2?usp=sharing" rel="nofollow noopener">Data if you want to see what I mean</a>: ultrasound image volume and calibration transform (as h5, txt and mat file)</p>
<p>Is there a way to visualize this transformed image in the 3D view?</p>

---

## Post #2 by @lassoan (2020-05-15 01:38 UTC)

<p>Which SlicerIGT tutorial have you followed?</p>
<p>Can you upload your Slicer scene and Plus configuration file somewhere and post the link here?</p>

---

## Post #3 by @Winona_Richey (2020-05-15 04:11 UTC)

<p>Thank you <em>so</em> much for replying so quickly!</p>
<p>The SlicerIGT tutorial I referenced above is here: <a href="https://github.com/SlicerIGT/SlicerIGT/wiki/Tracked-ultrasound-tutorial" class="inline-onebox" rel="noopener nofollow ugc">Tracked ultrasound tutorial · SlicerIGT/SlicerIGT Wiki · GitHub</a></p>
<p>I’ve uploaded a scene and the data (a sample US image with the applied calibration transform)  <a href="https://drive.google.com/open?id=1IhIy4-eHZGecZITXX67LKmGS3NJ37Ud2" rel="noopener nofollow ugc">here</a>.</p>
<p>Plus is configured to give a framegrabbed ultrasound (US) image and tracking info from NDI, and it does this successfully.</p>
<p>I’ve added further explanation and some pictures to help me better explain what’s going on. I’m trying to get a frame grabbed ultrasound image to display in world coordinates. The trouble happens when applying the probe calibration transform to an image volume.</p>
<p>I used an in-house calibration module to define the transformation from US image coordinates to the tracked US transducer (NDI tracking) in world coordinates. This gives a standard 4x4 calibration matrix. This matrix has low validation error – i.e. it generates  points/models/segmentations in correct world positions. The calibration matrix can correctly transform other node types (fiducials, models, segmentations, etc.). Here I have fiducials (pink), a model (blue), and a segmentation(green) shown in the green slice view (in image space). Clones of these objects are made and transformed (with NDI transforms and the calibration matrix) in 3D space. A model of the ultrasound image bounds is also shown (rectangle). What’s important is that these are all in the correct space in the world coordinates.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f02006e8bef94d245ce8a57c36ce095f0895ec.png" data-download-href="/uploads/short-url/5ysBN56rRx1WkSpNEcEvPNTgeni.png?dl=1" title="2020-05-14-Scene (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f02006e8bef94d245ce8a57c36ce095f0895ec_2_690x490.png" alt="2020-05-14-Scene (1)" data-base62-sha1="5ysBN56rRx1WkSpNEcEvPNTgeni" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f02006e8bef94d245ce8a57c36ce095f0895ec_2_690x490.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f02006e8bef94d245ce8a57c36ce095f0895ec.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f02006e8bef94d245ce8a57c36ce095f0895ec.png 2x" data-dominant-color="3D3E46"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-05-14-Scene (1)</span><span class="informations">799×568 79.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Via the aforementioned tutorial, I can get a live image volume displaying, moving with the tracked probe no problem BUT without the calibration applied. Here you can see the image, transformed by an NDI tracking transform, and visualized in the scene using the volume reslice driver. I turned on the yellow slice view to show an orthogonal (not resliced) plane.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef1517a7f78fe9c47e5b0fd7f69494397754c79.png" data-download-href="/uploads/short-url/fPrxIfChqB6wIl5PXJQNCF05YIF.png?dl=1" title="2020-05-14-Scene1 (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef1517a7f78fe9c47e5b0fd7f69494397754c79_2_690x490.png" alt="2020-05-14-Scene1 (1)" data-base62-sha1="fPrxIfChqB6wIl5PXJQNCF05YIF" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef1517a7f78fe9c47e5b0fd7f69494397754c79_2_690x490.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef1517a7f78fe9c47e5b0fd7f69494397754c79.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef1517a7f78fe9c47e5b0fd7f69494397754c79.png 2x" data-dominant-color="383942"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-05-14-Scene1 (1)</span><span class="informations">799×568 60.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The image “disappears” when I apply a transform node containing our calibration matrix, except for one line of pixels. Here I have the volume reslice driver set to show Transverse, Inplane, and Inplane-90, and you can see each corresponding line of pixels.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65f16c4a329cea78e8d20e68304fe0eda354542b.png" data-download-href="/uploads/short-url/exPtce3Ym3i8CxNPNmt6QhJOR0T.png?dl=1" title="2020-05-14-Scene1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65f16c4a329cea78e8d20e68304fe0eda354542b_2_616x500.png" alt="2020-05-14-Scene1" data-base62-sha1="exPtce3Ym3i8CxNPNmt6QhJOR0T" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65f16c4a329cea78e8d20e68304fe0eda354542b_2_616x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65f16c4a329cea78e8d20e68304fe0eda354542b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65f16c4a329cea78e8d20e68304fe0eda354542b.png 2x" data-dominant-color="2F2F3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-05-14-Scene1</span><span class="informations">741×601 21.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Basically, I want to visualize my calibrated tracked ultrasound image in the 3D view, but I am not able to. For some reason, it seems I can transform and visualize any other kind of node aside from an image.</p>

---

## Post #4 by @wRossw (2023-02-02 22:43 UTC)

<p>I wanted to bring this thread back up. Has a solution been found?</p>
<p>We have the exact same issue when applying a custom transform from our own calibration scripts. Tracking the US without a calibration transform applied works just fine. However, as soon as we apply our own transform the 2D US image is reduced into a line just as Winona</p>
<p>Please, let me know if there is a workaround.</p>

---

## Post #5 by @lassoan (2023-02-15 04:19 UTC)

<p>If you don’t see the image in the slice view then it means that you have chosen an incorrect transform for driving the slice view in Volume Reslice Driver module. Probably the easiest if you keep the IJKToRAS transform that is embedded in the image as identity matrix, and you position the image using ImageToReference (=ProbeToReference*ImageToProbe) transform.</p>

---
