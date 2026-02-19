---
topic_id: 37040
title: "Monai Auto3Dseg For Pigs"
date: 2024-06-26
url: https://discourse.slicer.org/t/37040
---

# MONAI auto3dseg for pigs

**Topic ID**: 37040
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/monai-auto3dseg-for-pigs/37040

---

## Post #1 by @Matteboo (2024-06-26 13:39 UTC)

<p>Hello,</p>
<p>First of all, it’s been one year that I’ve been using 3DSlicer and I want to thanks everyone for this amazing tool and for their help in this forum <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
<p>We are looking for a way to automatically segment the organs of pig using CTs scan. The reason is that we are developping a software for human but we need to do preclinical tests on pigs. We can use MONAI auto3dseg for human but we couldn’t find any software that works for pigs.</p>
<p>I think that leveraging the strength of MONAI auto3Dseg will make the development easier. It makes an easy implementation for us and it will help other people in the future.</p>
<p>My first question is  :<br>
<strong>1. What is needed to developp such a model?</strong></p>
<p>We could provide labelled CT scan and some computing power. The model would of course be public but we can’t put the dataset on opensource. My following questions are:</p>
<p><strong>2. How many labelled CT are needed ?<br>
3. How much computing power is required?<br>
4. Is it an issue that the dataset wont be opensource?</strong></p>
<p>If some people in the community want to offer some help or advice it would be very much appreciated.</p>

---

## Post #2 by @muratmaga (2024-06-26 15:01 UTC)

<aside class="quote no-group" data-username="Matteboo" data-post="1" data-topic="37040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p>My first question is :<br>
<strong>1. What is needed to developp such a model?</strong></p>
</blockquote>
</aside>
<p>Correctly segmented datasets, that you can meaningfully split into training/test/validation groups.</p>
<aside class="quote no-group" data-username="Matteboo" data-post="1" data-topic="37040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p><strong>2. How many labelled CT are needed ?</strong></p>
</blockquote>
</aside>
<p>Depending on complexity of the segmentation, and the accuracy you are comfortable with (for example 85-90% range), this might be as low as 20. To get 95+%, you might need 40-50.</p>
<aside class="quote no-group" data-username="Matteboo" data-post="1" data-topic="37040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<ol start="3">
<li>How much computing power is required?</li>
</ol>
</blockquote>
</aside>
<p>Depends on the size of the volumes, and other parameters. I would image you would need a large GPU with at least 24GB of RAM.</p>
<aside class="quote no-group" data-username="Matteboo" data-post="1" data-topic="37040">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p><strong>4. Is it an issue that the dataset wont be opensource?</strong></p>
</blockquote>
</aside>
<p>This is not a problem, if you are not planning to share your model. If it is only for your usage, you can do whatever you want.</p>

---

## Post #3 by @curtislisle (2024-06-26 15:57 UTC)

<p>Hi Matteboo,<br>
You are asking some good questions. There is no single or best way to train the model you are looking to build, but Auto3DSeg is a likely good choice to start with. The preprocessing / postprocessing included in Auto3DSeg are helpful to generate a better model than if you trained a model yourself without these utilities. Here are a few quick answers. Others in the community may respond with more detail, but this might help you get started:</p>
<ol>
<li><strong>What is needed to develop a model?</strong> You are correct that matching CT files and segmentation label maps are exactly what you need for source data to train your model from. If you are using a package like Slicer to prepare the data, it would be good to store the source CT images and the masks named similar on the filesystem of a GPU-equipped computer. More on the computer later. I suggest that NRRD format would be a good way to store images, but Nifti may also work for you. Nifti is optimized for neuroimaging and generally not as good for applications like yours, but it would probably work to get started.</li>
</ol>
<p><strong>2. How many labeled CTs are needed?</strong> As many as you have <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Generally, the larger your inpyyt dataset, the better your final model will perform. A really good number would be 50-100 or more matched CT/labelmap pairs, but you can start with whatever you have (10, for example?).</p>
<p><strong>3. How much computer power is required?</strong> The training can be configured differently depending on hardware available, but as a minimum, I would suggest a Linux or Windows PC with an NVidia GPU accelerator and at least 32 GB of system RAM. The GPU should have 16GB of RAM if possible, though I believe you could make some progress with an 8GB GPU. For example, this could be a desktop with an NVIDIA 2080 card or higher or a new laptop with a mobile NVIDIA chip embedded. There are ways to train without NVIDIA GPUs, but they are either slow or take advanced configuration (e.g. an AMD GPU) and I don’t recommend this for getting started. If you have more capable hardware available (larger system RAM and/or larger GPU memory, the model can generally be adapted to have better final perfrormance.</p>
<p><strong>4. Is it an issue that the dataset won’t be opensource?</strong> My personal understanding is that it is generally not a problem to train with private data and then open-source the resulting model. When your model training is finished, you can share the trained weights file generated, which usually happens automatically during training. You can use Slicer to preview the images and your predictions.</p>
<p>I hope these general responses are helpful. Good luck!</p>
<p>Curtis</p>

---

## Post #4 by @Matteboo (2024-06-28 09:40 UTC)

<p>Thank you both for your detailled answer</p>
<p>I will start on gathering and labelling the dataset.<br>
Right now, I have a RTX 2060 with 6Go of dedicated GPU memory and 15 of shared memory. I hope it will be enought</p>
<p>Is there a guide on how to train a model that I could read ?</p>

---
