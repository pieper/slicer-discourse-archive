---
topic_id: 3754
title: "Segment Editor Connect Between Slices Issue"
date: 2018-08-13
url: https://discourse.slicer.org/t/3754
---

# Segment Editor - Connect between Slices Issue

**Topic ID**: 3754
**Date**: 2018-08-13
**URL**: https://discourse.slicer.org/t/segment-editor-connect-between-slices-issue/3754

---

## Post #1 by @Trident (2018-08-13 09:44 UTC)

<p>Operating system: Windows 10, 64 bit<br>
Slicer version: Nightly Build 4.9.0</p>
<p>Expected behavior:<br>
I’m trying to create 3D models of all the pelvic organs using the “Visible Human Database” which means im not actually using CT/MRI scans but having a body in full color. I create a model, outlining for example the Os ilium every few slices and after doing that a couple of times I press “Fill between Slices” in order to use the interpolation method to fill out the whole model.</p>
<p>Actual behavior:<br>
My issue now is that as the model gets bigger and bigger the “Fill between Slices” functionality starts to interpolate not only between two slices next to each other but also slices very far apart, thus distorting my model more and more the bigger it gets. Is there a way to tell Slicer to only interpolate between new slices that are next to each other? And to leave the rest of the model as it is?</p>
<p>Thank you very much in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Cheers, Adrian</p>

---

## Post #2 by @lassoan (2018-08-13 09:47 UTC)

<p>If you don’t want certain slices to be connected then draw separate segments on them.</p>
<p>You may also stop interpolation by segmenting two direct neighbor slices.</p>

---

## Post #3 by @Trident (2018-08-13 13:22 UTC)

<p>I do want all of them connected but only to the neighbouring slice. So for example I have 400 slices and on every 5th slice I will draw the outline of my model I will then have an outline on slice 0,5,10,15,20 etc.<br>
I want it to only fill in the slices between 0 and 5, 5 and 10, 10 and 15, 15 and 20 etc. but for some reason it starts to connect 0 with 20 aswell, is there a way to stop it from doing that?</p>

---

## Post #4 by @Trident (2018-08-13 18:51 UTC)

<p>Solved it! Thank you!!</p>
<p>I had to create a new segmentation for each model (i.e. one segmentation for bladder, one for uterus etc.)</p>
<p>Now I’m running into another problem though: I can only have 8 segmentations… Is there a way to create more?</p>

---

## Post #5 by @lassoan (2018-08-14 07:07 UTC)

<p>There is no limit on the number of segmentations. What indicated that there was a limit?</p>
<p>You don’t need to create multiple segmentations, it is enough to create a separate segment for each structure. Moreover, you can exclude segments from “Fill between slices” by simply hiding them (turning off their visibility in the segment list).</p>

---

## Post #6 by @Trident (2018-08-14 10:13 UTC)

<p>Thank you very much for your quick answers. You solved my problem!</p>

---
