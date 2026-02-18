# Is there any way to get LabelStatistics to the python?

**Topic ID**: 7115
**Date**: 2019-06-10
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-get-labelstatistics-to-the-python/7115

---

## Post #1 by @batuhan_edguer (2019-06-10 19:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1536a8dca775ac051f75ccb41850a07baa73bb7.png" data-download-href="/uploads/short-url/piHeiQy74m3gn5avXkYryymXGUT.png?dl=1" title="Ek%20A%C3%A7%C4%B1klama%202019-06-10%20225453" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1536a8dca775ac051f75ccb41850a07baa73bb7.png" alt="Ek%20A%C3%A7%C4%B1klama%202019-06-10%20225453" data-base62-sha1="piHeiQy74m3gn5avXkYryymXGUT" width="690" height="98" data-dominant-color="F4ECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ek%20A%C3%A7%C4%B1klama%202019-06-10%20225453</span><span class="informations">832×119 9.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I want to get these datas to the script for GUI development.<br>
Is there any command to get these datas?</p>

---

## Post #2 by @pieper (2019-06-11 20:57 UTC)

<p>Yes - you can access the LabelStatisticsLogic and you can calculate these values.  (Note that in newer Slicer we suggest using Segment Statistics, which is similar).</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/LabelStatistics/LabelStatistics.py#L278-L380" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/LabelStatistics/LabelStatistics.py#L278-L380" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/LabelStatistics/LabelStatistics.py#L278-L380</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="278" style="counter-reset: li-counter 277 ;">
<li>class LabelStatisticsLogic(ScriptedLoadableModuleLogic):</li>
<li>  """Implement the logic to calculate label statistics.</li>
<li>  Nodes are passed in as arguments.</li>
<li>  Results are stored as 'statistics' instance variable.</li>
<li>  Uses ScriptedLoadableModuleLogic base class, available at:</li>
<li>  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</li>
<li>  """</li>
<li>
</li>
<li>  def __init__(self, grayscaleNode, labelNode, colorNode=None, nodeBaseName=None, fileName=None):</li>
<li>    #import numpy</li>
<li>
</li>
<li>    self.keys = ("Index", "Count", "Volume mm^3", "Volume cc", "Min", "Max", "Mean", "Median", "StdDev")</li>
<li>    cubicMMPerVoxel = reduce(lambda x,y: x*y, labelNode.GetSpacing())</li>
<li>    ccPerCubicMM = 0.001</li>
<li>
</li>
<li>    # TODO: progress and status updates</li>
<li>    # this-&gt;InvokeEvent(vtkLabelStatisticsLogic::StartLabelStats, (void*)"start label stats")</li>
<li>
</li>
<li>    self.labelNode = labelNode</li>
<li>    self.colorNode = colorNode</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/LabelStatistics/LabelStatistics.py#L278-L380" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
