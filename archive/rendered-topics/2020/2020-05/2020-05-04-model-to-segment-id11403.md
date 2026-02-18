# Model to segment

**Topic ID**: 11403
**Date**: 2020-05-04
**URL**: https://discourse.slicer.org/t/model-to-segment/11403

---

## Post #1 by @Melodicpinpon (2020-05-04 15:19 UTC)

<p>Hello,</p>
<p>I followed a topic about the way to import a model (.stl or .obj in my case) as a segment through the ‘Add data’ window of importation. The segmentation is well visible in my data and in the segments of this volume but although the visibility is toggled ‘on’ for the slices and the 3D view, nothing is visible. I clicked the ‘specify geometry’, selected the model/segmentation and set the spacing to 1 but do not a segment that I can see and edit.</p>
<p>Do you read something that sounds like a familiar mistake?</p>
<p>I also try some masking and logical operators techniques and I had understood that the label maps could not share a voxel, but that the segments could overlap. Therefore I am surprised to notice that every voxel used by one segment is automatically substracted from the other.</p>

---

## Post #3 by @cpinter (2020-05-04 15:43 UTC)

<p>A reference volume is not absolutely required. What you did with setting the geometry sounds fine. However, you only need this step if you want to use Segment Editor to edit the model or add other segments. But it sounds like you don’t have an image volume, in which case segment editing does not make much sense.</p>
<p>What I suspect is that you need to reset the view so that your segment is visible to the camera. Similarly to what was suggested in <a href="https://discourse.slicer.org/t/how-do-i-add-robot-arm-stl-into-a-scene/11395">this thread</a> very recently.</p>

---

## Post #4 by @muratmaga (2020-05-04 15:59 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a><br>
that’s definitely convenient and nice. I will delete my answer above…</p>

---

## Post #5 by @cpinter (2020-05-04 16:17 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> The ability to define volume geometry using a model or ROI is somewhat new. After choosing the node which defines the region, all you need to do is enter the desired spacing.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09fe75a0070b8a6e7897d8e81086b8eb8f14a2fe.png" alt="image" data-base62-sha1="1qptoB1rX3qUN8kzxA0oHwqhzaK" width="490" height="281"></p>

---

## Post #6 by @Melodicpinpon (2020-05-05 14:13 UTC)

<p>Thank you for your help!</p>

---
