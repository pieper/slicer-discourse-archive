---
topic_id: 19545
title: "Mirror Brain Ct"
date: 2021-09-07
url: https://discourse.slicer.org/t/19545
---

# Mirror brain CT

**Topic ID**: 19545
**Date**: 2021-09-07
**URL**: https://discourse.slicer.org/t/mirror-brain-ct/19545

---

## Post #1 by @bartvandijken (2021-09-07 13:47 UTC)

<p>Operating system: MacOS<br>
Slicer version: 4.8.1</p>
<p>I’m trying to create a mean radiotherapy dose map on a cohort of 12 brain tumor patients with dose accumulation and isodose lines using the RT extension. However, I first want to ‘flip/mirror’ 5 patients so all tumors are located on the “same” side/hemisphere. What is the easiest way to mirror the entire scan?</p>
<p>The surface toolbox works with input models/segmentations and thus is not helpful. I’ve tried to change the upper left value of the matrix (1 to -1) in the linear transform matrix, but then all disappears.</p>

---

## Post #2 by @lassoan (2021-09-08 02:02 UTC)



---

## Post #3 by @lassoan (2021-09-08 02:05 UTC)

<p>Inverting coordiante values not just mirrors but also repositions the objects. You need to click <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Reset field of view” button</a> to update the slice view to this new position.</p>
<p>Also make sure to update Slicer to the latest version. We have made hundreds of fixes and improvements since Slicer-4.8.1.</p>

---

## Post #4 by @chir.set (2021-09-08 06:46 UTC)

<aside class="quote no-group" data-username="bartvandijken" data-post="1" data-topic="19545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/839c29/48.png" class="avatar"> bartvandijken:</div>
<blockquote>
<p>but then all disappears</p>
</blockquote>
</aside>
<p>I’ve tried that in a recent version on Linux. Noticed that left/right does flip in the slice views while remaining visible, but it’s a volume rendering that disappears in 3D view. If you select a layout with two 3D views, one of them still shows a volume render.</p>
<p>Alternatively, you might use Filtering/Simple Filters/FlipImageFilter, and flip along the X axis and about origin. Here it’s not a transform, voxels are really moved around.</p>
<p>All, if I rightly understand your problem.</p>

---

## Post #5 by @lassoan (2021-09-08 14:14 UTC)

<p>When you apply a transform that has negative determinant (such as mirroring along a single axis), it turns the object inside out. This is bad for all data objects and can be resolved differently for each type.</p>
<p>For volumes, you can restore a meaningful geometry by resampling. For mirroring, the FlipImageFilter that <a class="mention" href="/u/chir.set">@chir.set</a> recommended above is the simplest solution. In general, for any kind of transform (warping, mirroring, shearing, …), you can use “Crop volume” module that allows you to resample the transformed volume into any rectangular region at any resolution.</p>

---
