---
topic_id: 16121
title: "Is There A Way To Segment Heart Valves From A Cta Scan Using"
date: 2021-02-21
url: https://discourse.slicer.org/t/16121
---

# Is there a way to segment heart valves from a CTA scan using 3D Slicer

**Topic ID**: 16121
**Date**: 2021-02-21
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-segment-heart-valves-from-a-cta-scan-using-3d-slicer/16121

---

## Post #1 by @dayanjan (2021-02-21 18:51 UTC)

<p>Hello All,</p>
<p>I’ve been tying to figure out a way to do this. Basically, I have a pretty high resolution CTA scan. I want to be able to segment out the heart valves. The only challenge is none of the 3 planes allow me to see a top down picture of any of the heart valves. I am guessing there is a way to rotate the planes so I can get the correct view and segment the heart valves from there? Does anyone know how to do this using CT scans?</p>
<p>Many thanks in advance!</p>

---

## Post #2 by @pieper (2021-02-21 22:10 UTC)

<p>You can use the Reformat widget from the slice controller or you can open the Reformat module (search for it with control-F).</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=reformat#slice-view" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=reformat#slice-view</a></p>

---

## Post #3 by @lassoan (2021-02-21 22:42 UTC)

<p>You can also use <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">Ctrl + Alt + Left-click-and-drag</a> to align your views with the valve axis (after you enabled <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#view-cross-reference">display of slice intersections</a> using the crosshair toolbar).</p>
<p>Then you can rotate slice views using SlicerHeart extension’s Valve View module.</p>

---

## Post #4 by @dayanjan (2021-02-22 13:38 UTC)

<p>Thank you Steve! This is most helpful. I just tried it out and it helps a lot!</p>

---

## Post #5 by @dayanjan (2021-02-22 13:39 UTC)

<p>Many thanks Andras. This helps a lot! This software that you guys created is really amazing!</p>

---
