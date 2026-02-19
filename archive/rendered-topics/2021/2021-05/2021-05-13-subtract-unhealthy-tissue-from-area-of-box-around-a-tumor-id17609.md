---
topic_id: 17609
title: "Subtract Unhealthy Tissue From Area Of Box Around A Tumor"
date: 2021-05-13
url: https://discourse.slicer.org/t/17609
---

# Subtract unhealthy tissue from area of box around a tumor

**Topic ID**: 17609
**Date**: 2021-05-13
**URL**: https://discourse.slicer.org/t/subtract-unhealthy-tissue-from-area-of-box-around-a-tumor/17609

---

## Post #1 by @Mostafa2020 (2021-05-13 19:23 UTC)

<p>Operating system:macOS<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi all,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787c08db2052ea0a9d365bb8aafbcfd05bdda316.jpeg" data-download-href="/uploads/short-url/hbR2rf2bBliM0zeSPyWTo6XSqRo.jpeg?dl=1" title="Screen Shot 2021-05-13 at 1.56.22 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/787c08db2052ea0a9d365bb8aafbcfd05bdda316_2_634x500.jpeg" alt="Screen Shot 2021-05-13 at 1.56.22 PM" data-base62-sha1="hbR2rf2bBliM0zeSPyWTo6XSqRo" width="634" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/787c08db2052ea0a9d365bb8aafbcfd05bdda316_2_634x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/787c08db2052ea0a9d365bb8aafbcfd05bdda316_2_951x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787c08db2052ea0a9d365bb8aafbcfd05bdda316.jpeg 2x" data-dominant-color="898989"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-05-13 at 1.56.22 PM</span><span class="informations">1026×809 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am trying to subtract unhealthy tissue from the area of the box surrounding the tumor. I used the Markups module, put a box around the segmented region, and I am going to subtract the unhealthy part from the area of the box to get the area of the healthy region. Please see the picture.</p>
<p>Thanks in advance for your help,</p>

---

## Post #2 by @lassoan (2021-05-13 19:24 UTC)

<p>You can blank out any part of a volume using “Mask volume” effect in Segment Editor module.</p>

---

## Post #3 by @Mostafa2020 (2021-05-13 19:41 UTC)

<p>Thanks, Andras. But how can I calculate the area of the box? By using “Mask volume”?</p>

---

## Post #4 by @lassoan (2021-05-13 20:04 UTC)

<p>You can get the volume of the box in the Measurements section in markups module.<br>
You can get the volume of the tumor using Segment Statistics module.</p>

---

## Post #5 by @Mostafa2020 (2021-05-18 14:24 UTC)

<p>Great. Thanks for your response. Is it possible to find ROI of the healthy tissue and then extract its feature? I am looking for a way to extract features from healthy and unhealthy regions inside the box.</p>

---

## Post #6 by @lassoan (2021-05-18 19:24 UTC)

<p>Yes, sure you can segment multiple tissue types (healthy, unhealthy, etc.). You can get their volumes and also their bounding box size using Segment statistics module.</p>

---

## Post #7 by @Mostafa2020 (2021-05-20 03:56 UTC)

<p>Thanks, Andras. I cannot see any options in “Measurement Settings” in the Measurements section in the markups module. There must be some options there to get the volume of the box?</p>

---

## Post #8 by @lassoan (2021-05-20 12:06 UTC)

<p>Volume measurement for markups ROI is available in recent Slicer Preview Releases.</p>

---

## Post #9 by @Mostafa2020 (2021-05-20 13:57 UTC)

<p>I am using version 4.11. Should I use version 4.13 instead?</p>

---

## Post #10 by @lassoan (2021-05-20 14:01 UTC)

<p>Yes. Volume measurement for markups ROI is available in recent Slicer Preview Releases, which is currently 4.13.</p>

---

## Post #11 by @rbumm (2021-05-22 13:03 UTC)

<p>You could also use the “Local Threshold” function from the “Segment Editor”. That is a good way to segment lung tumors:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19fa6eb7d390c79a68ff57d06a46a9cf14f2c8b4.jpeg" data-download-href="/uploads/short-url/3HOu7O0ijgRP7o6sxPsSQVNbvaQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19fa6eb7d390c79a68ff57d06a46a9cf14f2c8b4_2_690x361.jpeg" alt="image" data-base62-sha1="3HOu7O0ijgRP7o6sxPsSQVNbvaQ" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19fa6eb7d390c79a68ff57d06a46a9cf14f2c8b4_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19fa6eb7d390c79a68ff57d06a46a9cf14f2c8b4_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19fa6eb7d390c79a68ff57d06a46a9cf14f2c8b4_2_1380x722.jpeg 2x" data-dominant-color="A6AAA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1004 446 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>Create a ROI around the tumor</li>
<li>Experiment with the threshold to make the tumor solid, but the surrounding tissue transparent</li>
<li>CTRL+left click into the tumor</li>
<li>Wait some moments for the segmentation</li>
</ul>
<p>Next, you can call the “Segment Statistics” for the tumor volume.<br>
In this example, lung segments and airways were created by using the “Grow from Seeds” function of the “Segment Editor”.</p>
<p>Best regards<br>
Rudolf</p>

---

## Post #12 by @Mostafa2020 (2021-06-01 13:40 UTC)

<p>Thanks, Rduolf. It was very helpful. I also think about the way the distributions of voxels inside the ROI. Is there any options in 3D Slicer to do it? Thanks in advance.</p>

---

## Post #13 by @lassoan (2021-06-08 23:38 UTC)

<p>You can compute intensity distribution histogram in a segment as shown in this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">example in the script repository</a>.</p>

---
