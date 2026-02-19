---
topic_id: 29505
title: "Markups Angle Measurement Numerical Value"
date: 2023-05-17
url: https://discourse.slicer.org/t/29505
---

# MarkUps Angle measurement numerical value

**Topic ID**: 29505
**Date**: 2023-05-17
**URL**: https://discourse.slicer.org/t/markups-angle-measurement-numerical-value/29505

---

## Post #1 by @esomjai (2023-05-17 13:10 UTC)

<p>I was wondering if there’s an equivalent of the script used to assign linear measurement copying to keyboard shortcuts for angle measurement numerical values?</p>
<pre><code class="lang-auto">def copyLineMeasurementsToClipboard():
  measurements = []
  # Collect all line measurements from the scene
  lineNodes = getNodesByClass('vtkMRMLMarkupsLineNode')
  for lineNode in lineNodes:
    if lineNode.GetNumberOfDefinedControlPoints() &lt; 3:
      # incomplete line, skip it
      continue
    # Get node filename that the length was measured on
    try:
      volumeNode = slicer.mrmlScene.GetNodeByID(lineNode.GetNthControlPointAssociatedNodeID(0))
      imagePath = volumeNode.GetStorageNode().GetFileName()
    except:
      imagePath = '(unknown)'
    # Get line node n
    measurementName = lineNode.GetName()
    # Get length measurement
    lineNode.GetMeasurement('length').SetEnabled(True)
    length = str(lineNode.GetMeasurement('length').GetValue())
    # Add fields to results
    measurements.append('\t'.join([imagePath, measurementName, length]))
  # Copy all measurements to clipboard (to be pasted into Excel)
  outputText = "\n".join(measurements) + "\n"
  slicer.app.clipboard().setText(outputText)
  slicer.util.delayDisplay(f"Copied {len(measurements)} length measurements to the clipboard.")

shortcut2 = qt.QShortcut(slicer.util.mainWindow())
shortcut2.setKey(qt.QKeySequence("Ctrl+m"))
shortcut2.connect( 'activated()', copyLineMeasurementsToClipboard)
</code></pre>

---

## Post #2 by @lassoan (2023-05-17 14:42 UTC)

<p>Yes, sure, you can do the same for angle measurements. Probably all you need to do is to change <code>'vtkMRMLMarkupsLineNode'</code> to <code>'vtkMRMLMarkupsAngleNode'</code> and <code>'length'</code> to <code>'angle'</code>.</p>

---

## Post #3 by @esomjai (2023-05-22 12:20 UTC)

<p>This worked perfectly - I’ll add the script below in case anyone else will be looking for it:</p>
<pre><code class="lang-auto">def copyAngleMeasurementsToClipboard():
  measurements = []
  # Collect all line measurements from the scene
  angleNodes = getNodesByClass('vtkMRMLMarkupsAngleNode')
  for angleNode in angleNodes:
    if angleNode.GetNumberOfDefinedControlPoints() &lt; 3:
      # incomplete line, skip it
      continue
    # Get node filename that the length was measured on
    try:
      volumeNode = slicer.mrmlScene.GetNodeByID(angleNode.GetNthControlPointAssociatedNodeID(0))
      imagePath = volumeNode.GetStorageNode().GetFileName()
    except:
      imagePath = '(unknown)'
    # Get angle node n
    measurementName = angleNode.GetName()
    # Get angle measurement
    angleNode.GetMeasurement('angle').SetEnabled(True)
    angle = str(angleNode.GetMeasurement('angle').GetValue())
    # Add fields to results
    measurements.append('\t'.join([imagePath, measurementName, angle]))
  # Copy all measurements to clipboard (to be pasted into Excel)
  outputText = "\n".join(measurements) + "\n"
  slicer.app.clipboard().setText(outputText)
  slicer.util.delayDisplay(f"Copied {len(measurements)} angle measurements to the clipboard.")

shortcut2 = qt.QShortcut(slicer.util.mainWindow())
shortcut2.setKey(qt.QKeySequence("Ctrl+t"))
shortcut2.connect( 'activated()', copyAngleMeasurementsToClipboard)

</code></pre>

---
