# More efficient alternative to while/for loop for periodic action?

**Topic ID**: 41031
**Date**: 2025-01-10
**URL**: https://discourse.slicer.org/t/more-efficient-alternative-to-while-for-loop-for-periodic-action/41031

---

## Post #1 by @achiravu (2025-01-10 19:07 UTC)

<p>Hello!</p>
<p>I have a script (copied below) that records the mean and standard deviation of intensity values in a particular visible segment. I want to use this to periodically check the intensity values in the segmented region of a 2D ultrasound image, which is streamed live through the PLUS server using OpenIGTLink.</p>
<p>Currently, the script I have does the task, but each iteration of the script takes &gt;150ms to run while the PLUS server is running. Because of this, the refresh rate of the GUI and the ultrasound image drops down to 5-6 times per second. This is a much slower frame rate than I want. Is there a more efficient way of monitoring intensity values in a segment of a live ultrasound image?</p>
<p>Thanks!</p>
<pre><code class="lang-auto"># measuring average voxel intensity and standard deviation

import time
import numpy
# inputs
volumeNode = getNode('Image_Image')
segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")

# get voxels of visible segments as numpy arrays
visibleSegmentIds = vtk.vtkStringArray()
segmentationNode.GetDisplayNode().GetVisibleSegmentIDs(visibleSegmentIds)

#timestamp
import datetime
ct = datetime.datetime.now()
print('current time:', ct)

#while live image is displayed, collect mean and sd
meanArray = [];
sdArray = [];

for i in range(100): #for loop for testing purposes
    for segmentIdIndex in range(visibleSegmentIds.GetNumberOfValues()):
        segmentId = visibleSegmentIds.GetValue(segmentIdIndex)
        segmentName = segmentationNode.GetSegmentation().GetSegment(segmentId).GetName()
        if 'Target' in segmentName: #workshop this
            segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
            volumeArray = slicer.util.arrayFromVolume(volumeNode)
            volumeVoxelsInSegmentArray = volumeArray[segmentArray &gt; 0]
            contourMean = volumeVoxelsInSegmentArray.mean()
            contourSD = volumeVoxelsInSegmentArray.std()
            meanArray.append(contourMean)
            sdArray.append(contourSD)

            if i &gt; 0 and (meanArray[i] &gt; meanArray[i-1]+sdArray[i-1] or meanArray[i] &lt; meanArray[i-1]-sdArray[i-1]):
                print('Values in contour have changed and subject may have moved!')

    slicer.app.processEvents()   
</code></pre>

---
