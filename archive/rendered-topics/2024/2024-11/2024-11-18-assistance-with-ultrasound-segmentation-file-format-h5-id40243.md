---
topic_id: 40243
title: "Assistance With Ultrasound Segmentation File Format H5"
date: 2024-11-18
url: https://discourse.slicer.org/t/40243
---

# Assistance with Ultrasound Segmentation File Format (.h5)

**Topic ID**: 40243
**Date**: 2024-11-18
**URL**: https://discourse.slicer.org/t/assistance-with-ultrasound-segmentation-file-format-h5/40243

---

## Post #1 by @MReza (2024-11-18 13:38 UTC)

<p>Dear all,<br>
I am currently working on automatic segmentation in ultrasound imaging using the instructions provided on the AIGT GitHub repository.<br>
I have successfully trained my own model by following all the steps outlined there. As a result, I obtained several files, all named unet-DiceCE.<br>
However, I need the final segmentation model in .h5 format to use it for ultrasound segmentation with 3D Slicer. Could anyone advise on how to convert these files or generate the required .h5 format?<br>
Dear Dr. <a class="mention" href="/u/ungi">@ungi</a> , since you are actively involved in research on this topic, I would greatly appreciate your guidance.<br>
Thank you very much</p>

---

## Post #2 by @ungi (2024-11-18 16:50 UTC)

<p>Hi, if you are using this training script:<br>
<a href="https://github.com/SlicerIGT/aigt/blob/master/UltrasoundSegmentation/train.py" rel="noopener nofollow ugc">aigt/UltrasoundSegmentation/train.py at master · SlicerIGT/aigt</a><br>
then the models are saved in traced format, so you don’t need the source code that defines the model. You could change the lines where the traced model is saved to save in any format you like. But I’m not sure why would you want to do that.</p>

---

## Post #3 by @MReza (2024-11-18 17:13 UTC)

<p>Thank you for answering my question.<br>
Since the file format used for segmentation UNet (the extension in 3D Slicer) is .h5, I want to convert the final model to .h5.<br>
Do you mean this is not necessary?</p>

---

## Post #4 by @MReza (2024-11-18 19:08 UTC)

<p>I think I can imagine what is happening based on the final results of this model. From what I learned in your PowerPoint file (U38-live AIrec), the file needs to be in .h5 format to be imported into the SegmentationUNet extension. However, I noticed there are new extensions in your Git repository, such as <code>torch_live_ultrasound</code> or ‘torch sequence segmentation’. Should the final “model_traced_bes.pt” be used with this extension directly?</p>

---

## Post #5 by @ungi (2024-11-18 20:02 UTC)

<p>Oh, unfortunately that tutorial is outdated. It still works, but that is not how I would do things now.</p>
<p>For real-time applications, you will get best performance if you stream the ultrasound data directly to a segmentation script in a separate python environment. Then, that script streams the segmentations to Slicer. Here is an example for such a script: <a href="https://github.com/SlicerIGT/aigt/blob/master/UltrasoundSegmentation/Inference/ScanConversionInference.py" rel="noopener nofollow ugc">aigt/UltrasoundSegmentation/Inference/ScanConversionInference.py at master · SlicerIGT/aigt</a></p>
<p>And this example script expects traced models, so you don’t need to change the way models are saved.</p>

---

## Post #6 by @MReza (2024-11-18 20:36 UTC)

<p>Ah, I see—this likely means the ultrasound extension is outdated. May I ask what steps I should follow if I want to run the auto-segmentation using a recorded sequence in 3d slicer?</p>

---

## Post #7 by @ungi (2024-11-19 00:04 UTC)

<p>For that, you may use the Torch Sequence Segmentation module:<br>
<a href="https://github.com/SlicerIGT/aigt/tree/master/SlicerExtension/LiveUltrasoundAi/TorchSequenceSegmentation" rel="noopener nofollow ugc">aigt/SlicerExtension/LiveUltrasoundAi/TorchSequenceSegmentation at master · SlicerIGT/aigt</a></p>

---

## Post #8 by @MReza (2024-11-19 16:22 UTC)

<p>First of all, thank you for the guidance so far.<br>
However, I have encountered some problems using Torch Sequence Segmentation. With the settings configured as shown in the video, I selected my model, which is named <strong>model_traced_best</strong>. But when I choose 3D Volume Reconstruction and start, not only does nothing happen, but the image also freezes on the current slide. While the view updates based on transformations in the 3D view, the displayed image remains unchanged.</p>
<p>Moreover, the generated prediction file doesn’t actually contain any predictions.<br>
Is there anything specific I should pay attention to while using this extension?</p>
<p>I am attaching a video here to demonstrate what is happening.<br>
it shows before and after starting the torch segmentation.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/487be0d5211fea350b1694d47536aee907231108.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4de2c44a858f112dee8c180df8c54a747ca831b.jpeg">
  </div><p></p>

---

## Post #9 by @max_05ge (2025-10-11 20:37 UTC)

<p>Hello,</p>
<p>Have you found a solution to your problem?</p>
<p>I also want to perform segmentation of recorded ultrasound images.</p>

---
