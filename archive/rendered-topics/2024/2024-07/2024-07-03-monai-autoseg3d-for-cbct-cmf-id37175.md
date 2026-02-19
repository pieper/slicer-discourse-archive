---
topic_id: 37175
title: "Monai Autoseg3D For Cbct Cmf"
date: 2024-07-03
url: https://discourse.slicer.org/t/37175
---

# MONAI AutoSeg3D for CBCT (CMF)

**Topic ID**: 37175
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/monai-autoseg3d-for-cbct-cmf/37175

---

## Post #1 by @ssingh (2024-07-03 12:27 UTC)

<p>I tried MONAI AutoSeg3D auto-segmentation on CMF scan (CBCT).<br>
I see that the segmentation results appear like as if it was done on a downsampled image.</p>
<p>Please see the snapshot here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0ce1dd5a7840bda6c0471e084ba47fe62b7c0c0.jpeg" data-download-href="/uploads/short-url/rvDhaHX3tUNhDdkz1xpP26jAKA0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ce1dd5a7840bda6c0471e084ba47fe62b7c0c0_2_690x351.jpeg" alt="image" data-base62-sha1="rvDhaHX3tUNhDdkz1xpP26jAKA0" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ce1dd5a7840bda6c0471e084ba47fe62b7c0c0_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ce1dd5a7840bda6c0471e084ba47fe62b7c0c0_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0ce1dd5a7840bda6c0471e084ba47fe62b7c0c0_2_1380x702.jpeg 2x" data-dominant-color="999893"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×976 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have used Whole Body segmentation TS2. I think TS2 implies Total Segmentator V2. I Observed a similar result when I used the Total Segmentator extension.</p>
<p>I also see the following log in the AutoSeg3d:</p>
<pre><code class="lang-auto">
Using orientation_ras

Using crop_foreground

Using resample with resample_resolution [1.5, 1.5, 1.5]

Running Inference ...
</code></pre>
<p>So it appears it resamples the image to 1.5x1.5x1.5</p>
<p>Is it possible to run the AutoSeg3D to get a better(finer) segmentation mask result? The extension currently does not provide such a control.</p>
<p>Thanks</p>

---

## Post #2 by @Gauthier (2024-07-04 08:26 UTC)

<p>Hello,</p>
<p>To my knowledge Monain Auto3DSeg has not been trained on those kind of data for now. You could give a try to DentalSegmentator : <a href="https://discourse.slicer.org/t/new-extension-dentalsegmentator-for-automatic-dental-ct-cbct-segmentation">https://discourse.slicer.org/t/new-extension-dentalsegmentator-for-automatic-dental-ct-cbct-segmentation</a></p>
<p>Best,<br>
Gauthier</p>

---

## Post #3 by @ssingh (2024-07-04 08:35 UTC)

<p><a class="mention" href="/u/gauthier">@Gauthier</a> thanks for your reply.<br>
Yes, I have used DentalSegmentator and AMASSS. They perform better. I wanted to see the performance of this tool as well. Basically, then use the best one.</p>
<p>On Dental Segmentator: Only the extension code is open source, however I could not find the implementation on auto segmentation model training. Is that also available, say if someone wants to extend work on Dental Segmentator?</p>
<p>Regards,<br>
Sukhraj</p>

---

## Post #4 by @Gauthier (2024-07-04 08:41 UTC)

<p>Hello,</p>
<p>Thanks for your reply.</p>
<p>The pretrained nnU-Net model for DentalSegmentator is shared here : <a href="https://zenodo.org/doi/10.5281/zenodo.10829674" class="inline-onebox" rel="noopener nofollow ugc">DentalSegmentator nnU-Net pretrained model for CBCT image segmentation</a></p>
<p>Best regards,<br>
Gauthier</p>

---

## Post #5 by @ssingh (2024-07-04 08:48 UTC)

<p>So essentially, learn how to use and train further a pre-trained model in nn-Unet, is all that is needed to extend Dental Segmentator.</p>

---

## Post #6 by @Gauthier (2024-07-04 08:57 UTC)

<p>Yes that would be the idea! nnU-Net offers a basic implementation of finetuning: <a href="https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/pretraining_and_finetuning.md" class="inline-onebox" rel="noopener nofollow ugc">nnUNet/documentation/pretraining_and_finetuning.md at master · MIC-DKFZ/nnUNet · GitHub</a></p>
<p>We haven’t used it for now, so I could not tell you more about the performance bumps that coud be obtained. It will probably depend a lot on what is your objective!</p>

---

## Post #7 by @philippepellerin (2024-07-06 15:15 UTC)

<p>Have you tried the whole head model in Monai AutoSeg3D? You will get the skull, the mandible, the rachis, eyeball, brain, and masticatory muscles.</p>

---

## Post #8 by @ssingh (2024-07-07 16:28 UTC)

<p><a class="mention" href="/u/philippepellerin">@philippepellerin</a> I can’t find the Head Model int the model list, please see the snapshot:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df081363df6dce88ecfb41935f4c47b53611e8a4.png" alt="image" data-base62-sha1="vP1Mf3aLv6f4zJbQ8JZTwiLP9EU" width="579" height="216"></p>
<p>Am I missing something? I am using Slicer 5.7.x</p>

---

## Post #9 by @ssingh (2024-07-07 16:38 UTC)

<p><a class="mention" href="/u/philippepellerin">@philippepellerin</a> Thanks for noticing in detail.</p>
<p>I observed a head model “Whole Head Segmentation” is available in 5.6.2 version of slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd397909621f449d41e94c912895b8cfa4a15a7a.png" data-download-href="/uploads/short-url/thv10PVQ6TotMjGAx3JlWqAugK6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd397909621f449d41e94c912895b8cfa4a15a7a.png" alt="image" data-base62-sha1="thv10PVQ6TotMjGAx3JlWqAugK6" width="435" height="500" data-dominant-color="EDEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">588×675 26.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Camila_Da_Rocha_Camp (2024-12-29 22:58 UTC)

<p>It is not performing the “whole head segmentation on my software” function. Maybe you know what’s wrong with the software. I’m using 3D slicer version 5.6.2.<br>
Can you help me?</p>

---

## Post #11 by @ssingh (2025-03-31 07:34 UTC)

<p>Hello,</p>
<p>Sorry for the late reply.</p>
<p>Please download the latest Slicer 5.8.x and install the MONAI Auto3Dseg extension. You should be able to see the model:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae7ae925140a91530b67555e086755dd57a75d43.png" data-download-href="/uploads/short-url/oTwpIK57EDCN9qx0JmVHg9HIwRZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae7ae925140a91530b67555e086755dd57a75d43_2_303x500.png" alt="image" data-base62-sha1="oTwpIK57EDCN9qx0JmVHg9HIwRZ" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae7ae925140a91530b67555e086755dd57a75d43_2_303x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae7ae925140a91530b67555e086755dd57a75d43_2_454x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae7ae925140a91530b67555e086755dd57a75d43_2_606x1000.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">877×1446 50.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
