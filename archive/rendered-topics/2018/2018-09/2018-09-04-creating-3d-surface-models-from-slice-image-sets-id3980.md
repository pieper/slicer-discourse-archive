---
topic_id: 3980
title: "Creating 3D Surface Models From Slice Image Sets"
date: 2018-09-04
url: https://discourse.slicer.org/t/3980
---

# Creating 3D surface models from slice image sets

**Topic ID**: 3980
**Date**: 2018-09-04
**URL**: https://discourse.slicer.org/t/creating-3d-surface-models-from-slice-image-sets/3980

---

## Post #1 by @johnqeniac (2018-09-04 02:37 UTC)

<p>Operating system: macOS Sierra 10.12.6<br>
Slicer version: 4.8.1 r26813<br>
Expected behavior: not sure<br>
Actual behavior: not sure</p>
<p>My motivation for trying Slicer is that I wanted to create a 3D surface model from a set of slice image generated from a CT scan.  But it looks like slicer can only display a pre-existing 3D surface model, but cannot generate one from a set of slices.<br>
First, is that the case?<br>
If so, do you know of open source software to generate the 3D surface model?<br>
If not (that is, if Slicer can actually generate a 3D surface model from a set of slice images) then how do I generate the 3D surface model in Slicer?</p>
<p>Thank you,</p>
<p>Greg Slater<br>
East Palo Alto, CA</p>

---

## Post #2 by @pieper (2018-09-04 12:56 UTC)

<p>Hi -</p>
<p>Have a look at these image segmentation tutorials:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #3 by @johnqeniac (2018-09-04 16:03 UTC)

<p>Thanks very much for your reply.</p>
<p>I will read the linked tutorials.</p>
<p>Thanks,</p>
<p>Greg Slater</p>

---

## Post #4 by @lassoan (2018-09-04 17:03 UTC)

<aside class="quote no-group" data-username="johnqeniac" data-post="1" data-topic="3980">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/8dc957/48.png" class="avatar"> johnqeniac:</div>
<blockquote>
<p>I wanted to create a 3D surface model from a set of slice image generated from a CT scan</p>
</blockquote>
</aside>
<p>Probably Slicer is one of the best open-source software for medical image segmentation (and in several aspects it is the most advanced one).</p>
<p>You’ll mainly use Segment editor module. Nightly version of Slicer has a bit more editor features and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">nightly documentation</a> has a few more tutorials than the latest stable version (4.8).</p>

---

## Post #5 by @lassoan (2021-03-07 16:53 UTC)

<p>A post was split to a new topic: <a href="/t/need-help-with-segmentation-of-image-stack/16415">Need help with segmentation of image stack</a></p>

---
