# Edit Segmentation Locally

**Topic ID**: 35154
**Date**: 2024-03-28
**URL**: https://discourse.slicer.org/t/edit-segmentation-locally/35154

---

## Post #1 by @yaraabdelazim (2024-03-28 15:09 UTC)

<p>Hello,<br>
I have recently developped a module that segments an MRI based on edge/contour detection. However, some of the time, those contours aren’t “perfect”. For instance, sometimes they’re not closed. Other times, they’re too small or too large so I’m looking for a way to be able to edit them locally. For example, I would like to develop a tool that would allow me to drag the contour to stretch it or compress it. Or maybe a tool where I would mark a point in the image and the contour would go to it. However, I don’t really know where to begin to develop such a tool. I’ve tried looking into markup points but I don’t see how I can use them in this case. Does anyone have any ideas on how to proceed from here?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2024-03-28 16:15 UTC)

<p>You can use markup curves.</p>
<aside class="quote no-group" data-username="yaraabdelazim" data-post="1" data-topic="35154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yaraabdelazim/48/69460_2.png" class="avatar"> yaraabdelazim:</div>
<blockquote>
<p>I have recently developped a module that segments an MRI based on edge/contour detection</p>
</blockquote>
</aside>
<p>Note that neural networks such as nn-UNet and MONAI Auto3DSeg are so successful in image segmentation tasks that they make most previous approaches completely irrelevant. Instead of trying to fix some imperfect contours, I would recommend to consider using neural networks for segmentation.</p>
<p>What do you segment on what kind of images? We may be able to point to pre-trained models that can do the task already.</p>

---

## Post #3 by @yaraabdelazim (2024-03-28 16:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use markup curves.</p>
</blockquote>
</aside>
<p>How would I use markup curves to edit the segmentation?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="35154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you segment on what kind of images? We may be able to point to pre-trained models that can do the task already.</p>
</blockquote>
</aside>
<p>I am working with MRI images of the hepatobiliary system and I am segmenting the bile ducts. Here’s an example on one of the slices:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd073bd0549db52fe6631f3caa3f6dd2b19b138.png" alt="image" data-base62-sha1="kexVEyd8MX4vR57JOrcb2Jhu3b2" width="608" height="302"></p>

---

## Post #4 by @lassoan (2024-03-28 16:45 UTC)

<p>I haven’t tried any models for bile duct segmentation, but there are lots of models out there. You can simply google for <code>bile duct segmentation model</code> maybe also add <code>github</code> to find those that are openly available. They are most likely work significantly better than any contour based methods.</p>
<p>If you want to edit segmented bile ducts (provided by either AI models or some classic approaches), you can post-process the images a bit (e.g., Smoothing effect in Segment Editor) and then use VMTK extension to reconstruct a centerline.</p>

---
