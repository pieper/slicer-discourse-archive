---
topic_id: 20067
title: "Erosion Model When Contacted With Another Model"
date: 2021-10-08
url: https://discourse.slicer.org/t/20067
---

# Erosion model, when contacted with another model

**Topic ID**: 20067
**Date**: 2021-10-08
**URL**: https://discourse.slicer.org/t/erosion-model-when-contacted-with-another-model/20067

---

## Post #1 by @xianger-qi (2021-10-08 08:40 UTC)

<p>In the scene, there are a probe model, and femur model . I control the probe to grind femur, I want to erode the femur gradually when the probe model contact the femur model. The effect just like below.<br>
how can i implement ? Thanks for your reading!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5ff9e4dad9460287ed9db94e24b946e4541dad3a.gif" alt="lsmCutting" data-base62-sha1="dH2KOnFJVCggEXBZvdQTYGIWkUG" width="690" height="386" class="animated"></p>

---

## Post #2 by @chir.set (2021-10-08 09:16 UTC)

<p>While not really helpful to your request,  it seems legitimate to question :</p>
<p>Was it or is it Slicer’s purpose to animate models ?</p>
<p>Blender comes to mind easily for this kind of highly specialized 3D animation tasks. One should perhaps master this huge beast with models created in Slicer rather.</p>
<p>Regards.</p>

---

## Post #3 by @xianger-qi (2021-10-08 09:42 UTC)

<p>Maybe I talk about models interaction such as collision, intersection, difference and so on. Thanks a lot!</p>

---

## Post #4 by @pieper (2021-10-08 14:12 UTC)

<p>You can implement that kind of operation on surface models (meshes) but the operations can be time consuming and unstable depending on the resolution and other mesh properties (search for vtkPolyData booleans for details).  Better would be to operate on a volume and render with volume rendering.  Have look at the masking effects in the segment editor and at SlicerPrism for real time for options.  What method to choose depends on your exact needs and data.</p>

---

## Post #5 by @lassoan (2021-10-08 17:30 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="20067">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Was it or is it Slicer’s purpose to animate models ?</p>
</blockquote>
</aside>
<p>Note that this is not animation, but real-time surgical guidance (or surgical simulation). A very important use of Slicer is connecting it to surgical guidance systems and display position of tools and anatomy in real-time.</p>
<p>I agree with <a class="mention" href="/u/pieper">@pieper</a> that if performance and robustness is the goal then a labelmap representation is the most suitable. You can see from the staircase artifacts in the animated gif above that an implicit surface representation is used (i.e., a surface generated from an internal labelmap representation), probably on a partitioned model (you don’t regenerate the entire femur, only the one or few small modified pieces). You can do this in Slicer, but since we have good support for volume rendering, it is probably much simpler to just use direct volume rendering.</p>
<p>Similar questions has been discussed at the forum before, some people ended up with using the Segment Editor’s paint tool, while others ended up with volume rendering.</p>

---

## Post #6 by @slicer365 (2021-10-08 23:00 UTC)

<p>Auto Boolean subtraction may be helpful.</p>
<p>But there is no Automatic Option in this module<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d243bb8499705a676806500ec20d395be93d4a9b.png" alt="image" data-base62-sha1="u05nRTIGSSriS8qurD7RJacHtGj" width="396" height="361"></p>

---

## Post #7 by @xianger-qi (2021-10-09 01:27 UTC)

<p>boolean operation will consume much time</p>

---

## Post #8 by @xianger-qi (2021-10-09 08:56 UTC)

<p>what i want effect that is the robot arm control probe model to grind the femur bone model, meanwhile the bone disappear gradually. both the probe model and bone model are vtkpolydata.</p>

---

## Post #9 by @lassoan (2021-10-09 14:51 UTC)

<p>Boolean mesh operations can be very fast if the mesh is partitioned, but they are inherently unstable. Advantage of representing structure as labelmap (and displaying using isosurface or volume rendering) is that it is very stable and predictable.</p>
<p>This question had been discussed a couple of times on this forum, please search for it and copy here links to the topics you have found for future reference. If you don’t get answers to your questions from those topics then you can ask here.</p>

---
