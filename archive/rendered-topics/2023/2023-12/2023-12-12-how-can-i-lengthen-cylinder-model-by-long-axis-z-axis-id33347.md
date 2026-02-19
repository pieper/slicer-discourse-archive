---
topic_id: 33347
title: "How Can I Lengthen Cylinder Model By Long Axis Z Axis"
date: 2023-12-12
url: https://discourse.slicer.org/t/33347
---

# How can i lengthen cylinder model by Long axis(Z axis)

**Topic ID**: 33347
**Date**: 2023-12-12
**URL**: https://discourse.slicer.org/t/how-can-i-lengthen-cylinder-model-by-long-axis-z-axis/33347

---

## Post #1 by @yeong9316 (2023-12-12 06:02 UTC)

<p>I made the straight line created with Markups into a cylinder model using the Markups to model module, and I would like to increase the length of the cylinder in that state.</p>
<p>We are literally in a situation where we want to increase the length in the direction of the long axis of the cylinder, but if we apply Transform to the model to increase the size, the overall size, not the long axis, increases. help plz</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e702f56f66cb279373297e4089b3567335c6529b.png" data-download-href="/uploads/short-url/wXCDlSWUMA1yxR0oAOUtXvZSHij.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e702f56f66cb279373297e4089b3567335c6529b.png" alt="image" data-base62-sha1="wXCDlSWUMA1yxR0oAOUtXvZSHij" width="624" height="500" data-dominant-color="9D9FC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">633×507 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2023-12-12 10:09 UTC)

<p>Why not start from a longer markup?</p>
<p>By the way you can scale objects along one axis with the appropriate transform, you just need to add scaling only for the axis that you want to change the size of. If you rotated it before and hardened the transform, then you would need to create the object again because although you can find the principal axes, it seems an overkill.</p>

---

## Post #4 by @yeong9316 (2023-12-12 11:28 UTC)

<p>I currently converted the red Markups line formed by two red dots into the yellow cylindrical model in the photo above using the Markups to model module.</p>
<p>It would be nice to make the Markups line longer, but the two red dots are important landmarks, so they must be fixed.</p>
<p>Is there a way to increase the length of the Markup line while maintaining these two points? Or is there a way to make sure the Markup line passes through two specific points?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75f584ff0630f0f0441a9848f0103787647877ce.png" data-download-href="/uploads/short-url/gPvT0jUUZsmIZMCOFouDimc60RE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75f584ff0630f0f0441a9848f0103787647877ce_2_690x211.png" alt="image" data-base62-sha1="gPvT0jUUZsmIZMCOFouDimc60RE" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75f584ff0630f0f0441a9848f0103787647877ce_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75f584ff0630f0f0441a9848f0103787647877ce_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75f584ff0630f0f0441a9848f0103787647877ce.png 2x" data-dominant-color="66657D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1341×411 99.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @mikebind (2023-12-12 22:06 UTC)

<p>I would recommend just making a new markups line based on the existing one, but at the length you want it, and then making the cylinder from that one.</p>

---

## Post #6 by @cpinter (2023-12-13 10:04 UTC)

<p>I agree. It would be very easy to create a new markup programmatically.</p>
<p>This code pasted in the Python console works for me:</p>
<pre><code class="lang-auto">mn = getNode('L')
mn2 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode')
mn2.CopyContent(mn)
import numpy as np
p0 = np.zeros(3)
p1 = np.zeros(3)
mn2.GetNthControlPointPositionWorld(0, p0)
mn2.GetNthControlPointPositionWorld(1, p1)
axis = p1 - p0
p0a = p0 - axis / 4
p1a = p1 + axis / 4
mn2.SetNthControlPointPositionWorld(0, p0a)
mn2.SetNthControlPointPositionWorld(1, p1a)
</code></pre>
<p>You will need to replace <code>'L'</code> with the actual name of your markups node.</p>

---
