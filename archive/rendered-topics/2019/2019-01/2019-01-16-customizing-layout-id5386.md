# Customizing layout

**Topic ID**: 5386
**Date**: 2019-01-16
**URL**: https://discourse.slicer.org/t/customizing-layout/5386

---

## Post #1 by @muratmaga (2019-01-16 04:53 UTC)

<p>While there a quite a bit of pre-defined layout options, I occasionally need an odd layouts which there is no close approximation (such as two 3D viewers, one slice view, one quantitative and a table).</p>
<p>Would you guys consider perhaps adding a customization tool under preferences, where user can split the panes and drag items from a list to design their own preferred custom layout?</p>

---

## Post #2 by @lassoan (2019-01-16 05:14 UTC)

<p>This idea has come up many times (in addition to improving layouts to better support multiple monitors), but never got high enough priority because for developers it has been just always too easy to write that layout XML string and register/activate it with 2-3 method calls. It would be nice if you could spend some time on it. We would be happy to give advice.</p>

---

## Post #3 by @pieper (2019-01-16 21:15 UTC)

<p>Here’s some example code for generating custom views based on loaded data:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L195-L444" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L195-L444" target="_blank" rel="nofollow noopener">pieper/CompareVolumes/blob/master/CompareVolumes.py#L195-L444</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="195" style="counter-reset: li-counter 194 ;">
<li>class CompareVolumesLogic(ScriptedLoadableModuleLogic):</li>
<li>"""This class should implement all the actual</li>
<li>computation done by your module.  The interface</li>
<li>should be such that other python code can import</li>
<li>this class and make use of the functionality without</li>
<li>requiring an instance of the Widget</li>
<li>"""</li>
<li>def __init__(self):</li>
<li>  ScriptedLoadableModuleLogic.__init__(self)</li>
<li>  self.sliceViewItemPattern = """</li>
<li>    &lt;item&gt;&lt;view class="vtkMRMLSliceNode" singletontag="{viewName}"&gt;</li>
<li>      &lt;property name="orientation" action="default"&gt;{orientation}&lt;/property&gt;</li>
<li>      &lt;property name="viewlabel" action="default"&gt;{viewName}&lt;/property&gt;</li>
<li>      &lt;property name="viewcolor" action="default"&gt;{color}&lt;/property&gt;</li>
<li>    &lt;/view&gt;&lt;/item&gt;</li>
<li>   """</li>
<li>  # use a nice set of colors</li>
<li>  self.colors = slicer.util.getNode('GenericColors')</li>
<li>  self.lookupTable = self.colors.GetLookupTable()</li>
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
