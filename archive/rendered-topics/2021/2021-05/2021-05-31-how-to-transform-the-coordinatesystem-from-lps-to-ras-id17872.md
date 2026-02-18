# How to transform the CoordinateSystem from LPS to RAS

**Topic ID**: 17872
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/how-to-transform-the-coordinatesystem-from-lps-to-ras/17872

---

## Post #1 by @rongqi_lin (2021-05-31 00:51 UTC)

<p>Hi!<br>
I am a new 3D Slicer user, I want to ask how to tranform CoordinateSystem from LPS to RAS in 3D Slicer 4.11.<br>
I use the 3D Slicer to locate the depth electrodes, and I found the CoordinateSystem in 3D slicer was RAS,but when I save the marker as .fcsv files, the CoordinateSystem changed to the LPS.<br>
However, I need the RAS coordinate. How I could save marker in RAS CoordinateSyste?</p>
<pre><code class="lang-auto">#####
# Markups fiducial file version = 4.11
# CoordinateSystem = LPS
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
1,-4.090399259627052,37.13985137676667,59.97714160258411,0,0,0,1,1,1,0,I-1,,vtkMRMLScalarVolumeNode2
2,-6.3079157103909385,38.139851437085376,59.76311602698254,0,0,0,1,1,1,0,I-2,,vtkMRMLScalarVolumeNode2
3,-9.916078075369118,38.13985152320278,59.46243584005215,0,0,0,1,1,1,0,I-3,,vtkMRMLScalarVolumeNode2
4,-13.073220140355897,39.13985145598736,59.763116298765674,0,0,0,1,1,1,0,I-4,,vtkMRMLScalarVolumeNode2
5,-16.23036220744289,40.13985157886276,59.31209626495044,0,0,0,1,1,1,0,I-5,,vtkMRMLScalarVolumeNode2
6,-19.537844371775503,41.139851588103724,59.3120965270725,0,0,0,1,1,1,0,I-6,,vtkMRMLScalarVolumeNode2
7,-23.29634683162538,42.13985159860482,59.312096790454696,0,0,0,1,1,1,0,I-7,,vtkMRMLScalarVolumeNode2
8,-26.152808700020692,43.13985156856749,59.46243714982236,0,0,0,1,1,1,0,I-8,,vtkMRMLScalarVolumeNode2
######
</code></pre>

---

## Post #2 by @pieper (2021-06-09 14:02 UTC)

<p>Slicer displays RAS in the interface but saves in LPS for broader compatibility.  You can just negate the first two elements of each coordinate to convert.  Look at a few coordinates between your file and Slicer to confirm.</p>

---
