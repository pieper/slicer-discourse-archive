---
topic_id: 5194
title: "How To Get The Surface Of A Human Body From Dicom"
date: 2018-12-26
url: https://discourse.slicer.org/t/5194
---

# How to get the surface of a human body from DICOM

**Topic ID**: 5194
**Date**: 2018-12-26
**URL**: https://discourse.slicer.org/t/how-to-get-the-surface-of-a-human-body-from-dicom/5194

---

## Post #1 by @Moeka_Chan (2018-12-26 20:47 UTC)

<p>Hello, I am new to 3DSlicer.<br>
I watched the segmentation tutorials.<br>
However, I don’t know how to create the surface of a body…<br>
I painted the skin and space in the body and out of the body.<br>
I don’t get a good result…</p>

---

## Post #2 by @lassoan (2018-12-27 04:56 UTC)

<p>See this segmentation recipe for skin surface extraction: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>
<aside class="quote no-group" data-username="Moeka_Chan" data-post="1" data-topic="5194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moeka_chan/48/3388_2.png" class="avatar"> Moeka_Chan:</div>
<blockquote>
<p>I don’t get a good result</p>
</blockquote>
</aside>
<p>We would be happy to help but need more specific information. Describe what you do, what you expect to happen, and what happens instead. Also attach a screenshot if possible.</p>

---

## Post #3 by @Moeka_Chan (2018-12-27 05:20 UTC)

<p>Thanks. The link is helpful.<br>
It shows how to get a surface of a head.<br>
I want to get a surface of a human body.<br>
Hmm,but each click floor filling effect costs a few second…</p>

---

## Post #4 by @Moeka_Chan (2018-12-27 05:43 UTC)

<p>I use threshold effect and flood filling effect to solve my current problem.<br>
It looks much better.<br>
I have one more problem, is there any way to lower polygons?<br>
The generated mesh has too many vertices…</p>

---

## Post #5 by @lassoan (2018-12-27 05:46 UTC)

<p>You extract skin surface of a body part or the whole body the same way. You may need to adjust some parameters, such as neighborhood size.</p>
<aside class="quote no-group" data-username="Moeka_Chan" data-post="3" data-topic="5194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moeka_chan/48/3388_2.png" class="avatar"> Moeka_Chan:</div>
<blockquote>
<p>Hmm,but each click floor filling effect costs a few second…</p>
</blockquote>
</aside>
<p>That should be fine, as long as you only have a handful of air pockets to fill. If there are too many then it may be better to use Grow from seeds effect with two segments (“body” and “outside”). You can start with a few very bold strokes and make adjustments as needed.</p>
<aside class="quote no-group" data-username="Moeka_Chan" data-post="4" data-topic="5194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moeka_chan/48/3388_2.png" class="avatar"> Moeka_Chan:</div>
<blockquote>
<p>is there any way to lower polygons?</p>
</blockquote>
</aside>
<p>If you don’t need small details then you may resample the input volume before you start segmenting, using Crop volume module. If you just want to remove points from the generated surface mesh then you can decimate the closed surface representation as described in this post: <a href="https://discourse.slicer.org/t/size-of-stl-obj-files-too-many-triangles/5137/2" class="inline-onebox">Size of STL/OBJ files - too many triangles - #2 by cpinter</a>.</p>

---
