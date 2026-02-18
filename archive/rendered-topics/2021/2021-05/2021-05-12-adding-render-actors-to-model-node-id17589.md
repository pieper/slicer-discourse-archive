# adding render actors to model node

**Topic ID**: 17589
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/adding-render-actors-to-model-node/17589

---

## Post #1 by @jimbo (2021-05-12 12:27 UTC)

<p>Dear all,</p>
<p>I am new to slicer and I am having some issues creating model nodes. I have some code to render splines and surfaces which I render by creating  mappers, actors and then adding the actors to render window. Is there a way how I can simply add those actors to a model node so I can access them from the data module?</p>
<p>I greatly appreciate any help.</p>

---

## Post #2 by @pieper (2021-05-12 20:58 UTC)

<p>Since Slicer can have multiple threeD view instances that should have the same mapping from model nodes to vtk actors/mappers/widgets we have a layer called displayable managers.  <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DisplayableManagers">This documentation</a> is a bit old but it describes the basic operations.  The API docs <a href="https://apidocs.slicer.org/v4.10/classvtkMRMLAbstractDisplayableManager.html">are here</a>.  Most of these are in C++ but there is also a scripted version.</p>

---

## Post #3 by @lassoan (2021-05-13 04:41 UTC)

<p>You can render a vtkPolyData by calling <code>slicer.modules.models.logic().AddModel(polydata)</code>. See complete examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-simple-surface-mesh-as-a-model-node">script repository</a>.</p>

---
