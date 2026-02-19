---
topic_id: 4704
title: "How To Cut Cardiac 3D Model To See Inside Of Heart"
date: 2018-11-09
url: https://discourse.slicer.org/t/4704
---

# How to cut cardiac 3d model to see inside of heart

**Topic ID**: 4704
**Date**: 2018-11-09
**URL**: https://discourse.slicer.org/t/how-to-cut-cardiac-3d-model-to-see-inside-of-heart/4704

---

## Post #1 by @sarvpriya1985 (2018-11-09 18:30 UTC)

<p>Hi,<br>
Would anyone one know how to place cuts after building a 3d model of heart. I want to apply cuts through right atrium and right ventricle to see inside of heart via right ventricle. I am attaching a picture that I want to achieve.<br>
Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1658391a6b21dc47b16fae0aabe0f06c4c78017.jpeg" data-download-href="/uploads/short-url/rARDX7zLr2AEgYPKhEvWunWxXVB.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1658391a6b21dc47b16fae0aabe0f06c4c78017_2_690x301.jpeg" alt="Capture2" data-base62-sha1="rARDX7zLr2AEgYPKhEvWunWxXVB" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1658391a6b21dc47b16fae0aabe0f06c4c78017_2_690x301.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1658391a6b21dc47b16fae0aabe0f06c4c78017.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1658391a6b21dc47b16fae0aabe0f06c4c78017.jpeg 2x" data-dominant-color="A24E4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">917×401 58.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <a href="/uploads/short-url/mpT9CY8PnrNKatv8ifCmGbRCL5I.jpeg">Capture3|690x476</a></p>

---

## Post #2 by @stevenagl12 (2018-11-10 14:22 UTC)

<p>If your model is from a segmentation, or you can convert to a segmentation from a model by using the mesh to labelmap extension, and then converting from labelmap to segmentation by either segmenting the labelmap or there is a convert labelmap to segmentation mode if you hover over the labelmap and right click on it to get the additional options, you can use the segment editor which has a scissors and surface cut tool to manually cut the segmentation.</p>

---

## Post #3 by @sarvpriya1985 (2018-11-16 15:48 UTC)

<p>My model is from a segmentation using seed method. I have about 10 individual segments and need to see the inside of them as if cutting the front half and seeing what is inside. The craniotomy module didn’t help as it has only one segment and I could not replicate the effect with scissor also. Is there any other way?  Just want to let know that I am a beginner so while explaining I would appreciate a little detail.<br>
Thanks</p>

---

## Post #4 by @anandmulay3 (2018-11-14 14:28 UTC)

<p>i have already created a heart model using seed grow module and followed the video provided by <a class="mention" href="/u/lassoan">@lassoan</a>  , its really nice .<br>
But i want some inner detail of the heart , using above module and method i get nice heart model form outside ,<br>
experts ; can you please suggest me a method or module to get accurate inner detail of the heart model.</p>
<p>Thanks. <img src="/images/emoji/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @lassoan (2018-11-15 01:42 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="1" data-topic="4759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"><a href="https://discourse.slicer.org/t/get-heart-inner-details-in-segment/4759/1">Get heart inner details in segment</a></div>
<blockquote>
<p>But i want some inner detail of the heart</p>
</blockquote>
</aside>
<p>What do you mean exactly?</p>

---

## Post #6 by @anandmulay3 (2018-11-15 07:35 UTC)

<p>I want to make a Hollow Heart model with in detail inside view, like internal wall between left and right ventricle  , chamber view etc.</p>

---

## Post #7 by @lassoan (2018-11-15 20:28 UTC)

<aside class="quote no-group quote-modified" data-username="anandmulay3" data-post="3" data-topic="4759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"><a href="https://discourse.slicer.org/t/get-heart-inner-details-in-segment/4759/3">Get heart inner details in segment</a></div>
<blockquote>
<p>Hollow Heart model</p>
</blockquote>
</aside>
<p>Using “Hollow” effect on each segment would be a good start, then you can go on and paint in any additional details.</p>

---

## Post #8 by @sarvpriya1985 (2018-11-16 15:45 UTC)

<p>I tried this method and also the scissor method. But the exact inner details I am looking for could not be produced. I just need to cut the front part and see inside of heart. The craniotomy module that was suggested had only one segment and my model has about 10 individual heart segments. Any thing specific we could do for heart models.<br>
Thanks</p>

---

## Post #9 by @lassoan (2018-11-16 18:09 UTC)

<p>You need to hollow each ventricle/atrium and then merge them all into a single segment (create a new segment and add all existing segments using “Logical operators” effect’s “Add” method). You may need to edit the valves manually (e.g, cut a hole using “Erase” effect). Finally, you can cut away a part as shown in <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">Craniotomy recipe</a>.</p>

---

## Post #10 by @sarvpriya1985 (2018-11-16 18:21 UTC)

<p>Thanks will do so and update.</p>

---

## Post #11 by @anandmulay3 (2018-11-20 14:37 UTC)

<p>Hi <a class="mention" href="/u/sarvpriya1985">@sarvpriya1985</a> any progress ??</p>

---

## Post #12 by @sarvpriya1985 (2018-11-21 20:44 UTC)

<p>No Anand. I tried all methods as discussed but still no luck</p>

---

## Post #13 by @lassoan (2018-11-23 04:21 UTC)

<p>I’ve used the method that I described above successfully. If you have any problems then describe what you did, what you expected to happen, and what happened instead.</p>

---
