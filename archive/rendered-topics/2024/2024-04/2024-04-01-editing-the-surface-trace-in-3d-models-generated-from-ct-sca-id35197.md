---
topic_id: 35197
title: "Editing The Surface Trace In 3D Models Generated From Ct Sca"
date: 2024-04-01
url: https://discourse.slicer.org/t/35197
---

# Editing the Surface Trace in 3D Models Generated from CT Scan Segmentations

**Topic ID**: 35197
**Date**: 2024-04-01
**URL**: https://discourse.slicer.org/t/editing-the-surface-trace-in-3d-models-generated-from-ct-scan-segmentations/35197

---

## Post #1 by @rcapozza (2024-04-01 13:41 UTC)

<p>I’ve been working with 3D Slicer to generate 3D surface models from CT scan segmentations of bones. After completing the segmentation and generating the 3D surface, I’ve noticed that for each slice, the generated surface trace is visible. Specifically, this surface trace is displayed in green in the images I’ve produced.</p>
<p>My question is: Is there a way to edit or adjust this surface trace in the generated 3D model? I’m looking to refine the appearance of the surface for a project I’m working on, and any guidance on how to achieve this within 3D Slicer would be greatly appreciated.</p>
<p>Thank you in advance for any help or advice you can offer.</p>
<p>Best regards, Ricardo</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73cab35f94b65ba2ceb80323c5cd911db66c3e42.jpeg" data-download-href="/uploads/short-url/gwlbZ2IsUThZTC6Xw5VZAdZJjMe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73cab35f94b65ba2ceb80323c5cd911db66c3e42_2_690x369.jpeg" alt="image" data-base62-sha1="gwlbZ2IsUThZTC6Xw5VZAdZJjMe" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73cab35f94b65ba2ceb80323c5cd911db66c3e42_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73cab35f94b65ba2ceb80323c5cd911db66c3e42_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73cab35f94b65ba2ceb80323c5cd911db66c3e42_2_1380x738.jpeg 2x" data-dominant-color="8A8884"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1901×1017 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-04-01 14:12 UTC)

<p>Please describe the exact steps you do to get this model that you show in the screenshot.</p>

---

## Post #3 by @rcapozza (2024-04-01 14:40 UTC)

<p>The steps are:</p>
<ol>
<li>Create a new Segmentation.</li>
<li>Add a segment and select the Threshold method.</li>
<li>Set the threshold range (minimum and maximum).</li>
<li>Apply the changes.</li>
<li>In the Data View, select the Segmentation and export the visible segments to models.</li>
<li>Select the Segmentation models created and edit their properties.</li>
<li>Check the Visibility options for Slice Display.</li>
</ol>
<p>The window now displays the pathway generated for the current segmentation. To modify this pathway, is redefining the parameters of the segmentation method I used the only way?</p>

---

## Post #4 by @lassoan (2024-04-01 16:23 UTC)

<p>I’m not sure what you mean by “surface trace”. Do you mean “slice intersection” of a 3D model or segmentation?</p>
<p>Segmentation typically uses multiple representations - see details <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a>.In Segmentations module, you can choose to display “closed surface” representation in slice views, which may be what you attempted to describe.</p>
<p>We can provide help much more efficiently if you describe what is the purpose of generating 3D surface models - what is your clinical end goal?</p>

---

## Post #5 by @cpinter (2024-04-02 09:23 UTC)

<aside class="quote no-group" data-username="rcapozza" data-post="1" data-topic="35197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rcapozza/48/11682_2.png" class="avatar"> rcapozza:</div>
<blockquote>
<p>Is there a way to edit or adjust this surface trace in the generated 3D model?</p>
</blockquote>
</aside>
<p>I’ll assume that by surface trace you mean slice intersections in the 2D views. The way to edit this is by using Segment Editor. You can only edit the binary labelmap representation, and then the closed surface will be automatically updated (please read the basics of this following <a class="mention" href="/u/lassoan">@lassoan</a> 's link above). You can show the closed surface’s slice intersection in the Segmentations module:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea467f7ba8163d3e8ad3b6c3084878bdeff1ea4.png" alt="image" data-base62-sha1="8W9QblZp9WAm7mFMuk239nTm8Vm" width="519" height="370"></p>
<p>If you need “better control” over this slice intersection, you can increase the resolution of the segmentation (see 1 in the image below), and/or reduce/disable surface smoothing (2).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e62a8ce874af72d89773dab1ce4c780af8252d4.png" alt="image" data-base62-sha1="kjBb0Gbmj3PrKsYUFypXZWO8pkU" width="528" height="97"></p>

---
