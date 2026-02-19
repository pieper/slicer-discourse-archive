---
topic_id: 19786
title: "How To Decouple Segmentations From Model And Hide The Segmen"
date: 2021-09-21
url: https://discourse.slicer.org/t/19786
---

# How to decouple segmentations from model and hide the segmentations slice views?

**Topic ID**: 19786
**Date**: 2021-09-21
**URL**: https://discourse.slicer.org/t/how-to-decouple-segmentations-from-model-and-hide-the-segmentations-slice-views/19786

---

## Post #1 by @srivastavava (2021-09-21 14:32 UTC)

<pre><code class="lang-auto">import slicer 
import qt 
fname = qt.QFileDialog.getOpenFileName()
loadedVolumeNode = slicer.util.loadVolume(fname)
segfname = qt.QFileDialog.getOpenFileName()
segmentationNode = slicer.util.loadSegmentation(segfname)
labelmapNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapNode, loadedVolumeNode)
parameters = {}
parameters["InputVolume"] = segmentationNode
parameters["Decimate"] = 0
parameters["JointSmoothing"] = False
parameters["SplitNormals"] = False
parameters["PointNormals"] = True
parameters["Pad"] = True
outputH = slicer.vtkMRMLModelHierarchyNode()
outputH.SetScene(slicer.mrmlScene)
outputH.SetName("3D Models")
slicer.mrmlScene.AddNode(outputH)
parameters["ModelSceneFile"] = outputH
parameters["Filter Type"] = 'Laplacian'
parameters["Smooth"] = 15
modelMaker = slicer.modules.modelmaker
slicer.cli.runSync(modelMaker, None, parameters)
ras2lps = vtk.vtkMatrix4x4()
ras2lps.SetElement(0,0,-1)
ras2lps.SetElement(1,1,-1)
ras2lpsTransform = vtk.vtkTransform()
ras2lpsTransform.SetMatrix(ras2lps)
# This is to try 
slicer.util.setSliceViewerLayers(background=loadedVolumeNode)
segmentationNode.setSliceViewerLayers(0)
</code></pre>
<p>When I set the segmentationNode.setSliceViewerLayers(0), the 3D model created using the above mentioned script also gets hidden. How can I decouple the 3D model and the segmentations. I would just like to visualize the MRI volumes and the 3D models.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5b508bc2ed08655fd32002fd415eb0f6f13bfe4.jpeg" data-download-href="/uploads/short-url/pVshJg6eZtngHYgsvvL3vOmLYBm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b508bc2ed08655fd32002fd415eb0f6f13bfe4_2_690x382.jpeg" alt="image" data-base62-sha1="pVshJg6eZtngHYgsvvL3vOmLYBm" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b508bc2ed08655fd32002fd415eb0f6f13bfe4_2_690x382.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b508bc2ed08655fd32002fd415eb0f6f13bfe4_2_1035x573.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5b508bc2ed08655fd32002fd415eb0f6f13bfe4_2_1380x764.jpeg 2x" data-dominant-color="45464F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1393×772 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c52f62c80d092726b1398c47c5cfa55b222bc53a.jpeg" data-download-href="/uploads/short-url/s8nAinqqKnJFQe9HsZqo0KVnQGC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c52f62c80d092726b1398c47c5cfa55b222bc53a_2_690x389.jpeg" alt="image" data-base62-sha1="s8nAinqqKnJFQe9HsZqo0KVnQGC" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c52f62c80d092726b1398c47c5cfa55b222bc53a_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c52f62c80d092726b1398c47c5cfa55b222bc53a_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c52f62c80d092726b1398c47c5cfa55b222bc53a.jpeg 2x" data-dominant-color="43434F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1370×773 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-09-21 17:51 UTC)

<p>You can control visibility of segmentations by adjusting properties in the <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html">segmentation display node</a>. You can hide the segmentation in slice views like this:</p>
<pre><code class="lang-python">segmentationNode.GetDisplayNode().SetVisibility2D(False)
</code></pre>

---
