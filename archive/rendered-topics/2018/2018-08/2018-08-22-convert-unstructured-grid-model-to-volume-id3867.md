---
topic_id: 3867
title: "Convert Unstructured Grid Model To Volume"
date: 2018-08-22
url: https://discourse.slicer.org/t/3867
---

# Convert unstructured grid model to volume

**Topic ID**: 3867
**Date**: 2018-08-22
**URL**: https://discourse.slicer.org/t/convert-unstructured-grid-model-to-volume/3867

---

## Post #1 by @ghnguyen (2018-08-22 21:29 UTC)

<p>Hi,<br>
I tried loading the volumetric mesh (vtkUnstructuredGrid) by using both the interface Load Data as Volume and using “slicer.util.loadVolume(’/path/to/file’)” on the Python interactor to no avail. Slicer simply doesn’t load it up. However, loading it as Model would always work. How do I load it as Volume?</p>
<p>Here’s a sample unstructuredgrid below:</p>
<hr>
<h1>vtk DataFile Version 3.0</h1>
<p>2D scalar data<br>
ASCII</p>
<p>DATASET UNSTRUCTURED_GRID<br>
POINTS 18 float<br>
0 0 2<br>
1 0 2<br>
1 1 2<br>
0 1 2<br>
2 0 2<br>
3 0 2<br>
3 1 2<br>
2 1 2<br>
4 5 6<br>
2 2 4<br>
4 4 4<br>
6 5 2<br>
7 2 4<br>
3 4 2<br>
2 4 6<br>
1 3 5<br>
2 9 8<br>
8 7 5</p>
<p>CELLS 4 44<br>
10 0 1 2 8 9 4 5 13 12 11<br>
10 0 2 3 15 16 4 6 1 17 10<br>
10 1 4 2 9 10 11 12 13 14 16<br>
10 9 8 7 6 5 4 3 2 1 0</p>
<p>CELL_TYPES 4<br>
24<br>
24<br>
24<br>
24</p>

---

## Post #2 by @lassoan (2018-08-23 04:59 UTC)

<p>Surface and volumetric meshes are represented in Slicer as model nodes. You can convert a volumetric mesh to volume by sampling the mesh at each voxel using vtkProbeFilter. Here is a complete example of how to do that: <a href="https://github.com/lassoan/SlicerNotebooks/blob/master/UnstructuredGridToVolume.ipynb">https://github.com/lassoan/SlicerNotebooks/blob/master/UnstructuredGridToVolume.ipynb</a></p>

---

## Post #3 by @ghnguyen (2018-08-23 15:45 UTC)

<p>I was able to make it work thanks to your help. One thing I noticed was that the vtkUnstructuredGrid mesh must have CELL_DATA and POINT_DATA for Slicer to work correctly. I’m a beginner at vtk in general, so I guess my question would be which part of your code requires those two pieces of data? Or does volumetric mesh in general needs to have those in Slicer? I was able to generate volumes without those in vtkpython on conda and Paraview. Thanks a lot Andras!</p>

---

## Post #4 by @lassoan (2018-08-23 16:19 UTC)

<p>Maybe vtkProbeFilter specifically needs cell or point data (I don’t think you need both). You can convert between point and cell data as needed using <a href="https://www.vtk.org/doc/nightly/html/classvtkPointDataToCellData.html">vtkPointDataToCellData</a> and <a href="https://www.vtk.org/doc/nightly/html/classvtkCellDataToPointData.html">vtkCellDataToPointData</a>.</p>

---

## Post #5 by @Asees_Kaur (2020-10-02 00:37 UTC)

<p>hi this page has been taken down. would you mind reuploading it, im having a similar issue</p>

---

## Post #6 by @lassoan (2022-01-29 01:40 UTC)

<p>A post was split to a new topic: <a href="/t/convert-mesh-to-volume/21686">Convert mesh to volume</a></p>

---
