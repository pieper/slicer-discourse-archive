---
topic_id: 32861
title: "How To Slice Through The Model Like When Browsing A Series O"
date: 2023-11-16
url: https://discourse.slicer.org/t/32861
---

# How to "slice through" the model, like when browsing a series of images?

**Topic ID**: 32861
**Date**: 2023-11-16
**URL**: https://discourse.slicer.org/t/how-to-slice-through-the-model-like-when-browsing-a-series-of-images/32861

---

## Post #1 by @Blizna (2023-11-16 15:59 UTC)

<p>Hello!<br>
I’m a new user, neuroscientist, and I’m just exploring this amazing tool. I viewed a few tutorials and I managed to import a DICOM series of a brain MRI into the tool, and get it shown in 3D. However - and this is likely silly - I cannot figure out how to “slice through” the model. I can see the full model of the head, reconstructed from the complete DICOM series, and I cannot find a way how to render e.g. only half of it.<br>
I’m sorry for my English, hope the question makes sense.</p>

---

## Post #2 by @Deep_Learning (2023-11-16 16:37 UTC)

<p>From your post, I believe that you are using volume rendering.<br>
Volume rendering is not based on a segmentation and it cannot be be viewed as you desire.</p>
<p>Segmentation though the segmentation module, can be displayed over the images and one can slice though the images.</p>

---

## Post #4 by @Blizna (2023-11-16 16:42 UTC)

<p>Ah, thank you. Could you please advise me what to do when I would like to simply browse the model “through”? In my case, I see the whole head of a patient, and would like to move through to get to the brainstem.</p>

---

## Post #5 by @pieper (2023-11-16 18:49 UTC)

<aside class="quote no-group" data-username="Blizna" data-post="4" data-topic="32861">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/f0a364/48.png" class="avatar"> Blizna:</div>
<blockquote>
<p>I see the whole head of a patient, and would like to move through to get to the brainstem.</p>
</blockquote>
</aside>
<p>Maybe if you show a picture illustrating what you are trying to achieve we could advise you.  I.e. from another software or from a publication.</p>

---

## Post #6 by @Blizna (2023-11-16 18:55 UTC)

<p>I mean, this should be fairly basic. Imagine you load a MRI study, so that the volume rendering shows a complete human head/face. But I obviously need to look inside, ideally step by step, as if viewing the 2D images.<br>
Or simply - how do I show just a half of the model, so that I see inside? I can see a human bust <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @pieper (2023-11-16 18:58 UTC)

<p>It sounds like you want to use the cropping feature of the volume rendering module.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html</a></p>

---

## Post #8 by @Blizna (2023-11-16 20:50 UTC)

<p>That was exactly it - THANK YOU!</p>

---
