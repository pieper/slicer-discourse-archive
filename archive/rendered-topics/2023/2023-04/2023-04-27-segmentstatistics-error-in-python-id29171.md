# SegmentStatistics error in Python

**Topic ID**: 29171
**Date**: 2023-04-27
**URL**: https://discourse.slicer.org/t/segmentstatistics-error-in-python/29171

---

## Post #1 by @Markb (2023-04-27 11:59 UTC)

<p>Hi. I have a bunch of segments in an RTStruct file, and a bunch of images that I want to get some statistics from. Doing this manually is a bit of a timehog, so I looked into writing a quick python script and running it using the python interactor. It’s based largely on things I found on this forum and Google, so could be very wrong, but at the moment it seems to pull through the correct segments and scalars, and generates a data table, just doesn’t populate it.</p>
<p>At the moment, I get an error that</p>
<pre><code class="lang-auto">if not segmentationNode.GetParentTransformNode() is None:
AttributeError: 'NoneType' object has no attribute 'GetParentTransformNode'
</code></pre>
<p>My code is below:</p>
<pre><code class="lang-auto">print("Starting scalar volume processing loop...")
import SegmentStatistics

rtstruct_node = slicer.util.getFirstNodeByName("RTSTRUCT") #get the RTStruct Node
scalar_volume_nodes = slicer.util.getNodesByClass("vtkMRMLScalarVolumeNode") #retrieve all scalar nodes

for scalar_volume_node in scalar_volume_nodes:
    if 'Dose' in scalar_volume_node.GetName(): #check if dose is in the name, as don't want to analysis the CT etc.
        scalar_volume_name = scalar_volume_node.GetName() #Get the unique name for the scalar volume
        print("Quantifying node " + scalar_volume_name)
        statistics_table_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", scalar_volume_name + "_stat") #Create a new table node to hold the statistics

        for segment_index in range(rtstruct_node.GetSegmentation().GetNumberOfSegments()): #Loop through the segments and compute statistics for each segment
            segment_name = rtstruct_node.GetSegmentation().GetNthSegment(segment_index).GetName()
            segment_id = rtstruct_node.GetSegmentation().GetNthSegmentID(segment_index)
            print("Measuring segment " + segment_name + " with ID: " + segment_id)
            
            segmentStat = SegmentStatistics.SegmentStatisticsLogic()
            segmentStat.getParameterNode().SetParameter("Segmentation", segment_id)
            segmentStat.getParameterNode().SetParameter("ScalarVolume", scalar_volume_node.GetID())
            #segmentStat.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled","False")
            #segmentStat.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.voxel_count.enabled","False")
            segmentStat.computeStatistics()
            segmentStat.exportToTable(statistics_table_node)
            segmentStat.showTable(statistics_table_node)
</code></pre>
<p>Any help would be greatly appreciated! There aren’t many online resources (that I’ve found) and it is quite the learning curve.</p>

---

## Post #2 by @pearsonm (2023-04-27 22:24 UTC)

<p>Can you show the code where segmentationNode is defined?<br>
You will get this error if segmentationNode is equal to None and therefore has no attributes.</p>

---

## Post #3 by @Markb (2023-04-28 07:58 UTC)

<p>Ah, that is the entirety of the code I have, and that might be the issue. The segments are in the rtstruct file, so I thought slicer.util.getFirstNodeByName(“RTSTRUCT”) would retrieve this as the segmentation. As the print statements provided the right information back to me, I didn’t question this.</p>
<p>Do I need to change the first line in rtstruct_node to something like<br>
<code>restruct_node = slicer.util.getNodesByClass("vtkMRMLSegmentationNode")</code></p>
<p>I’m away from my computer at the moment to try this, but will give it a go later today.</p>
<p>Thank you</p>

---
