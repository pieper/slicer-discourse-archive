---
topic_id: 46642
title: "Spatial information in 2D segmentations"
date: 2026-04-02
url: https://discourse.slicer.org/t/46642
last_bumped: 2026-04-03T21:55:40.535Z
---

# Spatial information in 2D segmentations

**Topic ID**: 46642
**Date**: 2026-04-02
**URL**: https://discourse.slicer.org/t/spatial-information-in-2d-segmentations/46642

---

## Post #1 by @Antmaker (2026-04-02 18:40 UTC)

<p>According to <a href="https://discourse.slicer.org/t/2d-segmentation-possible/33743/2">this post</a>, 2D segmentation is possible in 3D Slicer. I am trying to figure out whether it is possible to incorporate spatial information such that I may calculate “area” instead of “volume (Volume Statistics extension)”.</p>
<p>Is it possible to incorporate spatial information into an image that is being segmented in 3D Slicer? If so, how would I approach integrating it and then calculate the segmented area? If not, how may I segment and calculate the pixel counts?</p>

---

## Post #2 by @mau_igna_06 (2026-04-02 23:33 UTC)

<p>If you enter a 2D image in Slicer it will automatically converted to 3D. Then you can change the spacing (z-axis) of the scalarVolumeNode in Slicer to be 1mm. If you calculate the volume for a segmentation of this image it will be also the area just change the unit to mm2</p>

---

## Post #3 by @lassoan (2026-04-03 12:32 UTC)

<p>Segment Statistics module computes area and volume of each segment. Area is computed in 3D, which means both sides of a flat single-slice segments are included. You can divide the reported surface value by 2 to get the cross-sectional area, i.e., the area that you see on a single image.</p>
<p>There are also several modules for computing area. I generated this summary using ChatGPT, but I confirm that it is accurate (I reviewed it and fixed minor inaccuracies):</p>
<hr>
<h3><a name="p-132983-h-1-segment-crosssection-area-in-sandbox-extension-1" class="anchor" href="#p-132983-h-1-segment-crosssection-area-in-sandbox-extension-1" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/pushpin.png?v=15" title=":pushpin:" class="emoji" alt=":pushpin:" loading="lazy" width="20" height="20"> 1. <strong>Segment Cross‑Section Area</strong> (in <strong>Sandbox</strong> extension)</h3>
<ul>
<li>This module computes cross‑sectional area of a segmentation <strong>along an image axis</strong> (e.g., axial, sagittal, coronal or any IJK axis you choose).</li>
<li>You can install it by opening the <strong>Extensions Manager</strong> in Slicer and installing the <strong>Sandbox</strong> extension.</li>
</ul>
<p><img src="https://emoji.discourse-cdn.com/twitter/backhand_index_pointing_right.png?v=15" title=":backhand_index_pointing_right:" class="emoji" alt=":backhand_index_pointing_right:" loading="lazy" width="20" height="20"> Best when you want area per slice along standard image axes.</p>
<hr>
<h3><a name="p-132983-h-2-segmentgeometry-in-slicerbiomech-extension-2" class="anchor" href="#p-132983-h-2-segmentgeometry-in-slicerbiomech-extension-2" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/pushpin.png?v=15" title=":pushpin:" class="emoji" alt=":pushpin:" loading="lazy" width="20" height="20"> 2. <strong>SegmentGeometry</strong> (in <strong>SlicerBiomech</strong> extension)</h3>
<ul>
<li>This extension can compute <strong>cross‑sectional area</strong> (plus other shape metrics) <strong>along an arbitrary direction or line</strong>, not just the image axes.</li>
<li>It’s useful if you want cross‑sections in non‑orthogonal directions or aligned with a specific anatomical axis.</li>
<li>It outputs area and additional geometric properties like perimeter, Feret diameter, moments of inertia, etc.</li>
</ul>
<p><img src="https://emoji.discourse-cdn.com/twitter/backhand_index_pointing_right.png?v=15" title=":backhand_index_pointing_right:" class="emoji" alt=":backhand_index_pointing_right:" loading="lazy" width="20" height="20"> Best when you need cross‑section metrics oriented in a custom way.</p>
<hr>
<h3><a name="p-132983-h-3-vmtk-modules-in-slicervmtk-extension-3" class="anchor" href="#p-132983-h-3-vmtk-modules-in-slicervmtk-extension-3" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/pushpin.png?v=15" title=":pushpin:" class="emoji" alt=":pushpin:" loading="lazy" width="20" height="20"> 3. <strong>VMTK modules</strong> (in <strong>SlicerVMTK</strong> extension)</h3>
<ul>
<li>The <strong>Vascular Modeling Toolkit (VMTK)</strong> extension includes modules like <em>Cross‑section analysis</em> or <em>Stenosis measurement</em>.</li>
<li>These can compute cross‑sections <strong>along a centerline or curved path</strong>, often used for vessels or tubular structures.</li>
</ul>
<p><img src="https://emoji.discourse-cdn.com/twitter/backhand_index_pointing_right.png?v=15" title=":backhand_index_pointing_right:" class="emoji" alt=":backhand_index_pointing_right:" loading="lazy" width="20" height="20"> Best for vascular work or when the structure follows a path rather than straight sections.</p>
<hr>
<h3><a name="p-132983-h-3-markups-module-4" class="anchor" href="#p-132983-h-3-markups-module-4" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/pushpin.png?v=15" title=":pushpin:" class="emoji" alt=":pushpin:" loading="lazy" width="20" height="20"> 3. <strong>Markups module</strong></h3>
<ul>
<li>If you need the area of a structure in a <strong>single 2D slice</strong>, you can draw a closed curve markup and enable <strong>area measurement</strong> in the Markups module’s <strong>Measurements</strong> section.</li>
</ul>
<p><img src="https://emoji.discourse-cdn.com/twitter/backhand_index_pointing_right.png?v=15" title=":backhand_index_pointing_right:" class="emoji" alt=":backhand_index_pointing_right:" loading="lazy" width="20" height="20"> Best for measuring area of a simple shape in a single 2D slice.</p>
<hr>

---

## Post #4 by @Antmaker (2026-04-03 21:09 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>, that is a great idea! Thank you, this is a very intuitive and explainable approach.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>, regarding dividing the area calculated by the Segment Statistics module, wouldn’t the surface area be a slight overestimation because it would include half of the perimeter of the segmented area?</p>

---

## Post #5 by @lassoan (2026-04-03 21:44 UTC)

<aside class="quote no-group" data-username="Antmaker" data-post="4" data-topic="46642">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/antmaker/48/81424_2.png" class="avatar"> Antmaker:</div>
<blockquote>
<p>wouldn’t the surface area be a slight overestimation because it would include half of the perimeter of the segmented area?</p>
</blockquote>
</aside>
<p>Probably the extra surface on the side is negligible (&lt;1%), but you can measure the surface using all the other methods that I described to confirm.</p>

---

## Post #6 by @Antmaker (2026-04-03 21:55 UTC)

<p>Yeah, I agree that the difference would be minimal. I was trying to confirm my understanding of the method. Thanks!</p>

---
