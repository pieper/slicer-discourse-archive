---
topic_id: 12875
title: "Skull Sutures In Ct"
date: 2020-08-06
url: https://discourse.slicer.org/t/12875
---

# Skull sutures in CT

**Topic ID**: 12875
**Date**: 2020-08-06
**URL**: https://discourse.slicer.org/t/skull-sutures-in-ct/12875

---

## Post #1 by @Mohamed_Attia (2020-08-06 14:47 UTC)

<p>Hello everyone,<br>
I am new to 3D slicer. I am working on a research project that needs to extract the skull sutures. I was able to used manually to approximate them. I used “shift” to make the sutures more evident. I was wondering if there is a plugin that can help me to visualise and extract the sutures automatically?</p>

---

## Post #2 by @lassoan (2020-08-06 15:55 UTC)

<p>Please have a look at this topic:</p>
<aside class="quote quote-modified" data-post="4" data-topic="12389">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/working-with-sutures-1-voxel-wide-on-infant-skull-ct/12389/4">Working with sutures &lt;1 voxel wide on infant skull CT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If you need the full skull as well, you should threshold what you need to get that first. 
Then what I do is use the “Editable Intensity Range” checkbox to Erase only those dark threshold values that will give you a nice gap between parts. It can be tedious but by setting that editable range, you can be messy when painting over the area and not worry too much about following the suture closely. Once you think you’ve separated it enough, you can create another segment for the temporal bone and us…
  </blockquote>
</aside>

<p>If you have further questions then let us know, describing in more details what you mean by “extract the skull suture” (do you need to just mark the suture lines or split the bone along sutures?) and what you mean by “I used shift to make the sutures more evident” (what did you shift?).</p>

---

## Post #3 by @Mohamed_Attia (2020-08-07 01:16 UTC)

<p>Thanks a lot for your prompt reply. I want to extract the sutures curves in 3D automatically. There is an option called “shift” at the left panel. It helped me to make them more evident. But, I still have to manually segment. I tried “he curve follow minimal bone density” but it did not work out for me as I have to use a lot of markdowns.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c1b2501e186b9f959e25587216b6c86323cdca8.jpeg" data-download-href="/uploads/short-url/40DwCq5LH9UWyGZyjKFTYh3sOhi.jpeg?dl=1" title="Screenshot from 2020-08-07 11-07-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c1b2501e186b9f959e25587216b6c86323cdca8_2_690x291.jpeg" alt="Screenshot from 2020-08-07 11-07-53" data-base62-sha1="40DwCq5LH9UWyGZyjKFTYh3sOhi" width="690" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c1b2501e186b9f959e25587216b6c86323cdca8_2_690x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c1b2501e186b9f959e25587216b6c86323cdca8_2_1035x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c1b2501e186b9f959e25587216b6c86323cdca8_2_1380x582.jpeg 2x" data-dominant-color="938588"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-07 11-07-53</span><span class="informations">2560×1080 626 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-08-07 03:03 UTC)

<p>The curve can follow minimum bone density very well, so it should be enough to drop only a few points. Setting up is not trivial (you need to segment the bone, export to model, then use Probe volume with model to get bone density mapped to the model, then use that intensity for minimal cost path search), so probably it is worth automating this using a short Python script.</p>
<p>What is the overall goal of the project? Depending on that, there could be other, simpler solutions.</p>

---

## Post #5 by @Mohamed_Attia (2020-08-20 02:58 UTC)

<p>Thanks a lot. I will try these steps. I appreciate your help.</p>

---

## Post #6 by @parna_eshraghi (2021-04-23 05:10 UTC)

<p>Hi<br>
I am wondering if you could figure it out how to automatically find the sutures with 3dslicer?</p>

---

## Post #7 by @parna_eshraghi (2021-04-23 14:37 UTC)

<p>Hi<br>
Did you find a solution for this?</p>

---

## Post #8 by @lassoan (2021-04-25 13:27 UTC)

<p>Yes, you can find suture curves automatically, quite well, by following the steps that I described in my post above.</p>

---
