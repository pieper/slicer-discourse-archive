---
topic_id: 20350
title: "Displaying Custom Vtk Class Inherited From Vtkdataset"
date: 2021-10-26
url: https://discourse.slicer.org/t/20350
---

# Displaying custom VTK class inherited from `vtkDataSet`

**Topic ID**: 20350
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/displaying-custom-vtk-class-inherited-from-vtkdataset/20350

---

## Post #1 by @keri (2021-10-26 01:19 UTC)

<p>Hi,</p>
<p>I’m implementing a class inherited directly from <code>vtkDataSet</code>.</p>
<p>When displayng it looks like in the picture (I do not explicitely set all the points but rather XYZ surface and Z spacings vector and thus I save RAM):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/116cb3e518253720979430b3312100a9b9e8f68f.jpeg" alt="image" data-base62-sha1="2u90Iad0ngSbvhidyOg9aYgUHtt" width="332" height="260"></p>
<p>Now I’m looking for a way to display it in SlicerCAT. It seems that neither <code>vtkMRMLModelNode</code> nor <code>vtkVolumeNode</code> is able to add custom vtk dataset to the scene.</p>
<p>If I inherit from <code>vtkMRMLDisplayableNode</code> will I be able to visualize this custom class?</p>
<p>P.S. I’m also looking for a way to inherit from concrete vtk class (instead of abstract vtkDataSet) like vtkPointSet, vtkPolyData or vtkImageData. In this case I expect it would be easier to add to the Slicer</p>

---

## Post #2 by @lassoan (2021-10-26 03:56 UTC)

<p>It is extremely limited what you can do with a custom vtkDataSet-derived object in VTK. I would recommend to derive from vtkPolyData, vtkUnstructuredGrid, or vtkImageData instead.</p>

---
