---
topic_id: 5835
title: "Copy Specific Slices From Existing Segments To Single Binary"
date: 2019-02-19
url: https://discourse.slicer.org/t/5835
---

# Copy specific slices from existing segments to single Binary Map

**Topic ID**: 5835
**Date**: 2019-02-19
**URL**: https://discourse.slicer.org/t/copy-specific-slices-from-existing-segments-to-single-binary-map/5835

---

## Post #1 by @triple_axel (2019-02-19 21:55 UTC)

<p>What I would specifically like to do is to get the 2D segments from specific slices from two different segmentations onto the same binary label map. (let’s say two slices from the axial direction).</p>
<p>Using those two specific slices, I want to automate the “fill between slices” widget in segment editor to create a smooth volume (which I have figured out already).</p>
<p>The intent of this would essentially be to make a segmentation look like one complete volume then two separate ones for a simulation.</p>
<p>I was wondering if anyone had any idea of how to do the first step using python code?</p>
<p>Thanks</p>

---

## Post #3 by @triple_axel (2019-02-20 17:07 UTC)

<p>If it is not possible to specify a slice from a segment, is there any way to interpolate between two segments rather then two slices?</p>

---

## Post #4 by @lassoan (2019-02-20 17:23 UTC)

<p>I don’t understand exactly what you would like to do, but it all sounds very easy, using existing Segment Editor effects. You can copy/move segments between segmentations and you can combine them using logical operators effect. See examples in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations</a></p>

---

## Post #5 by @triple_axel (2019-02-20 17:29 UTC)

<p>Hi, sorry I was quite convoluted in my initial question.</p>
<p>I got to the part where I combined two segments into one as seen below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61ee0c7984c981f277312c7f4f84ceedcd737493.jpeg" data-download-href="/uploads/short-url/dYkkyZwCRJdM8nfT6mLx2Fk30zh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61ee0c7984c981f277312c7f4f84ceedcd737493_2_257x500.jpeg" alt="image" data-base62-sha1="dYkkyZwCRJdM8nfT6mLx2Fk30zh" width="257" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61ee0c7984c981f277312c7f4f84ceedcd737493_2_257x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61ee0c7984c981f277312c7f4f84ceedcd737493_2_385x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/61ee0c7984c981f277312c7f4f84ceedcd737493_2_514x1000.jpeg 2x" data-dominant-color="3E3F3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">550×1070 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But what I would like to do is find a way to automate a method in “filling the gap” between the seperate segments. I thought of using the “fill in between slices” method, but that requires actually using paint to paint on two different slices to fill in the gap, which is not automatic. Is there any way to do this automatically?</p>

---
