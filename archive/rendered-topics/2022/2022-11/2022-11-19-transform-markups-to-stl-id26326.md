# Transform markups to STL

**Topic ID**: 26326
**Date**: 2022-11-19
**URL**: https://discourse.slicer.org/t/transform-markups-to-stl/26326

---

## Post #1 by @Santiodon (2022-11-19 20:08 UTC)

<p>Hello!! Does anyone know how to transform the fiducial mark ups into .STL files to be exported??</p>

---

## Post #2 by @lassoan (2022-12-01 06:59 UTC)

<p>Is this what you need?</p>
<aside class="quote" data-post="3" data-topic="26502">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/importing-a-model-to-stl-with-markups/26502/3">Exporting a model to STL with markups</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Alternatively, you can use a glyph filter like this: 
markup = getNode('F')
glyph = vtk.vtkSphereSource()
glyph.SetRadius(15.0)
glypher = vtk.vtkGlyph3D()
glypher.SetSourceConnection(glyph.GetOutputPort())
glypher.SetInputConnection(markup.GetCurveWorldConnection())
model = slicer.modules.models.logic().AddModel(glypher.GetOutputPort())
slicer.util.saveNode(model, "c:/tmp/something.stl")
  </blockquote>
</aside>


---
