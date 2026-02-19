---
topic_id: 14740
title: "How To Change The Ball"
date: 2020-11-23
url: https://discourse.slicer.org/t/14740
---

# How to change the ball

**Topic ID**: 14740
**Date**: 2020-11-23
**URL**: https://discourse.slicer.org/t/how-to-change-the-ball/14740

---

## Post #1 by @slicer365 (2020-11-23 11:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd28f440a7f49b83eaab0e1cb69a8a882bf36c34.jpeg" data-download-href="/uploads/short-url/A7yxIntE33RIRGy9gq7ye0EducY.jpeg?dl=1" title="001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd28f440a7f49b83eaab0e1cb69a8a882bf36c34_2_610x500.jpeg" alt="001" data-base62-sha1="A7yxIntE33RIRGy9gq7ye0EducY" width="610" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd28f440a7f49b83eaab0e1cb69a8a882bf36c34_2_610x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd28f440a7f49b83eaab0e1cb69a8a882bf36c34.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd28f440a7f49b83eaab0e1cb69a8a882bf36c34.jpeg 2x" data-dominant-color="5C5E65"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">001</span><span class="informations">737×604 41.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2db5c9ea4b2c2fe8c0903662c7468e980d7ed3ca.jpeg" data-download-href="/uploads/short-url/6wmXW7019reFZcdV77Gef9c6jhM.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2db5c9ea4b2c2fe8c0903662c7468e980d7ed3ca_2_345x171.jpeg" alt="捕获" data-base62-sha1="6wmXW7019reFZcdV77Gef9c6jhM" width="345" height="171" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2db5c9ea4b2c2fe8c0903662c7468e980d7ed3ca_2_345x171.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2db5c9ea4b2c2fe8c0903662c7468e980d7ed3ca_2_517x256.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2db5c9ea4b2c2fe8c0903662c7468e980d7ed3ca_2_690x342.jpeg 2x" data-dominant-color="A3A4A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1359×674 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I made a solid ball, then showed it in the" model "as a model, and showed the inside through plane cutting, and found that the whole ball became a hollow with very thin edges. How to get a solid ball, and the inside is solid after cutting.</p>

---

## Post #2 by @pieper (2020-11-23 15:12 UTC)

<p>You can use the scissors in the Segment Editor to cut the segment and that will be capped.</p>

---

## Post #3 by @lassoan (2020-11-24 18:39 UTC)

<p>Models are usually surface meshes (you can generate volumetric meshes, they are only used for very special applications, such as biomechanical simulations). Surface meshes have zero thickness, so if you cut away a part of a surface mesh then it will be an open surface and you can see what is inside.</p>
<p>If you want to keep the surface mesh closed then you can either edit it in Segment editor as <a class="mention" href="/u/pieper">@pieper</a> suggested above (as the segment editor maintains keeps the surface closed), or you can cut the model using Dynamic modeler module’s “Plane cut” tool (with “Cap surface” option enabled).</p>

---
