---
topic_id: 22089
title: "Vessel Quantification From Micro Ct Images"
date: 2022-02-21
url: https://discourse.slicer.org/t/22089
---

# Vessel quantification from micro-CT images

**Topic ID**: 22089
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/vessel-quantification-from-micro-ct-images/22089

---

## Post #1 by @Adela_Garcia (2022-02-21 17:15 UTC)

<p>Hi, I would like to quantified vascular vessel ( number of vessels, vessel diameter…) in mouse hind limd but first I need to remove the bone.The images to quantified are acquired with micro-CT. Which tools of 3D SLICER are recommend to slip the bones form the vascular system?<br>
Thank you.</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2022-02-21 17:18 UTC)

<p>This question was posted and got answered here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://forum.image.sc/t/vessel-quantification-micro-ct/63598/2?u=lassoan">
  <header class="source">
      <img src="https://aws1.discourse-cdn.com/business4/uploads/imagej/optimized/2X/4/4b3d366e9bd1c4abfb68ca23f7596edd29cb2f4a_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://forum.image.sc/t/vessel-quantification-micro-ct/63598/2?u=lassoan" target="_blank" rel="noopener" title="04:11PM - 21 February 2022">Image.sc Forum – 21 Feb 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:480/360;"><img src="https://aws1.discourse-cdn.com/business4/uploads/imagej/original/3X/f/6/f636b187edd09ba067da85145c24d43f0acfedab.jpeg" class="thumbnail" width="480" height="360"></div>

<h3><a href="https://forum.image.sc/t/vessel-quantification-micro-ct/63598/2?u=lassoan" target="_blank" rel="noopener">Vessel quantification micro-CT</a></h3>

  <p>There are several segmentation tools in 3D Slicer’s Segment Editor that can separate vessels from bones, even if they have the same intensity and very close to each other.  For cases where the vessel contrast is strong and vessels are not that close...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>To avoid parallel discussions, let’s continue it there.</p>

---

## Post #3 by @Adela_Garcia (2022-03-08 19:51 UTC)

<p>Hi,</p>
<p>I have already a segment with vessel of hind limb. Now  I try to quantified number of vessels, vessel diameter, but I can not find the plugging. Do you know How I can do it?</p>
<p>Thanks in advance!</p>
<p>Adela</p>

---

## Post #4 by @lassoan (2022-04-17 03:49 UTC)

<p>You can use VMTK extension in latest Slicer Preview Release. You can get vessel branches and radius values in <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/ExtractCenterline.md">Extract Centerline module</a>.</p>

---
