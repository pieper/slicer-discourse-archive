---
topic_id: 19328
title: "How To Use Slicer To Simulate The Effect Of Blood Flow In Bl"
date: 2021-08-24
url: https://discourse.slicer.org/t/19328
---

# How to use slicer to simulate the effect of blood flow in blood vessels

**Topic ID**: 19328
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/how-to-use-slicer-to-simulate-the-effect-of-blood-flow-in-blood-vessels/19328

---

## Post #1 by @slicer365 (2021-08-24 00:44 UTC)

<p>Slicer 4.11<br>
win 64<br>
Hello, friends,</p>
<p>I used Slicer to create a blood vessel model, which contains arteries and veins.</p>
<p>I want to know how to add blood flow animation to the blood vessels.</p>
<p>Any suggestions will be helpful.</p>
<p>Thank you！</p>

---

## Post #2 by @lassoan (2021-08-25 03:57 UTC)

<p>There are many ways to simulate blood flow. What is your end goal? Creating simulated vascular X-ray or CT fluoroscopy sequences?</p>

---

## Post #3 by @slicer365 (2021-08-25 04:14 UTC)

<p>Simulated vascular X-ray ，like DSA ，is ok.</p>
<p>Sure,I just want to get the animation effect of this kind of blood flow to tell the patients that the blood flows like this in the blood vessels of the brain.</p>

---

## Post #4 by @lassoan (2021-08-25 04:42 UTC)

<p>A simple, closed-form solution for computing contrast agent concentration along a vessel in response to a contrast injection is given in <a href="https://ieeexplore.ieee.org/document/938242">Kump 2001</a>. I just copy here the end result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cca7baa7e45a2dcb161b450f6eb2347614858aa5.png" data-download-href="/uploads/short-url/tcsLeZ9mXBAHzOJ47Eou5nosxtr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cca7baa7e45a2dcb161b450f6eb2347614858aa5_2_507x500.png" alt="image" data-base62-sha1="tcsLeZ9mXBAHzOJ47Eou5nosxtr" width="507" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cca7baa7e45a2dcb161b450f6eb2347614858aa5_2_507x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cca7baa7e45a2dcb161b450f6eb2347614858aa5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cca7baa7e45a2dcb161b450f6eb2347614858aa5.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">530×522 46.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It is very easy to use this for DSA image simulation: <em><code>C(z,t)</code></em> gives you the concentration at <em><code>z</code></em> distance from the injection points at time <em><code>t</code></em>. The gray value of the image is <em><code>k*C(z,t)</code></em>. The authors determined the parameters from measurements on leg DSA images and got these values:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/779c3a79112fecb3cb2c99c8a6e70825fb945dfd.png" alt="image" data-base62-sha1="h47xhukBWFRYDJfYTc11CWFpo8B" width="526" height="154"></p>
<p>You can use these as starting points and manually tune them a bit for blood flow in the brain.</p>
<p>You can simulate contrast filling by painting spheres along the centerline. Position and radius comes from the centerline computed by VMTK, z distance can be easily computed by accumulating distances between points, and the fill value <em><code>k*C(z,t)</code></em> can be computed by the formula above.</p>
<p>You can generate DSA images from the volumes using volume rendering, using the CT X-ray preset, setting the 3D view background to black.</p>
<aside class="quote no-group" data-username="slicer365" data-post="3" data-topic="19328">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>Sure,I just want to get the animation effect of this kind of blood flow to tell the patients that the blood flows like this in the blood vessels of the brain.</p>
</blockquote>
</aside>
<p>For patient education, computing patient-specific blood flow may be too much effort. Why don’t you show the patient his real DSA image?</p>

---
