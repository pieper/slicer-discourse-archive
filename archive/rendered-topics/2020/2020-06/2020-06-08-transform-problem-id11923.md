# Transform Problem

**Topic ID**: 11923
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/transform-problem/11923

---

## Post #1 by @Jini (2020-06-08 10:49 UTC)

<p>Operating system:<br>
Slicer version: 4.11.0-2019-11-28<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,</p>
<p><strong>I segmentation two model from two CT-scan</strong><br>
1)Sometimes when I transform two models with Finducial markups and General Brainsfit, these models don’t overlap. What else could I do?<br>
2) when I registered the model with Transform using Harden,  the model disappear and you only see one model? Who is the other model? What I can do?<br>
3) The landmark is does not work, why?</p>
<p>Thank you for your help</p>

---

## Post #2 by @lassoan (2020-06-08 14:20 UTC)

<aside class="quote no-group" data-username="Jini" data-post="1" data-topic="11923">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/5daacb/48.png" class="avatar"> Jini:</div>
<blockquote>
<p>Sometimes when I transform two models with Finducial markups and General Brainsfit, these models don’t overlap. What else could I do?</p>
</blockquote>
</aside>
<p>I’m not sure how fiducial markups registration works in Brainsfit. For landmark registration between two models, I would recommend to use Fiducial registration wizard module (in SlicerIGT extension).</p>

---

## Post #3 by @Jini (2020-06-09 12:17 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0bd2266b3b27fd1d3fbe91d019ad3694d3cd92f.png" data-download-href="/uploads/short-url/mVXC3uq90Ajvp8saAh4dYHlpVQb.png?dl=1" title="Transform_Harden" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0bd2266b3b27fd1d3fbe91d019ad3694d3cd92f_2_353x500.png" alt="Transform_Harden" data-base62-sha1="mVXC3uq90Ajvp8saAh4dYHlpVQb" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0bd2266b3b27fd1d3fbe91d019ad3694d3cd92f_2_353x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0bd2266b3b27fd1d3fbe91d019ad3694d3cd92f_2_529x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0bd2266b3b27fd1d3fbe91d019ad3694d3cd92f.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Transform_Harden</span><span class="informations">686×969 41.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
By transforming, I found that when using the Harden, the second model disappears completely (see picture). That was not the case last year. Why is that jet so?</p>
<p>Thank you very much</p>

---

## Post #4 by @lassoan (2020-06-10 02:14 UTC)

<p>You are using a very old Slicer version. Please try the latest Slicer Preview Release.</p>

---

## Post #5 by @Jini (2020-07-30 07:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c753fc983c2b6c046e194fdaed44f02f9b2b4e5f.jpeg" data-download-href="/uploads/short-url/srkXlOXtBW7X6aEkjkeaFWJMasv.jpeg?dl=1" title="5.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c753fc983c2b6c046e194fdaed44f02f9b2b4e5f_2_690x456.jpeg" alt="5.PNG" data-base62-sha1="srkXlOXtBW7X6aEkjkeaFWJMasv" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c753fc983c2b6c046e194fdaed44f02f9b2b4e5f_2_690x456.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c753fc983c2b6c046e194fdaed44f02f9b2b4e5f_2_1035x684.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c753fc983c2b6c046e194fdaed44f02f9b2b4e5f.jpeg 2x" data-dominant-color="3B393D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5.PNG</span><span class="informations">1217×805 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hi,<br>
how can i move two ct dates so that they are on top of each other?</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2020-07-31 03:50 UTC)

<p>You can try “General registration (Elastix)” module (provided by SlicerElastix extension). If that fails for some reason then you can register based on manually defined landmarks using “Landmark registration” module.</p>

---

## Post #7 by @Jini (2020-08-02 08:34 UTC)

<p>the problem with my scan is that the bones are rotated from two measurements (have changed position). I have to turn them properly and then overlap them. How can I turn both bones in the same position?<br>
And Landmark registration it does not work.</p>

---

## Post #8 by @pieper (2020-08-02 14:09 UTC)

<p>LandmarkRegistration has been fixed in recent preview builds (for the last couple months)</p>

---
