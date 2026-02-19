---
topic_id: 4932
title: "Transforming Segmentations And Images Together In Virtual Re"
date: 2018-12-03
url: https://discourse.slicer.org/t/4932
---

# Transforming segmentations and images together in virtual reality

**Topic ID**: 4932
**Date**: 2018-12-03
**URL**: https://discourse.slicer.org/t/transforming-segmentations-and-images-together-in-virtual-reality/4932

---

## Post #1 by @justdcinaus (2018-12-03 02:56 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.10.0<br>
Expected behavior: ‘grabbing’ a render in VR moves both the  render and the segmented section<br>
Actual behavior: Using the oculus joystick I can move both towards me, however when I then ‘grab’ the render the segmented section remains where it was.</p>
<p>Hi - I was hoping to show a foreign object highlighted in a volume render using overlapping renders (object breahed into lung).  I read a support topic saying to use a segment with the render, which worked extremely well, except that grabbing the rendered lung, left the segmented section behind.</p>
<p>Is there a method of getting around this?</p>
<p>Many thanks<br>
David</p>

---

## Post #2 by @lassoan (2018-12-03 03:10 UTC)

<p>Probably the easiest is to prevent objects from moving by making them “non-selectable” and <a href="https://github.com/KitwareMedical/SlicerVirtualReality#transform-entire-scene" rel="nofollow noopener">use two-handed gestures to move, rotate, scale the entire scene</a>.</p>
<p>See more details and advanced manipulation options (for example, define groups of objects that are moved together) described in <a href="https://github.com/KitwareMedical/SlicerVirtualReality" rel="nofollow noopener">SlicerVirtualReality documentation</a>.</p>
<p>By the way, avoid using “VR” acronym, because it may either mean “volume rendering” or “virtual reality” and it gets very confusing.</p>

---

## Post #3 by @justdcinaus (2018-12-04 01:42 UTC)

<p>Many thanks for the reply (And I’ll try to remember the VR tip!)</p>
<p>Your tip - and the link solved my problems perfectly.</p>
<p>regards</p>
<p>David</p>

---

## Post #4 by @sarvpriya1985 (2018-12-29 15:46 UTC)

<p>Hi,<br>
Based upon this discussion, I tried to move the 3d segment into virtual reality frame.<br>
My model was segmented by threshhold. I would like to clarify few things.</p>
<p>This is from virtual reality discussion" * Either left or right controller can be used to grab an object. Each controller can be used to grab an object and move independently."</p>
<ol>
<li>When its said that we can separate an object by moving the controller inside it, I was unable to separate the object. All my segments are individual. I have attached the screenshot here of my model. Can i separate individual colored segments by holding them and separate them.</li>
<li>How would I be able to slice volume with controller according to " * Make position of controllers available as transforms in the Slicer scene. These transforms can be used in custom modules to reslice volumes (using Volume Reslice Driver module in SlicerIGT extension) or transform any nodes in the scene".</li>
</ol>
<p>FYI: I have HP windows mixed reality headset.<br>
Thanks,<br>
Sarv</p>

---

## Post #5 by @lassoan (2018-12-29 17:05 UTC)

<aside class="quote no-group" data-username="sarvpriya1985" data-post="4" data-topic="4932">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarvpriya1985/48/4094_2.png" class="avatar"> sarvpriya1985:</div>
<blockquote>
<p>When its said that we can separate an object by moving the controller inside it, I was unable to separate the object. All my segments are individual. I have attached the screenshot here of my model. Can i separate individual colored segments by holding them and separate them.</p>
</blockquote>
</aside>
<p>A segmentation node is one object. To move segments independently, I would recommend to export segments to models (and hide the segmentation node). You can also split the segmentation to have one segment per segmentation mode and then you can move each segment separately. [quote=“sarvpriya1985, post:4, topic:4932”]<br>
How would I be able to slice volume with controller according to " * Make position of controllers available as transforms in the Slicer scene. These transforms can be used in custom modules to reslice volumes (using Volume Reslice Driver module in SlicerIGT extension) or transform any nodes in the scene".<br>
[/quote]</p>
<p>Follow the instructions that you have copied here. If you stuck at any point then let us know what you did, what you expected to happen, and what happened instead.</p>

---

## Post #6 by @sarvpriya1985 (2019-02-13 01:49 UTC)

<p>Hi Andras,<br>
I tried these methods but it happened in a different way.</p>
<p>I did export segmentation to models. But this is what happened when I try to grap one segment. It just extracted the entire model and left behind some external structures. I am not sure how this happened, but I was able to separate the extrernal structures but not the required model. Attached is the screenshot here.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/490661c9d7b0b74738b4be4526cd5ad31a4c1e8f.jpeg" data-download-href="/uploads/short-url/aq0wMgr1lG9gHUduQBSmUkS39Yr.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/490661c9d7b0b74738b4be4526cd5ad31a4c1e8f_2_690x359.jpeg" alt="Capture" data-base62-sha1="aq0wMgr1lG9gHUduQBSmUkS39Yr" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/490661c9d7b0b74738b4be4526cd5ad31a4c1e8f_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/490661c9d7b0b74738b4be4526cd5ad31a4c1e8f_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/490661c9d7b0b74738b4be4526cd5ad31a4c1e8f_2_1380x718.jpeg 2x" data-dominant-color="BBBDD8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1737×906 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(You can also split the segmentation to have one segment per segmentation mode and then you can move each segment separately): How to do this?</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #7 by @cpinter (2019-02-13 14:24 UTC)

<p>Please see my answer on your other thread: <a href="https://discourse.slicer.org/t/virtual-reality-controller-to-split-segments-labelling/5751" class="inline-onebox">Virtual reality controller to split segments/Labelling</a></p>

---
