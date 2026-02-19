---
topic_id: 15438
title: "Select Segmentations In 3D View"
date: 2021-01-10
url: https://discourse.slicer.org/t/15438
---

# select segmentations in 3D view

**Topic ID**: 15438
**Date**: 2021-01-10
**URL**: https://discourse.slicer.org/t/select-segmentations-in-3d-view/15438

---

## Post #1 by @LuckyLuke (2021-01-10 15:38 UTC)

<p>Is there a way to quickly select segmentations and make them invisible in the 3D view.</p>
<p>Namely, problem I encounter is that my boss asks me to show him a certain structure and I have to often remove 1 or 2 other segmentations to see it clearly.</p>
<p>I end up hovering my mouse over the segmentation i want to remove while holding the shift.</p>
<p>Next I look at the red slices and then I hover in them as well.<br>
Then it shows me the name of the segment and segmentation.<br>
Then I have to go to search it with filter through data<br>
After that I have to click right click and disable 3D view.</p>
<p>As you can see, it takes quite a lot of steps to remove just 1 structure.</p>
<p>Is there some plugin or something that can help me easily remove them?</p>
<p>Thank you</p>

---

## Post #3 by @NoobForSlicer (2021-01-12 15:52 UTC)

<p>Wait… you can just select them in data module and just right click and uncheck visibility.</p>
<p>I am not sure I understand what you are asking for</p>

---

## Post #4 by @lassoan (2021-01-12 19:49 UTC)

<p>There is no such built-in feature yet, but you can put together a Python script that does what you need. For example, you can set the crosshair in any views using Shift+MouseMove then run the following script to hide the segments at that position:</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
segmentationDisplayNode = segmentationNode.GetDisplayNode()

sliceViewWidget = slicer.app.layoutManager().sliceWidget('Red')
displayableManager2D = sliceViewWidget.sliceView().displayableManagerByClassName('vtkMRMLSegmentationsDisplayableManager2D')
crosshairNode=slicer.util.getNode('Crosshair')
crosshairNode.GetCrosshairRAS()
crosshairPosition = crosshairNode.GetCrosshairRAS()
# Look around crosshair position in all directions for a segment
# (necessary because picked position is at the segmentation boundary so it may be just outside the segment)
for attempts in range(16):
    crosshairPositionAdjusted = [crosshairPosition[0]-0.5+1.0*(attempts%2), crosshairPosition[1]-0.5+1.0*((attempts/2)%2), crosshairPosition[2]-0.5+1.0*((attempts/4)%8)]
    segmentIDs = vtk.vtkStringArray()
    segmentValues = vtk.vtkDoubleArray()
    displayableManager2D.GetVisibleSegmentsForPosition(crosshairPositionAdjusted, segmentationDisplayNode, segmentIDs, segmentValues)
    if segmentIDs.GetNumberOfValues() == 0:
        continue
    for i in range(segmentIDs.GetNumberOfValues()):
        segmentID = segmentIDs.GetValue(i)
        segmentationDisplayNode.SetSegmentVisibility(segmentID, False)
    break
</code></pre>

---

## Post #5 by @LuckyLuke (2021-01-29 15:09 UTC)

<p>I am sorry but I tried however I don’t know how to run this script…<br>
Like how does one run a script in Slicer?</p>

---

## Post #6 by @lassoan (2021-01-29 15:10 UTC)

<p>You can open the Python console (Ctrl-3) and copy-paste the code there.</p>

---
