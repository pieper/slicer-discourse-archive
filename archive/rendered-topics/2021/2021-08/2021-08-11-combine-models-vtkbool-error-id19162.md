# Combine Models vtkbool error

**Topic ID**: 19162
**Date**: 2021-08-11
**URL**: https://discourse.slicer.org/t/combine-models-vtkbool-error/19162

---

## Post #1 by @mikebind (2021-08-11 22:11 UTC)

<p>Hello, I’ve been trying to use the new <a href="https://discourse.slicer.org/t/new-experimental-feature-boolean-operations-union-intersection-difference-on-meshes/16048">“Combine Models” module</a> from the Sandbox extension, but have run into errors. Specifically, the error is “Contact ends suddenly at point 2.” from VTK, and the created union model is empty.  Searching, I found that <a class="mention" href="/u/lassoan">@lassoan</a> reported a similar error to the developer in March 2021 (<a href="https://github.com/zippy84/vtkbool/issues/40" class="inline-onebox" rel="noopener nofollow ugc">Difference of meshes sometimes an empty mesh · Issue #40 · zippy84/vtkbool · GitHub</a>) and had some back and forth.  I don’t fully understand what the issue is, or how to resolve it.  I am trying to combine a model derived from a segmentation with a portion of a rectangular solid. The overlap volume is deliberately small (but should be present) and the overlap volume includes two almost parallel faces, which I gather from reading the github issue might be part of the problem? I am trying to set up a workflow which will work the same way without failing across multiple cases.  I don’t really understand how to identify or fix “non-manifold edges” in my meshes, or how to tell if that is what is causing the problem. I can share the meshes which lead to the error if that would be helpful.  Thanks!</p>

---

## Post #2 by @mau_igna_06 (2021-08-12 00:11 UTC)

<p>vtkBool has worked quite well for <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" rel="noopener nofollow ugc">BoneReconstructionPlanner</a> project to make surgical guides.</p>
<p>In the past if the result was an empty model it was because there was no-contact between the input objects or some of the input models had non-manifold edges or the input models meshes were not made of triangles</p>
<p>Here is a way to check if a model has non-manifold edges:</p>
<pre><code class="lang-auto">myModel = getNode('myModel')
featureEdges = vtk.vtkFeatureEdges()
featureEdges.SetInputData(myModel.GetPolyData())
featureEdges.BoundaryEdgesOff()
featureEdges.FeatureEdgesOff()
featureEdges.ManifoldEdgesOff()
featureEdges.NonManifoldEdgesOn()
featureEdges.Update()
areNonManifoldEdges = featureEdges.GetOutput().GetNumberOfPoints()
</code></pre>
<p>Hope it helps you</p>

---

## Post #3 by @mikebind (2021-08-12 01:23 UTC)

<p>Thanks for the helpful code, I really appreciate it. It did not identify any non-manifold edges in my models, but after reading a bit more about them (<a href="https://www.sculpteo.com/en/3d-learning-hub/create-3d-file/fix-non-manifold-geometry/" rel="noopener nofollow ugc">helpful link</a>), I understand better what they are and why they might cause problems.  While neither model individually has non-manifold edges, the two models might just barely touch in places and end up sharing an edge or vertex when finding the union of the two.  Empirically, it was not a problem for me to just increase the degree of overlap by 1 mm, and this resolved the error. This is an OK workaround for me.</p>

---
