---
topic_id: 47417
title: "Lattice structure segmentation"
date: 2026-06-21
url: https://discourse.slicer.org/t/47417
last_bumped: 2026-06-22T22:17:48.061Z
---

# Lattice structure segmentation

**Topic ID**: 47417
**Date**: 2026-06-21
**URL**: https://discourse.slicer.org/t/lattice-structure-segmentation/47417

---

## Post #1 by @Tasrif-Ul_Anwar (2026-06-21 23:19 UTC)

<p>We are working with a 3D-printed TPMS lattice structure (fig b) that was tested under compression (we have 4 scans at different loading). I am currently segmenting the sample so that we can compare the deformation of individual unit cells (fig a) before and after loading.</p>
<p>For the unloaded sample, I can separate the unit cells (fig a) using a regular grid pattern because the geometry is still uniform. However, after compression, the unit cells are deformed and no longer align well with the original grid, so I am having difficulty separating each individual unit cell consistently.</p>
<p>Has anyone worked on a similar problem? Is there a recommended workflow for tracking or separating individual unit cells in a defor</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/783cc319695957eae1e7ecaa13a6bfb638cf340a.jpeg" data-download-href="/uploads/short-url/h9FtFZFuP05aL5bbeuutEQ44XJo.jpeg?dl=1" title="ChatGPT Image Jun 4, 2026, 03_16_32 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/783cc319695957eae1e7ecaa13a6bfb638cf340a_2_666x500.jpeg" alt="ChatGPT Image Jun 4, 2026, 03_16_32 PM" data-base62-sha1="h9FtFZFuP05aL5bbeuutEQ44XJo" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/783cc319695957eae1e7ecaa13a6bfb638cf340a_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/783cc319695957eae1e7ecaa13a6bfb638cf340a_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/783cc319695957eae1e7ecaa13a6bfb638cf340a.jpeg 2x" data-dominant-color="DCDCDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ChatGPT Image Jun 4, 2026, 03_16_32 PM</span><span class="informations">1080×810 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>med lattice structure?</p>

---

## Post #2 by @mikebind (2026-06-22 22:17 UTC)

<p>I have not worked with this type of repeating structure before, but if the deformations are less than one repeating unit, I would expect that non-linear registration (using ANTs or Elastix) would probably work well, extracting a deformation transformation between the undeformed and deformed versions. The process MIGHT work well even with larger deformations, but I could also see the process falling into bad local minima which spoil the optimization which drives the registration. If it works, you can define a set of points on your undeformed structure, and then use the deformation transformation on a copy of the points to see where each goes.  You can then follow the unit cells by following the points associated with each cell.</p>
<p>If the deformations are large and/or nonlinear registration does not work for you, you might be able to consistently get the same points by applying a 3D gaussian with a sigma based on your undeformed lattice spacing, smoothing your images and finding local maxima.  If the lattice isn’t ever fully crushed, I bet you could make this work. You’d have to figure out a reliable way to identify pair up the corresponding points, but maybe this will seem easier than finding the whole image matching deformation.</p>
<p>The easiest approach probably depends on the range of deformed results you see in your experiments.  If you’re fully crushing these sometimes, that’s a much harder problem than if they just squish a little bit.</p>

---
