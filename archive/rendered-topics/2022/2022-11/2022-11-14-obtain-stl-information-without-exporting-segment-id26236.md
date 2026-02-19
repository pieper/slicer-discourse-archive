---
topic_id: 26236
title: "Obtain Stl Information Without Exporting Segment"
date: 2022-11-14
url: https://discourse.slicer.org/t/26236
---

# Obtain STL information without exporting segment

**Topic ID**: 26236
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/obtain-stl-information-without-exporting-segment/26236

---

## Post #1 by @bserrano (2022-11-14 15:37 UTC)

<p>Hi,</p>
<p>I have a Python script that works with .stl files. In order to speed things up in Slicer, I would like to get the information from the .stl file without having to export it. Is it possible?</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2022-11-14 18:17 UTC)

<p>I guess you mean you would want to export to file without exporting to model node. You can do that by-right-clicking “Export to files…” function (in drop-down menu of the green right-arrow button in Segment Editor).</p>
<p>This feature is avaiable in the method: <a href="https://apidocs.slicer.org/main/classvtkSlicerSegmentationsModuleLogic.html#a4b5328985b2d98cbbc93a5b2ae7fde6b">slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles()</a></p>

---

## Post #3 by @Atsui_75 (2022-11-15 12:01 UTC)

<p>Hi!</p>
<p>I have created this function from information of different forums to get vertices and faces of segmentation in Slicer directly as numpy arrays. It works thanks to the module pyvista.</p>
<pre><code class="lang-auto">
def polydata(segmentation = 'Segmentation', segment = 'Segment_1'):
    segmentationNode = slicer.util.getNode(segmentation)
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segment)
    
    superficie = vtk.vtkPolyData()
    slicer.vtkSlicerSegmentationsModuleLogic.GetSegmentClosedSurfaceRepresentation(segmentationNode, segmentId, superficie, True)
    
    return pyvista.PolyData(superficie)
</code></pre>
<p>Is this what you are looking for?</p>

---

## Post #4 by @bserrano (2022-11-15 14:57 UTC)

<p>That’s it!</p>
<p>Grazas <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
