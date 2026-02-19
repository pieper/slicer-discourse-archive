---
topic_id: 36217
title: "Model To Volume Registration Or Model To Model Landmark Regi"
date: 2024-05-16
url: https://discourse.slicer.org/t/36217
---

# Model to volume registration or model to model landmark registration

**Topic ID**: 36217
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/model-to-volume-registration-or-model-to-model-landmark-registration/36217

---

## Post #1 by @mohammed_alshakhas (2024-05-16 19:40 UTC)

<p>is it possible to do model-to-volume registration or model-to-model landmark registration?<br>
thanks</p>

---

## Post #2 by @muratmaga (2024-05-16 19:51 UTC)

<p>You can do all:</p>
<p>Model 2 Model options:<br>
* Model Registration (SlicerIGT Extension)<br>
* FastModelAlign (SlicerMorph Extension)</p>
<p>Landmark Registration</p>
<ul>
<li>Fiducial Registration Wizard (SlicerIGT Extension)</li>
</ul>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a> for more information.</p>

---

## Post #3 by @mohammed_alshakhas (2024-05-19 19:58 UTC)

<p>landmark registration is volume to volume only , is not it ?</p>

---

## Post #4 by @muratmaga (2024-05-19 21:19 UTC)

<p>It is a landmark based registration. You can put one set of lms on a volumr and the other one on a model.</p>

---

## Post #5 by @mohammed_alshakhas (2024-05-20 19:52 UTC)

<p>i tried the fiducial registration. i created point using the landmark tool on  CT. add them to the fixed point<br>
but nothing actually happened<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac780c6827772ce29cb62a4874236889e01a4f1.png" data-download-href="/uploads/short-url/jNHk6bDkYTtkP06QqEEuAP0bqWR.png?dl=1" title="Screenshot 2024-05-20 at 21.52.38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ac780c6827772ce29cb62a4874236889e01a4f1_2_690x453.png" alt="Screenshot 2024-05-20 at 21.52.38" data-base62-sha1="jNHk6bDkYTtkP06QqEEuAP0bqWR" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ac780c6827772ce29cb62a4874236889e01a4f1_2_690x453.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac780c6827772ce29cb62a4874236889e01a4f1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac780c6827772ce29cb62a4874236889e01a4f1.png 2x" data-dominant-color="2A2928"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-20 at 21.52.38</span><span class="informations">998×656 53.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2024-05-20 19:54 UTC)

<p>You probably need 3 points for it to work.  I’ll be there’s a message in the error log.</p>

---

## Post #7 by @mohammed_alshakhas (2024-05-20 20:00 UTC)

<p>I tried  3 points, no error message, just nothing happening. i guess I’m not doing it right . is there an order or something else needed?</p>

---

## Post #8 by @LeidyMoraV (2024-05-20 20:05 UTC)

<p>In my perspective on Landmark Registration, such as with FiducialWizard, you need two groups of landmarks: one from the model or volume you want to move and the other from the model or volume that remains fixed. The module will then calculate the transform that describes the relationship between these two groups of landmarks. Once you have this transform, you apply it to the model or volume that you want to move, which will align it with the fixed model or volume.<br>
This video may help you: <a href="https://www.youtube.com/watch?v=TBHr2wizGTM" rel="noopener nofollow ugc">Align 3D objects using landmarks in 3D Slicer - YouTube</a></p>

---

## Post #9 by @muratmaga (2024-05-20 20:58 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="7" data-topic="36217" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>I tried 3 points, no error message, just nothing happening. i guess I’m not doing it right . is there an order or something else needed?</p>
</blockquote>
</aside>
<p>From the screenshot it appears you are saving each landmark into its own pointlist object. That’s  not what Fiducial Registration expects. You should have only two pointlist objects, and multiple landmarks (at least 4) in each.</p>

---

## Post #10 by @mohammed_alshakhas (2024-05-20 21:09 UTC)

<p>thnank for the video it really helped <a class="mention" href="/u/leidymorav">@LeidyMoraV</a> , <a class="mention" href="/u/pieper">@pieper</a> I was using points from landmarks not control points the correct, second is that I need to apply the movement from the navigation menu (  not obvious at all ),<br>
id suggest making these two points clear  in this module, its a great one and I’m going to use it from now on</p>

---
