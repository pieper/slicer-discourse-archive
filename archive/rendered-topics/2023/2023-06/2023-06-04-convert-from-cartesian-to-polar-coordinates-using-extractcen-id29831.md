# Convert from cartesian to polar coordinates using ExtractCenterline

**Topic ID**: 29831
**Date**: 2023-06-04
**URL**: https://discourse.slicer.org/t/convert-from-cartesian-to-polar-coordinates-using-extractcenterline/29831

---

## Post #1 by @Gening_Dong (2023-06-04 21:57 UTC)

<p>Hi all,</p>
<p>I’m trying to convert from Cartesian coordinates to polar coordinates for a heart lumen surface model. I used the module <code>Extract Centerline</code> to generate a centerline and <code>Cross-section analysis</code> to get some diameter data. However, I’m a bit confused from there.</p>
<ol>
<li>This table only contains ~2000 rows but the surface model should have 5002 points and the centerline curve has only 238 points. Where came those ~2000 points shown in the table and what is the column <code>Distance</code> mean?</li>
<li>Are the values under the column <code>Diameter</code> the diameters of maximal inscribed spheres for each point on the centerline?</li>
<li>Let’s say I’d like to save the mesh nodes on the surface model and convert their coordinates from Cartesian (Is this same as RAS btw?) to polar. Am I able to do this using the vmtk extension? If not, it would be greatly appreciated if anyone can suggest another method.</li>
</ol>
<p>Thanks much,<br>
Gening</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/222a2aadc9122180f81ad7029f3b2b2587069c94.jpeg" data-download-href="/uploads/short-url/4SezHeEXxjPl6AkLsHdO4jYsgjW.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/222a2aadc9122180f81ad7029f3b2b2587069c94_2_497x500.jpeg" alt="2" data-base62-sha1="4SezHeEXxjPl6AkLsHdO4jYsgjW" width="497" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/222a2aadc9122180f81ad7029f3b2b2587069c94_2_497x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/222a2aadc9122180f81ad7029f3b2b2587069c94_2_745x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/222a2aadc9122180f81ad7029f3b2b2587069c94_2_994x1000.jpeg 2x" data-dominant-color="9A9AC3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1156×1162 72.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27aa4932e7a5829f971bd2c3ba804dd7b460b414.png" data-download-href="/uploads/short-url/5ETslLL2qFdQN36Z0MUHCTgHtsg.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27aa4932e7a5829f971bd2c3ba804dd7b460b414.png" alt="3" data-base62-sha1="5ETslLL2qFdQN36Z0MUHCTgHtsg" width="536" height="500" data-dominant-color="F6F5F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1278×1192 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-06-05 04:14 UTC)

<aside class="quote no-group" data-username="Gening_Dong" data-post="1" data-topic="29831">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gening_dong/48/14706_2.png" class="avatar"> Gening_Dong:</div>
<blockquote>
<p>This table only contains ~2000 rows but the surface model should have 5002 points and the centerline curve has only 238 points. Where came those ~2000 points shown in the table and what is the column <code>Distance</code> mean?</p>
</blockquote>
</aside>
<p>The centerline curve is resampled at equal distances. Distance is distance from the curve starting point in millimeters.</p>
<aside class="quote no-group" data-username="Gening_Dong" data-post="1" data-topic="29831">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gening_dong/48/14706_2.png" class="avatar"> Gening_Dong:</div>
<blockquote>
<p>Are the values under the column <code>Diameter</code> the diameters of maximal inscribed spheres for each point on the centerline?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="Gening_Dong" data-post="1" data-topic="29831">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gening_dong/48/14706_2.png" class="avatar"> Gening_Dong:</div>
<blockquote>
<p>Let’s say I’d like to save the mesh nodes on the surface model and convert their coordinates from Cartesian (Is this same as RAS btw?) to polar. Am I able to do this using the vmtk extension? If not, it would be greatly appreciated if anyone can suggest another method.</p>
</blockquote>
</aside>
<p>Yes, RAS coordinate system is Cartesian. VMTK can compute a consistent curve coordinate using parallel transport method (with normal vectors that are consistent along the curve, with minimal torsion). We implemented an improved version of the this coordianate system computation in Slicer, which allows setting the direction of the initial normal vector.</p>
<p>See <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Markups/Testing/Python/MarkupsCurveCoordinateFrameTest.py">Slicer’s MarkupsCurveCoordinateFrameTest</a> for a full, detailed example. This is an example of the parallel transport based curve coordinate system:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb05f28c3ad9f97f740ac32ea901edf145d6f10b.png" data-download-href="/uploads/short-url/sY1Ft5MwRkNamycCl0JKgt9nFWz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb05f28c3ad9f97f740ac32ea901edf145d6f10b_2_665x500.png" alt="image" data-base62-sha1="sY1Ft5MwRkNamycCl0JKgt9nFWz" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb05f28c3ad9f97f740ac32ea901edf145d6f10b_2_665x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb05f28c3ad9f97f740ac32ea901edf145d6f10b_2_997x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb05f28c3ad9f97f740ac32ea901edf145d6f10b_2_1330x1000.png 2x" data-dominant-color="9B9DD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1334×1002 31.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
