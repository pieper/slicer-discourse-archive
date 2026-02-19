---
topic_id: 11197
title: "Real Time 3D Ultrasound Volume Reconstruction Using Slicerig"
date: 2020-04-20
url: https://discourse.slicer.org/t/11197
---

# Real-time 3D ultrasound volume reconstruction using SlicerIGT extension

**Topic ID**: 11197
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/real-time-3d-ultrasound-volume-reconstruction-using-slicerigt-extension/11197

---

## Post #1 by @lassoan (2020-04-20 06:23 UTC)

<p>3D Slicer’s SlicerIGT extension allows live data acquisition from a wide range of medical imaging, position tracking, and other devices and visualize and process the data in real-time.</p>
<p>We have recently implemented huge performance improvements in live 3D ultrasound image acquisition, which allows smooth, continuous reconstruction of high-resolution 3D ultrasound volumes, using inexpensive portable ultrasound and position tracker. For large volumes and performance-critical applications, the volume reconstructor can use all CPU threads or GPU acceleration (OpenCL). We have uploaded a short video of this new feature here:</p>
<div class="lazyYT" data-youtube-id="2vXeJxYFou4" data-youtube-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=131"></div>
<p>Thanks to company sponsors and our awesome SlicerIGT developers <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and <a class="mention" href="/u/ungi">@ungi</a> for making these available for the community.</p>
<p>Any questions, comments, and suggestions are welcome.</p>

---

## Post #2 by @kristjanq (2020-05-11 02:19 UTC)

<p>This is awesome!</p>
<p>I would like to address an issue I had with an already recorded sequence. I loaded the sequence in Plus (providing the full path in the config file.)<br>
Then I followed the steps as shown in the video. As a result, I do not get live reconstruction. Is it not supposed to behave the same as a real-time data acquisition and reconstruction scenario, given that Plus will replay the images from the sequence?</p>
<p>Also the button for “input sequence browser” does not work when chosen “Recorded sequence reconstruction” as an input method. Any input on this matter?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a59d64c62334fd40bd1afaf119a9060ad04238.png" data-download-href="/uploads/short-url/ucjzBUkuZnVgxU9t9jHZOdtX0ww.png?dl=1" title="3d reconstruction" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3a59d64c62334fd40bd1afaf119a9060ad04238_2_688x500.png" alt="3d reconstruction" data-base62-sha1="ucjzBUkuZnVgxU9t9jHZOdtX0ww" width="688" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3a59d64c62334fd40bd1afaf119a9060ad04238_2_688x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3a59d64c62334fd40bd1afaf119a9060ad04238_2_1032x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3a59d64c62334fd40bd1afaf119a9060ad04238_2_1376x1000.png 2x" data-dominant-color="8E8E91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d reconstruction</span><span class="informations">1595×1159 73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-05-16 16:10 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you help out with this?</p>

---

## Post #4 by @Sunderlandkyl (2020-05-16 17:27 UTC)

<p>What is the exact issue that you are having when doing live volume reconstruction?</p>
<p>The images that you receive from Plus should have a transform applied to them, either by receiving them directly as in the correct coordinate system (ex. Image_Reference), or by applying the transforms within Slicer. If this is already done, then I will need some more information about your Slicer scene, Plus config file and data to determine what the issue is.</p>
<p>For the “Recorded sequence reconstruction”, I assume the reason that you cannot select a sequence browser is that you do not have a loaded sequence in Slicer.</p>

---

## Post #5 by @lb123 (2021-12-15 12:46 UTC)

<p>Hi, can you please tell me where I can find the Plus Server configuration file to perform a real-time 3D ultrasound volume recontruction using this SlicerIGT extension?</p>

---

## Post #6 by @JakeZ (2021-12-15 13:21 UTC)

<p>Perhaps you could try U-34 in SlicerIGT Tutorials (<a href="http://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a>) where sample data is also available.</p>

---

## Post #8 by @lb123 (2021-12-16 10:03 UTC)

<p>Thank you. I used that data and it worked</p>

---

## Post #9 by @whu (2022-05-12 13:28 UTC)

<p>Dear Sir,</p>
<p>does this module（volume reconstruction）support the TEE living data or offline record data ?</p>
<p>there mabye a position tracking device.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb67f3e6e35509756371ca091af6450167201812.jpeg" alt="image" data-base62-sha1="zS2yTqaky9wzC8bn3BWCV7igdEK" width="383" height="406"></p>
<p>thanks</p>

---

## Post #10 by @lassoan (2022-05-12 13:29 UTC)

<p>It does continuous live recording and volume reconstruction. You can also feed pre-recorded data or reconstruct offline from pre-recorded data.</p>

---

## Post #11 by @whu (2022-05-12 14:57 UTC)

<p>Thanks very much, I will try the TEE  pre-recored data.</p>

---

## Post #12 by @Javan (2023-03-01 21:11 UTC)

<p>Hello,<br>
I am using a system with an NVIDIA GeForce RTX 3070 GPU. I want to use it for volume reconstruction. Can you please let me know if there is a way to configure Slicer to use it for volume reconstruction?<br>
Thank you.</p>

---

## Post #13 by @lassoan (2023-03-01 22:44 UTC)

<p>GPU is used for volume reconstruction and volume rendering.</p>

---

## Post #14 by @Javan (2023-03-01 23:31 UTC)

<p>Thank you for your reply.<br>
The issue is that when I make the region of interest larger for real-time reconstruction then I see lag and there are missing parts and gaps in the reconstructed result.<br>
I checked “slicer.vtkSlicerVolumeReconstructionLogic().IsGpuAccelerationSupported()” and it was false. Does this mean my GPU is not used?<br>
Would you please let me know how I can have a bigger area for reconstruction with no lag? should I upgrade any hardware? or is there any other way to solve this issue?<br>
Thank you.</p>

---

## Post #15 by @lassoan (2023-03-01 23:54 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is GPU acceleration available on factory-built IGSIO packages? If not, what would be needed to enable it?</p>
<p><a class="mention" href="/u/javan">@Javan</a> using the GPU will accelerate volume reconstruction but there is a lot of other things to happen quickly to be able to significantly increase the frame rate. Most of these things cannot run on the GPU. So, in general, you need to slow down if you see gaps. What are the dimensions and voxel size of the volume that you are trying to insert frames into? What are the dimensions and pixel size of the ultrasound image? What is the ultrasound image acquisition rate?</p>

---

## Post #16 by @Sunderlandkyl (2023-03-02 01:57 UTC)

<p>It doesn’t look like it’s included in the factory-built packages. It should be automatically included if the factory has OpenCL installed.</p>

---

## Post #17 by @Javan (2023-03-02 18:13 UTC)

<p>I tried with image size  800x600  spacing 0.08  with fps 10, and volume size 800x800x800 and spacing 0.1.<br>
For the GPU that means I don’t have OpenCL installed? is there any way to install it on my system? and will that help to solve the issue?<br>
Thank you in advance.</p>

---

## Post #18 by @Sunderlandkyl (2023-03-02 18:18 UTC)

<aside class="quote no-group" data-username="Javan" data-post="17" data-topic="11197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ec9cab/48.png" class="avatar"> Javan:</div>
<blockquote>
<p>For the GPU that means I don’t have OpenCL installed? is there any way to install it on my system? and will that help to solve the issue?</p>
</blockquote>
</aside>
<p>You shouldn’t need to have OpenCL installed on your own computer. The OpenCL SDK just needs to be installed on the machine that is building the extension.</p>

---

## Post #19 by @lassoan (2023-03-02 18:36 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Do you know if there is any disadvantage of building with OpenCL? (for example, what happens if the package is built with OpenCL SDK but then on the user’s computer there is no OpenCL or not even a GPU)? If there are no disadvantages then we could download the OpenCL SDK in SlicerIGSIO build.</p>
<p><a class="mention" href="/u/javan">@Javan</a> Do you have experience in building C++ code? You can then test if the speed improvement by reconstructing on the GPU is significant enough.</p>

---

## Post #20 by @Sunderlandkyl (2023-03-02 18:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="19" data-topic="11197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you know if there is any disadvantage of building with OpenCL? (for example, what happens if the package is built with OpenCL SDK but then on the user’s computer there is no OpenCL or not even a GPU)?</p>
</blockquote>
</aside>
<p>I believe that the user should still be able to use the OpenCL GPU-acceleration optimization. I’ll look into including OpenCL as part of the SlicerIGSIO superbuild process.</p>

---

## Post #21 by @Javan (2023-03-02 20:59 UTC)

<p>Unfortunately, not.<br>
I didn’t understand why I am not able to use GPU-acceleration now. Would you please let me know if it is possible how I can use it? or am I able to use it after OpenCL is included in SlicerIGSIO?</p>

---
