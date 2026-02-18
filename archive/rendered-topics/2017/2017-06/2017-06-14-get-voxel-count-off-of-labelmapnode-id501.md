# Get Voxel count off of LabelMapNode?

**Topic ID**: 501
**Date**: 2017-06-14
**URL**: https://discourse.slicer.org/t/get-voxel-count-off-of-labelmapnode/501

---

## Post #1 by @jks1995 (2017-06-14 15:29 UTC)

<p>How would I get the number of voxels off of a label map node?</p>

---

## Post #2 by @lassoan (2017-06-14 15:43 UTC)

<p>Use Labelmap statistics module to get the number of non-zero voxels.</p>

---

## Post #3 by @jks1995 (2017-06-14 17:44 UTC)

<p>How would I go about that?</p>

---

## Post #4 by @lassoan (2017-06-15 02:17 UTC)

<ul>
<li>Open Label statistics module</li>
<li>Select Grayscale volume</li>
<li>Select Label map volume</li>
<li>Click Apply</li>
</ul>
<p><code>Count</code> column contains the number of voxels.</p>

---

## Post #5 by @jks1995 (2017-06-15 14:33 UTC)

<p>How would I access this through python?</p>

---

## Post #6 by @ihnorton (2017-06-15 15:14 UTC)

<p>The module is written in Python, so any specific functionality could be easily extracted/duplicated in your own script. Here is the relevant section:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Scripted/LabelStatistics/LabelStatistics.py#L310-L345" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Scripted/LabelStatistics/LabelStatistics.py#L310-L345" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Scripted/LabelStatistics/LabelStatistics.py#L310-L345</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="310" style="counter-reset: li-counter 309 ;">
<li># logic copied from slicer3 LabelStatistics</li>
<li># to create the binary volume of the label</li>
<li># //logic copied from slicer2 LabelStatistics MaskStat</li>
<li># // create the binary volume of the label</li>
<li>thresholder = vtk.vtkImageThreshold()</li>
<li>thresholder.SetInputConnection(labelNode.GetImageDataConnection())</li>
<li>thresholder.SetInValue(1)</li>
<li>thresholder.SetOutValue(0)</li>
<li>thresholder.ReplaceOutOn()</li>
<li>thresholder.ThresholdBetween(i,i)</li>
<li>thresholder.SetOutputScalarType(grayscaleNode.GetImageData().GetScalarType())</li>
<li>thresholder.Update()</li>
<li>
</li>
<li># this.InvokeEvent(vtkLabelStatisticsLogic::LabelStatsInnerLoop, (void*)"0.25");</li>
<li>
</li>
<li>#  use vtk's statistics class with the binary labelmap as a stencil</li>
<li>stencil = vtk.vtkImageToImageStencil()</li>
<li>stencil.SetInputConnection(thresholder.GetOutputPort())</li>
<li>stencil.ThresholdBetween(1, 1)</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/eefeac9286f48552e8418a11f412b2823a09b407/Modules/Scripted/LabelStatistics/LabelStatistics.py#L310-L345" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2017-06-15 16:36 UTC)

<p>If you want to build anything on this, then I would strongly recommend to switch to Segmentations/Segment Editor/Segment statistics modules now. These modules are much more capable than the old Editor/Label statistics - those old modules will be kept around for a while but they will not be developed any further.</p>
<p>See complete example of using Segment statistics in Python below. You can run the test by enabling developer mode in Slicer application settings, opening Segment statistics module, and clicking on <code>Reload and test</code> button.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L435-L483" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L435-L483" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L435-L483</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="435" style="counter-reset: li-counter 434 ;">
<li>  segment = segmentationNode.GetSegmentation().GetSegment(segmentID)</li>
<li>  statistics = self.getStatistics()</li>
<li>  if segmentID not in statistics["SegmentIDs"]:</li>
<li>    statistics["SegmentIDs"].append(segmentID)</li>
<li>  statistics[segmentID,"Segment"] = segment.GetName()</li>
<li>
</li>
<li>  # apply all enabled plugins</li>
<li>  for plugin in self.plugins:</li>
<li>    pluginName = plugin.__class__.__name__</li>
<li>    if self.getParameterNode().GetParameter(pluginName+'.enabled')=='True':</li>
<li>      stats = plugin.computeStatistics(segmentID)</li>
<li>      for key in stats:</li>
<li>        statistics[segmentID,pluginName+'.'+key] = stats[key]</li>
<li>        statistics["MeasurementInfo"][pluginName+'.'+key] = plugin.getMeasurementInfo(key)</li>
<li>
</li>
<li>def getPluginByKey(self, key):</li>
<li>  """Get plugin responsible for obtaining measurement value for given key"""</li>
<li>  for plugin in self.plugins:</li>
<li>    if plugin.toShortKey(key) in plugin.keys:</li>
<li>      return plugin</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py#L435-L483" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
