# Issue with version inconsistency

**Topic ID**: 16283
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/issue-with-version-inconsistency/16283

---

## Post #1 by @justomont (2021-03-01 11:52 UTC)

<p>Hello everybody!</p>
<p>I’m having a problem with my code when I run it in slicer v4.10.2, and it worked fine on v4.10.1.</p>
<p>This is the code, in which I select a segmentation (already in the scene) and convert it to a LabelmapVolumeNode. Then I take this Labelmap and obtain its voxel array.</p>
<pre><code>segmentationNode = getNode('Segmentation')

try : 
    segmentLabelmapNode = getNode('res_map')
except: 
    segmentLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()
    segmentLabelmapNode.SetName('res_map')

# segmentLabelmapNode = slicer.vtkMRMLLabelMapVolumeNode()
# segmentLabelmapNode.SetName('res_map')
slicer.mrmlScene.AddNode(segmentLabelmapNode)
segmentIDs = vtk.vtkStringArray()
segmentationNode.GetSegmentation().GetSegmentIDs(segmentIDs)
referenceNode = segmentationNode.GetNodeReference(slicer.vtkMRMLSegmentationNode.GetReferenceImageGeometryReferenceRole())
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, segmentIDs, segmentLabelmapNode, referenceNode)

voxelArray = slicer.util.arrayFromVolume(segmentLabelmapNode)
</code></pre>
<p>As said, it perfectly works with v4.10.1, but in version 4.10.2 this error pops-up:</p>
<pre><code>File "C:\Program Files\Slicer 4.10.2\bin\Python\slicer\util.py", line 798, in arrayFromVolume

 nshape = tuple(reversed(volumeNode.GetImageData().GetDimensions()))

AttributeError: 'NoneType' object has no attribute 'GetDimensions'
</code></pre>
<p>Referring to the line where the voxelArray is created. Is there any difference between versions that I’m not aware of? The API documentation I used as a reference was this: <a href="https://apidocs.slicer.org/v4.10/index.html" rel="noopener nofollow ugc">Slicer API v4.10</a>.</p>
<p>Thanks in advance! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"></p>

---

## Post #2 by @lassoan (2021-03-01 14:18 UTC)

<p>I would recommend to update to current Slicer version and let us know if you have still have questions.</p>
<p>Slicer-4.10 was released several years ago. While sometimes some people volunteer to help out people who get stuck on older Slicer versions, in general we all work with and provide support for current stable or preview releases. <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners">Slicer commercial partners</a> may be able to help with any Slicer version, but of course you need to pay for their services.</p>

---
