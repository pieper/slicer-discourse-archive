---
topic_id: 15518
title: "Make Slicers Perpendicular To Other"
date: 2021-01-14
url: https://discourse.slicer.org/t/15518
---

# Make Slicers perpendicular to other

**Topic ID**: 15518
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/make-slicers-perpendicular-to-other/15518

---

## Post #1 by @manjula (2021-01-14 06:42 UTC)

<p>After reformating one slice is there a way to make the other 2 slicer exactly perpendicular to the original along the other two axes?</p>

---

## Post #2 by @lassoan (2021-01-14 14:09 UTC)

<p>I would recommend to rotate slice views by keeping them orthogonal. A few options for that:</p>
<ul>
<li>Option A: Rotate slices using Ctrl+Alt+Left-click-and-drag. This rotates slices so that they remain orthogonal.</li>
<li>Option B: Rotate using transform: Install SlicerIGT extension, create a transform, use that in Volume Reslice Driver module to reslice the volume (choose modes: Inplane, Inplane 90, Transverse). You can edit the transform using sliders in Transforms module, or other modules (for example, if you want to reslice along a curve then you can use Endoscopy module or CrossSectionAnalysis module (in SlicerVMTK).</li>
</ul>
<p>What would you like to achieve? Trace a nerve or vessel? Or review/segment a rotationally symmetric object? There are specific modules for these.</p>

---

## Post #3 by @manjula (2021-01-14 17:53 UTC)

<p>Dear Prof Lasso,</p>
<p>My use case is not specific but generic. I find the “Fit slice plane to markup fiducials” script very useful and use it to orient slices.</p>
<p>But when  I use the script I would like to have the other two planes (green and yellow) to reorient them self relative to the red slice. (i.e keep the perpendicular relationship like in the original)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342ece36f2e3659c834f7747262a73a3ffdf054e.png" data-download-href="/uploads/short-url/7rD6KnFzXn800T19UpQYoybeIzA.png?dl=1" title="Screenshot from 2021-01-14 18-38-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342ece36f2e3659c834f7747262a73a3ffdf054e.png" alt="Screenshot from 2021-01-14 18-38-11" data-base62-sha1="7rD6KnFzXn800T19UpQYoybeIzA" width="690" height="255" data-dominant-color="A29A8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-01-14 18-38-11</span><span class="informations">1069×396 9.01 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a way to make this happen maybe straight from the script ?</p>

---

## Post #4 by @lassoan (2021-01-14 18:59 UTC)

<p>After you set the computed SliceToRAS transform into one slice, you can apply 90-degree rotations to to this transform and apply that to the two other slice views. Or, do not set the computer transform directly as SliceToRAS, but set it into a transform node that controls all slices via Volume Reslice Driver.</p>

---
