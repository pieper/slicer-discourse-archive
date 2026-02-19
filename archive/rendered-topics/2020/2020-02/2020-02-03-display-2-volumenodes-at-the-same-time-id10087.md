---
topic_id: 10087
title: "Display 2 Volumenodes At The Same Time"
date: 2020-02-03
url: https://discourse.slicer.org/t/10087
---

# Display 2 VolumeNodes at the same time

**Topic ID**: 10087
**Date**: 2020-02-03
**URL**: https://discourse.slicer.org/t/display-2-volumenodes-at-the-same-time/10087

---

## Post #1 by @electus (2020-02-03 14:07 UTC)

<p>Hi guys,</p>
<p>I am trying to diyplay 2 volumes at the same time in the 2D Views and i am facing 2 problems.<br>
One of the volume is a CT and the other has some random values, while being of the same size as the CT.</p>
<p>When I add the Volume Node to the scene, that works and I can see it in the Subject Hirarchy; but it is invisible in the 2D views. When i toggle it visible in the subject hirarchy my CT Vlume atomatically dissappears. I think that tas should technically be possible but i am definetly doing something wrong.<br>
Here is my code.</p>
<pre><code>nodeName = "MyNewVolume"
imageSize = [116, 116, 60]
voxelType=vtk.VTK_FLOAT
imageOrigin = [-57.5, -29.5, -57.5]
imageSpacing = [1.0, 1.0, 1.0]
imageDirections = [[1,0,0], [0,0,1], [0,1,0]]

imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.AllocateScalars(voxelType, 1)
for z in range(0,60):
  for y in range(0,116):
    for x in range(0,116):
      imageData.SetScalarComponentFromDouble(x,y,z,0,0.5*z)

volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetIJKToRASDirections(imageDirections)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()

self.displayNode = volumeNode.GetDisplayNode()
self.displayNode.SetVisibility(True)
self.displayNode.SetWindowLevelFromPreset(0)
self.displayNode.SetOpacity(0.3)
</code></pre>
<p>I would like both volumes to be visible at the same time. But my defined opacity here is not changing the opacity in the 2D views. So probably there is something wrong aswell.</p>
<p>Thanks for help!</p>

---

## Post #2 by @Juicy (2020-02-05 06:52 UTC)

<p>Have you tried:</p>
<pre><code>slicer.util.setSliceViewerLayers(background=volumeNode, foreground=&lt;insert variable name of other CT volume here&gt;, foregroundOpacity=0.7)
</code></pre>
<p>This should work as long as both the volumes are overlaid on top of each other. The background image is used as a mask so you may want to swap which volume is foreground and which is background depending on what you are after.</p>

---
