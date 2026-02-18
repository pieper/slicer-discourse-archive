# Minimum Distance Between Segmentations

**Topic ID**: 14646
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/minimum-distance-between-segmentations/14646

---

## Post #1 by @ahopf (2020-11-16 18:46 UTC)

<p>I am trying to calculate the minimum Hausdorff distance between two segmentations. I am new to coding and wondering if someone can tell me if the code (from the Support discussion thread “Distance between two segments”) as I have it is correct according to the pictured scene:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3edbfd4861958f9883433367e17a2e224e9a5cf5.png" alt="image" data-base62-sha1="8Y4VycFPUxPQ8Jb4P6fzCUyRNUF" width="509" height="116"></p>
<pre><code class="lang-auto">import vtkSlicerSegmentComparisonModuleLogicPython
s=getNode('Left Excised Volume') 
p1=s.GetClosedSurfaceRepresentation('Left Excised Volume') 
p2=s.GetClosedSurfaceRepresentation('Left Structures')
pdf=vtkSlicerSegmentComparisonModuleLogicPython.vtkPolyDataDistanceHistogramFilter()
pdf.SetInputReferencePolyData(p1)
pdf.SetInputComparePolyData(p2)
pdf.Update()
pdf.GetNthPercentileHausdorffDistance(0)
</code></pre>
<p>As I am using it, Slicer crashes after “pdf.SetInputReferencePolyData(p1)."</p>

---

## Post #2 by @lassoan (2020-11-16 19:36 UTC)

<p>Segment comparison is for comparing segments, so it assumes that segments are similar, therefore it computes maximum distance.</p>
<p>If you want to compute maximum Hausdorff distance: The methods you found are for low-level manipulations only. Instead, I would recommend to add a new <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SegmentComparison/Logic/vtkMRMLSegmentComparisonNode.h">vtkMRMLSegmentComparisonNode</a> to the scene, set all the inputs into that node, and call <code>slicer.modules.segmentcomparison.logic().ComputeDiceStatistics(mySegmentComparisonNode)</code> to compute the results.</p>
<p>If you want to compute minimum distance (e.g., asses safety margin) then you can use ModelToModelDistance extension for that. You can get computed distance values from the model by using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPointData">slicer.util.arrayFromModelPointData</a> (you can then get the minimum value, a histogram of the distance distribution, etc. using numpy).</p>

---

## Post #3 by @ahopf (2020-11-17 21:41 UTC)

<p>Thank you, Dr. Lasso. I wonder if you can help me to understand how to properly use slicer.util.arrayFromModelPointData and numpy to generate these values.</p>
<p>I assigned the model node:<br>
modelNode = slicer.util.getNode(‘facialnerveoutput’)<br>
<span class="hashtag">#facialnerveoutput</span> is the output model from the “model to model” extension</p>
<p>Attempted to run:<br>
slicer.util.arrayFromModelPointData(modelNode, ‘array1’)<br>
AND<br>
distances = slicer.util.arrayFromModelPointData (modelNode, ‘Array1’)</p>
<p>In both cases, using ‘modelNode’ or the assigned ‘facialnerveoutput’ node, I receive this error:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py”, line 855, in arrayFromModelPointData<br>
narray = vtk.util.numpy_support.vtk_to_numpy(arrayVtk)<br>
File “C:\Program Files\Slicer 4.10.2\bin\Lib\site-packages\vtkmodules\util\numpy_support.py”, line 216, in vtk_to_numpy<br>
typ = vtk_array.GetDataType()<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetDataType’</p>

---

## Post #4 by @lassoan (2020-11-19 03:14 UTC)

<p>The distance array name is not <code>Array1</code>. Latest Slicer Preview Release provides more meaningful error message if you give incorrect input to <code>arrayFromModelPointData</code>.</p>

---
