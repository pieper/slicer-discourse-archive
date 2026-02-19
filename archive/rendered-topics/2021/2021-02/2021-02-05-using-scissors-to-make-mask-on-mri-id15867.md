---
topic_id: 15867
title: "Using Scissors To Make Mask On Mri"
date: 2021-02-05
url: https://discourse.slicer.org/t/15867
---

# Using Scissors to make mask on MRI

**Topic ID**: 15867
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/using-scissors-to-make-mask-on-mri/15867

---

## Post #1 by @HodaGH (2021-02-05 18:08 UTC)

<p>Hi all,</p>
<p>I’m trying to create a mask for registration of MRI and CT pelvis scans using scissors in segment editor. It works perfectly for CT but when I draw the same free-form area on the MRI the mask only goes half through the space that I drew as shown in the images. I tried other tools like draw and paint but they also can fill up to the lower half of the MRI scan and not the upper half. What can I do to solve this issue ? Thank you.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b855dd33f4add31f413cd2d568a555914e10e79.jpeg" alt="Screen Shot 2021-02-05 at 12.51.05 PM" data-base62-sha1="6d0gAPVUibycnEkfmX5SCJRU7wJ" width="541" height="331"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad09db7c98b1dcf39135aa928caafd84cc4106e.jpeg" alt="Screen Shot 2021-02-05 at 12.50.38 PM" data-base62-sha1="1xFJq8F4P0sxeQ6tjfdwICD9F9Q" width="424" height="349"></p>

---

## Post #2 by @lassoan (2021-02-05 18:42 UTC)

<p>You can paint up to the boundaries of the segmentation. See how to change that in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">Segment Editor module documentation</a>.</p>

---

## Post #3 by @HodaGH (2021-02-09 06:52 UTC)

<p>Thanks for your reply. I want to feed the result of this registration with mask to the second round of registration to see if my result improves (with Elastix) but I don’t see a way to do this! I mean non of the parameter files have transformation information so that I can edit the files the same way. how do I do multiple registrations with Elastix in 3D slicer?</p>

---

## Post #4 by @lassoan (2021-02-10 03:52 UTC)

<aside class="quote no-group" data-username="HodaGH" data-post="3" data-topic="15867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>how do I do multiple registrations with Elastix in 3D slicer?</p>
</blockquote>
</aside>
<p>I’m not sure how exactly registration stages in Elastix pass on the transforms, you can ask it on Elastix or ITK forums.</p>
<p>If you want, you can run one registration phase at a time. First pass only a single parameter file to elastix, inspect the results, tune the parameters as needed. Then, run elastix again using the transformed (resampled) moving volume as input for this registration phase. Resample a volume several times is not ideal (each resampling is a lossy operation), so in the end it is better to concatenate all the transforms and apply it at once to the original moving volume.</p>

---
