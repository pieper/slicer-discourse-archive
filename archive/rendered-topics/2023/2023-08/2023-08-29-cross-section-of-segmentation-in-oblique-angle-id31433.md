---
topic_id: 31433
title: "Cross Section Of Segmentation In Oblique Angle"
date: 2023-08-29
url: https://discourse.slicer.org/t/31433
---

# Cross section of segmentation in oblique angle

**Topic ID**: 31433
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/cross-section-of-segmentation-in-oblique-angle/31433

---

## Post #1 by @lukasvanderstricht (2023-08-29 13:32 UTC)

<p>Hello everyone!</p>
<p>I am interested in calculating cross section areas of my segmentations. I have a segmentation with 1 label (except for the background label) and I want to calculate the area of the cross section of my segment on certain slices. To do that, I installed the <code>Segment Cross-Section Area</code> module by installing the <code>Sandbox</code> extension in the Extension Manager. This works very well!!</p>
<p><strong>Problem</strong><br>
However, I now would want to measure the area of the intersection of my segment with a plane that is not perpendicular to any of the axes.  In other words, I would want to calculate the cross section area of my segmentation under a given oblique angle.<br>
In the <code>Segment Cross-Section Area</code> module you can however only choose between <code>slice</code>, <code>row</code> and <code>column</code>.</p>
<p><strong>What I have already tried</strong><br>
I have already tried a few things based on what I found online and what I already know you can do in Slicer from experience.</p>
<ul>
<li>
<p>I have tried simply rotating my volume and segmentation with the help of a transform. However, after this rotation, the results of the <code>Segment Cross-Section Area</code> module stay the same, meaning that this module doesn’t change its concept of <code>slices</code> along with the transform.</p>
</li>
<li>
<p>Even after hardening this transformation, no change could be noticed in the way <code>Segment Cross-Section Area</code> handles the volume and the segmentation.</p>
</li>
<li>
<p>I also tried adjusting my views using the <code>Reformat</code> module, but again the <code>Segment Cross-Section Area</code> module doesn’t take these adjustments into account.</p>
</li>
</ul>
<p><strong>Question</strong></p>
<p>Does anyone have an idea as to how to solve my problem?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2023-08-29 15:18 UTC)

<p>Hardening a linear transform only changes the mapping from pixels to physical space (ijkToRAS).  Instead, you can resample the volume to apply the transform.  See:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/resamplescalarvectordwivolume.html</a></p>

---

## Post #3 by @lukasvanderstricht (2023-08-30 07:47 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>This indeed does the trick!</p>
<p>Thanks a lot for the help!</p>
<p>Kind regards</p>

---

## Post #4 by @lukasvanderstricht (2023-08-31 07:33 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>The resampling module “Resample Scalar/Vector/DWI Volume” seems to work at first sight. The rotation works, but the result is cropped because it obviously cannot fit in the dimensions of the original volume anymore. When I just manually apply the rotation transformation to the volume, the whole volume is visible and no cropping is made.<br>
Is there any way to make the resample module convert the volume without loss of any part of the image?<br>
Below were the settings in the module that I used.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d485fda4c15fd1fbae035e663bfc27688c214f01.png" data-download-href="/uploads/short-url/uk4isjRbWfShsb6iR1WkqlJQ6o9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d485fda4c15fd1fbae035e663bfc27688c214f01_2_268x499.png" alt="image" data-base62-sha1="uk4isjRbWfShsb6iR1WkqlJQ6o9" width="268" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d485fda4c15fd1fbae035e663bfc27688c214f01_2_268x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d485fda4c15fd1fbae035e663bfc27688c214f01_2_402x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d485fda4c15fd1fbae035e663bfc27688c214f01_2_536x998.png 2x" data-dominant-color="E6E8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">594×1108 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance!</p>

---

## Post #5 by @chir.set (2023-08-31 09:25 UTC)

<aside class="quote no-group" data-username="lukasvanderstricht" data-post="1" data-topic="31433">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7ba0ec/48.png" class="avatar"> lukasvanderstricht:</div>
<blockquote>
<p>area of the cross section of my segment on certain slices</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lukasvanderstricht" data-post="1" data-topic="31433">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7ba0ec/48.png" class="avatar"> lukasvanderstricht:</div>
<blockquote>
<p>under a given oblique angle.</p>
</blockquote>
</aside>
<p>If you don’t want to transform your volume, there are alternative ways you might investigate.</p>
<ol>
<li>
<p>You may use ‘Stenosis measurement: 2D’ module in SlicerVMTK extension that you can install vie the ‘Extensions manager’. Reorient a slice view to your required obliqueness, place a fiducial point in your segment, click on it and apply. You can repeat after changing obliquity and location as required.</p>
</li>
<li>
<p>You may use ‘Cross-section analysis’ module in SlicerVMTK too in a hackish way. Place an open markups curve in your segment corresponding to your required obliqueness, with 2 control points only. Select this curve and your segment, then apply. It will calculate the cross-section area at each point between the 2 control points, by default 10 points. The ‘CE diameter’ output may not be of interest to you. You may also resample your curve to add more control points on the line (don’t move any control point, lock the curve quickly), so that the area can be measured 10x(number of control points -1).</p>
</li>
</ol>

---

## Post #6 by @lukasvanderstricht (2023-08-31 09:52 UTC)

<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a></p>
<p>Thank you for your response! The problem is that I eventually want to automate everything in my workflow using Python code. Placing markups is hence in my case not an easy thing to do.<br>
I think the transformation of my volume is the way to go for me. However, I’m struggling with some aspects of it, namely having correct dimensions after applying the resampling, such as described <a href="https://discourse.slicer.org/t/cross-section-of-segmentation-in-oblique-angle/31433/4">here</a>.</p>
<p>Thank you for taking your time to respond!</p>

---

## Post #7 by @pieper (2023-08-31 14:23 UTC)

<aside class="quote no-group" data-username="lukasvanderstricht" data-post="4" data-topic="31433">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7ba0ec/48.png" class="avatar"> lukasvanderstricht:</div>
<blockquote>
<p>the result is cropped because it obviously cannot fit in the dimensions of the original volume</p>
</blockquote>
</aside>
<p>You can use the CropVolume module first to create a buffer area around the volume so the rotation won’t crop.  You can eyeball this and set the ROI to fit, or in your code you could calculate the needed size based on the rotation.  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/batch.html#extracting-volume-patches-around-segments">This example</a> should help.</p>

---

## Post #8 by @lukasvanderstricht (2023-08-31 14:40 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Thank you for your answer!</p>
<p>In the meantime I have found another way to do it: by creating an empty volume node with the right dimensions, origin etc. and then using this volume as a reference volume.</p>
<p>Thank you for helping me!</p>

---
