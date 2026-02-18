# Merging models with keeping labels

**Topic ID**: 10479
**Date**: 2020-02-29
**URL**: https://discourse.slicer.org/t/merging-models-with-keeping-labels/10479

---

## Post #1 by @Aep93 (2020-02-29 16:18 UTC)

<p>Hello all,<br>
How should I merge two models so that each of them has a specific label in the merged model?<br>
I tried merge models module but it does not work and I think it is because one of my models is volumetric.</p>

---

## Post #2 by @lassoan (2020-02-29 20:34 UTC)

<p>Array values that can be found in all input meshes will be available in the output mesh, too. To merge volumetric meshes, you need to use <a href="https://vtk.org/doc/nightly/html/classvtkAppendFilter.html">vtkAppendFilter</a> instead of vtkAppendPolyData.</p>
<p>It would be nice if you could update <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI/MergeModels">MergeModels</a> module to be able to load and merge volumetric meshes (unstructure grids) and not just surface meshes (polydata). But if you are not familiar with C++ then you can implement appending in your own script/module in a few lines of Python code.</p>

---

## Post #3 by @Aep93 (2020-02-29 20:41 UTC)

<p>Thank you very much for your answer. I am not very good with c++ but if I want to use the python codes, what resources can I use to find how to code such a command?<br>
The other question is whether this way assigns a specific label to each model after they merged. Because I want a single merged model in which different parts have different labels.</p>

---

## Post #4 by @lassoan (2020-02-29 20:59 UTC)

<p>Append operation preserves scalar values. You can assign constant scalar values before append.</p>

---

## Post #5 by @Aep93 (2020-02-29 21:52 UTC)

<p>Thank you very much. I think there is no module  for assigning label to a pre-existing model and I should use the following command.<br>
modelNode.GetDisplayNode().SetActiveScalar(“selection”, vtk.vtkAssignAttribute.CELL_DATA)<br>
Am I right?</p>

---

## Post #6 by @lassoan (2020-03-01 01:25 UTC)

<p>To assign a point scalar array with a constant value for all the points, you can either manipulate the VTK data object (add an array, set the size to the number of points/cells, and fill with a constant) or use VTK filters (such as <a href="https://vtk.org/doc/nightly/html/classvtkArrayCalculator.html">vtkArrayCalculator</a>)</p>
<p>You can learn VTK from the VTK <a href="https://lorensen.github.io/VTKExamples/site/VTKBook/00Preface/">textbook</a>, the huge collection of tests and <a href="https://lorensen.github.io/VTKExamples/site/">examples</a>, and <a href="https://vtk.org/doc/nightly/html/">API documentation</a>.</p>
<p>You can find lots of examples of how to use VTK for processing MRML nodes in Slicer in the Slicer script repository. For example, adding a cell array with a constant value is shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points">here</a>.</p>

---

## Post #7 by @Aep93 (2020-03-01 01:54 UTC)

<p>Thank you very much for your help.</p>

---
