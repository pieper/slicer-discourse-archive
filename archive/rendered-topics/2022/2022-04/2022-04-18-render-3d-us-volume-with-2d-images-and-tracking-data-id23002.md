---
topic_id: 23002
title: "Render 3D Us Volume With 2D Images And Tracking Data"
date: 2022-04-18
url: https://discourse.slicer.org/t/23002
---

# Render 3D US Volume with 2D images and tracking data

**Topic ID**: 23002
**Date**: 2022-04-18
**URL**: https://discourse.slicer.org/t/render-3d-us-volume-with-2d-images-and-tracking-data/23002

---

## Post #1 by @JJenkins (2022-04-18 17:20 UTC)

<p>Hello,<br>
I am looking to use Slicer to generate a 3D ultrasound volume from 2D images and tracking data. The goal is for the image acquisition to be done by hand, so the image spacing will not be regular or in one dimension.</p>
<p>The US images are processed and stored in RGBA format. The tracking information I have are the distance and orientation of the sensor from the tracking source.</p>
<p>I found this ticket which is very similar to what I am trying to do:</p><aside class="quote quote-modified" data-post="1" data-topic="19615">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/8e7dd6/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-position-data-tracking-for-images/19615">Import position data (tracking) for images</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everybody, 
I am Matthieu working on a 3D free-hand project involving ultrasound imaging and electromagnetic device.  I am interested to use 3D Slicer for volume visualization instead of Matlab. I am also thinking that the toolbox SlicerIGT can be the solution to generate a volume of my acquisition data without using Matlab however I do not know/did not find the way to do it. 
I am using a research scanner (Verasonics Vantage system) acquiring at a high frame rate (100 Hz) where we save all t…
  </blockquote>
</aside>

<p>The differences are that we are not using Matlab to stitch our 2D images together. Is there a way for Slicer to do this for us? I have looked into the NRRD file format and it does not support variable image spacing in multiple dimensions. There are also no real-time requirements</p>
<p>Operating system: Windows 10 x64<br>
Slicer version: 4.11</p>
<p>Thank you for your time</p>

---

## Post #2 by @lassoan (2022-04-18 21:42 UTC)

<blockquote>
<p>The differences are that we are not using Matlab to stitch our 2D images together. Is there a way for Slicer to do this for us?</p>
</blockquote>
<p>Absolutely. 3D volume reconstruction of freehand tracked 2D ultrasound is a core IGT feature, it is well tested and thoroughly optimized, has many compounding options, hole filling, etc. It works real-time on live data, or you can do it from pre-recorded data. Some optimizations are only implemented for single component (grayscale, not RGB/RGBA) images. See for example this demo/tutorial video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="l0BcW8c9CnI" data-video-title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" data-video-start-time="497" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI&amp;t=497" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/l0BcW8c9CnI/maxresdefault.jpg" title="Tracked ultrasound AI segmentation and 3D reconstruction tutorial" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="JJenkins" data-post="1" data-topic="23002">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png" class="avatar"> JJenkins:</div>
<blockquote>
<p>I have looked into the NRRD file format and it does not support variable image spacing in multiple dimensions.</p>
</blockquote>
</aside>
<p>We store image pose for each slice in custom fields in the nrrd header. See full specification <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">here</a>. See an example file <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/TestImages/NwirePhantomFreehand.igs.nrrd">here</a>.</p>

---
