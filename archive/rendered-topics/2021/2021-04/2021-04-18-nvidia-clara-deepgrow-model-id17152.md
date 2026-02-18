# NVIDIA Clara deepgrow model

**Topic ID**: 17152
**Date**: 2021-04-18
**URL**: https://discourse.slicer.org/t/nvidia-clara-deepgrow-model/17152

---

## Post #1 by @Wahnfried (2021-04-18 03:53 UTC)

<p>Hello!</p>
<p>When using the NVIDIA Clara AIAA extension, the deepgrow function does not seem to work for me (tested using Slicer 4.11 and Slicer 4.13) as I cannot choose a model to start with; there is no list opening up when clicking the box. The markup buttons are greyed out, too.<br>
Is this a problem on my side or a missing model on the default public server? I’d love to try it before possibly going through the struggle of setting up my own server.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-04-18 05:19 UTC)

<p>The public demo server does not support this feature yet. We tried to update the Clara server software, but the new version was not stable with the current GPU. There is a shortage of GPUs that are strong enough to serve many requests in a shared server and has reasonable cost, so we are not sure when the update will happen. I would recommend to not wait for us but set up your own server.</p>

---

## Post #3 by @Wahnfried (2021-04-18 10:40 UTC)

<p>Dear Andras,</p>
<p>thanks for your answer! Unfortunately the other models are not quite what I’m looking for (I have to do a ton of eyeball segmentations and due to the contrast of my dataset the local threshold approach does not work) so I’m hoping to get a little help from Clara <img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue.png?v=9" title=":stuck_out_tongue:" class="emoji" alt=":stuck_out_tongue:"> I will try to configure a server.</p>
<p>Anyways, it is awesome that 3D slicer offers such a server for free! I hope to deliver a training model as soon as I’m done with the segmentations.</p>

---

## Post #4 by @bagginstyrone (2021-04-19 06:07 UTC)

<p><a class="mention" href="/u/wahnfried">@Wahnfried</a>  I was facing same problem then i saw your post thanks for sharing this.</p>

---

## Post #5 by @Fernando (2021-04-19 13:21 UTC)

<p>Pinging <a class="mention" href="/u/diazandr3s">@diazandr3s</a> in case he can offer some help/insight in the future.</p>

---

## Post #6 by @diazandr3s (2021-04-19 17:45 UTC)

<p>This is an interesting conversation. Thanks <a class="mention" href="/u/fernando">@Fernando</a> for the tag.<br>
<a class="mention" href="/u/wahnfried">@Wahnfried</a> which image modality are you using?<br>
We’re currently working on a new MONAI tool easy to install and use in 3D Slicer. In addition to DeepGrow 2D and 3D, it’ll have other capabilities for easy medical image annotation.<br>
Please stay tuned with the MONAI (<a href="https://monai.io/" rel="noopener nofollow ugc">https://monai.io/</a>) updates.</p>

---

## Post #7 by @Wahnfried (2021-04-19 17:58 UTC)

<p>Hi!<br>
The dataset consists of CT images.<br>
The MONAI project looks very promising, I’m looking forward to it being implemented!</p>

---

## Post #8 by @bagginstyrone (2021-04-22 10:02 UTC)

<p>Thanks for doing this hospitality. <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"> <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---

## Post #9 by @lassoan (2021-04-22 12:50 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="6" data-topic="17152">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>We’re currently working on a new MONAI tool easy to install and use in 3D Slicer.</p>
</blockquote>
</aside>
<p>This sounds awesome. There would be so many synergies between monai and Slicer, integration possibilities via the Segment Editor, Jupyter notebooks, etc. It is great to hear that somebody is working on this. Let us know if we can help with anything.</p>

---

## Post #10 by @diazandr3s (2021-06-01 20:29 UTC)

<p>Hi <a class="mention" href="/u/bagginstyrone">@bagginstyrone</a> ,</p>
<p>Just wanted to make sure you know the <a href="https://github.com/Project-MONAI/MONAILabel" rel="noopener nofollow ugc">MONAILabel</a> repo is public now. It is still under development, but I think it is in good shape to test it on your project.</p>

---
