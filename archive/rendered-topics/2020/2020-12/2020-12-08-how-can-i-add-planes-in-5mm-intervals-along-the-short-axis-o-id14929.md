---
topic_id: 14929
title: "How Can I Add Planes In 5Mm Intervals Along The Short Axis O"
date: 2020-12-08
url: https://discourse.slicer.org/t/14929
---

# How can I add planes in 5mm intervals along the short-axis of a heart from apex to base?

**Topic ID**: 14929
**Date**: 2020-12-08
**URL**: https://discourse.slicer.org/t/how-can-i-add-planes-in-5mm-intervals-along-the-short-axis-of-a-heart-from-apex-to-base/14929

---

## Post #1 by @jsalas424 (2020-12-08 01:12 UTC)

<p>Hello,</p>
<p>I’ve generated a 3D shell of the left ventricle of a heart using the IGT → Markups to Model module. I<br>
have fiducial points marked in the model that correspond to points of scientific interest in an excised heart.</p>
<p>I want to cut planes in 5mm intervals from apex to base in the model. I have cut the excised heart in 5mm increments from apex to base and want to eventually figure out in which slice # I can find respective fiducial points.</p>
<p>Here’s what the model looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/231840fd768223fbb57c23c807d21f25d24c357e.png" data-download-href="/uploads/short-url/50sFRe71s78np47YO9ZXp51Vho2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/231840fd768223fbb57c23c807d21f25d24c357e_2_690x431.png" alt="image" data-base62-sha1="50sFRe71s78np47YO9ZXp51Vho2" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/231840fd768223fbb57c23c807d21f25d24c357e_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/231840fd768223fbb57c23c807d21f25d24c357e_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/231840fd768223fbb57c23c807d21f25d24c357e_2_1380x862.png 2x" data-dominant-color="665E6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2880×1800 446 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-12-08 01:18 UTC)

<p>You can simply use the divide the third (S) coordinate of the fiducial point coordinate to get the slice index. If you use oblique slices (not aligned to patient axes directions) then you can apply a linear transform first that transforms the point coordinates to this rotated coordinate system and use these transformed coordinate values.</p>

---

## Post #3 by @jsalas424 (2020-12-08 03:21 UTC)

<p>Thank you for your answer! I’m not certain I completely understand, is there any documentation or examples for performing this divide? What modules would accomplish this?</p>
<p>I will definitely need to perform a linear transformation but am already comfortable with that aspect.</p>

---

## Post #4 by @lassoan (2020-12-08 04:09 UTC)

<p>No modules are needed, you should be able to implement what you need with a couple of lines of Python code, in a Slicer Jupyter notebook or just by copy-pasting the code into the Python console in Slicer. The division is just a simple division of a number (third coordinate value) by another (interval of 5mm).</p>

---

## Post #5 by @jsalas424 (2020-12-08 13:37 UTC)

<p>Gotcha, in which case I have a more rudimentary question since I have not interacted with the python side of this.</p>
<ol>
<li>
<p>How do I export my model to python? I have thus far created this all with the GUI.</p>
</li>
<li>
<p>How do I establish the apex of this model in the code? I’m guessing that this matrix will be part of the code and I’ll just the minimum value of the relevant plane and go from there?</p>
</li>
</ol>

---

## Post #6 by @lassoan (2020-12-09 01:38 UTC)

<p>All the models are already “in Python”. If you want to get point coordinates as numpy array then you can use <code>slicer.util.arrayFromModelPoints()</code>. You can get minimum coordinate value using standard numpy functions (for example, <code>min</code>). There are lots of examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---
