---
topic_id: 33667
title: "Select Segment Ids In A Segmentation With Multiple Segments"
date: 2024-01-08
url: https://discourse.slicer.org/t/33667
---

# Select segment IDs in a Segmentation with multiple segments

**Topic ID**: 33667
**Date**: 2024-01-08
**URL**: https://discourse.slicer.org/t/select-segment-ids-in-a-segmentation-with-multiple-segments/33667

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-01-08 11:01 UTC)

<p>Hi to everyone. Today I’m trying to solve a very concerning problem. The situation is the next one:</p>
<pre><code class="lang-auto">suffix = '_manualSegmentation'
segmentationName = f"{patientID}{suffix}"
segmentName = f"{patientID}_coronaryTree{suffix}"
namesCorrect = False
  
while(not namesCorrect):
    try:
        segmentationNode = slicer.util.getNode(segmentationName)
        segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
        
        if (not segmentId == ''):
            namesCorrect = True
            
    except:
        input("Check that segmentation name and segment name are: " + 
              segmentationName + " and " + segmentName + ",respectively."
              + "And press key to continue...")
        namesCorrect = False
</code></pre>
<p>This code works properly to be sure that the user puts fine the segmentation and segment names. But only when I have one segment. If I have more than one, the code crashes and Slicer stops working… Am I doing something wrong ?</p>
<p>Thanks to everyone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @Sunderlandkyl (2024-01-08 16:04 UTC)

<p>I think the code is just getting caught in an infinite while loop where namesCorrect is never True.</p>
<p>I’ve tested the code on a segmentation with multiple segments. If the segment name is found then it works fine, but if “segmentName” is not the name of a segment, there will be an infinite loop.</p>

---
