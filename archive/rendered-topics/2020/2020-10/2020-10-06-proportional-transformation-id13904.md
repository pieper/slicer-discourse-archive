---
topic_id: 13904
title: "Proportional Transformation"
date: 2020-10-06
url: https://discourse.slicer.org/t/13904
---

# Proportional Transformation

**Topic ID**: 13904
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/proportional-transformation/13904

---

## Post #1 by @manjula (2020-10-06 19:59 UTC)

<p>Hi all,</p>
<p>Is there a way to move a part of  a segment proportionally in relation to another segment 3D Slicer?<br>
I have attached a photo to illustrate it something i did via Blender.</p>
<p>For example, when I move the mandible i want the skin to move with it but not 1 to 1 but proportionately. If the center of the chin move 0.8 of the movement of the mandible and as it goes away from the center of the chin (skin) the corresponding movement should be less like 0.7, 0.6 etc…</p>
<p>I am wondering if this is possible with the 3D slicer for surgical simulation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92a0587fe94359bff133d279d9037ebff517d836.jpeg" data-download-href="/uploads/short-url/kV7fu6wkXWqY9M44gX46MB10wCi.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92a0587fe94359bff133d279d9037ebff517d836_2_575x500.jpeg" alt="Untitled" data-base62-sha1="kV7fu6wkXWqY9M44gX46MB10wCi" width="575" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92a0587fe94359bff133d279d9037ebff517d836_2_575x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92a0587fe94359bff133d279d9037ebff517d836_2_862x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92a0587fe94359bff133d279d9037ebff517d836_2_1150x1000.jpeg 2x" data-dominant-color="6A7672"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1790×1556 507 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-10-06 20:19 UTC)

<p>You can use thin-plate spline transform for smooth warping, which usually pretty well simulates soft tissue motion (available in SlicerIGT extension / Fiducial registration wizard module) and might be acceptable for approximate visualization of surgical outcomes. You can of course also compute transforms automatically from other transforms, with 3-4 lines of Python scripts (add an observer to the affected transforms and compute interpolated/combined transform in the callback function).</p>
<p>There are many options for more realistic computations, too.</p>
<p>To model rigid bone motion, you would need to define some kind of a skeleton (bones and joints). There was a 3D Slicer-based project, <a href="https://blog.kitware.com/bender-2-0/">Bender</a>, which allowed to create highly realistic volumetric animations (not just realistic-looking outside surface motion as basic rigged models in Blender work). You could probably revive this application and rig a head model.</p>
<p>You could also export your segmentation, load it into FeBIO Studio, do FEM analysis, and import the displacements back to Slicer for visualization.</p>

---

## Post #3 by @manjula (2020-10-06 21:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>soft tissue motion (available in SlicerIGT extension / Fiducial registration wizard module)</p>
</blockquote>
</aside>
<p>Dear Prof <a class="mention" href="/u/lassoan">@lassoan</a> many thanks for your reply.</p>
<p>Do you mean in the Fiducial registration wizard module creating a transform and applying a warping transformation?</p>
<p>I tried that and the results don’t really make sense to me. so maybe you meant something else?</p>
<p>Can you please give me bit more information on how to do the  thin-plate spline transform for smooth warping ? I am not sure I doing it right.</p>
<p>Also thank you for the information with Bender. Unfortunately, the binary files are not there and I will try to compile it to play with it and see.</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2020-10-08 01:22 UTC)

<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="13904">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Do you mean in the Fiducial registration wizard module creating a transform and applying a warping transformation?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="13904">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>I tried that and the results don’t really make sense to me. so maybe you meant something else?</p>
<p>Can you please give me bit more information on how to do the thin-plate spline transform for smooth warping ? I am not sure I doing it right.</p>
</blockquote>
</aside>
<p>You can follow these steps to warp any nodes (volumes, segmentations, models, etc):</p>
<ul>
<li>Create a markups fiducial node and place 10 control points distributed evenly over the skin surface and another 10 inside the volume. You will prescribe displacement at these positions: either to move it somewhere else or to keep it at the same place.</li>
<li>Clone the markups fiducial node (in Data module, right-click on the markups node), and name one of them “From points” and the other “To points”.</li>
<li>Lock “From points” to make sure those point positions are not modified (in Markups module / Control Points / Interaction in views → click on the lock icon)</li>
<li>In Fiducial registration wizard:
<ul>
<li>From fiducials → “From points”</li>
<li>To fiducials → “To points”</li>
<li>Registration result transform → Select a linear transform → Create new transform</li>
<li>Result transform type → Warping</li>
</ul>
</li>
<li>Apply transform to the nodes if you want to see real-time update of the warping results (in Data module, right-click on transform icon and choose the created Transform node)</li>
<li>Drag-and-drop “To points” to warp the nodes</li>
</ul>

---
