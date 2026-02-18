# Is there a way to get the volume of just one segment within a segmentation?

**Topic ID**: 19093
**Date**: 2021-08-06
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-get-the-volume-of-just-one-segment-within-a-segmentation/19093

---

## Post #1 by @J1234 (2021-08-06 04:12 UTC)

<p>Apologies if this is fairly obvious, learning python has been a steep learning curve. I have a segmentation that includes two segments: blood and bone. Using the docs, I’ve been able to find code that automatically prints the volume of both:</p>
<p>import SegmentStatistics<br>
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()</p>
<h1><a name="p-64316-segstatlogicgetparameternodesetparameterscalarvolume-volumenodegetid-1" class="anchor" href="#p-64316-segstatlogicgetparameternodesetparameterscalarvolume-volumenodegetid-1" aria-label="Heading link"></a>segStatLogic.getParameterNode().SetParameter(“ScalarVolume”, volumeNode.GetID())</h1>
<p>segStatLogic.getParameterNode().SetParameter(“Segmentation”, segmentationNode.GetID())<br>
segStatLogic.computeStatistics()<br>
stats = segStatLogic.getStatistics()</p>
<p>for segmentId in stats[“SegmentIDs”]:<br>
volume_mm3 = stats[segmentId,“LabelmapSegmentStatisticsPlugin.volume_mm3”]<br>
segmentName = segmentationNode.GetSegmentation().GetSegment(segmentId).GetName()<br>
print(f"{segmentName} volume = {volume_mm3} mm3")</p>
<p>However, is there a way to return ONLY one of the segment volumes from a segmentation? For example:</p>
<p>stats[“SegmentIDs”][0] correponds to the blood segment, and stats[“SegmentIDs”][1] to the bone segment. Is it possible to alter the above code to get just the blood volume?</p>

---

## Post #2 by @lassoan (2021-08-07 01:59 UTC)

<p>You can enable the option that computes statistics for visible segments only, and can (temporarily) hide the segment that you want to exclude from the computation.</p>
<p>If this is not good enough then you can add an API to Segment Statistics module so that it can take an optional Segment ID list. The module is a simple Python scripted module, so you can change it very easily. If you implement this then submit a pull request so that we can merge it into Slicer core.</p>

---
