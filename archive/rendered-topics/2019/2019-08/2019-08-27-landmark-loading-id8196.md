# Landmark loading

**Topic ID**: 8196
**Date**: 2019-08-27
**URL**: https://discourse.slicer.org/t/landmark-loading/8196

---

## Post #1 by @kab (2019-08-27 14:45 UTC)

<p>I have a set of 3D landmarks that are in the same image space as my image volume. How can I load/view both?</p>
<p>I found a documentation for creating landmarks from inside slicer, but not a mechanism for loading an externally created set.</p>

---

## Post #2 by @lassoan (2019-08-27 17:31 UTC)

<p>You can load landmarks from a .csv file (that you can create/edit in Excel) and change the file extension to <code>.fcsv</code> to make Slicer recognize it as a markups fiducial file. Example file:</p>
<pre><code class="lang-nohighlight"># Markups fiducial file version = 4.10
# CoordinateSystem = 0
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
vtkMRMLMarkupsFiducialNode_0,-12.818,-5.885,-10.214,0.000,0.000,0.000,1.000,1,1,0,F-1,,vtkMRMLScalarVolumeNode1
vtkMRMLMarkupsFiducialNode_1,26.127,42.795,-10.214,0.000,0.000,0.000,1.000,1,1,0,F-2,,vtkMRMLScalarVolumeNode1
</code></pre>

---
