---
topic_id: 2876
title: "Vtk Merge To Create 3D Image"
date: 2018-05-22
url: https://discourse.slicer.org/t/2876
---

# VTK merge to create 3D image

**Topic ID**: 2876
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/vtk-merge-to-create-3d-image/2876

---

## Post #1 by @Alex_Wiley (2018-05-22 14:21 UTC)

<p>Operating system:<br>
Slicer version: 4.3.1<br>
Expected behavior:<br>
Actual behaviour:</p>
<p>I am trying to merge VTK files to stitch together a 3D image.</p>

---

## Post #2 by @lassoan (2018-05-22 18:25 UTC)

<p>Does this post answer your question? <a href="https://discourse.slicer.org/t/how-to-stitch-together-two-sets-of-ct-slices-to-make-one-file/1197/4?u=lassoan">How to stitch together two sets of CT slices to make one file</a></p>
<p>Important: use latest stable version of Slicer (or even latest nightly version). You miss out on years of fixes and improvements if you still use Slicer-4.3.1.</p>

---

## Post #3 by @Alex_Wiley (2018-05-24 12:36 UTC)

<p>No it does not. I am using VTK 3D image files. They all contain about 250 slices. I need to stitch multiple together.</p>
<p>Alex</p>

---

## Post #4 by @Alex_Wiley (2018-05-24 13:36 UTC)

<p>The error isL</p>
<p>slicer:000007FEE58BD840: exception caught!</p>
<p>itk:: MemoryAllocationError (00000000046699E8)<br>
location: “unknown”</p>

---

## Post #5 by @lassoan (2018-05-24 17:51 UTC)

<p>If you use legacy “.vtk” files then in “Add data” dialog you need select “Volume” in  the description column (since .vtk files can contain meshes, volumes, etc.).</p>

---

## Post #6 by @lassoan (2018-05-24 17:55 UTC)

<aside class="quote no-group" data-username="Alex_Wiley" data-post="3" data-topic="2876">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ccd318/48.png" class="avatar"> Alex_Wiley:</div>
<blockquote>
<p>No it does not. I am using VTK 3D image files. They all contain about 250 slices. I need to stitch multiple together.</p>
</blockquote>
</aside>
<p>The link that I’ve posted above explains exactly this. Follow the steps described and if you get stuck at any point then let us know.</p>

---
