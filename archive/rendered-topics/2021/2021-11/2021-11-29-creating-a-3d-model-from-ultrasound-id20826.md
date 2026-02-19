---
topic_id: 20826
title: "Creating A 3D Model From Ultrasound"
date: 2021-11-29
url: https://discourse.slicer.org/t/20826
---

# Creating a 3D model from Ultrasound

**Topic ID**: 20826
**Date**: 2021-11-29
**URL**: https://discourse.slicer.org/t/creating-a-3d-model-from-ultrasound/20826

---

## Post #1 by @Anastasiia.vbel (2021-11-29 02:52 UTC)

<p>Hi all,</p>
<p>I am a Masters student currently working on a project that involves converting an ultrasound image of a knee into a 3D model (.stl or a .STEP file).<br>
I was directed towards 3D slicer to do this, but I am a bit lost. Is there a certain number of images I need to collect from the US to create a 3D model? Can I use a regular hospital US for this, or do I need specialised equipment?</p>
<p>Any advice on this would be very helpful! Thank you.</p>

---

## Post #2 by @lassoan (2021-11-30 00:02 UTC)

<p>We have been using Slicer/SlicerIGT/SlicerAIGT for 3D reconstruction from bone surface using tracked ultrasound. Here is a demo/tutorial video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="2vXeJxYFou4" data-video-title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=2vXeJxYFou4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/2vXeJxYFou4/maxresdefault.jpg" title="Real-time 3D ultrasound reconstruction using 3D Slicer + SlicerIGT" width="" height="">
  </a>
</div>

<p>The setup, calibration, and the bone surface extraction from ultrasound are not trivial, but there are a number of additional videos in the same channel and there are <a href="http://www.slicerigt.org/wp/user-tutorial/">tutorials at SlicerIGT website</a>, and you can also ask specific questions here.</p>
<aside class="quote no-group" data-username="Anastasiia.vbel" data-post="1" data-topic="20826">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3e96dc/48.png" class="avatar"> Anastasiia.vbel:</div>
<blockquote>
<p>Is there a certain number of images I need to collect from the US to create a 3D model?</p>
</blockquote>
</aside>
<p>There is no minimum number of frames. There is a practical speed limit on of how fast you can move the transducer when scanning a patient, so the longer you scan the larger area you can cover. As shown in the demo videos, you can continuously acquire images, extract the bone surface using a neural network, and insert the bone-enhanced images into a volume.</p>
<aside class="quote no-group" data-username="Anastasiia.vbel" data-post="1" data-topic="20826">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3e96dc/48.png" class="avatar"> Anastasiia.vbel:</div>
<blockquote>
<p>Can I use a regular hospital US for this, or do I need specialised equipment?</p>
</blockquote>
</aside>
<p>Yes, you can use the ultrasound system that is used already by the clinicians. However, for testing, it often make sense to get an inexpensive ultrasound (such as a Telemed micrUS for about $2500), so that you can get familiar with the calibration process, do phantom experiments, etc. without keep asking for accessing a clinically used 50-100x more expensive ultrasound.</p>
<p>You need to attach a position tracker (for example, OptiTrack Duo, about $3000) to the transducer so that you know where each frame is acquired. For small regions, specific bone shapes, etc. you might be able to recover the image slice pose just from the image content, without an optical tracker, but it would make the volume reconstruction a computationally much harder task. Therefore, If your goal is to set up a 3D US acquisition system as soon as possible then I would recommend using an optical tracker.</p>

---
