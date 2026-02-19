---
topic_id: 31611
title: "Getting External And Internal Diameter Of A Bone"
date: 2023-09-07
url: https://discourse.slicer.org/t/31611
---

# Getting external and internal diameter of a bone

**Topic ID**: 31611
**Date**: 2023-09-07
**URL**: https://discourse.slicer.org/t/getting-external-and-internal-diameter-of-a-bone/31611

---

## Post #1 by @Henry_Lopes (2023-09-07 22:12 UTC)

<p>Hello everyone, this is my first post here.</p>
<p>What would be the best method to measure external and internal diameters of a hollow and long bone, for instance, such a long shank bone without its internal stuff?<br>
Some additional info:</p>
<ol>
<li>My CT scan is reasonably clean (the slices look like rings varying their dimensions);</li>
<li>Using GIMP to measure the screen shots works fine, however for some unknown reason the same silce sometimes has different measurements (diameters shift between a 0.5mm error);</li>
<li>An important conclusion here is knowing which part of the bone is the largest (inside, and outside). The imprecision I get in no 2) makes it hard;</li>
<li>Getting the average diameter of the cross section is the more important feature I need now, but I may ask for a little more measurements later.</li>
</ol>
<p>I have tried some methods recommended here but they have some issues:</p>
<ol>
<li>Segment Geometry is ridiculously slow in my computer;</li>
<li>Segment Cross section area module shows varying diameters according to PA or LR changes (the bone is not straight). The margin is pretty small, yet unacceptable for my project (I need 0.01mm precision).</li>
<li>Slicer ext. VMTK apparently does the job, also detecting the shape of the non-straight object. The problem is I am not being able to compute a center line which travels exactly trough the center of the internal diameter, I think the module is supposed to work with solid objects (my bone is already hollow inside, and reasonably free from noises).</li>
<li>I’ve also tried a module supposed to compute the thickness of bones (Bone Thickness Mapping). It isn’t exactly what I need but it would be also extremely useful to know where the bone is thicker. The module simply doesn’t work, it stays in “calculating: 0%” forever (yet the software and interface don’t hang, they still work normally).</li>
</ol>
<p>Thank you very much!</p>

---

## Post #2 by @lassoan (2023-09-08 04:02 UTC)

<aside class="quote no-group" data-username="Henry_Lopes" data-post="1" data-topic="31611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/henry_lopes/48/67396_2.png" class="avatar"> Henry_Lopes:</div>
<blockquote>
<p>I need 0.01mm precision</p>
</blockquote>
</aside>
<p>What is the resolution of your image (image spacing along each axis)?</p>
<aside class="quote no-group" data-username="Henry_Lopes" data-post="1" data-topic="31611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/henry_lopes/48/67396_2.png" class="avatar"> Henry_Lopes:</div>
<blockquote>
<p>The problem is I am not being able to compute a center line which travels exactly trough the center of the internal diameter</p>
</blockquote>
</aside>
<p>If you segment the bone then you can use the Segment Editor module to automatically get the internal cavity and external surface of the bone using <a href="https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248/2">Wrap Solidfy</a> effect. This will allow you to get the centerline of either the internal cavity or the external surface of the bone.</p>
<aside class="quote no-group" data-username="Henry_Lopes" data-post="1" data-topic="31611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/henry_lopes/48/67396_2.png" class="avatar"> Henry_Lopes:</div>
<blockquote>
<p>I’ve also tried a module supposed to compute the thickness of bones (Bone Thickness Mapping). It isn’t exactly what I need but it would be also extremely useful to know where the bone is thicker. The module simply doesn’t work</p>
</blockquote>
</aside>
<p>We don’t hear much from the developers of this extension, so I’m not sure if it is still maintained, but please report the issue at the <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-BoneThicknessMapping">extension’s repository</a> and hopefully you’ll get a response.</p>

---

## Post #3 by @Henry_Lopes (2023-09-08 04:41 UTC)

<p>Thank you for your reply. Is this the resolution, 512x512?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81876bd8bdc288462aa043ee0be717522d98b316.png" alt="image" data-base62-sha1="itRJptqrEX2FzCqHwQFntHBRIKW" width="423" height="183"></p>
<p>I will now try the operations you suggested me, thank you very much.</p>

---

## Post #4 by @lassoan (2023-09-08 13:26 UTC)

<p>Resolution (image spacing) is displayed in “Volumes” module’s “Volume information” section. To measure with 0.01mm precision, ideally you need spacing value of one magnitude less (0.001mm).</p>

---

## Post #5 by @Henry_Lopes (2023-09-08 21:39 UTC)

<p>Hmmm… bad news!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6b9d332a373ad6667af3dcb70f94057faaca0f3.png" data-download-href="/uploads/short-url/wV5WG0j1TIUA22uWnjsvVvGcZVh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b9d332a373ad6667af3dcb70f94057faaca0f3_2_690x123.png" alt="image" data-base62-sha1="wV5WG0j1TIUA22uWnjsvVvGcZVh" width="690" height="123" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b9d332a373ad6667af3dcb70f94057faaca0f3_2_690x123.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6b9d332a373ad6667af3dcb70f94057faaca0f3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6b9d332a373ad6667af3dcb70f94057faaca0f3.png 2x" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">714×128 11.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What precision do you think I am able to get under this spacing? Also, the “rings” (slices) alone are extremely pixeled, they smooth only using “interpolate”, is this usual?</p>
<p>Thank you again.</p>

---

## Post #6 by @lassoan (2023-09-08 22:11 UTC)

<p>This voxel size is not uncommon in clinical images and it means that the error of length measurements is about 1mm. You would need a microCT to acquire images where you can measure length with 0.01mm error, but of course you cannot use it on live patients and it may not be able to scan larger bones.</p>

---

## Post #7 by @Henry_Lopes (2023-09-09 00:32 UTC)

<p>Thank you very much for the precious information. If you and any other are curious to know exactly what I am doing, here are some more details.<br>
First, a correction: I meant I need at least 0.1mm precision, and errors from 0.01 to 0.05mm don’t matter.<br>
The object is not a person, but something in a museum I want to help them making a replica (a totally academic, non-commercial purpose). The object resembles a (hollow) bone (shank like), so I thought writing about a bone would be better since it will help more people doing the same task. The museum object is a 400 years old boxwood pipe (about 60cm long, 27mm external, 17mm internal); it is supposed to be cylindrical inside and slightly (homeopathically) conical outside (the thicker area being about 1mm thicker than the narrowest).</p>
<p>I think it would be great if the museum used a micro CT scan as you said, but they don’t want to spend more money in testes before they have some replica, they think they already spent too many time and money measuring the piece (in the past manually, now they finally did a CT scan). There are more peculiarities about the piece, I am not touching it because I fear it be too off-topic as it isn’t really medicine-related; yet I have another important question about differences between measurements got by manual tools (by the museum crew) and CT scans, I will ask it later in a separate topic since I guess it is also relevant for medicine purposes.</p>
<p>Thank you very much again, I will now finally do the operations you told me.</p>

---

## Post #8 by @Henry_Lopes (2023-09-13 21:40 UTC)

<p>Thank you very much for your help, mr. Lasso. The VMTK plugin is working fine, I am getting convincing measurements of the “MIS diameter”. However, I am not being able to get the cross section area. Am I doing anything wrong?</p>

---
