---
topic_id: 1406
title: "Partial Texture Effect Like This"
date: 2017-11-08
url: https://discourse.slicer.org/t/1406
---

# Partial texture effect like this

**Topic ID**: 1406
**Date**: 2017-11-08
**URL**: https://discourse.slicer.org/t/partial-texture-effect-like-this/1406

---

## Post #1 by @AndFor (2017-11-08 13:38 UTC)

<p>Hello<br>
I’ve found this picture on google search</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/3d0f4e1f3492de8a46484d8ff0f668498cdc4bb9.jpg" width="670" height="440"></p>
<p>I’ve read that is done with Blender</p>
<p>Does is possible with Slicer?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2017-11-08 14:43 UTC)

<p>You can create images like this in Slicer:</p>
<ul>
<li>Use Swiss skull stripper to remove the skull (or use Segment editor to do it manually)</li>
<li>Use slice view controllers to show slices in 3D</li>
<li>In Volumes module, enable thresholding to not show the black boundary around the slice; select a colormap that you like (you can also tune any existing colormap in Colors module)</li>
<li>Create a segment of the brain surface using Segment editor</li>
<li>Export segment to model using Segmentations module</li>
<li>Hide the segmentation (so that you can only see the exported model)</li>
<li>In Models module, select your brain surface model, check Clipping in 3D Display section, check top 3 checkboxes in Clipping planes section</li>
</ul>
<p>If you prefer volume rendering, then after skull stripping, switch to Segment editor, create a segment for the cutout using scissors effect, apply Volume masking to blank out that part of the volume, and use Volume rendering to display the result. Adjust volume rendering transfer functions for coloring.</p>

---
