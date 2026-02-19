---
topic_id: 37629
title: "Transformations And Reference Point"
date: 2024-07-31
url: https://discourse.slicer.org/t/37629
---

# Transformations and reference point

**Topic ID**: 37629
**Date**: 2024-07-31
**URL**: https://discourse.slicer.org/t/transformations-and-reference-point/37629

---

## Post #1 by @mayaambar (2024-07-31 07:24 UTC)

<p>Hello<br>
Im working with 3d slicer and aurora sensor via plus.<br>
Im trying to understand if it is possible to get the information from the sensor in reference to a point in my model, meaning to determine the (0 0 0) point in a point that I choose. I cant seem to find how to do it and Ill realy appericiate help.</p>
<p>also I’m trying to understand if I need to do pivot caliberation. Im working with the needle model and I dont understand how to define a needle tip</p>
<p>Thank you so much<br>
have a nice day<br>
Maya</p>

---

## Post #2 by @ungi (2024-08-04 01:44 UTC)

<p>Hi, these are tutorials made with an earlier version of Slicer, but they are still very informative for projects that use position trackers:<br>
<a href="https://1drv.ms/f/s!AhiABcbe1DBylnlkJEgmTsI1WF8P?e=zijasb" class="onebox" target="_blank" rel="noopener nofollow ugc">https://1drv.ms/f/s!AhiABcbe1DBylnlkJEgmTsI1WF8P?e=zijasb</a></p>
<p>To interface with the Aurora tracker, use the PLUS toolkit. A PLUS server can stream the tracking data to 3D Slicer via OpenIGTLink. You will find tool calibration methods in the tutorial slides, including pivot calibration for stylus.</p>
<p>I hope this helps.</p>

---

## Post #3 by @lassoan (2024-08-04 04:23 UTC)

<aside class="quote no-group" data-username="mayaambar" data-post="1" data-topic="37629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mayaambar/48/76746_2.png" class="avatar"> mayaambar:</div>
<blockquote>
<p>Im trying to understand if it is possible to get the information from the sensor in reference to a point in my model, meaning to determine the (0 0 0) point in a point that I choose.</p>
</blockquote>
</aside>
<p>This is called “patient registration” and typically done using landmark registration. The (0,0,0) point in the patient coordinate system is usually not physically touchable (because the origin is usually in the center of the body part or region of interest) and in general your also want to specify not just the origin but directions as well, we typically choose 4-6 points in the patient model and touch them physically with the pointer tip. Step-by-step instructions are in the U12 tutorial.</p>

---

## Post #4 by @mayaambar (2024-11-27 09:59 UTC)

<p>ok thank you very much for your answer… im trying for weeks to do registration to a heart model… and its never seems to be accurate enough.<br>
here is the process in which Im doing the registration:</p>
<ol>
<li>Im making a pivot and spin caliberation, usually Im not able to get a RMS smaller than 1, I apply the transformation to the needle</li>
<li>I move the needle to a specific points on the model or making a route with the sensor on a specific vein then those point I collected is a point list called NP1</li>
<li>then im making a new point list called LA(left artium) and put the point on the same locations that the needle was on the model</li>
<li>Im using registration=&gt; fiducial registration to make a transformation and choosing a linear transformation.</li>
<li>I apply the linear transformation to the needle…</li>
</ol>
<p>after this the needle is closed to where it suppost to be but there are some error- for instance - sometimes it goes out of the model when it is still suppost to be in the model<br>
our model is elastic so we think this may be an issue - the model is moving sometimes - we are thinking of printing a harden model.<br>
before we do that- is the process I describe seems ok? how can I improve it?</p>
<p>thank you for reading this and for all your help<br>
Maya</p>

---
