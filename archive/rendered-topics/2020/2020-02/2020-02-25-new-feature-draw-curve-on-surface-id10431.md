# New feature: draw curve on surface

**Topic ID**: 10431
**Date**: 2020-02-25
**URL**: https://discourse.slicer.org/t/new-feature-draw-curve-on-surface/10431

---

## Post #1 by @Sunderlandkyl (2020-02-25 19:18 UTC)

<p>In the latest 3D Slicer Preview Release, markup curves can now be drawn on surface of model nodes. This allows users to do measurements on surfaces or extract selected parts of a surface. By default, curve is created by connecting control points with the shortest path on surface, but optionally point scalar values can be used to make the curve attracted to certain points (e.g., ridge or valley points).</p>
<p>To try this, download Slicer Preview Release revision 28793 (or later), load a model, draw a curve, and set the curve type to “Shortest distance on surface” within the Markups module. The path between control points is calculated by minimizing the weighted distance. Weighting can be changed by using the cost function and distance weighting function options. If a control point is not on the surface then the closest point on the mesh is used instead.</p>
<div class="lazyYT" data-youtube-id="UeGhzSGUZOA" data-youtube-title="Drawing curves on surface mesh" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Constraining curves is applicable not to just surfaces but to other geometries, such as bronchial or vascular trees (such as those created by VMTK):</p>
<div class="lazyYT" data-youtube-id="UpfDP6ejCjg" data-youtube-title="Finding shortest path between two points in the bronchial tree" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>In the near future, we plan to implement a module that can clip a model based on surface curves and planes.</p>
<p>For developers:<br>
The relevant new functions in the vtkMRMLMarkupsCurveNode are:</p>
<ul>
<li>SetCurveTypeToShortestDistanceOnSurface(vtkMRMLModelNode*)</li>
<li>SetSurfaceCostFunctionType(int)</li>
<li>SetSurfaceDistanceWeightingFunction(const char*)</li>
</ul>
<p>Development was funded in part by CANARIE’s Research Software Program, OpenAnatomy, and Brigham and Women’s Hospital through NIH grant R01MH112748.</p>

---

## Post #2 by @manjula (2020-02-25 20:31 UTC)

<p>works perfectly … <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"> Thanks</p>

---

## Post #3 by @oc34 (2020-02-28 22:14 UTC)

<p>Great and perfect!!! <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e25bc9613fc17d0e80d15aa4061e6a395a7a1648.png" data-download-href="/uploads/short-url/wisyJL318451TULb8qPQxdKVltS.png?dl=1" title="draw lines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25bc9613fc17d0e80d15aa4061e6a395a7a1648_2_690x286.png" alt="draw lines" data-base62-sha1="wisyJL318451TULb8qPQxdKVltS" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25bc9613fc17d0e80d15aa4061e6a395a7a1648_2_690x286.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e25bc9613fc17d0e80d15aa4061e6a395a7a1648_2_1035x429.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e25bc9613fc17d0e80d15aa4061e6a395a7a1648.png 2x" data-dominant-color="F4F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">draw lines</span><span class="informations">1162×482 33.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I imported STL binary file. I am using 4.11.0 version. I tried to draw lines. “Active Scalar” doesn’t show “curv”  How can it be enabled?</p>
<p>Also another question. I want only export drawn lines as STL. Is that possible?</p>

---

## Post #4 by @lassoan (2020-02-29 04:24 UTC)

<p>You need to load a mesh that has point scalars, or compute scalars yourself. You can use VTK filters to compute <a href="https://vtk.org/doc/nightly/html/classvtkCurvatures.html">curvature</a>, distances, etc.</p>

---

## Post #5 by @markokuralt (2021-02-04 09:59 UTC)

<p>I have similar question as oc34.</p>
<p>I have no visible active scalars for my 3D model, despite having curvature values per point. More specifically, I calculated surface curvature in MeshLab and exported it as PLY with saving curvature values per point as quality (property float quality). However, after importing PLY model into Slicer, no active scalars are visible.</p>
<p>Help?</p>

---

## Post #6 by @lassoan (2021-02-04 14:16 UTC)

<p>Maybe the curvature is not saved in the PLY file or VTK’s PLY importer ignores additional arrays. Can you upload a sample PLY file somewhere that contains curvature and post the link here?</p>
<p>Note that you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Apply_VTK_filter_on_a_model_node">compute curvature in Slicer by copy-pasting 3 lines of Python code into the Python console</a> and if needed we can add a small module with a GUI, so there should be no need to use external software for such a simple operation.</p>

---

## Post #7 by @markokuralt (2021-02-05 06:49 UTC)

<p>Link to the sample 3D model in PLY file format (bunny) with curvature saved as quality from MeshLab - <a href="https://easyupload.io/58mtdq" rel="noopener nofollow ugc">https://easyupload.io/58mtdq</a><br>
Any suggestions how to overcome the import problems, would be very welcome.</p>
<p>Thanks. I didn’t know about possibility of calculating curvature in Slicer. Is it possible to calculate anything else the Gauss curvature? A small module with GUI with possibility of calculation of surface curvature would be amazing. With all four paramters, i.e., mean, Gauss, max, and min. Eventually, shape index and curvedness would be nice, too. But for a start basics would be plenty.</p>
<p>Thanks</p>

---

## Post #8 by @markokuralt (2021-04-10 06:02 UTC)

<p>Hey,</p>
<p>Are there any updates regarding calculating surface curvature in Slicer.</p>
<p>Thank you</p>

---

## Post #9 by @lassoan (2021-04-15 19:06 UTC)

<p>It seems that VTK’s PLY reader only supports a <a href="https://github.com/Kitware/VTK/blob/48f8d11f2b79e552fc25d1ab407f9881b51dce0a/IO/PLY/vtkPLYReader.cxx#L147-L163">set of predefined vertex properties</a>. If you want VTK to read more then probably you need to implement it or contract a developer to do it for you.</p>
<p>VTK can compute mean, Gauss, max, and min curvatures - see <a href="https://vtk.org/doc/nightly/html/classvtkCurvatures.html">documentation</a>.</p>
<p>You can copy paste those few lines of code to the Python console in Slicer and if that is not convenient enough then you can create a very simple scripted module as explained in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">this tutorial</a>.</p>

---

## Post #10 by @markokuralt (2021-06-18 17:11 UTC)

<p>Is there a methodological paper to cite when using weighed pathfinding by using shortest distance on surface &amp; surface curvature in surface curve creation?</p>
<p>Thanks</p>

---

## Post #11 by @lassoan (2021-06-18 19:46 UTC)

<p>You can cite the <a href="https://vtk.org/doc/nightly/html/classvtkDijkstraGraphGeodesicPath.html#details">paper that inspired the VTK implementation</a>. Please always cite 3D Slicer as well (it helps us demonstrating impact when applying for continued grant funding for Slicer development, maintenance, and support).</p>

---
