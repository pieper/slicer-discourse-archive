---
topic_id: 34837
title: "Segment Registration And Measure Distance With Heat Map"
date: 2024-03-12
url: https://discourse.slicer.org/t/34837
---

# Segment registration and measure distance with heat map

**Topic ID**: 34837
**Date**: 2024-03-12
**URL**: https://discourse.slicer.org/t/segment-registration-and-measure-distance-with-heat-map/34837

---

## Post #1 by @sumerm (2024-03-12 01:26 UTC)

<p>Hello,</p>
<p>I have preoperative and postoperative skull CTs, i also have STL files. I am trying to create a heat map according to distance between 2 models/segments.</p>
<p>So which is the proper way to do it ?</p>
<p>I have uploaded STL files as segments, but i could not register or superimpose the models using some landmarks. Automated registration is not working because there are some changes in maxilla and also mandible.</p>
<p>Thanks for your help.</p>

---

## Post #2 by @muratmaga (2024-03-12 02:55 UTC)

<p>Are the STLs derived from the pre/post operative CTs, do they line up with them correctly?</p>
<p>if so, you should rigidly register the pre/post op CT scans using the Elastix or the General Registration module, and then use the resultant transform to line up STLs. Then you can calculate the distance between those two models.</p>

---

## Post #3 by @sumerm (2024-03-12 06:50 UTC)

<p>Thank you for your reply,</p>
<p>STLs are generated from CT’s, but the problem is i cannot align them according to landmarks. I tried to do it but couldn’t make it.</p>
<p>So the first question is, is it possible to superimpose those stls according to point based superimposition ? if yes, how ?</p>
<p>Second question is, I’ve imported STL’s as segments, if i could align those stls according to those points, how to create a heat map according to distance? In that way i could see which part is changed more.</p>
<p>Thank you !!</p>

---

## Post #4 by @sumerm (2024-03-12 06:56 UTC)

<p>To make it more clear, I am trying to create a heat map something like this;</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eedad5424adf7451753e3f9ba35663f510f38a64.jpeg" data-download-href="/uploads/short-url/y50u6DMnIGLyPjtWehxusk0jSHW.jpeg?dl=1" title="Ekran Resmi 2024-03-12 09.55.15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedad5424adf7451753e3f9ba35663f510f38a64_2_562x499.jpeg" alt="Ekran Resmi 2024-03-12 09.55.15" data-base62-sha1="y50u6DMnIGLyPjtWehxusk0jSHW" width="562" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedad5424adf7451753e3f9ba35663f510f38a64_2_562x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedad5424adf7451753e3f9ba35663f510f38a64_2_843x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eedad5424adf7451753e3f9ba35663f510f38a64_2_1124x998.jpeg 2x" data-dominant-color="0C0B5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Resmi 2024-03-12 09.55.15</span><span class="informations">1292×1148 49.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2024-03-12 15:47 UTC)

<aside class="quote no-group" data-username="sumerm" data-post="3" data-topic="34837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sumerm/48/69637_2.png" class="avatar"> sumerm:</div>
<blockquote>
<p>STLs are generated from CT’s, but the problem is i cannot align them according to landmarks. I tried to do it but couldn’t make it.</p>
<p>So the first question is, is it possible to superimpose those stls according to point based superimposition ? if yes, how ?</p>
</blockquote>
</aside>
<p>If you have CTs automated registrations with original images may work better than landmarks. If you just want to use landmarks, then the easiest tool for that is the 'Fiducial Landmark Wizard` in the SlicerIGT extension. You need to collect same number of landmarks from both of your objects (doesn’t matter if it is a 3D model or a volume, or something else), exactly in the same order.</p>
<p>Then choose to output a Rigid Transform, and apply that transform to the object you derived the source landmarks from. If you are not familiar with these modules, please take a look at the Slicer documentation at: <a href="https://slicer.readthedocs.io">https://slicer.readthedocs.io</a></p>

---

## Post #6 by @sumerm (2024-03-12 17:44 UTC)

<p>Thank you for your help, I will try this solution.</p>
<p>How about if i have CTs? how to register and post-process for heat maps ?</p>

---

## Post #7 by @muratmaga (2024-03-12 19:36 UTC)

<p>You can use Elastix or general brain registration modules to register them.</p>
<p>If you have the head STLs aligned correctly (using the output of registration), then you can use the Model 2 Model Distance module to create the distance heatmap.</p>

---
