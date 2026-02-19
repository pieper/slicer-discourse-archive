---
topic_id: 13344
title: "Radiomics For Entire Image Not Only On Segmentation"
date: 2020-09-04
url: https://discourse.slicer.org/t/13344
---

# Radiomics for entire image- not only on segmentation

**Topic ID**: 13344
**Date**: 2020-09-04
**URL**: https://discourse.slicer.org/t/radiomics-for-entire-image-not-only-on-segmentation/13344

---

## Post #1 by @KLH (2020-09-04 20:22 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.10.2<br>
Expected behavior: Features extracted from whole image<br>
Actual behavior: Need segmentation</p>
<p>I am using radiomics to analyze grayscale confocal microscopy images and I do not want to use a segmentation. I would like to analyze the whole image so that i can compare different histogram processes to one another (HE, CLAHE, WL). I want to show quantitatively that structures present in original image are best preserved/enhanced using CLAHE and when other methods are used, structures in the image are lost.<br>
When I segment the images- for example using a threshold, then the darkest regions of the image not captured by the threshold are not being analyzed? I want to compare the entire grayscale images to one another- not just a thresholded region of the images. Is it possible to extract the radiomic features from the whole image without using a segmentation or binary label?</p>

---

## Post #2 by @Pascal_Yamlome (2021-10-31 23:51 UTC)

<p>Hello I am new to this package. I have a similar problem. I will also like toe extract features from the entire image. Please let me know if you find a way around it.</p>

---

## Post #3 by @lassoan (2021-11-11 06:11 UTC)

<p>Can you attach an example image that you want to analyze? Often the “entire image” contains air, patient table, clothes, blank regions (outside the cylinder shaped reconstructed area) that you must exclude from the analysis because these may alter some metrics.</p>
<aside class="quote no-group" data-username="KLH" data-post="1" data-topic="13344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/f07891/48.png" class="avatar"> KLH:</div>
<blockquote>
<p>When I segment the images- for example using a threshold, then the darkest regions of the image not captured by the threshold are not being analyzed?</p>
</blockquote>
</aside>
<p>You should be able to specify a threshold value that is lower than all the voxel values in the image, so you would not miss any part of the image. What software do you use for this thresholding?</p>

---
