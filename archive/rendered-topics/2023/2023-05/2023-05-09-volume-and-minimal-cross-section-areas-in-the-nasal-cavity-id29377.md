---
topic_id: 29377
title: "Volume And Minimal Cross Section Areas In The Nasal Cavity"
date: 2023-05-09
url: https://discourse.slicer.org/t/29377
---

# Volume and minimal cross section areas in the nasal cavity

**Topic ID**: 29377
**Date**: 2023-05-09
**URL**: https://discourse.slicer.org/t/volume-and-minimal-cross-section-areas-in-the-nasal-cavity/29377

---

## Post #1 by @AKue (2023-05-09 10:50 UTC)

<p>Hello! I would like to segment the nasal cavity with the aim to get:</p>
<ul>
<li>the total volume of the whole nasal cavity</li>
<li>the volume of different parts of the nasal cavity</li>
<li>the minimal cross section areas of the right and the left nasal cavity?</li>
</ul>
<p>How would you do it? I’m relatively new to 3D Slicer.<br>
Would you start by defining the nasal cavity with thresholding? Or is it better to set points, landmarks and planes to define the cavity?<br>
Thresholding is quite difficult, as the nasal cavity has no proper boundaries nor a starting or end point, as it’s open to the outside.</p>
<p>Is there a way to define different planes and then to get the volume between them? And is there a way to get the program to calculate the minimal cross section area of a volume?</p>
<p>Many thanks for your help!!</p>

---

## Post #2 by @lassoan (2023-05-10 03:02 UTC)

<p>Probably the easiest is to segment the nasal cavity (e.g., Draw tube effect, with masking settings set to paint only inside air), then you can extract the centerline using “Extract centerline” module and get the cross-sectional areas using “Cross-section analysis module”. These tools are provided by <em>SegmentEditorExtraEffects</em> and <em>VMTK</em> extensions.</p>

---

## Post #4 by @lassoan (2023-05-11 22:50 UTC)

<aside class="quote no-group quote-post-not-found" data-username="AKue" data-post="3" data-topic="29377">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> AKue:</div>
<blockquote>
<p>What is the easiest way, to get the „Draw tube“ effect only painting the inside air?</p>
</blockquote>
</aside>
<p>Use Threshold effect to find intensity range of air then click “use for masking”.</p>

---

## Post #6 by @lassoan (2023-05-13 01:39 UTC)

<p>I may be possible that the “Draw tube” effect Ig ores intensity thresholding. I’ll check.</p>
<p>In the meantime, you can erase the non-air regions using Erase effect, as that effect respects editable intensity range for sure.</p>

---

## Post #8 by @lassoan (2023-05-18 18:55 UTC)

<p>After you segment the nasal cavity, you can extract the centerline using “Extract centerline” module and get the cross-sectional areas using “Cross-section analysis module”. These tools are provided by <em>SegmentEditorExtraEffects</em> and <em>VMTK</em> extensions.</p>
<p>A lot may depend on the complexity of the cavity, so it would be useful if you could share a sample data set (if cannot share your own data then you can get a similar image from “Sample Data” module).</p>

---

## Post #10 by @lassoan (2023-05-31 14:32 UTC)

<p>If you have one segmentation and specify two endpoints then you’ll get only one (the best) centerline between them. To get an alternative route, I would recommend to use a single inlet point and two slightly different outlet points (each closer to the nasal cavity on one side). If you really want to use the exact same inlet and outle points then you could extract one centerline, edit the segmentation to disrupt that path (e.g., erase a part of it), and then extract centerline on this modified segmentation.</p>

---
