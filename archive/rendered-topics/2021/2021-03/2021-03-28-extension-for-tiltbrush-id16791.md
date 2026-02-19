---
topic_id: 16791
title: "Extension For Tiltbrush"
date: 2021-03-28
url: https://discourse.slicer.org/t/16791
---

# Extension for TiltBrush

**Topic ID**: 16791
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/extension-for-tiltbrush/16791

---

## Post #1 by @smallvalthoss (2021-03-28 01:32 UTC)

<p>Hello, I’m thinking of doing an extension that incorporates google’s tilt brush into Slicer. Has anyone done anything similar? Or thought of it?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-03-28 14:46 UTC)

<p>Slicer can already display the scene and and interact with the nodes in virtual reality. It would be probably much easier to enable the Segment Editor paint tool work in virtual reality than integrating a completely new virtual reality framework.</p>
<p>That said, you probably don’t want to segment by free painting in 3D. Painting in 2D is already tedious and slow, and in 3D it would be much worse. However, a smoothing brush, or marker brush (to not paint new objects but mark suspicious regions for cleanup), or scissors could work well in virtual reality.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #3 by @cpinter (2021-03-30 09:09 UTC)

<p>Yes we have been planning to integrate Segment Editor into SlicerVR for at least two years now (wow). The biggest obstacle currently is using SlicerVR with VTK9, which is far from trivial due to the major change in the way VTK9 handles external modules. Once that is solved, we need to do some work to be able to use a virtual user interface panel in VR, then integrating Segment Editor will be relatively easy (there are parts already done, but need to hammer out a few details).</p>
<p>Personally I am quite optimistic that we’ll have it done in a few months. It depends on two important things, however:</p>
<ol>
<li>Sorting out the build issue against VTK9. Maybe <a class="mention" href="/u/jcfr">@jcfr</a> can give an update as we have been in contact about this regularly, but not recently.</li>
<li>The decision on a grant proposal in which the user interface panel is involved. We are supposed to hear about it “today, tomorrow, or early next week”.</li>
</ol>
<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a> in that using a VR paintbrush is probably not a good idea to do segmentation from scratch because it is very hard to see the contours/borders even with a high quality volume rendering. Also agree that smoothing brush and touch-ups will be great. However, my suspicion is that we will only be able to assess the real advantages and best uses once we are actually able to try it. It will be quite a fun research and a good paper!</p>

---

## Post #4 by @smallvalthoss (2021-04-13 20:44 UTC)

<p>I was thinking more of an annotation tool paint brush. So that you can paint inside the VR module for slicer. More of an artistic tool than a medical one. Any thoughts?</p>

---

## Post #5 by @lassoan (2021-04-14 04:02 UTC)

<p>Slicer’s main focus is medical applications. If you are just looking for a virtual reality platform for artistic/entertainment purposes then probably gaming engines, such as Unity or Unreal will work better.</p>

---

## Post #6 by @smallvalthoss (2021-04-16 19:16 UTC)

<p>Hey! Thanks for the reply. I understand slicers main focus. My boss is wondering if this is possible. I am willing to put in the time to create an extension that does this. I am simply wondering if it is possible and hoping for a little direction.</p>

---

## Post #7 by @lassoan (2021-04-16 21:50 UTC)

<p>It is not easy to give directions if the overall goal is not clear, but probably the big decision you need to make early on is if you want to represent content as image volume or polygonal mesh. Boolean operations (add/subtract) are trivial in an image volume but volume rendering is computationally more demanding and less rendering effects are available (lighting, physically-based rendering, special render passes, etc.).</p>

---

## Post #8 by @smallvalthoss (2021-04-16 22:53 UTC)

<p>I would probably opt for using polygonal mesh then. I suppose a simple explanation would be this, I want to:</p>
<ul>
<li>Be able to create a paint like substance at the head of one of the controllers</li>
<li>Have those substances be modifiable using in VR UI. I believe you answered a question about getting 2D actors to work on a given plane for better rendering.</li>
</ul>
<p>Does this help with the goal? Tiltbrush has their code available here: <a href="https://github.com/googlevr/tilt-brush" class="inline-onebox" rel="noopener nofollow ugc">GitHub - googlevr/tilt-brush</a><br>
I am wondering how useful this code would be to use in slicer? Using it as a basis to create something similar in slicer.</p>

---

## Post #9 by @lassoan (2021-04-17 00:55 UTC)

<aside class="quote no-group" data-username="smallvalthoss" data-post="8" data-topic="16791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/848f3c/48.png" class="avatar"> smallvalthoss:</div>
<blockquote>
<p>Does this help with the goal?</p>
</blockquote>
</aside>
<p>It is still nto clear what the goal is. Why do you want to do artistic drawing in Slicer? What you would like to achieve as an end goal? What problem you would like to solve?</p>
<aside class="quote no-group" data-username="smallvalthoss" data-post="8" data-topic="16791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/848f3c/48.png" class="avatar"> smallvalthoss:</div>
<blockquote>
<p>I am wondering how useful this code would be to use in slicer?</p>
</blockquote>
</aside>
<p>Since Slicer uses VTK as rendering engine, which has very little in common with Unity, probably it would be hard to reuse anything directly, but you could learn a lot from studying the tilt-brush source code.</p>

---

## Post #10 by @smallvalthoss (2021-04-22 21:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="16791">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is still nto clear what the goal is. Why do you want to do artistic drawing in Slicer? What you would like to achieve as an end goal? What problem you would like to solve?</p>
</blockquote>
</aside>
<p>You’re absolutely right, we are wanting to be able to use 3D DICOM data with tiltbrush, but I might just be able to use tilbrush and modify it to load data into it as a sort of canvas. Thank you.</p>

---

## Post #11 by @lassoan (2021-04-22 21:54 UTC)

<p>You can certainly load DICOM data into Slicer, segment it, and export it as a surface mesh, which TiltBrush should be able to load.</p>

---
