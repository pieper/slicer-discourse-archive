---
topic_id: 35313
title: "Determine Labels Based On Rt Structure"
date: 2024-04-05
url: https://discourse.slicer.org/t/35313
---

# Determine labels based on RT structure

**Topic ID**: 35313
**Date**: 2024-04-05
**URL**: https://discourse.slicer.org/t/determine-labels-based-on-rt-structure/35313

---

## Post #1 by @anhthu (2024-04-05 14:20 UTC)

<p>Hi everyone,</p>
<p>I need to define labels based on RT structure similar to the example below to perform MC simulation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a70c9caf3674b21f6448fe85ad0279f43442a48b.jpeg" data-download-href="/uploads/short-url/nPML2Epils2jpcalUsPKlvbSGLx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a70c9caf3674b21f6448fe85ad0279f43442a48b_2_690x323.jpeg" alt="image" data-base62-sha1="nPML2Epils2jpcalUsPKlvbSGLx" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a70c9caf3674b21f6448fe85ad0279f43442a48b_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a70c9caf3674b21f6448fe85ad0279f43442a48b_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a70c9caf3674b21f6448fe85ad0279f43442a48b_2_1380x646.jpeg 2x" data-dominant-color="8B93C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1507×706 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to know the specific tags for each agency for example:<br>
MaterialTagNumbers = 7 0 1 2 3 4 5 6<br>
MaterialNames = 7 “TG186Water” “TG186Water” “TG186CorticalBone” “TG186MeanMaleSoftTissue” “TG186Prostate”  “Air” “TG186MeanMaleSoftTissue”</p>
<p>Thank you for your help,<br>
Thu</p>

---

## Post #2 by @cpinter (2024-04-08 09:40 UTC)

<p>You can export the segmentation to a labelmap in the Segmentations module (or right-clicking the segmentation in the Data module). You won’t have direct control over the labels, but you’ll be able to see them in the Data Probe (bottom left corner) after showing the labelmap in the 2D views and moving the mouse over the structures. Then you can edit the labels in your MC script to have a match.</p>

---

## Post #3 by @anhthu (2024-04-08 13:04 UTC)

<p>Your advice is really helpful to me.<br>
Thank you for your help.</p>

---
