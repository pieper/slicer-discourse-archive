---
topic_id: 5019
title: "Facial Bones Segmentation"
date: 2018-12-09
url: https://discourse.slicer.org/t/5019
---

# Facial bones segmentation

**Topic ID**: 5019
**Date**: 2018-12-09
**URL**: https://discourse.slicer.org/t/facial-bones-segmentation/5019

---

## Post #1 by @alexk (2018-12-09 04:06 UTC)

<p>Operating system: Mac<br>
Slicer version: 4,8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,<br>
I would like to do an anatomical work on the facial bones.<br>
For that I would like to segment all the bones and to be able to isolate them separately.<br>
I saw the 3F tutorial to make a segmentation with ITKSnap.<br>
Is it possible to do otherwise?</p>
<p>Where can I find how to smooth 3D volumes ?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-12-09 05:31 UTC)

<p>You should be able to segment and separate bones very well using Segment Editor module in latest nightly version of Slicer (4.8 version that you are using is more than a year old, we have made huge improvements since then). See for example this tutorial on segmentation and separation of fused bones:</p>
<div class="lazyYT" data-youtube-id="8Nbi1Co2rhY" data-youtube-title="Femur segmentation using masked region growing in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>You can also separate bone parts using Scissors effect, as shown in the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/" rel="nofollow noopener">craniotomy segmentation recipe</a>.</p>
<p>You can find more <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">segmentation tutorials here on the Slicer wiki</a> and we are happy to help with any specific questions. Post general questions about segmentation to “Support” category.</p>

---
