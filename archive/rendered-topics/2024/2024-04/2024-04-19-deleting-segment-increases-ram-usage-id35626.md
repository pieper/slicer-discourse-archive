---
topic_id: 35626
title: "Deleting Segment Increases Ram Usage"
date: 2024-04-19
url: https://discourse.slicer.org/t/35626
---

# Deleting segment increases RAM usage

**Topic ID**: 35626
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/deleting-segment-increases-ram-usage/35626

---

## Post #1 by @Kostr (2024-04-19 20:31 UTC)

<p>Hello,</p>
<p>For my undergraduate project, I am developing a Slicer extension that opens a volume and a segmentation containing numerous segments.</p>
<p>Since some segments within the segmentation are incorrect, my extension should enable users to remove them individually. This can be done by hovering over the segment with the mouse, pressing a button, and deleting the segment.</p>
<p>So far I implemented a working function that looks like this:</p>
<details>
<summary>
Code</summary>
<pre data-code-wrap="python"><code class="lang-python">def eraseSegment(self):
    def getSegmentNames(segNode,pntListNode):
      ras = [0, 0, 0]
      sliceViewLabel = "Red"  # any slice view where segmentation node is visible works
      sliceViewWidget = slicer.app.layoutManager().sliceWidget(sliceViewLabel)
      segmentationsDisplayableManager = sliceViewWidget.sliceView().displayableManagerByClassName("vtkMRMLSegmentationsDisplayableManager2D")
      pntListNode.GetNthControlPointPositionWorld(0, ras)
      segmentIds = vtk.vtkStringArray()
      segmentationsDisplayableManager.GetVisibleSegmentsForPosition(ras, segNode.GetDisplayNode(), segmentIds)
      for idIndex in range(segmentIds.GetNumberOfValues()):
        segment = segNode.GetSegmentation().GetSegment(segmentIds.GetValue(idIndex))
        return segment.GetName()

    crosshairNode = slicer.util.getNode("Crosshair")
    pos = [0, 0, 0]
    crosshairNode.GetCursorPositionRAS(pos)
    slicer.modules.markups.logic().AddControlPoint(pos[0], pos[1], pos[2])
    pointListNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsFiducialNode")
    volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLVolumeNode")
    segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
    try:
pointListNode.AddObserver(slicer.vtkMRMLMarkupsPlaneNode.PointModifiedEvent, getSegmentNames)
      segmentId = getSegmentNames(segmentationNode,pointListNode)
      segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
      segmentArray[:] = 0  
      slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId, volumeNode) # Every time that this is called and erase a segment, the memory used on the RAM increases
    except:
      segNode = None
      print("No segmentation nodes found") 
</code></pre>
</details>
<p>In summary, when the user calls the function, the mouse position is determined and used to retrieve the segment ID at that location. The segment is then deleted by calling:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
segmentArray[:] = 0  
slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId, volumeNode) 
</code></pre>
<p>However, each time that this line is called:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId, volumeNode) 
</code></pre>
<p>the memory used on the RAM increases a lot (almost by a fourth); which is unelegant and unpractical when a lots of segments need to be removed.</p>
<p>I feel that I am missing something, what is the cause for this and what could be an alternative way to delete a specific segment using its ID?</p>
<p>Cheers,<br>
Ludo</p>

---

## Post #2 by @Kostr (2024-04-20 14:37 UTC)

<p>I found a solution that I share, maybe useful to somebody else.</p>
<p>Rather than deleting the segment everytime, I hide the incorect segment and then export only the visible segment of the segmentation.</p>
<p>Maybe my RAM increase was due to the fact that the function:</p>
<pre data-code-wrap="python"><code class="lang-python">updateSegmentBinaryLabelmapFromArray()
</code></pre>
<p>deep-copy the voxel (see the warning <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py" rel="noopener nofollow ugc">here</a>).</p>

---

## Post #3 by @rfenioux (2024-04-22 12:00 UTC)

<p>To delete a segment you can use :<br>
<code>segmentationNode.GetSegmentation().RemoveSegment(segmentID)</code></p>

---
