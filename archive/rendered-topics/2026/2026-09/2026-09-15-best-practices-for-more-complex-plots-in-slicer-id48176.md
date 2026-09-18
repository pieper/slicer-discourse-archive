---
topic_id: 48176
title: "Best practices for more complex plots in Slicer?"
date: 2026-09-15
url: https://discourse.slicer.org/t/48176
last_bumped: 2026-09-17T17:21:22.713Z
---

# Best practices for more complex plots in Slicer?

**Topic ID**: 48176
**Date**: 2026-09-15
**URL**: https://discourse.slicer.org/t/best-practices-for-more-complex-plots-in-slicer/48176

---

## Post #1 by @mikebind (2026-09-15 22:12 UTC)

<p>The slicer.util.plot() infrastructure is pretty limited. It’s OK for basic viewing of data that is already in MRML tables, but clunky for other data and incapable of nicer data visualizations.  It would be really nice to be able to use or display more complex plots in Slicer or at least from Slicer.  However, whenever I try to find nice solutions (using matplotlib, seaborn, etc.) I run into problems.  The default backend in matplotlib crashes Slicer.  wxPython is heavy but does provide a functional (but poorly styled) interactive plot window… until you try to close the plot, which hangs and crashes Slicer. The best option I found in the forum is this suggestion using pyqtgraph <a href="https://discourse.slicer.org/t/pythonqt-properties-shadowing-methods/16992/15" class="inline-onebox">PythonQt properties shadowing methods - #15 by fbordignon</a> , but it appears like it might require a manual patch to PythonQt, and PySide2, which appears to no longer be compatible with Slicer’s python version (it requires &lt;3.10), so is not really an option any more in recent Slicer versions.  It seems likely that some options will become available when Slicer fully shifts to Qt6 (it seems like this hasn’t happened in 5.12, but I’m not sure I’m understanding the release notes).  In the meantime, what do people use?  It sounds possible to save static plots to image files and then stretch those across a qt widget.  Is that the best current option for more advanced plots in Slicer?</p>

---

## Post #2 by @pieper (2026-09-16 22:54 UTC)

<p>A couple ideas:</p>
<ul>
<li>
<p>For the reasons you pointed out, trying to force some of these python plotting packages into Slicer can lead to dependency clashes and random crashes.  Another option is to write out the data and plot independently in a subshell with a different python interpreter (being careful with the paths in the environment).  You can use the web server (and the exec endpoint) to get any data you need out of Slicer and make any changes you want to slicer in response to interactions with the plot.</p>
</li>
<li>
<p>But my personal preference is to use <a href="https://echarts.apache.org/en/index.html">Apache ECharts</a> with the qSlicerWebWidget.  Here’s a project page that describes it: <a href="https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/MultidimensionalExplorerGeneralization/">https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/MultidimensionalExplorerGeneralization/</a>.  You have to feel comfortable using python and javascript together (or comfortable asking Claude to do it).</p>
</li>
</ul>
<p>Also, regarding Qt6, yes, it should be working everywhere now, we just haven’t made releases for it yet.</p>

---

## Post #3 by @mikebind (2026-09-17 16:34 UTC)

<p>Thanks for these suggestions, <a class="mention" href="/u/pieper">@pieper</a> .  The examples on the project page are very cool, and Apache ECharts does look quite capable.  Is there any example code available showing how to integrate this with Slicer?  I see the gist linked from the project page demonstrating the interactive html page, but would be curious to see an example of linking one of these plots to Slicer (like the MultiMapper module example shown in one of the linked videos), if it is possible to share that.</p>
<p>Separately, while I really enjoy being able to explore data like this in thoughtfully constructed interactive ways, it also takes an investment of time to create and develop them.  For cases where what I am looking for is closer to just displaying a static plot (but where I’d love to be able to zoom and pan), the subshell approach seems simpler and easier.  You caution that it’s necessary to be careful with the environment paths, is there an example that I could follow to try this approach as well?</p>
<p>As always, the help is much appreciated, thanks!</p>

---

## Post #4 by @pieper (2026-09-17 17:00 UTC)

<p>This code is a bit older, but it is the implementation that shows how to tie the js-based plotting to slicer features (here an older package the was pre-ECharts and an older version of Slicer, but the method is portable).</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/pieper/SlicerMultiMapper">
  <header class="source">

      <a href="https://github.com/pieper/SlicerMultiMapper" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/6aafb27e95770e3012482e61709d30b9/pieper/SlicerMultiMapper" class="thumbnail">

  <h3><a href="https://github.com/pieper/SlicerMultiMapper" target="_blank" rel="noopener">GitHub - pieper/SlicerMultiMapper: Tools for creating parametric maps from...</a></h3>

    <p><span class="github-repo-description">Tools for creating parametric maps from multidimensional MRI</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The code goes both ways - you can select image intensity ranges from the plot and see the corresponding segmentation, or you can use the segmentation statistics to generate the plot.</p>
<p>I do agree that the ECharts option is “weird” since it mixes different programming worlds and may not be everyone’s favorite.  FWIW, modern coding agents don’t have much problem with mixing and matching feature from different languages, so I wouldn’t try writing from scratch as just asking the agent to adapt the code to your use case.</p>
<p>If you want to go with the two-process model and use standard python stuff I don’t have a specific plotting example, but here’s an example of how to launch a python based program (note the <code>useShartupEnvironment</code>option) and communicate using RPyC, which is actually quite powerful and convenient, but it bogs down on large data, so we use shared memory for numpy arrays.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30">
  <header class="source">

      <a href="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30" target="_blank" rel="noopener">github.com/SlicerTMS/SlicerTMS</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30" target="_blank" rel="noopener">Experiments/SlicerSimNIBSClient.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30" rel="noopener"><code>tmsservice</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="20" style="counter-reset: li-counter 19 ;">
          <li></li>
          <li></li>
          <li>slicer.mrmlScene.Clear()</li>
          <li></li>
          <li>try:</li>
          <li>    process.kill()</li>
          <li>except NameError:</li>
          <li>    pass</li>
          <li></li>
          <li>cmdList = [simnibs_pythonPath, SimNIBSServicePath]</li>
          <li class="selected">process = slicer.util.launchConsoleProcess(cmdList, useStartupEnvironment=True)</li>
          <li></li>
          <li>port = 18891</li>
          <li></li>
          <li>for attempt in range(10):</li>
          <li>	try:</li>
          <li>		simnibs = rpyc.connect("localhost", port,</li>
          <li>			config = {</li>
          <li>				"allow_public_attrs": True,</li>
          <li>				"allow_pickle": True,</li>
          <li>				"sync_request_timeout": None</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @mikebind (2026-09-17 17:21 UTC)

<p>Thanks, this is really helpful. I’ll probably explore some in both these directions and mark this solved.</p>

---
