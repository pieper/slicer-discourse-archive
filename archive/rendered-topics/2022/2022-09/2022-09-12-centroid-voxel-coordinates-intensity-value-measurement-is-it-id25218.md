---
topic_id: 25218
title: "Centroid Voxel Coordinates Intensity Value Measurement Is It"
date: 2022-09-12
url: https://discourse.slicer.org/t/25218
---

# Centroid Voxel/Coordinates Intensity Value Measurement - Is it possible?

**Topic ID**: 25218
**Date**: 2022-09-12
**URL**: https://discourse.slicer.org/t/centroid-voxel-coordinates-intensity-value-measurement-is-it-possible/25218

---

## Post #1 by @dokay1 (2022-09-12 13:29 UTC)

<p>I bumped into an issue I can’t seem to find a solution for. I have a large number (&gt;400) of segments for each I want to measure the intensity (essentially the anatomical location off an atlas) from the centroid voxel. I used Segment Statistics to export the Centroid coordinates and I can import those into a fiducial list.</p>
<p>I’m wondering what would be the best way to get the intensity data from the centroids?<br>
A) I could import the coordinates into a fiducial list, but is there a way to get values from the fiducial’s coordinates?<br>
B) Can I shrink the segments to a single central voxel? (this would be the simplest)<br>
C) DO i have to generate 400+ transforms with the coordinates and use a single central voxel to get the data?</p>
<p>Please help!</p>

---

## Post #2 by @dokay1 (2022-09-28 14:43 UTC)

<p>Solution:</p>
<ol>
<li>I used LabelmapSegmentStatistics to pull the centroid for each segment in the Segmentation</li>
<li>Then I used the centroid coordinates to generate new spherical segments with a 1mm diameter (or radius?)</li>
<li>These can be used with Segment statistics to query core lesion locations based on anatomical atlases</li>
</ol>
<pre><code class="lang-auto">#  Pull Centroids and generate 1mm spheric lesions in centroid for anatomical assessment 
# Adjust name for "Segmentation" and "Volume" as needed

import numpy as np
import SegmentStatistics
segmentationNode = slicer.util.getNode("Segmentation")
volume_node = slicer.util.getNode("Volume")
segmentation = segmentationNode.GetSegmentation()
segnum = segmentation.GetNumberOfSegments()
for i in range(segnum):
    segment = segmentation.GetNthSegment(i) 
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegment(segment)
    segmentName = segment.GetName()
    segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
    segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
    segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.centroid_ras.enabled", str(True))
    segStatLogic.computeStatistics()
    stats = segStatLogic.getStatistics()
    print(segmentName)
    centroid_ras = stats[segmentId,"LabelmapSegmentStatisticsPlugin.centroid_ras"]
    print(centroid_ras)
    tumorCentroid = vtk.vtkSphereSource()
    tumorCentroid.SetCenter(centroid_ras)
    tumorCentroid.SetRadius(1)
    tumorCentroid.Update()
    CentroidSegmentName = segmentName + "-centroid"
    segmentId = segmentationNode.AddSegmentFromClosedSurfaceRepresentation(tumorCentroid.GetOutput(), CentroidSegmentName, [1.0,0.0,0.0])
</code></pre>

---
