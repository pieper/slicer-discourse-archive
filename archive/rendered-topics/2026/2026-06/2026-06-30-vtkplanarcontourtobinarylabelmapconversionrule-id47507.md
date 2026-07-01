---
topic_id: 47507
title: "vtkPlanarContourToBinaryLabelmapConversionRule"
date: 2026-06-30
url: https://discourse.slicer.org/t/47507
last_bumped: 2026-06-30T15:41:29.425Z
---

# vtkPlanarContourToBinaryLabelmapConversionRule

**Topic ID**: 47507
**Date**: 2026-06-30
**URL**: https://discourse.slicer.org/t/vtkplanarcontourtobinarylabelmapconversionrule/47507

---

## Post #1 by @ferhue (2026-06-30 11:29 UTC)

<p>I am interested in creating a variant of <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx at master · SlicerRt/SlicerRT · GitHub</a></p>
<p>that directly converts a 2D Planar Contour to a 2D Binary Labelmap (and if I have more than 1 slice, that will become naturally 3D), without the overhead of triangulating a closed surface as intermediate step, etc. There was some related discussion here <a href="https://discourse.slicer.org/t/convert-binary-label-map-into-2d-contours-ideally-splines-and-back/11135/4" class="inline-onebox">Convert binary label map into 2D contours (ideally splines) and back - #4 by cpinter</a> but I thought not to necro-bump an old thread.</p>
<p>My reason is that I have hundreds/thousands of datasets (I cannot change) all using Planar contours (RTstruct.dcm format) as representation, and I just want to extract the binary labelmap (and doing this quickly matters for my application), not visualize them as closed surface. Contours are exactly aligned with CT slices, so they can be treated independently and fully parallelized, unlike if you try to reconstruct a 3D surface.</p>
<p>Currently, my workaround is to use in my C++ project a parallel-for loop for each slice, reading the slice 2D contour, and calling <code>vtkPolygon::PointInPolygon</code> for each pixel to fill the matrix.</p>
<p>But I thought it’s maybe wiser to profit/reuse the more advanced handling of keyholes of <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx#L183" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx at master · SlicerRt/SlicerRT · GitHub</a> for which maybe PointInPolygon is not prepared to deal well with if not preprocessed.</p>
<p>I’d be happy to hear comments / suggestions from <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @cpinter (2026-06-30 11:40 UTC)

<p>The reason for going via closed surfaces is not the need of visualization in 3D, but as an intermediate step towards converting to labelmap. This is a very hard geometrical problem, so I don’t suggest jumping headfirst into it, because it already took two masters projects and it’s much more complex than it seems. See paper</p>
<p><a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Sunderland2015-manuscript.pdf">Reconstruction of surfaces from planar contours through contour interpolation</a></p>

---

## Post #3 by @ferhue (2026-06-30 14:06 UTC)

<p>Thanks Csaba for the prompt reply and the link to the paper.</p>
<p>The paper states: <em>These structures must be converted into 3D meshes in order to be visualized or to be used for treatment planning and further analyses.</em></p>
<p>Maybe I should frame the conditions of my problem differently: the contours of all these datasets are manual 2D contours done by hand. So for this specific type of input, it makes less sense to me to try to go to 3D as intermediate step in order to convert to a 2D labelmap.<br>
Since what the physician is actually doing is drawing a 2D labelmap with his mouse on a CT slice. This is why simply the function <code>vtkPolygon::PointInPolygon</code> works rather well for my specific application of creating a 2D labelmap.</p>
<p>In my mind, that would simplify the issues commented in this paper:</p>
<p><em>One issue that needs to be solved by all triangulation algorithms is determining which contours should be connected by triangles between each of the slices. This is referred to as the correspondence problem. Another obstacle to overcome is the occurrence of branching contours. A branching contour occurs when a single contour on one of the slices must be</em><br>
<em>connected to two or more contours on an adjacent slice.</em></p>
<p>The issue though that has to be dealt with in the independent 2D problem is the other one:</p>
<p><em>Another issue that can occur is the existence of keyholes within the set of contours. The DICOM standard (RT structure set module) defines the storage of hollow structures as keyholes that are represented as an inner and outer contour connected by an arbitrarily small channel in order to be considered one contour.</em></p>
<p>which I agree is a hard geometrical problem, but I still do not see the need to go to a 3D problem to solve it (which also prevents parallelization for each slice). Here a related discussion: <a href="https://stackoverflow.com/a/218081/7471760" rel="noopener nofollow ugc">https://stackoverflow.com/a/218081/7471760</a> <a href="https://github.com/Aditi1993/Point_in_Polygon" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Aditi1993/Point_in_Polygon: Application can tell whether a point is inside or outside a complex polygon with holes. · GitHub</a> <a href="https://alienryderflex.com/polygon/" class="inline-onebox" rel="noopener nofollow ugc">Determining Whether A Point Is Inside A Complex Polygon</a></p>
<p>Maybe the <a href="https://github.com/AngusJohnson/Clipper2" class="inline-onebox" rel="noopener nofollow ugc">GitHub - AngusJohnson/Clipper2: Polygon Clipping, Offsetting &amp; Triangulation in C++, C# and Delphi · GitHub</a> library that <a class="mention" href="/u/lassoan">@lassoan</a> mentioned some time ago could be useful in this regard to be able to process the CLOSEDPLANAR_XOR 2D contour types.</p>

---

## Post #4 by @cpinter (2026-06-30 15:31 UTC)

<p>I haven’t re-read the paper but as I remember the main purpose for the triangulation was to facilitate interpolation between the slices (avoid the staircase effect). Handling the different special cases is harder with surface meshes than with labelmaps, I agree.</p>
<p>We have another conversion path, via ribbon models. If you go to the Segmentations module and click Update in the Representations section for Binary labelmap, and choose the path via Ribbon models, you’ll see how the output changes.</p>
<p>If you use this path via ribbons would it help? I’d argue that it is basically what you want, if I understand it correctly.</p>
<p>And if you need better interpolation, we could use the algorithm that is behind the Fill between slices Segment Editor effect.</p>

---

## Post #5 by @ferhue (2026-06-30 15:41 UTC)

<p>Thanks for the reply!</p>
<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="47507">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If you use this path via ribbons would it help? I’d argue that it is basically what you want, if I understand it correctly.</p>
</blockquote>
</aside>
<p>Yes, I first thought so, but then I noticed that</p>
<ul>
<li>Major: the function <code>FixKeyhole</code> is not present in <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToRibbonModelConversionRule.cxx" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToRibbonModelConversionRule.cxx at master · SlicerRt/SlicerRT · GitHub</a> but only in <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx" class="inline-onebox" rel="noopener nofollow ugc">SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx at master · SlicerRt/SlicerRT · GitHub</a></li>
<li>Minor: there might be some 3D-specific overhead <code>// Attempt to compute plane equation with brute force</code></li>
</ul>
<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="47507">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>And if you need better interpolation,</p>
</blockquote>
</aside>
<p>In principle not, in this case I am looking towards performance/parallelization more than precision.</p>

---
