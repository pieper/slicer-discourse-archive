---
topic_id: 31379
title: "Why Is Segmentstatistics Slower In Python Console"
date: 2023-08-26
url: https://discourse.slicer.org/t/31379
---

# Why is SegmentStatistics slower in Python console?

**Topic ID**: 31379
**Date**: 2023-08-26
**URL**: https://discourse.slicer.org/t/why-is-segmentstatistics-slower-in-python-console/31379

---

## Post #1 by @chir.set (2023-08-26 12:57 UTC)

<p>SegmentStatistics computation runs at least at half speed in the Python console than in the module’s widget.</p>
<p>With a single segment drawn with the Paint tool at 3% and a sphere brush, the execution time is 0.40 secs in the module’s widget and 1.08 secs in the Python console with the following call :</p>
<pre><code class="lang-auto">import SegmentStatistics
segmentation = slicer.util.getNode("Segmentation")
volume = slicer.util.getNode("CTA-cardio")
logic = SegmentStatistics.SegmentStatisticsLogic()
logic.getParameterNode().SetParameter("Segmentation", segmentation.GetID())
logic.getParameterNode().SetParameter("ScalarVolume", volume.GetID())
logic.computeStatistics()
</code></pre>
<p>The difference increases more than twofold with multiple segments.</p>
<p>It’s not a fundamental issue requiring a fix in the module itself, I’m more interested to know if it can be remedied by the caller in his code.</p>
<p>Thank you for any suggestion.</p>

---

## Post #2 by @chir.set (2024-07-01 08:12 UTC)

<p>Fixed in this <a href="https://github.com/Slicer/Slicer/commit/453c5befb470bc20ac69dfa06a5f404a85b9f092" rel="noopener nofollow ugc">commit</a>, and it’s really fast, thanks.</p>

---
