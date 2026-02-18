# Multi-modality/label Brain Tumor segmentation

**Topic ID**: 9977
**Date**: 2020-01-28
**URL**: https://discourse.slicer.org/t/multi-modality-label-brain-tumor-segmentation/9977

---

## Post #1 by @brt2002 (2020-01-28 04:45 UTC)

<p>I’m trying to re-manually segment tumors from the BRATS dataset and attempting to follow the tutorial from here: <a href="https://www2.imm.dtu.dk/projects/BRATS2012/Jakab_TumorSegmentation_Manual.pdf" rel="nofollow noopener">https://www2.imm.dtu.dk/projects/BRATS2012/Jakab_TumorSegmentation_Manual.pdf</a></p>
<p>The motivation of the tutorial is to create a labelmap that is derived from 2 different sequences. It is outdated and I’m currently trying to  re-adapt it for 4.X. However, the main idea is as follows.</p>
<p>Use one sequence (FLAIR/T2) to wholy everything of segment everything. Then use another sequence (t1gd) to segment something within this area, and then do T2 (whole area) minus T1gd to create a third label. I’m one week in, and I’m at my wits end.</p>
<p>The tutorial recommends paint + slice interpolation, but region growing makes more intuitive sense to me. Any idea how I can adapt that for this tutorial? Or if there are better tutorials available?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-01-28 04:56 UTC)

<p>The tutorial is way outdated. We have incomparably better tools in Slicer now.</p>
<p>Use Segment Editor module for segmentation. You can switch master volume (the volume that is used by effects that need intensity values as input) any time. You can use masking section (near the bottom of Segment editor module panel) to restrict editing to a certain region (intensity range, segment, combination of segments, etc.).</p>
<aside class="quote no-group" data-username="brt2002" data-post="1" data-topic="9977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/9de053/48.png" class="avatar"> brt2002:</div>
<blockquote>
<p>The tutorial recommends paint + slice interpolation, but region growing makes more intuitive sense to me</p>
</blockquote>
</aside>
<p>If there is good contrast difference between regions you need to segment then “Grow from seeds” effect will work better (less manual work needed) than “Fill between slices”.</p>
<p>You may find the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Neurosurgical_Planning_Tutorial">neurosurgical planning tutorial</a> (and other segmentation tutorials on that page) useful.</p>
<p>It would be great if you could create an update version of Andras Jakab’s tutorial and share it. We could help you with tips and fine-tuning the workflow.</p>

---

## Post #3 by @brt2002 (2020-01-28 16:35 UTC)

<p>Sure that sounds good. I’ve got it working as well.</p>
<p>I’ll send you an email about it!</p>

---

## Post #4 by @pieper (2020-01-28 16:59 UTC)

<p>It’ll be great to see this updated - thanks for working on it!</p>
<p>I also suggest you consider oversampling the segmentation compare to the labelmap.  Those BRATS segmentations have been used in a lot to train deep learning models and it would help to generate the most faithful anatomical models possible (oversample the MRs too if you need the labels to match the background image grid).</p>

---
