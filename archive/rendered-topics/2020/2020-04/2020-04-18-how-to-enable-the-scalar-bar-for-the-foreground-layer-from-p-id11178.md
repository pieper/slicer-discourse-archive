---
topic_id: 11178
title: "How To Enable The Scalar Bar For The Foreground Layer From P"
date: 2020-04-18
url: https://discourse.slicer.org/t/11178
---

# How to enable the scalar bar for the foreground layer from Python terminal?

**Topic ID**: 11178
**Date**: 2020-04-18
**URL**: https://discourse.slicer.org/t/how-to-enable-the-scalar-bar-for-the-foreground-layer-from-python-terminal/11178

---

## Post #1 by @xlucox (2020-04-18 21:12 UTC)

<p>Hi everyone!!!</p>
<p>I’m trying to enable the scalar bar for the foreground layer from Python terminal.</p>
<p>Does anyone have idea how to set this?</p>

---

## Post #2 by @cpinter (2020-04-19 19:44 UTC)

<p>Here is an example:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py#L165-L167" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py#L165-L167" target="_blank">SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py#L165-L167</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="165" style="counter-reset: li-counter 164 ;">
<li>self.sliceAnnotations = DataProbeLib.SliceAnnotations(self.layoutWidget.layoutManager())
</li>
<li>self.sliceAnnotations.scalarBarEnabled = 0
</li>
<li>self.sliceAnnotations.updateSliceViewFromGUI()
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Please note that for you things will be a bit simpler because in this example a separate layout manager is used, and you won’t have to create one like this.</p>

---
