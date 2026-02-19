---
topic_id: 23572
title: "What Is The Best Way To Draw A Triangle Shape With Python"
date: 2022-05-24
url: https://discourse.slicer.org/t/23572
---

# What is the best way to draw a triangle shape with Python

**Topic ID**: 23572
**Date**: 2022-05-24
**URL**: https://discourse.slicer.org/t/what-is-the-best-way-to-draw-a-triangle-shape-with-python/23572

---

## Post #1 by @minhtan16 (2022-05-24 19:10 UTC)

<p>Hi everyone,</p>
<p>I’m new to 3D Slicer and I was wondering what would be the best way for me to draw a triangle on a 2D and 3D view using python. Considering I have a specific coordinates, I could process it into 3 points (to represent the triangle), at that point what would the best options to draw the triangle?</p>
<p>After some research I saw that I could use Segmentation, a bit like in this <a href="https://discourse.slicer.org/t/programmatically-create-a-segmentationnode-and-labelmapnode-from-polygon-coordinates/8448/4">topic</a></p>
<p>Is this the way to go or is there some kind of extension that is already doing such thing?</p>
<p>Thank you in advance,</p>
<p>Minh.</p>

---

## Post #2 by @pieper (2022-05-24 19:31 UTC)

<p>The thread you linked makes sense if your goal is to make a filled triangle (segmentation).  If you just want lines, you could make a closed curve markup and set the interpolation to linear.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically</a></p>

---
