---
topic_id: 19623
title: "Assign Multiple Segment To Specific Area Roi"
date: 2021-09-11
url: https://discourse.slicer.org/t/19623
---

# Assign multiple segment to specific area / ROI

**Topic ID**: 19623
**Date**: 2021-09-11
**URL**: https://discourse.slicer.org/t/assign-multiple-segment-to-specific-area-roi/19623

---

## Post #1 by @shubham_agrawal (2021-09-11 17:44 UTC)

<p>Hi,<br>
I wanted to mark a specific area / ROI and assign multiple segments to it, I even thought of using logical operator but it copies complete segment. Kindly suggest some methods.</p>

---

## Post #2 by @lassoan (2021-09-12 11:46 UTC)

<p>Do you want to split a segment to multiple regions? Could you attach an annotated screenshot or illustration that explains what you want to achieve?</p>
<p>What is the high-level goal, clinical problem that you are trying to solve?</p>

---

## Post #3 by @shubham_agrawal (2021-09-15 10:04 UTC)

<p>No,<br>
I have to classify type of fracture, so for example a area selected have to classified in type of fracture, location etc etc.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fcb514a32bf96cc1bd3fc9776a86ef2ebf7aa10.jpeg" data-download-href="/uploads/short-url/6OO2UoiGKRD3JodgAvjEj88j1Ti.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fcb514a32bf96cc1bd3fc9776a86ef2ebf7aa10_2_690x388.jpeg" alt="image" data-base62-sha1="6OO2UoiGKRD3JodgAvjEj88j1Ti" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fcb514a32bf96cc1bd3fc9776a86ef2ebf7aa10_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fcb514a32bf96cc1bd3fc9776a86ef2ebf7aa10_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fcb514a32bf96cc1bd3fc9776a86ef2ebf7aa10_2_1380x776.jpeg 2x" data-dominant-color="4E4F55"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Now this area should have multiple segments as shown in segment editor. It should have both the segment.</p>

---

## Post #4 by @lassoan (2021-09-15 13:33 UTC)

<p>You can specify anatomical region using standard DICOM terminology (by double-clicking on the colored rectangle). You can specify additional terms in a text file (in DCMQI anatomical region json format) if the terms in the built-in dictionaries are not sufficient.</p>
<p>For store additional findings, such as fracture type, I see two options.</p>
<p>Option A: You may use segment properties. These are key:value pairs that can be added to each segment (there is no limitation on the number or length of these). The attributes are stored in the saved .seg.nrrd file and can be easily accessed in any software, for example using <a href="https://pypi.org/project/slicerio/">slicerio</a> Python package. This is a general-purpose feature and we have not added user interface for it in the Segment Editor, but you can create a short Python script that allows adding labels using some small GUI or keyboard shortcuts. We can help you implementing this if you are willing to give it a try.</p>
<p>Option B. You can use a very low-tech way of specifying all kinds of metadata for segments. You can establish a convention for naming the segments. For example, of you specify that <code>FT</code> means fracture type, and <code>ST</code>, <code>TC</code>, <code>IT</code>, … means subcapital, transcervical, intertrochanteric, … then the segment name could be something like <code>femur left FT=TC</code> (or if you choose the values to be unique then it could be simply <code>femur left TC</code>).</p>
<p>I would recommend Option A for a larger study with multiple raters, especially if they work at different institutions; as it can enforce correct, consistent labeling. Option B may be sufficient work if you do all the labeling and you don’t want to spend any time with Python scripting.</p>

---
