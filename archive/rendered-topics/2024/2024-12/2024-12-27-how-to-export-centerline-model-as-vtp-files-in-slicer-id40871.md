# How to export centerline model as .vtp files in slicer

**Topic ID**: 40871
**Date**: 2024-12-27
**URL**: https://discourse.slicer.org/t/how-to-export-centerline-model-as-vtp-files-in-slicer/40871

---

## Post #1 by @pc666nice (2024-12-27 14:56 UTC)

<p>Dear all:<br>
I used the python code that has been proposed by <a href="https://here" rel="noopener nofollow ugc">https://discourse.slicer.org/t/automatic-centerline/14829/23?u=pc666nice</a>, but I can only generate the centerline curve, how I can generate centerline model and export as the vtp file. Here is my code:</p>
<pre><code class="lang-auto">segmentationName = 'MCA-2 1' # D:\PengChen\data-zhongshan\stlall1

segmentName = 'MCA-2 1'

segmentationNode = slicer.util.getNode(segmentationName)

segmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)

extractLogic = ExtractCenterline.ExtractCenterlineLogic()

# Preprocess the surface 

inputSurfacePolyData = extractLogic.polyDataFromNode(segmentationNode, segmentID)

targetNumberOfPoints = 5000.0

decimationAggressiveness = 4 # I had to lower this to 3.5 in at least one case to get it to work, 4 is the default in the module

subdivideInputSurface = False

slicer.app.processEvents()

preprocessedPolyData = extractLogic.preprocess(inputSurfacePolyData, targetNumberOfPoints, decimationAggressiveness, subdivideInputSurface)

##############################################################

# Auto-detect the endpoints

endPointsMarkupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", "Centerline endpoints")

networkPolyData = extractLogic.extractNetwork(preprocessedPolyData, endPointsMarkupsNode)

startPointPosition=None

endpointPositions = extractLogic.getEndPoints(networkPolyData, startPointPosition)

endPointsMarkupsNode.RemoveAllMarkups()

for position in endpointPositions:

endPointsMarkupsNode.AddControlPoint(vtk.vtkVector3d(position))

# Extract the centerline

centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", "Centerline curve")

slicer.app.processEvents() # force update

# centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(preprocessedPolyData, endPointsMarkupsNode) ##################

centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(preprocessedPolyData, endPointsMarkupsNode, curveSamplingDistance=0.001) ##################

slicer.app.processEvents() # force update

centerlinePropertiesTableNode = None

extractLogic.createCurveTreeFromCenterline(centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode)
</code></pre>

---
