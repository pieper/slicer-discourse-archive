---
topic_id: 16223
title: "Problem In Adding Rt Dose Volumes With Simplefilters Module"
date: 2021-02-25
url: https://discourse.slicer.org/t/16223
---

# Problem in adding RT Dose volumes with SimpleFilters module

**Topic ID**: 16223
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/problem-in-adding-rt-dose-volumes-with-simplefilters-module/16223

---

## Post #1 by @aseman (2021-02-25 21:47 UTC)

<p>Slicer version:4.11<br>
Hi 3d slicer experts and all<br>
I have 4 RT Doses that I  have exported them from Treatment Planning System(TPS). the prescribed dose for this patient is 70Gy; and the sum of these 4 doses in TPS is 70Gy. I used Simple Filters module(AddImageFilter) to calculate the sum of them in 3d slicer; i.e total dose(sum1,2,3,4). unfortunately, when I choose this total dose in the Isodose module, its value is 68.42Gy; which is less than its actual value(70 Gy). Therefore, after calculating the DVH curves using Dose Volume Histogram module, the dose of various organs is less than their actual value in TPS. can you help me?<br>
1- How can I correct the value of 68.42Gy?<br>
2- Is it possible to calculate the sum of these 4 RT Dose correctly?<br>
Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/108d4f056873c9df92e05fdf63e5067a291593e8.jpeg" data-download-href="/uploads/short-url/2mqoiJnFnqeoK5xGTiBD5TBlYqA.jpeg?dl=1" title="picture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/108d4f056873c9df92e05fdf63e5067a291593e8_2_690x388.jpeg" alt="picture" data-base62-sha1="2mqoiJnFnqeoK5xGTiBD5TBlYqA" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/108d4f056873c9df92e05fdf63e5067a291593e8_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/108d4f056873c9df92e05fdf63e5067a291593e8_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/108d4f056873c9df92e05fdf63e5067a291593e8_2_1380x776.jpeg 2x" data-dominant-color="7C7D7F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture</span><span class="informations">4128×2322 3.33 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-26 13:38 UTC)

<p>Each TPS computes the region of interest from contours in the RT structure set slightly differently. If you are talking about <em>maximum</em> dose then the 2% difference may be completely normal, because the DVH tend to have a very long, thin tail. If the structure is small and the its contours are near high-dose-gradient regions then you can expect even larger differences.</p>
<p>Note that there are a few additional fields that a scalar volume needs to have to make it show up as a dose volume. You can add those fields programmatically or using the GUI (in Data module, right-click on the volume and choose “Convert to RT dose volume”).</p>

---
