---
topic_id: 43230
title: "Aligning Local Coordinate System With Ras"
date: 2025-06-05
url: https://discourse.slicer.org/t/43230
---

# Aligning local coordinate system with RAS

**Topic ID**: 43230
**Date**: 2025-06-05
**URL**: https://discourse.slicer.org/t/aligning-local-coordinate-system-with-ras/43230

---

## Post #1 by @mariammtch (2025-06-05 13:06 UTC)

<p>Hello everyone. I have several CT scans which are all positioned differently. It is not important to align them with each other but it is very important for me that I use the local coordinate system for the measurements. How can I make sure that the axes which I have defined as local X Y and Z are actually being used for this purpose?</p>
<p>E.g I want to measure distance of every point of one segment from the centroid reference plane to the articular surface of the bone. How can I make sure that csv file exported uses my X Y and Z?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d53a1f3d85d58e72404b051425a0e2dcaa9b48.png" data-download-href="/uploads/short-url/udXA9ovu9DXDpgfp1tYFkG7dGhW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3d53a1f3d85d58e72404b051425a0e2dcaa9b48_2_690x388.png" alt="image" data-base62-sha1="udXA9ovu9DXDpgfp1tYFkG7dGhW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3d53a1f3d85d58e72404b051425a0e2dcaa9b48_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3d53a1f3d85d58e72404b051425a0e2dcaa9b48_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3d53a1f3d85d58e72404b051425a0e2dcaa9b48_2_1380x776.png 2x" data-dominant-color="CFD0E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2048×1152 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Million thanks in advance</p>

---

## Post #2 by @mraihan (2025-06-05 14:29 UTC)

<p>if you think that the body in 3D slicer has different position and orientation than your defined cordinate system I would do these:</p>
<p>a) Find the origin/centroid of the local cordinate system (LCS) of the body<br>
b) Find the unit basis vectors of the LCS (one way to do this is computing the bounding box/use any reference plane like length or normals)</p>
<p>and then compare the two (your defined LCS vs LCS of the body in 3D slicer).</p>
<p>If they dont match, then you can apply a transformation. You can apply this transformation after or before exporting.</p>

---
