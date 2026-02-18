# Retrieving SegmentationStatistics from Large Datasets Using 3D Slicer API

**Topic ID**: 37924
**Date**: 2024-08-17
**URL**: https://discourse.slicer.org/t/retrieving-segmentationstatistics-from-large-datasets-using-3d-slicer-api/37924

---

## Post #1 by @JoshOnichino (2024-08-17 06:05 UTC)

<p>Hello! I a healthcare researcher working on medical image segmentation. I am hoping to automate the retrieval of SegmentationStatistics tables using 3D Slicer’s Python API. However, when I was developing my program, I ran into an issue with the code below.</p>
<pre><code>volume_path = os.path.join(input_directory, filename, f'{filename}.nrrd')
segmentation_path = os.path.join(input_directory, filename, f'{filename}_corrected.seg.nrrd')

volume_node = slicer.util.loadVolume(volume_path)
segmentation_node = slicer.util.loadSegmentation(segmentation_path)

segmentStatisticsLogic = SegmentStatistics.SegmentStatisticsLogic() 
segmentStatisticsLogic.getParameterNode().SetNodeReferenceID("Segmentation", segmentation_node.GetID())
segmentStatisticsLogic.getParameterNode().SetNodeReferenceID("ScalarVolume", volume_node.GetID())

segmentStatisticsLogic.computeStatistics()
</code></pre>
<p>When I run the above, the final line of code throws an Attribute Error<br>
(AttributeError: ‘NoneType’ object has no attribute ‘GetParentTransformNode’). I looked into the API source code to try to find the root of the error and found that the error comes from the beginning of the computeStatistics method.</p>
<pre><code>def computeStatistics(self):
    """Compute statistical measures for all (visible) segments"""
    self.reset()

    segmentationNode = slicer.mrmlScene.GetNodeByID(self.getParameterNode().GetParameter("Segmentation"))
    transformedSegmentationNode = None
    try:
        if not segmentationNode.GetParentTransformNode() is None:
            ...
</code></pre>
<p>It seems that the segmentationNode is None, but I am not sure why. Is there an error with the way that I loaded the files? Or is there something else I am not considering?</p>
<p>I am new to 3D Slicer (and segmentation, at large) so any insight into this would be a huge help! Thank you very much in advance for your time and consideration and take care.</p>

---

## Post #2 by @chir.set (2024-08-17 08:14 UTC)

<aside class="quote no-group" data-username="JoshOnichino" data-post="1" data-topic="37924">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joshonichino/48/77651_2.png" class="avatar"> JoshOnichino:</div>
<blockquote>
<p><code>self.getParameterNode().GetParameter("Segmentation")</code></p>
</blockquote>
</aside>
<p>It seems that the parameter node of your class does not have a parameter named “Segmentation”. You may be confusing with the parameter node of segmentStatisticsLogic.</p>

---

## Post #3 by @JoshOnichino (2024-08-17 15:23 UTC)

<p>Thank you very much for your response! I took a dive into the source code (<a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L355" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/Scripted/SegmentStatistics/SegmentStatistics.py at main · Slicer/Slicer · GitHub</a>) and found out that I was indeed confusing the logic.</p>
<p>Essentially, the error came from a mistake in the way the parameters belonging to the node were set.</p>
<p>Incorrect Code:</p>
<pre><code class="lang-auto">segmentStatisticsLogic.getParameterNode().SetNodeReferenceID("Segmentation", segmentation_node.GetID())
segmentStatisticsLogic.getParameterNode().SetNodeReferenceID("ScalarVolume", volume_node.GetID())
</code></pre>
<p>Correct Code:</p>
<pre><code class="lang-auto">segmentStatisticsLogic.getParameterNode().SetParameter("Segmentation", segmentation_node.GetID())            
segmentStatisticsLogic.getParameterNode().SetParameter("ScalarVolume", volume_node.GetID())
</code></pre>
<p>So, SetParameter is the correct method to use since I could not find SetNodeReferenceID as a method for SegmentStatisticsLogic in the source code linked above.</p>
<p>Thanks again and take care!</p>

---
