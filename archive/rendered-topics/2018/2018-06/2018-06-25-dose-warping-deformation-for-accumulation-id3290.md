---
topic_id: 3290
title: "Dose Warping Deformation For Accumulation"
date: 2018-06-25
url: https://discourse.slicer.org/t/3290
---

# Dose warping/deformation for accumulation

**Topic ID**: 3290
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/dose-warping-deformation-for-accumulation/3290

---

## Post #1 by @Lowey (2018-06-25 22:37 UTC)

<p>Hi there,</p>
<p>I am trying to deform the dose distribution output from my TPS for research purposes. I have tried using the Plastimatch extension/module but am having difficulty loading my data without errors. Is there some documentation somewhere or an easy workflow to follow that allows for dose warping?</p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2018-06-25 23:58 UTC)

<aside class="quote no-group" data-username="Lowey" data-post="1" data-topic="3290">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/e36b37/48.png" class="avatar"> Lowey:</div>
<blockquote>
<p>am having difficulty loading my data without errors</p>
</blockquote>
</aside>
<p>What data do you have? What is the error?<br>
Have you installed SlicerRT extension?</p>

---

## Post #3 by @Lowey (2018-06-26 05:20 UTC)

<p>Hi Andras,</p>
<p>Yes I have SlicerRT extension and have now managed to load my data correctly. Probably the issues I’m now having are just related to me being new to the software.</p>
<p>For background, I am trying to deform a planning CT (pCT) image to match the anatomy of daily CBCT images, resulting in a number of deformed CTs (dCTs) for a head-and-neck radiotherapy research project. I think the limited CBCT FOV is causing issues. Ideally, I would like the dCTs to have the same anatomy as the pCT when outside the CBCT FOV and have deformed anatomy to match the CBCT anatomy when inside the CBCT FOV. Hopefully that makes sense. Essentially a ‘stitched’ CT.</p>
<p>Right now, I am unable to even get a deformed registration that looks realistic. The deformed registrations are very incorrect. But more time with the software should fix that. However, these registrations only work on the CBCT FOV. So my two questions are,</p>
<ol>
<li>Can I somehow create a ‘stitched’ CT as described above?</li>
<li>Does this require the use of masking? If so, if there some documentation somewhere about how to create masks?</li>
</ol>
<p>Many thanks for your help! Very appreciated!</p>

---

## Post #4 by @cpinter (2018-06-26 09:27 UTC)

<p>Hi Lowey,</p>
<p>Just in case you haven’t seen this yet, here’s a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials">tutorial about dose accumulation with SlicerRT</a> (the World Congress one). This is a good overview of the whole workflow.</p>
<p>About the registration:</p>
<ol>
<li>The deformation field’s extent is the same as the fixed image volume. If there is no data outside the moving volume, then the deformation field will be empty there, and I think the deformation in those regions will be kind of “locally linear”.</li>
<li>There is an Image Mask and Pre-processing section in the General Registration (BRAINS) module to specify a mask if you need it.</li>
</ol>
<p>Have you tried the SlicerElastix extension to do the registration? In some cases it yields better results with the default settings.</p>

---

## Post #5 by @Lowey (2018-06-26 23:08 UTC)

<p>Hi Cpinter,</p>
<p>Thanks for your reply, I have been playing around with the different registrations and am getting closer to my desired result. Haven’t been able to create the ‘stitched CT’ yet but I assume it’s possible.</p>
<p>Regarding the tutorial you linked, is there another source I can access it from? The current link gives me the ‘File Not Found’ error</p>
<p>Thanks!</p>

---

## Post #6 by @cpinter (2018-06-27 06:52 UTC)

<p>Thanks for reporting it! I fixed those links just now. Please try again</p>

---
