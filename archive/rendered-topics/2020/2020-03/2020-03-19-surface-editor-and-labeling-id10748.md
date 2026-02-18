# Surface editor and labeling

**Topic ID**: 10748
**Date**: 2020-03-19
**URL**: https://discourse.slicer.org/t/surface-editor-and-labeling/10748

---

## Post #1 by @juanprietob (2020-03-19 18:48 UTC)

<p>I would like to start this discussion to develop a 3D surface editor in Slicer that will allow coloring/labeling/spray paint a surface mesh or perform other operations such as cut, clip, smoothing. All the tools should be interactive.</p>

---

## Post #2 by @muratmaga (2020-03-19 19:03 UTC)

<p>You can use all the existing segmentation effects in <code>Segment Editor</code> to edit surface models, if you convert your model as a segmentation, or import it (if it is stl or obj) directly as segmentation.</p>
<p>While as a user part of me also would like to have this functionality, given the existing range of functions in Segment Editor and how easy <code>Segmentations</code> module makes it go back from a scalar volume to 3D models back and forth, I think it would be hard to justify the time investment.</p>
<p>There is also a <code>Surface Toolbox</code> with a range of function to edit meshes.</p>

---

## Post #3 by @lassoan (2020-03-19 19:53 UTC)

<p>Operations on surface meshes are necessary for some projects, especially when you work with open surfaces (segmentations are always closed surfaces). We already have lots of tools in place, some more are coming withing weeks, while others we don’t have plans for.</p>
<p>Existing features:</p>
<ul>
<li>labelling: point labels can be attached to surfaces and points are moved on surfaces by default</li>
<li>smoothing, decimation, cleaning, hole filling, etc.: provided by Surface Toolbox module</li>
<li>EasyClip extension can do some clipping with a plane</li>
</ul>
<p>Planned:</p>
<ul>
<li>clip: dynamic clipping with multiple planes and on-surface curves - <a href="https://github.com/Slicer/Slicer/pull/4746">plane widget pull request</a> is already under review, clipping tool is expected to be released within 1-2 months</li>
<li>creation of parametric surfaces (curved planes) - in 6-12 months</li>
<li>Picking of models: you should be able to pick a model and choose operations on it by right-clicking - in 6-12 months</li>
<li>Boolean operations: built-in VTK Boolean filters are broken but <a href="https://github.com/zippy84/vtkbool">Romer’s vtkbool package</a> is supposed to work much better, we can integrate that into Slicer</li>
</ul>
<p>Not planned:</p>
<ul>
<li>coloring/spray paint</li>
<li>sculpting tools (use Segment Editor instead)</li>
<li>CAD-style parametric editing (use CAD tools instead; for example, we could implement a bridge to open-source Python-based FreeCAD)</li>
</ul>

---
