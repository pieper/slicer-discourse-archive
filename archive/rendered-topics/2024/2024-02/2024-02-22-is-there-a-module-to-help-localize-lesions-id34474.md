---
topic_id: 34474
title: "Is There A Module To Help Localize Lesions"
date: 2024-02-22
url: https://discourse.slicer.org/t/34474
---

# Is there a module to help localize lesions？

**Topic ID**: 34474
**Date**: 2024-02-22
**URL**: https://discourse.slicer.org/t/is-there-a-module-to-help-localize-lesions/34474

---

## Post #1 by @brynn_martinsons (2024-02-22 14:46 UTC)

<p>Operating system:<br>
Slicer version:5.4.0<br>
Expected behavior:<br>
I would like to pinpoint the location of the lesion by 3Dslicer. It is OK to only locate in the lobes of the brain, here are the steps I envisioned</p>
<ol>
<li>
<p>Prepare a normal anatomical template and align the patient’s skull to the normal template.</p>
</li>
<li>
<p>Sketch the location of the lesion on the aligned cranium.</p>
</li>
<li>
<p>Overlap the mask of the lesion with the mask on the normal cranial template, and compare the size of the lesion in different locations (volume or percentage or other indicators that can be compared ).</p>
</li>
<li>
<p>Determine the location of the tumor based on comparation.</p>
</li>
</ol>
<p>Actual behavior:</p>
<ol>
<li>
<p>The cranial and lesion edges after alignment are not clear, and localization may be shifted</p>
</li>
<li>
<p>No module or method can be found to realize the  step 4 above</p>
</li>
</ol>
<p>For the above reasons I would like to know if the steps I envisioned are feasible, and I’m hoping any experienced 3Dslicer users can give me some advice on whether or not to tweak the steps of the implementation, or recommend some modules or tutorials, thanks.</p>

---

## Post #2 by @Maryam_Riazi (2024-06-21 16:58 UTC)

<p>I have also the same question.<br>
Did you find anything?</p>

---

## Post #3 by @lassoan (2024-06-21 19:08 UTC)

<aside class="quote no-group" data-username="brynn_martinsons" data-post="1" data-topic="34474">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brynn_martinsons/48/69442_2.png" class="avatar"> brynn_martinsons:</div>
<blockquote>
<p>The cranial and lesion edges after alignment are not clear, and localization may be shifted</p>
</blockquote>
</aside>
<p>If the image is correctly registered to the anatomical template then the alignment is correct. Lesions can be segmented on the original image (before registering to the template) and the transformation that aligns the image to the template can be applied to the segmentation as well.</p>
<aside class="quote no-group" data-username="brynn_martinsons" data-post="1" data-topic="34474">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brynn_martinsons/48/69442_2.png" class="avatar"> brynn_martinsons:</div>
<blockquote>
<p>No module or method can be found to realize the step 4 above</p>
</blockquote>
</aside>
<p>There are many ways to do it already, even without any custom scripting. For example, you can copy the lesion into the template segmentation and invert it (in <code>Logical operators</code> effect, with <code>bypass masking</code> option disabled) and then remove this inverted lesion segment. The result is that all segments will be cleaned out except the region where they overlapped with the lesion. You can then go to <code>Segment statistics</code> module to get which template segments the lesion overlapped with (and the volume of overlap for each).</p>

---
