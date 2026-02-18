# Warning messages during Extract Centerline Execution

**Topic ID**: 40817
**Date**: 2024-12-20
**URL**: https://discourse.slicer.org/t/warning-messages-during-extract-centerline-execution/40817

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-12-20 12:09 UTC)

<p>Hi to everyone. Today I’m involved in a pipeline that uses ExtractCenterline module to programmatically generate one centerline from one vessel. This pipeline regenerates the segment several times until the  final segment is done. I’m sure that in the first steps the segment is not topologically closed and for sure doesn’t ensure the requirements needed from create a centerline, but at this point I’m quite concern with this two warnings:</p>
<p>The first one, which appears dozens of times per step:<br>
[VTK] Generic Warning: In vtkMath.cxx, line 591<br>
[VTK] Unable to factor linear system</p>
<p>And the second one, which only appears sometimes.<br>
[VTK] Warning: In vtkDelaunay3D.cxx, line 526<br>
[VTK] vtkDelaunay3D (000002B9B69AECA0): 522 degenerate triangles encountered, mesh quality suspect</p>
<p>Now some technical details:</p>
<p>OS: Windows 11.<br>
Slicer’s version: 5.6.2</p>
<p>Code used:</p>
<pre><code class="lang-auto">def extractCenterline(endPointsMarkupsNode, segmentationNode, segmentID,centerlineName):

    extractLogic = ExtractCenterline.ExtractCenterlineLogic()

    # Preprocess the surface

    inputSurfacePolyData = extractLogic.polyDataFromNode(segmentationNode, segmentID)

    targetNumberOfPoints = 5000.0

    decimationAggressiveness = 2.5 # I had to lower this to 3.5 in at least one case to get it to work, 4 is the default in the module

    subdivideInputSurface = False

    preprocessedPolyData = extractLogic.preprocess(inputSurfacePolyData, targetNumberOfPoints, decimationAggressiveness, subdivideInputSurface)


    # Extract the centerline

    centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", centerlineName)

    centerlinePolyData, _ = extractLogic.extractCenterline(preprocessedPolyData, endPointsMarkupsNode)

    centerlinePropertiesTableNode = False

    extractLogic.createCurveTreeFromCenterline(centerlinePolyData, centerlineCurveNode, centerlinePropertiesTableNode)
  

    return centerlineCurveNode
</code></pre>
<p>What I’m wondering is:</p>
<ul>
<li>What means each of this  warnings?</li>
<li>Can I mute the messages in the console?</li>
<li>Can I do anything to avoid this warnings (smooth the geometry, make it thinner or fatter…)</li>
</ul>
<p>To be clear the code runs well, and ExtractCenterline works as I expect, but  I want to understand better the situation.<br>
Thanks a lot.</p>

---
