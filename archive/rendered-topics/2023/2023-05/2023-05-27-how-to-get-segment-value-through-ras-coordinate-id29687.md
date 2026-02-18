# How to get segment value through ras coordinate

**Topic ID**: 29687
**Date**: 2023-05-27
**URL**: https://discourse.slicer.org/t/how-to-get-segment-value-through-ras-coordinate/29687

---

## Post #1 by @jay1987 (2023-05-27 07:30 UTC)

<p>hi,Community<br>
My train of thought to solve the problem is this:<br>
1.get ras coordinate (ras_x,ras_y,ras_z) through crosshair node<br>
2.get segmentationNode’s rastoijk matrix use code below</p>
<pre><code class="lang-auto">commonGeometryString = segmentationNode.GetSegmentation().DetermineCommonLabelmapGeometry(slicer.vtkSegmentation.EXTENT_UNION_OF_SEGMENTS, None)
commonGeometryImage = slicer.vtkOrientedImageData()
slicer.vtkSegmentationConverter.DeserializeImageGeometry(commonGeometryString, commonGeometryImage, False) 
ijkToRas = vtk.vtkMatrix4x4()
commonGeometryImage.GetImageToWorldMatrix(ijkToRas)
rastoijk = vtk.vtkMatrix4x4()
vtk.vtkMatrix4x4.Invert(ijkToRas, rastoijk)
</code></pre>
<p>3.change ras point to ijk point</p>
<blockquote>
<p>point_Ijk = [0, 0, 0, 1]<br>
rastoijk.MultiplyPoint(np.append(ras,1.0), point_Ijk)<br>
point_Ijk = [ int(round(c)) for c in point_Ijk[0:3] ]</p>
</blockquote>
<p>4.change the 0th segment into numpy array</p>
<pre><code class="lang-auto">segmentid = util.GetNthSegmentID(segment_node,0)
segmentArray = util.arrayFromSegment(segmentationNode,segmentid).T
</code></pre>
<p>5.get segment value through ijk point<br>
final_value = segmentArray[point_Ijk[0],point_Ijk[1],point_Ijk[2]]</p>
<p>The final result is wrong, it seems that there is always a matrix transformation difference between the correct result, but I don’t know where the error occurred</p>

---

## Post #2 by @lassoan (2023-05-28 00:38 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-segments-visible-at-a-selected-position">This example in the script repository</a> shows how to get list of segments visible at a specific position.</p>

---

## Post #3 by @jay1987 (2023-05-28 02:48 UTC)

<p>thank you lassoan ,it’s work!</p>

---
