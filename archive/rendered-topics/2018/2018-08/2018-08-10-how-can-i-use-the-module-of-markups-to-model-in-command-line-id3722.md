---
topic_id: 3722
title: "How Can I Use The Module Of Markups To Model In Command Line"
date: 2018-08-10
url: https://discourse.slicer.org/t/3722
---

# How can I use the module of "Markups to Model" in command line?

**Topic ID**: 3722
**Date**: 2018-08-10
**URL**: https://discourse.slicer.org/t/how-can-i-use-the-module-of-markups-to-model-in-command-line/3722

---

## Post #1 by @shahrokh (2018-08-10 14:44 UTC)

<p>Hi<br>
Dear developers and users</p>
<p>How can I use the module of “Markups to Model” in command line?<br>
I noticed that I can create a tube model around of centerline using the module of “Markups to Model” . At now, I want create this tube using this module in the command line. How can I do it?<br>
Is it another module  to create the tube around centerline?</p>
<p>Please guide me.<br>
Shahrokh</p>

---

## Post #2 by @tavaughan (2018-08-10 15:24 UTC)

<p>Hi shahrokh,</p>
<p>You mean through python interactor?</p>
<p>There is no public function in the module yet to do this, but I can add one. In the meantime you can use vtk.vtkTubeFilter (<a href="https://www.vtk.org/doc/nightly/html/classvtkTubeFilter.html" rel="nofollow noopener">https://www.vtk.org/doc/nightly/html/classvtkTubeFilter.html</a>) to create tube poly data around the points. Something like this (note I haven’t personally tried running this so you may need to tweak it):</p>
<pre><code class="lang-auto">  numPoints = pointsToConnect.GetNumberOfPoints()
  lineCellArray = vtk.vtkCellArray()
  lineCellArray.InsertNextCell( numPoints )

  for i in xrange(0,numPoints)
  {
    lineCellArray.InsertCellPoint( i )
  }

  linePolyData = vtk.vtkPolyData()
  linePolyData.SetPoints( pointsToConnect )
  linePolyData.SetLines( lineCellArray )

  tubeSegmentFilter = vtk.vtkTubeFilter()
  tubeSegmentFilter.SetInputData( linePolyData )
  tubeSegmentFilter.SetRadius( tubeRadius ) #INSERT VALUE
  tubeSegmentFilter.SetNumberOfSides( tubeNumberOfSides ) #INSERT VALUE
  tubeSegmentFilter.CappingOn()
  tubeSegmentFilter.Update()

  # Access poly data by calling tubeSegmentFilter.GetOutput()
</code></pre>
<p>If you want to assign it to a vtkMRMLModelNode you’ll need to do:</p>
<pre><code class="lang-auto">  modelNode.SetAndObservePolyData( tubeSegmentFilter.GetOutput() )
  modelNode.CreateDefaultDisplayNodes()
</code></pre>
<p>I hope that helps. If it doesn’t answer your question please let me know.</p>
<p>Thomas</p>

---

## Post #3 by @shahrokh (2018-08-13 14:26 UTC)

<p>Hello<br>
Dear Thomas,</p>
<p>Thanks a lot for your guidance. At now, I want to create tube poly data around the points in my vtp centerline file according with your commands.<br>
I have some problems to do it.<br>
I enter the following commands in python interactor of Slicer.</p>
<p>import vtk<br>
filename = “~/centerlineRodCT001.vtp”<br>
reader = vtk.vtkXMLPolyDataReader()<br>
reader.SetFileName(filename)<br>
reader.Update()<br>
numPoints = reader.GetNumberOfPoints()<br>
lineCellArray = vtk.vtkCellArray()<br>
lineCellArray.InsertNextCell(numPoints)<br>
for i in range(0,numPoints):<br>
lineCellArray.InsertCellPoint( i )<br>
linePolyData = vtk.vtkPolyData()<br>
linePolyData.SetPoints(reader)</p>
<p>At this moment, I get the following error.<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: SetPoints argument 1: method requires a vtkPoints, a vtkXMLPolyDataReader was provided.</p>
<p>Please guide me. How can I get vtkPoints argument?<br>
Best regards,<br>
Shahrokh</p>

---

## Post #4 by @shahrokh (2018-08-14 14:17 UTC)

<p>Excuse me. Unfortunately I can not find any python code example about reading centelines vtp file and applying vtktubefilter to it. Please let me know where I wrong it.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #5 by @tavaughan (2018-08-14 17:01 UTC)

<p>Assuming that the points saved in the file are already in the correct order…</p>
<p>This should get you a vtkPolyData object:<br>
polydata = reader.GetOutput()</p>
<p>This should get you a vtkPoints object from the vtkPolyData object:<br>
points = polydata.GetPoints()</p>

---

## Post #6 by @shahrokh (2018-08-14 17:23 UTC)

<p>Dear Thomas<br>
Thanks a lot for your guidance. I’m sure this solves my problem.<br>
Best regards.</p>

---

## Post #7 by @shahrokh (2018-08-15 09:15 UTC)

<p>Dear Thomas</p>
<p>Thanks a lot for your guidance. Finally, I can create a tube around the centerline vtp file with the following lines:</p>
<p>import vtk</p>
<p>filename = “/home/sn/centerlineRodCT001.vtp”<br>
reader = vtk.vtkXMLPolyDataReader()<br>
reader.SetFileName(filename)<br>
reader.Update()<br>
polydata = reader.GetOutput()<br>
points = polydata.GetPoints()<br>
numPoints = reader.GetNumberOfPoints()<br>
lineCellArray = vtk.vtkCellArray()<br>
lineCellArray.InsertNextCell(numPoints)<br>
for i in range(0,numPoints):<br>
lineCellArray.InsertCellPoint( i )<br>
linePolyData = vtk.vtkPolyData()<br>
linePolyData.SetPoints(points)<br>
linePolyData.SetLines( lineCellArray )<br>
tubeSegmentFilter = vtk.vtkTubeFilter()<br>
tubeSegmentFilter.SetInputData( linePolyData )<br>
tubeSegmentFilter.SetRadius(2)<br>
tubeSegmentFilter.SetNumberOfSides(10)<br>
tubeSegmentFilter.SetOutputPointsPrecision(1)<br>
tubeSegmentFilter.CappingOn()<br>
tubeSegmentFilter.Update()<br>
tubeSegmentFilter.GetOutput()<br>
writer = vtk.vtkXMLPolyDataWriter()<br>
writer.SetFileName(“tube.vtp”)<br>
writer.SetInputDataObject(tubeSegmentFilter.GetOutput())<br>
writer.Write()</p>
<p>Best regards,<br>
Shahrokh</p>

---
