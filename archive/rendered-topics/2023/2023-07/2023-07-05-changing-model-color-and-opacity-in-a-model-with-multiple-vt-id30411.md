---
topic_id: 30411
title: "Changing Model Color And Opacity In A Model With Multiple Vt"
date: 2023-07-05
url: https://discourse.slicer.org/t/30411
---

# Changing Model Color and Opacity in a Model with Multiple vtk Sources

**Topic ID**: 30411
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/changing-model-color-and-opacity-in-a-model-with-multiple-vtk-sources/30411

---

## Post #1 by @rhodesdante (2023-07-05 15:12 UTC)

<p>I am trying to create models that have multiple distinct components using vtk’s appendFilter (shown in the example below). I would like to adjust the opacity and color of the different components separately. As a start, I tried to follow <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#select-cells-of-a-model-using-markups-point-list" rel="noopener nofollow ugc">this example</a> but was unable to change any colors this way. Any help would be greatly appreciated–thanks!</p>
<pre><code class="lang-auto">    # Component 1
    source1 = vtk.vtkCubeSource()
    source1.SetXLength(10)
    source1.SetYLength(10)
    source1.SetZLength(10)
    source1.SetCenter(0,0,-5)
    source1.Update()

    input1 = vtk.vtkPolyData()
    input1.ShallowCopy(source1.GetOutput())

    # Component 2
    source2 = vtk.vtkCubeSource()
    source2.SetXLength(10)
    source2.SetYLength(10)
    source2.SetZLength(10)
    source2.SetCenter(0,0,5)
    source2.Update()

    input2 = vtk.vtkPolyData()
    input2.ShallowCopy(source2.GetOutput())

    # AppendFilter -&gt; Model
    appendFilter.AddInputData(input1)
    appendFilter.AddInputData(input2)
    appendFilter.Update()
    model= slicer.modules.models.logic().AddModel(appendFilter.GetOutput())

    # Something like this to change the model components' colors, though I'd like to change their colors separately
    colorArray = vtk.vtkUnsignedCharArray()  # Set color scalars
    colorArray.SetName("color")
    nCells = appendFilter.GetOutput().GetNumberOfCells()
    colorArray.SetNumberOfTuples(nCells)
    for i in range(nCells):
        colorArray.InsertTuple3(i, 255, 0, 0)
    model.GetDisplayNode().SetActiveScalar("color", vtk.vtkAssignAttribute.CELL_DATA)
    model.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeWarm1")
    model.GetDisplayNode().SetScalarVisibility(True)
</code></pre>

---
