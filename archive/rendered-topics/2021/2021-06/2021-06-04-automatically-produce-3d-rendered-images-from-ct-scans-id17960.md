# Automatically produce 3D rendered images from CT scans

**Topic ID**: 17960
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/automatically-produce-3d-rendered-images-from-ct-scans/17960

---

## Post #1 by @linhu (2021-06-04 19:50 UTC)

<p>I have a set of 4000 head CT scans, and I need a fast way to screen each scan for the percentage of face coverage as a way to remove potential personal health information.</p>
<p>I saw on 3D slicer that there is a volume rendering function that can show how the CT scan looks in 3D space. Is there a way traverse all 4000 CT scans through Python, and create a PNG image of the 3D rendered scan at the skin level (as a collage of their anterior, posterior, left and right views)?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-06-04 20:48 UTC)

<p>It is very easy to do this. There are many examples in the script repository that you can use for putting together your script, but prove ly this one is the closest to what you need (set up volume rendering and capture screenshot): <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-random-deformations-to-image" class="inline-onebox">Script repository — 3D Slicer documentation</a> (you can of course remove the part where you apply random warping transforms to the volume).</p>

---
