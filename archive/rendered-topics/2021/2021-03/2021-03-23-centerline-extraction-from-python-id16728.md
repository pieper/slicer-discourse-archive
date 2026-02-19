---
topic_id: 16728
title: "Centerline Extraction From Python"
date: 2021-03-23
url: https://discourse.slicer.org/t/16728
---

# Centerline extraction from python

**Topic ID**: 16728
**Date**: 2021-03-23
**URL**: https://discourse.slicer.org/t/centerline-extraction-from-python/16728

---

## Post #1 by @Ge_Tang (2021-03-23 21:11 UTC)

<p>Operating system: Mac<br>
Slicer version:4.11<br>
Expected behavior: The centerline model from GUI of slicer has a different number of points compared with the centerline model I get from the python script<br>
Actual behavior:</p>
<p>This is the code I use in python to get a centerline model:</p>
<pre><code class="lang-python">import ExtractCenterline
def centerlineExtractcenterline(nameSeg:str, nameRegion:str, nameFids:str):
    ec = ExtractCenterline.ExtractCenterlineLogic()
    n = getNode(nameSeg) 
    s = n.GetSegmentation()
    ss = s.GetSegment(s.GetSegmentIdBySegmentName(nameRegion)).GetRepresentation('Closed surface')
    fids = getNode(nameFids)
    centerlinePolyData,voronoiDiagramPolyData = ec.extractCenterline(ss, fids)
    return centerlinePolyData, voronoiDiagramPolyData

centerlinePolyData, voronoiDiagramPolyData = centerlineExtractcenterline('seg_nerve', 'R_optic_nerve', 'F1')

model = slicer.vtkMRMLModelNode()
model.SetAndObservePolyData(centerlinePolyData)
modelDisplay = slicer.vtkMRMLModelDisplayNode()

modelDisplay.SetColor(1, 1, 0)
modelDisplay.BackfaceCullingOff()
modelDisplay.SetOpacity(0.8)
modelDisplay.SetPointSize(3)

modelDisplay.SetSliceIntersectionVisibility(True)
modelDisplay.SetVisibility(True)
slicer.mrmlScene.AddNode(modelDisplay)
model.SetAndObserveDisplayNodeID(modelDisplay.GetID())
modelDisplay.SetInputPolyDataConnection(model.GetPolyDataConnection())
slicer.mrmlScene.AddNode(model)
</code></pre>
<p>Thank you so much!</p>
<p>Ge Tang</p>

---

## Post #2 by @lassoan (2021-03-24 16:19 UTC)

<p>I don’t see any obvious problem with your code snippet. I would recommend to compare the execution path in the Centerline module GUI by stepping through the code step by step using a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools">Python debugger</a>.</p>

---

## Post #3 by @Ge_Tang (2021-03-25 17:14 UTC)

<p>Thank you Dr. Lassonan. I figured out that the python code did not run the preprocess input surface. But the GUI set this as default​. <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---
