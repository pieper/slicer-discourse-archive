---
topic_id: 33646
title: "Tensorflow X Slicer"
date: 2024-01-05
url: https://discourse.slicer.org/t/33646
---

# TensorFlow x Slicer

**Topic ID**: 33646
**Date**: 2024-01-05
**URL**: https://discourse.slicer.org/t/tensorflow-x-slicer/33646

---

## Post #1 by @VincentMillot (2024-01-05 18:01 UTC)

<p>Dear Slicer Community,</p>
<p>I’m new here and I wanted to share an extension I made to use my TensorFlow models for image segmentation directly into slicer. I’ve already read here that most deep learning models are developed under Pytorch in the medical field, but I though it would be fun trying to create an extension focused on TensorFlow.</p>
<p>The model input size is detected to resize the selected image/volume to compatible size and range of values.</p>
<p>For now the segmentation can only be segmented slice by slice (1 image as input - 1 segmentation as output) but I’ll try to implement 2.5D approach (N images as input - 1 segmentation as output) and 3D approach (full volume as input - full volume as output).</p>
<p>Rep of the extension : <a href="https://github.com/VincentMillotMaysounabe/Slicer-TensorFlow" rel="noopener nofollow ugc">https://github.com/VincentMillotMaysounabe/Slicer-TensorFlow</a></p>
<p>If any of you have comments on how I could enhance the project it could be really precious to me.</p>
<p>Thanks,<br>
Vincent</p>

---

## Post #2 by @pieper (2024-01-05 19:52 UTC)

<p>Hi - welcome, this sounds really interesting, and yes, it’s common. to use pytorch but tensorflow should work fine too if it gets installed right.  For me on a linux test with a recent build, <code>pip_install("tensorflow[and-cuda]")</code> in the python console completed but crashed whtn I tried to import it.  I suspect there may be similar issues with cuda drivers since there have been many with pytorch.</p>
<p>BTW, your repository would benefit with some examples and screenshots so it’s clear what the module currently does.</p>
<p>Also since it’s pure python you should be able to provide instructions for people to install it locally.  This doesn’t need to be in the extension manager until it’s ready for use by the general user population.</p>

---

## Post #3 by @VincentMillot (2024-01-17 20:09 UTC)

<p>Hi<br>
Thanks so much for your answer !<br>
I was not aware of those installation issues since it worked fine for me. I’m on Windows using Slicer 5.6.1 and TensorFlow 2.15.0. I’d like to investigate more about this, have you any idea of where to start ?</p>
<p>I recently updated my repository with a quick overview of the extension and a full tutorial with example files and a -not so accurate- U-net model for prostate segmentation.</p>

---

## Post #4 by @pieper (2024-01-17 21:10 UTC)

<p>Regarding GPU driver issues you can just search this discourse for questions about TotalSegmentator and you’ll find a lot of questions about installation issues.  Maybe more on linux than windows but both come up.  Usually they can be resolved if someone has the patients and some technical experience, but it’s a barrier to widespread use.</p>

---

## Post #5 by @VincentMillot (2024-03-24 19:42 UTC)

<p>Hi again,<br>
I’ve been working for some weeks on a way to deal with the installation issues for tensorflow. The solution I came up with is to give the possibility to perform a remote prediction by sending the model and inputs to a raspberry Pi through an API. Then tensorflow is not needed anymore.</p>
<p>Since models can be heavy in h5 format, i’ve mainly worked with models saved with tflite format, but i’m working on making both availables. (tflite extension will always compute faster since models can be 2-3 times lighter). This solution is working well but you have to wait about 50 seconds to have the prediction with a model ~25MB and 20 images to compute.</p>
<p>Everything should be ready within a week, i’ll update my repo at this moment.</p>
<p>I’d be happy to know what you think about this idea !</p>

---

## Post #6 by @lassoan (2024-03-28 16:39 UTC)

<p>Most computers that are used for running Slicer are magnitudes stronger than a Raspberry Pi. Therefore, most people would want to run inference on the computer that runs Slicer.</p>
<p>That said, the same server that you implement for receiving images from Slicer, running the inference, and sending back segmentations to Slicer could be used on the same computer, to run inference in another Python environment that is compatible with TensorFlow.</p>
<p>I would just note that nowadays I barely see any projects using TensorFlow for medical image computing anymore. If you want to maximize the impact of your efforts in this field then you might consider working with PyTorch.</p>

---

## Post #7 by @VincentMillot (2024-03-28 20:22 UTC)

<p>Thank you so much for the advices.</p>
<p>The extension was primarely using local inferences, but to do so, you still have to install tensorflow dependencies. The idea of having a Raspberry Pi running inferences is to provide a ready-to-go solution, despite poor performances. Anyway the user will still have both choices available on the extension.</p>
<p>I expected this concerns about using TensorFlow instead of PyTorch. After few investigation about model saving and loading with PyTorch, I couldn’t find any way to load the model without having the corresponding python class. This makes unknown model loading way harder than with tensorflow and I’ll have to create a specific workflow for it. I guess the user will have to provide the python file with the corresponding python class.</p>

---

## Post #8 by @lassoan (2024-03-28 21:51 UTC)

<aside class="quote no-group" data-username="VincentMillot" data-post="7" data-topic="33646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/c68b51/48.png" class="avatar"> VincentMillot:</div>
<blockquote>
<p>I couldn’t find any way to load the model without having the corresponding python class</p>
</blockquote>
</aside>
<p>You usually don’t need to implement models from scratch, but pip install a package tha provides the model (e.g., MONAI) and you just load the model weights. It is all automated, you can run a model on an image by a single click. See for example <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/">MONAIAuto3DSeg extension</a>.</p>

---
