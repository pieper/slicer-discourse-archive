---
topic_id: 15666
title: "Zspace Iao And Vr Extension"
date: 2021-01-26
url: https://discourse.slicer.org/t/15666
---

# Zspace IAO and VR extension

**Topic ID**: 15666
**Date**: 2021-01-26
**URL**: https://discourse.slicer.org/t/zspace-iao-and-vr-extension/15666

---

## Post #1 by @David_Yang (2021-01-26 01:50 UTC)

<p>Hey, I’m new using Slicer3D,I didn’t find any informations about Zspace monitor ( <a href="https://zspace.com/" rel="noopener nofollow ugc">https://zspace.com/</a> ) and slicer VR extension so hope someone who can clear me about it.<br>
So my problem : It seems we can “easily” display on a 3D view any 3D models,do some processing (ex:segmentation),with the VR extension ( <a href="https://blog.kitware.com/slicervirtualreality/" class="inline-onebox" rel="noopener nofollow ugc">Bringing Virtual Reality to 3D Slicer - Kitware Blog</a> ) but this require using a headset and controller.</p>
<p>What about to display it as a Hologram with this Zspace using this time a classical 3D glasses like in the first link, and be able to do the same thing as with the headset.</p>
<p>Also i wanted to know what is the extension/format of the model on the 3D view?<br>
Thank for your anwser.</p>

---

## Post #2 by @lassoan (2021-01-26 02:38 UTC)

<p>Slicer supports Looking glass (<a href="https://docs.lookingglassfactory.com/3DSlicer/">https://docs.lookingglassfactory.com/3DSlicer/</a>) screen, which does not require headset and tracking and works for any number of users.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="7-ROJ6awzqk" data-video-title="3D Slicer and Looking Glass Factory's Holographic Display" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=7-ROJ6awzqk" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/7-ROJ6awzqk/hqdefault.jpg" title="3D Slicer and Looking Glass Factory's Holographic Display" width="" height="">
  </a>
</div>

<p>Slicer can also be used with most virtual reality systems, which cost fraction of the price, more portable, and much more capable than a zSpace system (two 6-DOF controllers with rich interaction capability, immersive view, etc.).</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F_UBoE4FaoY" data-video-title="Pedicle screw insertion in virtual reality" data-video-start-time="18s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F_UBoE4FaoY&amp;t=18s" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F_UBoE4FaoY/maxresdefault.jpg" title="Pedicle screw insertion in virtual reality" width="" height="">
  </a>
</div>

<p>For convenient, high-accuracy segmentation, to be used for an extended period of time, a more traditional system, such as a digitizer tablet or Surface Studio is probably better suited.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="QQ9kFT8XhtA" data-video-title="3D Slicer on a Microsoft Surface Studio" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=QQ9kFT8XhtA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/QQ9kFT8XhtA/maxresdefault.jpg" title="3D Slicer on a Microsoft Surface Studio" width="" height="">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="zlrUFaP9q1w" data-video-title="Fast ultrasound segmentation for generating AI training data" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=zlrUFaP9q1w" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/zlrUFaP9q1w/maxresdefault.jpg" title="Fast ultrasound segmentation for generating AI training data" width="" height="">
  </a>
</div>

<p>There may be still some applications where zSpace performs better than its competitors, but it is not easy find them. Despite being around for so many years, zSpace still appears to be a very low-volume product (they don’t have a list price but you need to ask for a quote; there is very low traffic on their forum, etc.), have fundamental limitations (single user, need to wear glasses, single wired stylus as a controller, etc.), and integration with Slicer would be not be trivial (they don’t mention OpenXR in their developer documentation, so probably you would need to use their custom API instead of a standard interface), so as a Slicer developer I don’t find the system very attractive overall.</p>
<aside class="quote no-group" data-username="David_Yang" data-post="1" data-topic="15666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/david_yang/48/9035_2.png" class="avatar"> David_Yang:</div>
<blockquote>
<p>Also i wanted to know what is the extension/format of the model on the 3D view?</p>
</blockquote>
</aside>
<p>Slicer can read/write many file formats. See more details <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#supported-data-formats">here</a>.</p>

---

## Post #3 by @David_Yang (2021-01-26 19:50 UTC)

<p>Thank you Sir for your anwser I’ll investigate on it</p>

---
