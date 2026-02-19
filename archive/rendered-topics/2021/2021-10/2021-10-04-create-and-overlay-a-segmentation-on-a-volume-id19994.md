---
topic_id: 19994
title: "Create And Overlay A Segmentation On A Volume"
date: 2021-10-04
url: https://discourse.slicer.org/t/19994
---

# Create and overlay a segmentation on a volume

**Topic ID**: 19994
**Date**: 2021-10-04
**URL**: https://discourse.slicer.org/t/create-and-overlay-a-segmentation-on-a-volume/19994

---

## Post #1 by @S_Arbabi (2021-10-04 17:49 UTC)

<p>I want to apply a threshold value on an image and overlay this threshold result as a segmentation (or labelmap) on the image.<br>
Based on a sample in script repository I tried to do it this way:</p>
<pre><code class="lang-auto">    threshold = 500
    
    #getting volume node and its image as array
    volumeNode = slicer.util.getNode("volume")
    volumeNode_array = slicer.util.arrayFromVolume(volumeNode)

    #creating new segmentation node and segment and set its reference image geometry to volume node
    segmentationNode = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(segmentationNode)
    segmentationNode.CreateDefaultDisplayNodes()
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
    segmentationNode.GetSegmentation().AddEmptySegment()
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('Segment_1')

    #get the array of segmentation, update its values and refresh the segmentatin
    segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
    segmentArray[:] = 0
    segmentArray[volumeNode_array &gt; threshold] = 1
    slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId, volumeNode)
</code></pre>
<p>this returns this error:</p>
<pre><code class="lang-auto">    segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)
TypeError: arrayFromSegmentBinaryLabelmap() takes 2 positional arguments but 3 were given
</code></pre>
<p>I see in the documentation though this function can take 3 arguments, the last one is reference volume:</p>
<pre><code class="lang-auto">referenceVolumeNode: a volume node that determines geometry (origin, spacing, axis directions, extents) of the array.
</code></pre>
<p>It is also stated that:</p>
<pre><code class="lang-auto">If not specified then the volume that was used for setting the segmentation's geometry is used as for the reference volume.
</code></pre>
<p>since I’m setting the reference image geometry upper in code, if I don’t pass the referenceVolumeNode I will get this error:</p>
<pre><code class="lang-auto">    segmentArray[volumeNode_array &gt; threshold] = 1
IndexError: boolean index did not match indexed array along dimension 0; dimension is 0 but corresponding boolean dimension is 135
</code></pre>
<p>I appreciate any ideas in this regard.</p>

---

## Post #2 by @lassoan (2021-10-04 18:19 UTC)

<p><em>Latest</em> version of the Slicer documentation on ReadTheDocs (this is the one that is shown by default when you don’t specify a version) is for latest Slicer Preview Release. The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">code snippet</a> works well for the latest Slicer Preview Release.</p>
<p>For older versions of the script repository, you would need to choose the corresponding version in the lower-left corner in ReadTheDocs, but since we migrated the script repository in Slicer-4.13, there are no earlier archived versions.</p>
<p>Therefore, you either need to update your Slicer or modify the code snippet to match the API of the Slicer version you are using. I would recommend updating your Slicer, as the new Slicer Stable Release will be out soon, which will have the same API as the latest Slicer Preview Release.</p>

---
