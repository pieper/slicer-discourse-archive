---
topic_id: 1490
title: "Issues With Generating A Model From Ultrasound Quasi Paralle"
date: 2017-11-19
url: https://discourse.slicer.org/t/1490
---

# Issues with generating a model from ultrasound quasi-parallel slices

**Topic ID**: 1490
**Date**: 2017-11-19
**URL**: https://discourse.slicer.org/t/issues-with-generating-a-model-from-ultrasound-quasi-parallel-slices/1490

---

## Post #1 by @thefcpk (2017-11-19 16:06 UTC)

<p>Hello all,</p>
<p>Apologies if this something answered in the past, I have been digging old forum threads and scratching my head for quite some time now.<br>
I am currently trying to render a 3D surface from a series of(unfortunately) relatively low resolution deep ultrasound images.<br>
I am currently able to:</p>
<ul>
<li>import as a volume the image series, setting spacing relatively correctly</li>
<li>go into volume rendering, display the volume, crop it properly</li>
</ul>
<p>A side issue at this point is that with the normal “composite with shading” technique, all I see is what appears to be a completly opaque volume, regardless of what volume properties I set. However going to “maximum intensity projection” there does allow me to see in space the elements of the volume(though in a particularly fuzzy way). Is this something expected?</p>
<p>I then thought of using modelmaker/greyscale model maker, but both of these will not let me choose any volume in “input volume”.</p>
<p>Thoughts on both questions?</p>
<p>Thanks,</p>
<p>-fcpk</p>

---

## Post #2 by @lassoan (2017-11-19 19:54 UTC)

<p>Ultrasound images of real tissues are usually so noisy that 3D visualization requires segmentation. The only exception is when you image fluid-filled cavities (such as cardiac images) or phantom images.</p>
<p>See for example live 3D ultrasound volume reconstruction and visualization of spine phantom in Slicer using SlicerIGT extension (<a href="http://www.slicerigt.org">www.slicerigt.org</a>):</p>
<div class="lazyYT" data-youtube-id="lfZeXabDjMg" data-youtube-title="Live ultrasound volume reconstruction in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Note that SlicerIGT provides real-time tracked 2D ultrasound display in Slicer and can reconstruct volumes from arbitrarily oriented and spaced images.</p>

---

## Post #3 by @lassoan (2017-11-19 19:56 UTC)

<p>If you tell us more about your application (what anatomy you would like to visualize, for what purpose) then we can advise how to implement it in Slicer.</p>

---

## Post #4 by @thefcpk (2017-11-19 20:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1490">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that SlicerIGT provides real-time tracked 2D ultrasound display in Slicer and can reconstruct volumes from arbitrarily oriented and spaced images.</p>
</blockquote>
</aside>
<p>Thanks for the answer!<br>
I had been looking at SlicerIGT but as I do not have tracking equipment and only access to recorded imagery, this makes it more difficult. In this case this is a liquid filled cavity(intra-uterine trans abdominal scans during early pregnancy). The purpose is to create an understandable surface from a convex probe scan that was done from a single point with a constant angle motion. As this is trans-adominal but with “lower” grade (older generation) hardware, there is no tracking and only the ability to acquire image sequences.</p>

---

## Post #5 by @lassoan (2017-11-19 21:35 UTC)

<p>Fetus in uterus should be possible to visualize without segmentation.</p>
<p>For $3000 you can get a good quality optical tracker (Optitrack Duo), but if you don’t want to invest that much then you can also use an orientation sensor (PhidgetSpatial, $150; provides orientation with sub-degree accuracy), or just attach a 2D barcode on your probe and track it using a webcam:</p>
<div class="lazyYT" data-youtube-id="MOqh6wgOOYs" data-youtube-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>All these options are supported by SlicerIGT/Plus, no programming is needed.</p>

---

## Post #6 by @thefcpk (2017-11-20 11:57 UTC)

<p>Thank you very much for the detailed information. I will be looking into acquiring one of these trackers, the PhidgetSpatial actually does look like it would bring quite decent accuracy, and proper SlicerIGT support.</p>
<p>Pending acquiring and testing this hardware, is there any workflows for doing grayscale image volume-&gt;point cloud-&gt;surface (possibly marching cubes, but anything works)? The grayscale volume does currently look like it has decent enough spatial data, but I could be wrong.</p>

---

## Post #7 by @lassoan (2017-11-20 13:52 UTC)

<p>Model generation from grayscale volume: switch to Segment editor module, create initial segmentation with <code>Threshold</code> effect, and follow up with <code>Islands</code> effect to remove speckle and <code>Smoothing</code> effect to reduce noise. If in <code>Threshold</code> effect you cannot find a threshold value that gives decent results, then paint a few strokes in the fluid with one segment, and paint a few strokes in the fetus with another segment using <code>Paint</code> effect; then use <code>Grow from seeds</code> to create a complete segmentation.</p>

---

## Post #8 by @lassoan (2019-06-19 16:43 UTC)

<p>A post was split to a new topic: <a href="/t/ultrasound-slice-is-not-aligned-with-reconstructed-volume/7247">Ultrasound slice is not aligned with reconstructed volume</a></p>

---
