---
topic_id: 19364
title: "Segment Editor On Large Template"
date: 2021-08-26
url: https://discourse.slicer.org/t/19364
---

# Segment editor on large template

**Topic ID**: 19364
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/segment-editor-on-large-template/19364

---

## Post #1 by @Ge_Tang (2021-08-26 10:00 UTC)

<p>Hello,</p>
<p>I have problems with running 3D slicer “segment editor” module on a huge template (around 5GB). Each time I select the segment editor, the computer power went off immediately. My computer has 128 GB RAM, I don’t think it is a memory issue, instead, it is a computer power issue.</p>
<p>I created this template by using the “resample scalar volume” module,<br>
(spacing : 0.2, 0.2, 0.2, interpolation method: linear) on a 1mm 46 MB template.</p>
<p>Is there a way for me to use the segment editor on this huge template?</p>
<p>Are there any other solutions to create a high-resolution template with a smaller file size?</p>
<p>Thank you so much!</p>
<p>Ge</p>

---

## Post #2 by @lassoan (2021-08-27 01:34 UTC)

<p>It seems that your computer has a hardware issue: the power supply is not strong enough to support an overworked CPU (along with GPU, etc.). You may try to lock the maximum CPU frequency in your BIOS/UEFI settings, but probably you need to buy a larger power supply.</p>
<p>The 5x oversampling an all axes (125x larger volume overall) is quite extreme. Why do you think it is necessary?</p>
<p>If you cannot fix your hardware then you can either reduce the oversampling or segment the image in smaller pieces.</p>

---

## Post #3 by @Ge_Tang (2021-08-27 21:26 UTC)

<p>Hi, Andras,</p>
<p>Thank you so much for the explanation. We want to have a high-resolution template for segmentation; thus, we can have better segments. Is this reasonable?</p>
<p>I cannot fix the hardware immediately, so I cropped the volume to an ROI and segmented on the cropped volume. The following question is whether the segmentations on the cropped volume can be directly transferred to the original volume? Because I have registered the individual images to the template. Could I register these segmentations via the same transformation? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Best,</p>
<p>Ge</p>

---

## Post #4 by @lassoan (2021-08-27 21:57 UTC)

<aside class="quote no-group" data-username="Ge_Tang" data-post="3" data-topic="19364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ge_tang/48/9935_2.png" class="avatar"> Ge_Tang:</div>
<blockquote>
<p>We want to have a high-resolution template for segmentation</p>
</blockquote>
</aside>
<p>Oversampling the image up to a factor if 2x might make sense, but 5x is extreme. You just don’t have that much more information in the image that it would worth oversampling that much.</p>
<aside class="quote no-group" data-username="Ge_Tang" data-post="3" data-topic="19364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ge_tang/48/9935_2.png" class="avatar"> Ge_Tang:</div>
<blockquote>
<p>whether the segmentations on the cropped volume can be directly transferred to the original volume</p>
</blockquote>
</aside>
<p>Cropping and resampling do not change the physical position of the volume or segmentation, so everything remains well aligned.</p>

---

## Post #5 by @Ge_Tang (2021-08-30 13:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="19364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and resampling do not change the physical position of the volume or segmentation, so everything remains well aligned.</p>
</blockquote>
</aside>
<p>Thank you so much! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
