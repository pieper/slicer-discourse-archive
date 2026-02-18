# How to export model node to VRML 2 and STL (ascii and binary)

**Topic ID**: 10804
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/how-to-export-model-node-to-vrml-2-and-stl-ascii-and-binary/10804

---

## Post #1 by @mjg (2020-03-23 19:35 UTC)

<p>Hello,</p>
<p>I need to be able to export a model node as VRML 2, ascii STL, and binary STL files for a module I am developing. I know essentially nothing about vtk so any help or resources you could provide would be lovely.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-03-23 19:51 UTC)

<p>The easiest to export to binary STL and OBJ is to use this <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a4b5328985b2d98cbbc93a5b2ae7fde6b">ExportSegmentsClosedSurfaceRepresentationToFiles</a> method.</p>
<p>VRML is really really old, I would not recommend to use it, but fortunately VTK still supports it. VTK also has ASCII option for writing STL. You can do the export in two steps:</p>
<ol>
<li>Export segmentation to model - <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_nodes_from_segmentation_node">se example here</a>
</li>
<li>Get vtkPolyData from the created model nodes and use <a href="https://vtk.org/doc/nightly/html/classvtkSTLWriter.html">vtkSTLWriter</a> and <a href="https://vtk.org/doc/nightly/html/classvtkVRMLExporter.html">vtkVRMLExporter</a>. See examples for getting vtkPolyData from a model node and write to file in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>; a complete example of using an exporter in <a href="https://github.com/PerkLab/SlicerOpenAnatomy/blob/master/OpenAnatomyExport/OpenAnatomyExport.py">this module</a>.</li>
</ol>

---

## Post #3 by @mjg (2020-03-23 21:18 UTC)

<p>Perfect, I got it working. Thank you so much!</p>

---
