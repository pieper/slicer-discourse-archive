---
topic_id: 30909
title: "Addsegmentfromclosedsurfacerepresentation Performance"
date: 2023-08-01
url: https://discourse.slicer.org/t/30909
---

# AddSegmentFromClosedSurfaceRepresentation performance

**Topic ID**: 30909
**Date**: 2023-08-01
**URL**: https://discourse.slicer.org/t/addsegmentfromclosedsurfacerepresentation-performance/30909

---

## Post #1 by @d0rnkernsky (2023-08-01 15:27 UTC)

<p>Hello,</p>
<p>I am working on a custom module where I need to add many (360) objects to an existing segmentation node. Although the code seems very simple it takes hours to finish. I am not sure what causes the slowdown. Maybe there is a way to add all objects in a batch without calling AddSegmentFromClosedSurfaceRepresentation for each object. I will greatly appreciate any help.</p>
<p><strong>My code:</strong></p>
<pre><code class="lang-auto">segmentationNode = slicer.mrmlScene.GetFirstNodeByName("My segmentation")
for wedge in wedges:
      wedgeID = segmentationNode.AddSegmentFromClosedSurfaceRepresentation(wedge["wedgePD"], wedge["seg_name"], wedge["seg_colour"])
</code></pre>
<p>The time to execute AddSegmentFromClosedSurfaceRepresentation increases with the number of wedges added. Below is the time to execution time for first 30 steps<br>
1st call to AddSegmentFromClosedSurfaceRepresentation finished in 0.009<br>
2nd call to AddSegmentFromClosedSurfaceRepresentation finished in 0.188<br>
3rd call to AddSegmentFromClosedSurfaceRepresentation finished in 0.248<br>
…<br>
10th call to AddSegmentFromClosedSurfaceRepresentation finished in 0.448<br>
…<br>
30th call to AddSegmentFromClosedSurfaceRepresentation finished in 1.101</p>

---

## Post #2 by @lassoan (2023-08-02 04:30 UTC)

<p>You probably have multiple representations in your segmentation. Each time you add a new segment, all the representations might need to be recomputed. You can make adding a segment take 0 seconds by setting the source (master) representation to “closed surface” and remove the “binary labelmap” representation.</p>

---

## Post #3 by @d0rnkernsky (2023-08-21 20:18 UTC)

<p>Setting the master representation as closed surface helped, but it didn’t make it instant. Right now it takes around 0.5-0.8 sec. to add one surface. I have a follow up question. How do I check how many representations I have? When I open the Segmentation module and select the active segmentation I only see one segmentation.</p>

---

## Post #4 by @lassoan (2023-08-25 13:11 UTC)

<p>May be able to speed up the import if you do enclose all the import steps between a <code>StartModify</code> and an <code>EndModify</code> call.</p>
<p>If you only have one representation listed then you have only that representation. You can get the list of representation by calling methods od the vtkSegmentation object that is stored in the segmentation node.</p>

---
