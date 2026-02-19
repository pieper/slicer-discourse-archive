---
topic_id: 45593
title: "Can Tumor Volume Be Accurately Measured"
date: 2025-12-24
url: https://discourse.slicer.org/t/45593
---

# Can tumor volume be accurately measured?

**Topic ID**: 45593
**Date**: 2025-12-24
**URL**: https://discourse.slicer.org/t/can-tumor-volume-be-accurately-measured/45593

---

## Post #1 by @jung (2025-12-24 10:22 UTC)

<p>Can tumor volume be accurately measure? on CT or MRI for medical and research purposes, even in anatomically complex regions such as sinonasal cancers?</p>

---

## Post #2 by @mau_igna_06 (2025-12-24 20:05 UTC)

<p>You should not have any problem to make measurements on slicer in any 2D (XRay, US) or 3D (CT, MRI). The quality of the measurement is only limited by the sensibility of the hardware acquiring the image and the parameters used on the machine at the moment the image creation. Think about it as taking a nice picture, it depends in the camera of the device but also on that the region of interest is correctly focused.</p>
<p>After having a good enough image for your purpose, you can measure using rulers, ellipses to get major and minor diameters, circles to get their diameters. Also you can measure, after doing some segmentation (i.e. selecting a region of interest) of an organ, its centroid, total volume, outer surface, etc.</p>
<p>All these things are possible in Slicer and after you have a concrete workflow you can write python code to reduce your number of clicks (or processing time per patient) to the minimum</p>
<p>If you need to do longitudinal research (i.e. of the same patient on different time points) Slicer allows to do registration of image which means making overlaying them in a way they can be compared. Slicer already has powerful registration algorithms that you can test on your own and decide which one is better for your application</p>
<p>Another point to highlight the quality might depend on your imaging device, Slicer is not only used for research on humans, 3D images from microCT machines are usually processed for morphometric analysis on mouse embryos and other animals.</p>
<p>But, to answer your questions:</p>
<aside class="quote no-group" data-username="jung" data-post="1" data-topic="45593" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/dfb087/48.png" class="avatar"> jung:</div>
<blockquote>
<p>Can tumor volume be accurately measure? on CT or MRI for medical and research purposes, even in anatomically complex regions such as sinonasal cancers?</p>
</blockquote>
</aside>
<p>Anything you can measure as an approximate ellipsoid (you’ll need to measure its 3 diameters) can give you an approximate volume. Any 3D image you can segment will have an accurate automatic volume measurement that only depends on the imaging device and the acquisition parameters.</p>

---

## Post #3 by @Esteban_Barreiro (2026-01-07 03:11 UTC)

<p>Yes, you can do it with Segment Statistics, under Quantification.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7843b822de3b548a378f560f6ea18c25996dab57.png" data-download-href="/uploads/short-url/h9UnPqxsmmLIUzKnSaov69Kto4D.png?dl=1" title="screencap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7843b822de3b548a378f560f6ea18c25996dab57_2_473x500.png" alt="screencap" data-base62-sha1="h9UnPqxsmmLIUzKnSaov69Kto4D" width="473" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7843b822de3b548a378f560f6ea18c25996dab57_2_473x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/7843b822de3b548a378f560f6ea18c25996dab57_2_709x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/7843b822de3b548a378f560f6ea18c25996dab57.png 2x" data-dominant-color="2F302C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screencap</span><span class="informations">742×784 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
