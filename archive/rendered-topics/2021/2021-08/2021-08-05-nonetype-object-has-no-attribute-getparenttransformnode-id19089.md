---
topic_id: 19089
title: "Nonetype Object Has No Attribute Getparenttransformnode"
date: 2021-08-05
url: https://discourse.slicer.org/t/19089
---

# 'NoneType' Object has no attribute 'GetParentTransformNode'?

**Topic ID**: 19089
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/nonetype-object-has-no-attribute-getparenttransformnode/19089

---

## Post #1 by @J1234 (2021-08-05 19:35 UTC)

<p>I’m not really sure what happened… my code was working well yesterday and this morning I can’t figure out what changed.</p>
<p>My goal is to iterate through all the segmentation files in a directory and use the Segment Statistics module to get the segment volumes for each one. All my segmentation files are saved as “study_id_number_segmentations.seg.nrrd” and the corresponding volumes are saved as “study_id_number_MRI.nii”, where each study_id_number refers to a particular patient. So far I have:</p>
<h1><a name="p-64299-setup-imports-1" class="anchor" href="#p-64299-setup-imports-1" aria-label="Heading link"></a>Setup imports</h1>
<p>import os<br>
import glob<br>
from path lib import Path<br>
import SegmentStatistics</p>
<h1><a name="p-64299-load-a-specific-segmentation-and-corresponding-node-2" class="anchor" href="#p-64299-load-a-specific-segmentation-and-corresponding-node-2" aria-label="Heading link"></a>Load a specific segmentation and corresponding Node</h1>
<p>segmentation_file = “path/to/study_id_1_segmentations.seg.nrrd”<br>
segmentationNode = getNode(“study_id_1_segmentations”)</p>
<h1><a name="p-64299-compute-segment-statistics-for-that-segmentation-3" class="anchor" href="#p-64299-compute-segment-statistics-for-that-segmentation-3" aria-label="Heading link"></a>Compute segment statistics for that segmentation</h1>
<p>segStatLogic = SegmentStatistics.SegmentStatisticsLogic()<br>
segStatLogic.getParameterNode().SetParameter(“study_id_1_segmentations”, segmentationNode.GetID())<br>
segStatLogic.computeStatistics()<br>
stats = segStatLogic.getStatistics()</p>
<p>I’m (seemingly) able to load the volume and the node, but when I try to compute segment statistics I get the error: ‘NoneType’ object has no attribute ‘GetParentTransformNode’. Am I missing something here?</p>

---

## Post #2 by @Juicy (2021-08-05 22:38 UTC)

<p>Just a very quick observation: The line:</p>
<pre><code class="lang-auto">segStatLogic.getParameterNode().SetParameter(“study_id_1_segmentations”, segmentationNode.GetID())
</code></pre>
<p>Looks a bit wrong. I think it should be:</p>
<pre><code class="lang-auto">segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
</code></pre>
<p>Also if you want statistics like mean pixel values etc which come from the volume, you should also point segment statistics toward the correct volume:</p>
<pre><code class="lang-auto">segStatLogic.getParameterNode().SetParameter("ScalarVolume", volumeNode.GetID())
</code></pre>
<p>You would first need to load the volume though and assign it to the variable ‘volumeNode’</p>

---

## Post #3 by @J1234 (2021-08-06 04:05 UTC)

<p>That works, thanks for the correction!</p>

---
