---
topic_id: 4797
title: "Simple Example To Add A Vtk Object To Slicer 3D View"
date: 2018-11-19
url: https://discourse.slicer.org/t/4797
---

# Simple example to add a vtk object to Slicer 3D view

**Topic ID**: 4797
**Date**: 2018-11-19
**URL**: https://discourse.slicer.org/t/simple-example-to-add-a-vtk-object-to-slicer-3d-view/4797

---

## Post #1 by @brhoom (2018-11-19 10:54 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.10</p>
<p>This is not a question but a simple example for beginners. The sphere can be replaced by other polydata object.</p>
<pre><code> import vtk
 source = vtk.vtkSphereSource()
 source.SetRadius(50.0)
 source.SetCenter(0,0,0)
 source.Update() 
 pd = source.GetOutput() # a polydat aobject
 slicer.modules.models.logic().AddModel(pd)</code></pre>

---

## Post #2 by @lassoan (2018-11-19 13:32 UTC)

<p>Thanks for taking the time to share this. We maintain a list of code snippets in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>. It would be great if you could add it there.</p>
<p>I also have a suggestion for possible simplification of the code, using the source’s output port:</p>
<pre><code class="lang-auto">import vtk
source = vtk.vtkSphereSource()
source.SetRadius(50.0)
source.SetCenter(0,0,0)
modelNode = slicer.modules.models.logic().AddModel(source.GetOutputPort())
</code></pre>

---
