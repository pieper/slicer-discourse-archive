---
topic_id: 12876
title: "Rescale Voxel Values Of Cbct To Mdct Hu"
date: 2020-08-06
url: https://discourse.slicer.org/t/12876
---

# Rescale voxel values of CBCT to MDCT HU

**Topic ID**: 12876
**Date**: 2020-08-06
**URL**: https://discourse.slicer.org/t/rescale-voxel-values-of-cbct-to-mdct-hu/12876

---

## Post #1 by @ahmad_abbas (2020-08-06 14:48 UTC)

<p>I have a CBCT and MDCT of the same specimen and I want to “convert” the grey values in CBCT accordingly the ones in MDCT and consequently be able to measure “HU” values in the CBCT volume?</p>

---

## Post #2 by @ahmad_abbas (2020-08-06 14:07 UTC)

<p>I have a CBCT and MDCT of the same specimen and I want to “convert” the grey values in CBCT accordingly the ones in MDCT and consequently be able to measure “HU” values in the CBCT volume?</p>

---

## Post #3 by @lassoan (2020-08-06 16:07 UTC)

<p>If you know the correspondence between original values and HU then applying that transformation to voxel intensities should be trivial. If you need don’t know it then you need to do a few measurements.</p>
<p>These topics should help:</p>
<aside class="quote" data-post="1" data-topic="11782">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/d07c76/48.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/from-ct-to-qct/11782">From CT to qCT?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Dear all 
Is there an extension that allows to extract segment statistics for known CT calibration parameters? 
I would like to extract bone density values instead of HU. 
Thanks
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="11010">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/bone-mineral-density-bmd-measurement-method/11010">Bone Mineral Density (BMD) measurement method</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    I have been told a method of calculating BMD from micro CT data using a proprietary software and i am wondering about the accuracy of the method and replicating it with the 3D Slicer. 
The way it was done in the software was, 
we use 3 phantoms of know density, water and 0.25 and 0.75   and the mean hounsfield values  was 
water 0 = -575.936 
0.25 = 1142.4 
0.75 = 3267.8 
so the equation was 
X =(y+11.708)/4381.1 
so i try to do this the same with the 3D Slicer, 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c3777513cdaa0fb9ae449f088c19bbba892b311.jpeg" data-download-href="/uploads/short-url/1K4z2yqzj2RgOJYybXK8kAARDCF.jpeg?dl=1" title="Screenshot from 2020-04-06 10-07-50" rel="noopener nofollow ugc">[Screenshot from 2020-04-06 10-…</a>
  </blockquote>
</aside>

<p>Note that for many operations, such as visualization, registration, segmentation, a calibrated CT is useful, but not essential. What is your application? What would you like to achieve overall?</p>

---

## Post #4 by @ahmad_abbas (2020-08-06 19:23 UTC)

<p>i need the HU units for the treatment planning system and monte carlo simulation</p>

---

## Post #5 by @lassoan (2020-08-07 03:15 UTC)

<p>For radiation therapy treatment planning you indeed need voxels in HU, so you need to calibrate the intensity as described in the topics linked above.</p>

---
