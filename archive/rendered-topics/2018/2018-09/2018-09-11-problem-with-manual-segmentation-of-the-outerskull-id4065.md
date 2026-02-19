---
topic_id: 4065
title: "Problem With Manual Segmentation Of The Outerskull"
date: 2018-09-11
url: https://discourse.slicer.org/t/4065
---

# Problem with manual segmentation of the outerskull

**Topic ID**: 4065
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/problem-with-manual-segmentation-of-the-outerskull/4065

---

## Post #1 by @m.hilani (2018-09-11 14:51 UTC)

<p>Hi,</p>
<p>I am trying to manually segment the outerskull surface of a brain MRI. I managed to have the contour of that surface using the “threshold” option in the segment editor.<br>
But now what I have is the 3D segmented contour with a hollow inside and many holes in it.<br>
I tried using “paint”,  “Draw” and “level Tracing” to fill the voids but each time I do that nothing happens and the inside is still not painted.</p>
<p>Is this a problem with my computer or is there a way to solve this and fill these voids?</p>
<p>Thank you!<br>
Michel</p>

---

## Post #2 by @cpinter (2018-09-11 14:57 UTC)

<p>Some basic questions first:</p>
<ul>
<li>Which Slicer version do you use? For Segment Editor usage we suggest the latest 4.9.0 nightly</li>
<li>Have you clicked apply on the threshold effect?</li>
<li>Do you have the thresholded segment selected when you paint/draw/etc?</li>
</ul>

---

## Post #3 by @m.hilani (2018-09-11 16:30 UTC)

<p>Thanks a lot for your reply.</p>
<p>Yes I am using the 4.9.0 nightly version on a Linux ubuntu.<br>
I did click the apply on the threshold effect. And yes I am trying to apply paint/draw on a selected thresholded segment.</p>
<p>Thanks again!</p>

---

## Post #4 by @muratmaga (2018-09-11 17:47 UTC)

<p>From your description it is not sufficient to tell why things are not working. I would suggest working with the provided MRHead.nrrd data with slicer (through the Sample Data volume) first, and read the segment editor document at <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a></p>
<p>If you have success with that dataset, you can try the same with your own data.</p>

---

## Post #5 by @lassoan (2018-09-11 18:15 UTC)

<aside class="quote no-group" data-username="m.hilani" data-post="1" data-topic="4065">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/77aa72/48.png" class="avatar"> m.hilani:</div>
<blockquote>
<p>segment the outerskull surface of a brain MRI</p>
</blockquote>
</aside>
<p>This is not a typical use case and not an easy one to solve, since bone is typically not visible very well on MRI images.</p>
<p>You can use simple thresholding to extract skin surface (followed by post-processing to fill holes and reduce noise). See step-by-step instructions here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>
<p>You can use SwissSkullStripper extension to extract skull inner surface. If you edit the atlas labelmap so that it contains the outer surface of the skull (instead of the default, inner surface of the skull) then the module might be able to provide that fully automatically.</p>

---
