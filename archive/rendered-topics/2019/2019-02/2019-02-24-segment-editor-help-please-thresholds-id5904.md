---
topic_id: 5904
title: "Segment Editor Help Please Thresholds"
date: 2019-02-24
url: https://discourse.slicer.org/t/5904
---

# Segment Editor help please (thresholds)

**Topic ID**: 5904
**Date**: 2019-02-24
**URL**: https://discourse.slicer.org/t/segment-editor-help-please-thresholds/5904

---

## Post #1 by @Andrei_V (2019-02-24 13:49 UTC)

<p>Operating system: Windows 8.1<br>
Slicer version: 4.10.1<br>
Expected behavior: Hello all. I am trying to segment CT slices. On the same slice I need to highlight both muscle and fat, which have different thresholds.<br>
Actual behavior: It seems that the “Threshold Range” settings are linked. For example, if I “Add new empty segment” and change the threshold, it changes it for all segments. Likewise, if I “Create new segmentation” and then select the thresholds for each different segmentation, it is still linked (i.e. same threshold). I want to be able to define different thresholds for muscle and fat, and then switch between measuring them. Is this possible?</p>
<p>Thank you, and have a good day!</p>

---

## Post #2 by @cpinter (2019-02-24 17:11 UTC)

<p>You’re right, currently the threshold setting is global. However if you can use threshold to segment your multiple structures, then there is a good chance that the Grow from seeds can do it too. I strongly suggest trying it.</p>
<p>Please check out this video: <a href="https://www.youtube.com/watch?v=8Nbi1Co2rhY" rel="nofollow noopener">https://www.youtube.com/watch?v=8Nbi1Co2rhY</a></p>

---

## Post #3 by @lassoan (2019-02-24 20:16 UTC)

<p>If you just want approximate segmentation purely based on Hounsfield units, you can use this short Python script, which creates fat, muscle, bone segments using thresholding and then reports their volumes:</p>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37</a></h4>
<h5>SegmentByThresholding.py</h5>
<pre><code class="Python"># Download a sample data set (chest CT)
import SampleData
masterVolumeNode = SampleData.SampleDataLogic().downloadCTChest()

# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>You can find more segmentation scripting examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---
