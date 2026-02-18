# How to find the volume of a segmentation node whose master representation is closed surface representation

**Topic ID**: 44738
**Date**: 2025-10-13
**URL**: https://discourse.slicer.org/t/how-to-find-the-volume-of-a-segmentation-node-whose-master-representation-is-closed-surface-representation/44738

---

## Post #1 by @Victor_Wayne (2025-10-13 05:33 UTC)

<p>Hello,</p>
<p>I want to find the volume of a segmentation node with closed surface representation. How can I do that using segment statistics module? I have found an example in script repository but I think it is only applicable for binary lablemap representation. Here is the code I found.</p>
<pre data-code-wrap="python"><code class="lang-python">segmentationNode = getNode("Segmentation")

# Compute segment statistics
import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.computeStatistics()
stats = segStatLogic.getStatistics()

# Display volume of each segment
for segmentId in stats["SegmentIDs"]:
  volume_cm3 = stats[segmentId,"LabelmapSegmentStatisticsPlugin.volume_cm3"]
  segmentName = segmentationNode.GetSegmentation().GetSegment(segmentId).GetName()
  print(f"{segmentName} volume = {volume_cm3} cm3")
</code></pre>
<p>Thanks for your help in advance.</p>

---

## Post #2 by @lassoan (2025-10-14 02:49 UTC)

<p>You can use metrics provided by <code>ClosedSurfaceSegmentStatisticsPlugin</code>.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/ad238246c73ef8323d87dcef047e2514f937ae0f/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/ClosedSurfaceSegmentStatisticsPlugin.py#L14">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/ad238246c73ef8323d87dcef047e2514f937ae0f/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/ClosedSurfaceSegmentStatisticsPlugin.py#L14" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/ad238246c73ef8323d87dcef047e2514f937ae0f/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/ClosedSurfaceSegmentStatisticsPlugin.py#L14" target="_blank" rel="noopener">Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/ClosedSurfaceSegmentStatisticsPlugin.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/ad238246c73ef8323d87dcef047e2514f937ae0f/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/ClosedSurfaceSegmentStatisticsPlugin.py#L14" rel="noopener"><code>ad238246c</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="4" style="counter-reset: li-counter 3 ;">
          <li>from SegmentStatisticsPlugins import SegmentStatisticsPluginBase</li>
          <li></li>
          <li></li>
          <li>class ClosedSurfaceSegmentStatisticsPlugin(SegmentStatisticsPluginBase):</li>
          <li>    """Statistical plugin for closed surfaces"""</li>
          <li></li>
          <li>    def __init__(self):</li>
          <li>        super().__init__()</li>
          <li>        self.name = "Closed Surface"</li>
          <li>        self.title = _("Closed Surface")</li>
          <li class="selected">        self.keys = ["surface_mm2", "volume_mm3", "volume_cm3"]</li>
          <li>        self.defaultKeys = self.keys  # calculate all measurements by default</li>
          <li>        # ... developer may add extra options to configure other parameters</li>
          <li></li>
          <li>    def computeStatistics(self, segmentID):</li>
          <li>        import vtkSegmentationCorePython as vtkSegmentationCore</li>
          <li></li>
          <li>        requestedKeys = self.getRequestedKeys()</li>
          <li></li>
          <li>        segmentationNode = slicer.mrmlScene.GetNodeByID(self.getParameterNode().GetParameter("Segmentation"))</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Victor_Wayne (2025-10-16 09:00 UTC)

<p>Thank you. This works.</p>

---
