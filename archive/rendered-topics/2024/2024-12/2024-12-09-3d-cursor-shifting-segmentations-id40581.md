---
topic_id: 40581
title: "3D Cursor Shifting Segmentations"
date: 2024-12-09
url: https://discourse.slicer.org/t/40581
---

# 3D Cursor shifting segmentations

**Topic ID**: 40581
**Date**: 2024-12-09
**URL**: https://discourse.slicer.org/t/3d-cursor-shifting-segmentations/40581

---

## Post #1 by @yasmin.mcquinlan (2024-12-09 14:42 UTC)

<p>Slicer v5.6.2</p>
<p>When holding down the Shift Key + Dragging cursor, in either the sagittal or coronal view, the segmentation present on the axial shifts away from the segmented anatomy visualised on the Source Volume.</p>
<p>Using the Interactive Plane Intersection tool, with the crosshairs, you can see where the cursor is on one plane and relative to the others as well – but this also appeared to shift the segmentations.</p>
<p>So far, the only way to resolve this, is to:</p>
<ol>
<li>drag the 3D cursor again until the annotation and image are matched (but this is only visually, and is done manually, not automatically)</li>
<li>reopening and overlaying the image again, and deleting the old one (then the image and segmentation matches automatically).</li>
</ol>
<p>This is occurring across a number of CT volumes. The tags SliceThickness (2.5mm) and SpacingBetweenSlices (3.27mm) are the same across these volumes.</p>
<p>Any help/ideas on this is greatly appreciated!</p>

---

## Post #2 by @lassoan (2024-12-09 15:03 UTC)

<p>While this behavior may be surprising first, this is all good and there is no actual shift of the segmentation. What you see is the difference between linear interpolation (applied to the grayscale image) and nearest neighbor interpolation (applied to the segmentation). In the middle of the voxel they match, but as you get farther from the center a deviation may be visible. You can enable display of slice intersections and zoom in to see all the details. Usually the difference is negligible. You can only see a difference if shape of the voxels in the segmentation is not cube-shaped but stick-like. For example. If you have an image with a spacing of 0.7x0.7x2.5mm voxel size then your voxels are long sticks, and obviously they can represent 3D shapes very poorly.</p>
<p>Your data acquisition and processing can be improved at many different levels:</p>
<ul>
<li>A. Ask your imaging technologist to acquire higher-resolution images. Often they actually acquire high-resolution images but then they create 3 image, each with stick-shaped voxels (each having low resolution along one axis), because this saves a little disk space and when humans are reviewing the images they don’t mind. Of course, this is really bad for any 3D processing. If this is the case, you may just need to request to archive the original thin-slice images for patients participating in your study (or at least don’t delete it immediately and then you go and fetch the thin-slice images before they remove them from the scanner).</li>
<li>B. Resample the input image <em>before</em> segmentation to have the same resolution along all axes. It is very easy to do it in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">Crop Volumes module</a>.</li>
<li>C. Resample the segmentation <em>after</em> segmentation is completed, using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">Specify Geometry</a> button.</li>
<li>D. Do not resample anything, just switch to show the interpolated segmentation in 2D views (Segmentations module → Display → Advanced → Representation in 2D views → Closed surface).</li>
</ul>
<p>These solutions are ordered, the first (A) is the best (you preserve the most information and get the highest quality results), and D is the worst (you work with anisotropic data all the way, and just interpolate in the end for display).</p>

---

## Post #3 by @yasmin.mcquinlan (2024-12-09 15:19 UTC)

<p>Thank you for your quick response, Andras <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20">.</p>
<p>I’ll have to check with my team to see if it is suitable for us to resample, we are using retrospective data for research.</p>
<p>It was more disconcerting for my annotators, when they use the intersection tool as they are annotating, because they <em>appear</em> to be seeing a shift. Then they’re not quite sure where to annotate next or if they have the boundaries right (as you describe in your response, this is more visible at the edges of the annotation). So they feel the need to reload the image, before continuing with their work.</p>
<p>Funny thing is, our last batch of data was acquired using a similar protocol, with identical spacing and thickness and we didn’t see a problem with it. It’s just this new batch which has left us scratching our heads!</p>
<p>If resampling turns out not to be an option for us, is there an easier way of ‘refreshing’ the viewer, instead of having to reload the image?</p>

---

## Post #4 by @lassoan (2024-12-09 15:29 UTC)

<aside class="quote no-group" data-username="yasmin.mcquinlan" data-post="3" data-topic="40581">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/9fc29f/48.png" class="avatar"> yasmin.mcquinlan:</div>
<blockquote>
<p>If resampling turns out not to be an option for us, is there an easier way of ‘refreshing’ the viewer, instead of having to reload the image?</p>
</blockquote>
</aside>
<p>There could be, but I don’t even want to think about it. It is great that this mismatch made you realize that you had a mistake in your data processing pipeline. This should not be ignored.</p>
<p>If you want to use this segmentation for AI training then you must resample anyway, because first step of AI training is that your images are resampled to have cubic voxels. If your segmentation has stick-shaped voxels then you will have suboptimal quality input data for the AI training.</p>
<p>I would recommend Option B (resample the source image), as it is easier to understand for annotators when each source image voxel corresponds to one voxel in the segmentation’s binary labelmap representation.</p>

---

## Post #5 by @pieper (2024-12-09 15:29 UTC)

<p>If you think something is different about this batch of data please include screenshots of the difference you are seeing.  Also see if you can reproduce the issue with public data to show exactly what you are seeing.</p>

---
