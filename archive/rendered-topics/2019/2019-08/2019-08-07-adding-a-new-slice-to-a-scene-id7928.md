---
topic_id: 7928
title: "Adding A New Slice To A Scene"
date: 2019-08-07
url: https://discourse.slicer.org/t/7928
---

# Adding a new slice to a scene

**Topic ID**: 7928
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/adding-a-new-slice-to-a-scene/7928

---

## Post #1 by @Neil_Seller (2019-08-07 20:42 UTC)

<p>How would one go ahead adding a new slice to a scene?</p>
<p>I’ve tried:<br>
VLA = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSliceNode”)</p>
<p>but this crashes everytime.</p>
<p>I want to do this in order to create alternative views of the same volume - e.g. a long axis plane of a cardiac CT.</p>
<p>Thank you</p>
<p>Neil</p>

---

## Post #2 by @pieper (2019-08-07 21:05 UTC)

<p>Rather than create your own view nodes, you probably want to define a custom layout and then assign different volumes or views of volumes to be shown in the various slice views.  The code linked below demonstrates how to control these things from python.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L195-L444" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L195-L444" target="_blank" rel="nofollow noopener">pieper/CompareVolumes/blob/master/CompareVolumes.py#L195-L444</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="195" style="counter-reset: li-counter 194 ;">
<li>class CompareVolumesLogic(ScriptedLoadableModuleLogic):</li>
<li>  """This class should implement all the actual</li>
<li>  computation done by your module.  The interface</li>
<li>  should be such that other python code can import</li>
<li>  this class and make use of the functionality without</li>
<li>  requiring an instance of the Widget</li>
<li>  """</li>
<li>  def __init__(self):</li>
<li>    ScriptedLoadableModuleLogic.__init__(self)</li>
<li>    self.sliceViewItemPattern = """</li>
<li>      &lt;item&gt;&lt;view class="vtkMRMLSliceNode" singletontag="{viewName}"&gt;</li>
<li>        &lt;property name="orientation" action="default"&gt;{orientation}&lt;/property&gt;</li>
<li>        &lt;property name="viewlabel" action="default"&gt;{viewName}&lt;/property&gt;</li>
<li>        &lt;property name="viewcolor" action="default"&gt;{color}&lt;/property&gt;</li>
<li>      &lt;/view&gt;&lt;/item&gt;</li>
<li>     """</li>
<li>    # use a nice set of colors</li>
<li>    self.colors = slicer.util.getNode('GenericColors')</li>
<li>    self.lookupTable = self.colors.GetLookupTable()</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L195-L444" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
