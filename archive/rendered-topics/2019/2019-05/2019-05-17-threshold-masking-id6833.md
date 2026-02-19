---
topic_id: 6833
title: "Threshold Masking"
date: 2019-05-17
url: https://discourse.slicer.org/t/6833
---

# Threshold masking

**Topic ID**: 6833
**Date**: 2019-05-17
**URL**: https://discourse.slicer.org/t/threshold-masking/6833

---

## Post #1 by @prorai (2019-05-17 12:53 UTC)

<p>How can i apply threshold for masking in segmentation process, using python code?</p>

---

## Post #2 by @lassoan (2019-05-17 12:55 UTC)

<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">examples of using segment editor from Python scripts in the script repository</a>.</p>

---

## Post #3 by @prorai (2019-05-17 14:54 UTC)

<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b</a></h4>
<h5>SegmentGrowCutSimple.py</h5>
<pre><code class="Python"># Generate input data
################################################

import SampleData

# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation</code></pre>
This file has been truncated. <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I’m using this seed grow example but i want to use threshold masking with this ,<br>
i tried effect.self().onUseForPaint() and its not working</p>

---

## Post #4 by @prorai (2019-05-21 14:39 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , i tried seed grow with masking(applying threshold for paint) , and it works if i put the python code in python interactor in slicer .</p>
<p>same code i have added in my scriptable module and seed grow works normally but i’m not seeing masking is applied before seefGrow.</p>

---
