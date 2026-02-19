---
topic_id: 36950
title: "Workflow For Segmentation With Vmtk Vesselness Filtering"
date: 2024-06-22
url: https://discourse.slicer.org/t/36950
---

# Workflow for segmentation with Vmtk Vesselness Filtering

**Topic ID**: 36950
**Date**: 2024-06-22
**URL**: https://discourse.slicer.org/t/workflow-for-segmentation-with-vmtk-vesselness-filtering/36950

---

## Post #1 by @Olivier (2024-06-22 10:15 UTC)

<p>Hello,</p>
<p>I am trying to figure out a workflow to segment connective tissue in muscle volume reconstructions from ultrasound.</p>
<p>What I thought of doing is:</p>
<ol>
<li>segment the muscle</li>
<li>apply a vesselness filter to the segmented volume <strong>only</strong></li>
<li>segment (threshold?) the connective tissue highlighted in the previous step</li>
<li>visualise the segment connective tissue in 3D</li>
</ol>
<p>I am however unsure about how to best do steps 2 and 3. I tried to look at online tutorials and posts from this forum but couldn’t figure it out.<br>
Any pointer would be much appreciated!</p>

---

## Post #2 by @lassoan (2024-06-22 12:03 UTC)

<p>Ultrasound is usually very noisy and has many artifacts, so if you use simple classic segmentation methods (e.g., threshold, grow from seeds,…) then the results may not be good enough.</p>
<p>Vesselness filtering slightly improves signal to noise ratio of tubular structures but usually not that much so that you could then extract vessels by simple global thresholding.</p>
<p>If you pay a few sample images and your preliminary processing results then we may be able to give you more specific advice. But most likely you will need to invest significant manual efforts to create good segmentations, which you can then use to train fully automatic AI segmentation models.</p>

---

## Post #3 by @Olivier (2024-06-22 14:22 UTC)

<p>Thanks!</p>
<p>Yes, automating muscle segmentation is probably not fully possible without AI. I am not there yet. Here I just want to explore what I get from the reconstructed volumes with a simple vesselness filter. The goal is to see whether I can segment - and eventually measure the orientation of - the connective tissue between fibres.</p>
<p>Not sure how to share an nrrd file but to illustrate the kind of reconstruction that I have, here is a typical transversal view of a muscle:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fe7ea4aecad61b29d5bb72c246aee377b02e479.jpeg" data-download-href="/uploads/short-url/kx39zaCV9bx1n2tsUsyEDJxeRst.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe7ea4aecad61b29d5bb72c246aee377b02e479_2_690x353.jpeg" alt="image" data-base62-sha1="kx39zaCV9bx1n2tsUsyEDJxeRst" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe7ea4aecad61b29d5bb72c246aee377b02e479_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fe7ea4aecad61b29d5bb72c246aee377b02e479_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fe7ea4aecad61b29d5bb72c246aee377b02e479.jpeg 2x" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1320×676 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would then segment the muscle itself and look for a way to implement the steps listed in my previous post.</p>

---

## Post #4 by @lassoan (2024-06-23 22:29 UTC)

<p>Frangi’s vesselness filter method takes several steps to suppress direction dependence of tube detection. Therefore, if the goal is to determine direction of fibers then I would not recommend using vesselness filter.</p>
<p>Instead, you can use those simple convolutional filters that are used internally in the vessel enhancement algorithm. Each filter can enhance tubular structures in a certain direction at certain size scale.</p>

---
