# Exporting a DTI object as a 3D File

**Topic ID**: 987
**Date**: 2017-09-01
**URL**: https://discourse.slicer.org/t/exporting-a-dti-object-as-a-3d-file/987

---

## Post #1 by @vascopontinha (2017-09-01 03:36 UTC)

<p>Operating system: macOS<br>
Slicer version: 4.3 &amp; 4.7</p>
<p>Hi everyone,</p>
<p>While I was building a tractography display, Slicer allows me to export it as a *.obj file, however, it fails to export the labels file. Thus, when I try to open that *.obj file in any 3D modeler, it does not have the colors associated with the tractography analysis.<br>
I already read the thread Export a tractography display as a 3D file, but the code provided by James and Steve does not seem to work on  Slicer 4.3 nor Slicer 4.7.</p>
<p>Can anyone help me out with this? Is is possible to merge the label files with the object/model file?</p>
<p>I used the following source-code:</p>
<p>Slicer 4.3<br>
plyFilePath = “/tmp/fibers.ply”</p>
<p>lineDisplayNode = getNode(“<em>LineDisplay</em>”)</p>
<p>tuber = vtk.vtkTubeFilter()<br>
tuber.SetInput(lineDisplayNode.GetOutputPolyData())</p>
<p>tubes = tuber.GetOutput()<br>
tubes.Update()<br>
scalars = tubes.GetPointData().GetArray(0)<br>
scalars.SetName(“scalars”)</p>
<p>triangles = vtk.vtkTriangleFilter()<br>
triangles.SetInput(tubes)</p>
<p>colorNode = lineDisplayNode.GetColorNode()<br>
lookupTable = vtk.vtkLookupTable()<br>
lookupTable.DeepCopy(colorNode.GetLookupTable())<br>
lookupTable.SetTableRange(0,1)</p>
<p>plyWriter = vtk.vtkPLYWriter()<br>
plyWriter.SetInput(triangles.GetOutput())<br>
plyWriter.SetLookupTable(lookupTable)<br>
plyWriter.SetArrayName(“scalars”)</p>
<p>plyWriter.SetFileName(plyFilePath)<br>
plyWriter.Write()</p>
<p>Slicer 4.7 (James mentioned it was untested and it does not effectively work)<br>
plyFilePath = “/tmp/fibers.ply”</p>
<p>lineDisplayNode = getNode(“<em>LineDisplay</em>”)</p>
<p>tuber = vtk.vtkTubeFilter()<br>
tuber.SetInputData(lineDisplayNode.GetOutputPolyData())</p>
<p>tubes = tuber.GetOutputData()<br>
tubes.Update()<br>
scalars = tubes.GetPointData().GetArray(0)<br>
scalars.SetName(“scalars”)</p>
<p>triangles = vtk.vtkTriangleFilter()<br>
triangles.SetInputConnection(tubes)</p>
<p>colorNode = lineDisplayNode.GetColorNode()<br>
lookupTable = vtk.vtkLookupTable()<br>
lookupTable.DeepCopy(colorNode.GetLookupTable())<br>
lookupTable.SetTableRange(0,1)</p>
<p>plyWriter = vtk.vtkPLYWriter()<br>
plyWriter.SetInputConnection(triangles.GetOutputPort())<br>
plyWriter.SetLookupTable(lookupTable)<br>
plyWriter.SetArrayName(“scalars”)</p>
<p>plyWriter.SetFileName(plyFilePath)<br>
plyWriter.Write()<br>
Thanks in advance,</p>
<p>Vasco Pontinha</p>

---

## Post #2 by @pieper (2017-09-01 14:09 UTC)

<p>Hi Vasco -</p>
<p>I updated the example script here and it worked for me with Slicer 4.7-2017-08-10 with SlicerDMRI installed.  There was a missing update for the triangle filter.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_fiber_tracts_to_Blender.2C_including_color</a></p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @vascopontinha (2017-09-15 19:54 UTC)

<p>Hi Steve,</p>
<p>Thank you so much for updating the code - I was successful in exporting the file!!</p>
<p>Vasco</p>

---

## Post #4 by @pedro_luis_solarte (2018-04-26 13:34 UTC)

<p>Hi, Where do I have to put that script?</p>

---

## Post #5 by @ihnorton (2018-04-26 13:50 UTC)

<p>The script is now available as a module in SlicerDMRI in SlicerPreview (nightly) builds, called <code>Export tractography to PLY (mesh)</code>.</p>

---

## Post #6 by @pedro_luis_solarte (2018-04-26 17:01 UTC)

<p><strong>Hi, I tried to do like that but it was this error</strong></p>
<p>Traceback (most recent call last):<br>
File “C:/Users/AIDE/AppData/Roaming/NA-MIC/Extensions-27159/SlicerDMRI/lib/Slicer-4.9/qt-scripted-modules/TractographyExportPLY.py”, line 149, in onExport<br>
number_of_sides = self.numSidesSelector.value)<br>
File “C:/Users/AIDE/AppData/Roaming/NA-MIC/Extensions-27159/SlicerDMRI/lib/Slicer-4.9/qt-scripted-modules/TractographyExportPLY.py”, line 180, in exportFiberBundleToPLYPath<br>
tuber.SetNumberOfSides(number_of_sides)<br>
TypeError: SetNumberOfSides argument 1: integer argument expected, got float</p>
<p><strong>I do not know what to do.</strong></p>

---

## Post #7 by @ihnorton (2018-04-26 20:59 UTC)

<p>Thanks for the report. I pushed a fix that will be available in the SlicerPreview build tomorrow. For a quick local fix, you can edit the file:</p>
<blockquote>
<p>C:/Users/AIDE/AppData/Roaming/NA-MIC/Extensions-27159/SlicerDMRI/lib/Slicer-4.9/qt-scripted-modules/TractographyExportPLY.py`</p>
</blockquote>
<p>and change line 180 from</p>
<blockquote>
<p>tuber.SetNumberOfSides(number_of_sides)</p>
</blockquote>
<p>to</p>
<blockquote>
<p>tuber.SetNumberOfSides(int(number_of_sides))</p>
</blockquote>

---

## Post #8 by @pedro_luis_solarte (2018-05-02 09:12 UTC)

<p>Thank you help me Can I export it with color?</p>

---

## Post #9 by @pedro_luis_solarte (2018-05-02 11:22 UTC)

<p>Hi. How do I export the tractography with the colors in windows 10?</p>

---

## Post #10 by @ihnorton (2018-05-02 12:45 UTC)

<p>Color export works – try setting the color mode to <code>FractionalAnisotropy</code> in the Tractography Display module (I checked PLY output in MeshLab). The issue is that the range is set to [0,1] for all modes, which is too wide for some of the scalar maps. In those cases most/all of the mesh vertices end up clamped to one end of the colormap range.</p>
<p>I will make this an option in the GUI, but here is a change you can make locally for now:</p>
<pre><code class="lang-auto">diff --git a/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py b/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py
index 7de1b31b6..ce782ddf1 100644
--- a/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py
+++ b/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py
@@ -194,7 +194,8 @@ class TractographyExportPLYLogic(ScriptedLoadableModuleLogic):
     colorNode = lineDisplayNode.GetColorNode()
     lookupTable = vtk.vtkLookupTable()
     lookupTable.DeepCopy(colorNode.GetLookupTable())
-    lookupTable.SetTableRange(0,1)
+    scalarRange = lineDisplayNode.GetScalarRange()
+    lookupTable.SetTableRange(scalarRange[0], scalarRange[1])

     plyWriter = vtk.vtkPLYWriter()
     plyWriter.SetInputData(triangles.GetOutput())
</code></pre>

---

## Post #11 by @ihnorton (2018-06-27 18:28 UTC)

<p>A post was split to a new topic: <a href="/t/save-derived-dti-heatmap/3319">Save derived DTI heatmap</a></p>

---
