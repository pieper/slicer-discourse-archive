---
topic_id: 8494
title: "Export Segment With Transparent Material"
date: 2019-09-19
url: https://discourse.slicer.org/t/8494
---

# Export segment with transparent material

**Topic ID**: 8494
**Date**: 2019-09-19
**URL**: https://discourse.slicer.org/t/export-segment-with-transparent-material/8494

---

## Post #1 by @prorai (2019-09-19 08:04 UTC)

<p>How can i export segment with transparent material using slicer editor or export functionality using python code.</p>

---

## Post #2 by @lassoan (2019-09-19 12:32 UTC)

<p>You can export the entire scene with all display properties to a model file as shown in this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_entire_scene_as_VRML" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_entire_scene_as_VRML</a></p>
<p>Instead of VRML you can use <a href="https://vtk.org/doc/nightly/html/classvtkExporter.html" rel="nofollow noopener">other exporters</a>, such as vtkOBJExporter.</p>

---

## Post #3 by @prorai (2019-09-19 12:37 UTC)

<p>in my case i use ExportSegmentsClosedSurfaceRepresentationToFiles() method to export. is it possible with this method ?</p>

---

## Post #4 by @lassoan (2019-09-19 12:46 UTC)

<p>Yes, you can use <code>ExportSegmentsClosedSurfaceRepresentationToFiles</code>, too. Make sure to save into OBJ format, since color and transparency of each segment is saved in this file format (while STL file format can only store geometry of the mesh and not any display properties).</p>

---

## Post #5 by @prorai (2019-09-23 07:11 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a><br>
Actually i’m using AddSegmentFromClosedSurfaceRepresentation here where i can pass color values [1.0,1.0,1.0] in this format as RGB , how can i add transparency alpha value here?</p>

---

## Post #6 by @prorai (2019-09-23 10:02 UTC)

<p>Edit:<br>
i also tried this<br>
segmentationDisplayNode = self.segmentationNode.GetDisplayNode()<br>
segmentationDisplayNode.SetOpacity3D(0.5)</p>
<p>but it only updates it in slicer 3D view , i’m not getting that opacity in generated output.</p>

---

## Post #7 by @lassoan (2019-09-23 11:36 UTC)

<p>In the exported obj file’s material file you can see that transparency (T value) is set to the opacity of the segment.</p>

---

## Post #8 by @prorai (2019-09-23 12:03 UTC)

<p>Thanks,<br>
segmentationDisplayNode.SetSegmentOpacity3D worked for me… <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
