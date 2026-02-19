---
topic_id: 14924
title: "Retrieving Transform Matrix From Transforms Module"
date: 2020-12-07
url: https://discourse.slicer.org/t/14924
---

# Retrieving Transform Matrix From Transforms Module

**Topic ID**: 14924
**Date**: 2020-12-07
**URL**: https://discourse.slicer.org/t/retrieving-transform-matrix-from-transforms-module/14924

---

## Post #1 by @YBurakD (2020-12-07 10:26 UTC)

<p>Hi,</p>
<p>I have 3D images that I need to rotate and to do this I am using the transforms module. I want to do the rotation in the gui with sliders and retrieve the transform matrix via python code to apply the transform with ITK later. However, in transform node I couldn’t find any function that returns this information. Is there any way to get the transform matrix?<br>
Here is the code I use to create transform node and visualize the transform</p>
<pre><code>        slicer.util.mainWindow().moduleSelector().selectModule('Transforms')
        transformNode = slicer.vtkMRMLTransformNode()
        slicer.mrmlScene.AddNode(transformNode)
        
        volumeNode = slicer.util.loadVolume(filePath)
        volRenLogic = slicer.modules.volumerendering.logic()
        
        #Display the volume
        displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)
        displayNode.SetVisibility(True)
        
        #Center 3d Volume
        layoutManager = slicer.app.layoutManager()
        threeDWidget = layoutManager.threeDWidget(0)
        threeDView = threeDWidget.threeDView()
        threeDView.resetFocalPoint()
        
        volumeNode.SetAndObserveTransformNodeID(transformNode.GetID())</code></pre>

---

## Post #2 by @lassoan (2020-12-07 22:15 UTC)

<p>Transform’s module developer documentation should answer all the above questions: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Information_for_Developers">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Information_for_Developers</a></p>
<p>Let us know if you have any remaining questions.</p>

---
