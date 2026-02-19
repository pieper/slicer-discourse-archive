---
topic_id: 24007
title: "Seek The Source Technique For Ct And Ultrasound Based Mitral"
date: 2022-06-23
url: https://discourse.slicer.org/t/24007
---

# Seek the source technique for CT and Ultrasound based Mitral Valve/ Annulus

**Topic ID**: 24007
**Date**: 2022-06-23
**URL**: https://discourse.slicer.org/t/seek-the-source-technique-for-ct-and-ultrasound-based-mitral-valve-annulus/24007

---

## Post #1 by @whu (2022-06-23 08:27 UTC)

<p>Dear All,</p>
<p>Since 3d slicer support CT and Ultrasound based Mitral Valve/ Annulus segmentation.</p>
<p>Where can I found the source technique papers?</p>
<p>Maybe that is the way open-source benifits for researchers.</p>
<p>Thanks for suggestion.</p>

---

## Post #2 by @lassoan (2022-06-24 05:15 UTC)

<p>You can use <code>Valve Annulus Analysis</code> module in <code>SlicerHeart</code> extension to specify the annulus curve.</p>
<p>If you want to segment the leaflets then I would recommend to use <code>Crop volume</code> module to crop the image to the valve and resample it to 0.3mm isotropic resolution as a very first step. Then, segment this image using <code>Paint</code> tool in <code>Segment Editor</code> module. You can set <code>Editable intensity range</code> to a range that only paints in bright regions, because then you can use a large sphere brush to get an approximate segmentation very quickly. You then need to disable <code>Editable intensity range</code> and fix the segmentation (for example fill the discontinuities in the leaflets that are due to just signal dropout). Once you have  good-quality segmentation, you can use <code>Scissors</code> effect to split the leaflet into two separate segments.</p>
<p>We’ll release a module soon that automates some of these steps (cropping, resampling, etc.) saving a little time. We have been also working on fully automatic deep-learning based leaflet segmentation tools (e.g., <a href="https://www.researchgate.net/publication/356912840_Segmentation_of_Tricuspid_Valve_Leaflets_From_Transthoracic_3D_Echocardiograms_of_Children_With_Hypoplastic_Left_Heart_Syndrome_Using_Deep_Learning">tricuspid valves with HLHS</a>) that we’ll soon release publicly. There have been many other groups developing similar tools for mitral valves.</p>

---

## Post #3 by @whu (2022-06-27 01:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="24007">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use <code>Valve Annulus Analysis</code> module in <code>SlicerHeart</code> extension to specify the annulus curve.</p>
</blockquote>
</aside>
<p>This step, we need to segment the annulus firstly, right ?</p>
<p>Here I got a CTA DICOM data, I try to segment the annulus.</p>
<p>Thanks.</p>

---
