---
topic_id: 41505
title: "How To Change Dose X Axis Increments On A Dose Volume Histog"
date: 2025-02-05
url: https://discourse.slicer.org/t/41505
---

# How to change Dose (X-axis) increments on a Dose-Volume-Histogram?

**Topic ID**: 41505
**Date**: 2025-02-05
**URL**: https://discourse.slicer.org/t/how-to-change-dose-x-axis-increments-on-a-dose-volume-histogram/41505

---

## Post #1 by @Jeremy_Fockenier (2025-02-05 02:18 UTC)

<p>Hello fellow Slicers,</p>
<p>I am currently testing Monte-Carlo simulations on a synthetic lung with a proton beam (all input files are in DICOM) and am trying to output a DVH file. However, since the DVH program seems to only register voxel doses on a 0.1 Gy increment and my max voxel dose is much below that, I end up with a problem : my DVH table simply states that 100% of the selected volume receives at least 0 Gy and 0% of that same volume receives 0.1 Gy.</p>
<p>Is there a way to change the default increments of 0.1 Gy?</p>
<p>Thanks in advance,</p>
<p>Jeremy</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c5147e9558b77451bb1a29e9cc737ff5b70b03b.png" data-download-href="/uploads/short-url/fsdI2yvjGHnfOkjwspKM41bp0in.png?dl=1" title="Capture d’écran du 2025-02-04 15-37-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5147e9558b77451bb1a29e9cc737ff5b70b03b_2_690x390.png" alt="Capture d’écran du 2025-02-04 15-37-01" data-base62-sha1="fsdI2yvjGHnfOkjwspKM41bp0in" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5147e9558b77451bb1a29e9cc737ff5b70b03b_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5147e9558b77451bb1a29e9cc737ff5b70b03b_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5147e9558b77451bb1a29e9cc737ff5b70b03b_2_1380x780.png 2x" data-dominant-color="BEB9B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran du 2025-02-04 15-37-01</span><span class="informations">1854×1048 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Jeremy_Fockenier (2025-03-25 18:57 UTC)

<p>I have since resolved this issue thanks to this answer to a previous question :</p>
<aside class="quote quote-modified" data-post="7" data-topic="4648">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/dose-accumulation-weighting-slicerrt/4648/7">Dose accumulation weighting SlicerRT</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    By downscaling the dose by a factor of 33.3x, computing the histogram, and then upscaling the result, you essentially scale up histogram quantization error by 33.3x. 
To maintain error at the same level, despite of this aggressive scaling, you need to set a smaller histogram bin width (=DVH step size). You can get current step size by opening the Python console (Ctrl-3) and typing: 
slicer.modules.dosevolumehistogram.logic().GetStepSize()

To set a new value, type for example this: 
slicer.modul…
  </blockquote>
</aside>

<p>Jeremy</p>

---
