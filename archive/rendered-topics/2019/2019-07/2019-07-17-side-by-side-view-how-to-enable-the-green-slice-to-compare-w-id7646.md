# Side by side view: How to enable the green slice to compare with the red one?

**Topic ID**: 7646
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/side-by-side-view-how-to-enable-the-green-slice-to-compare-with-the-red-one/7646

---

## Post #1 by @NoobForSlicer (2019-07-17 22:55 UTC)

<p>So far I can only see the red and yellow one side by side… ANy idea how to see the green and red side by side?</p>

---

## Post #2 by @lassoan (2019-07-17 23:17 UTC)

<p>There are many layouts to choose from. Click the layout selector button on the toolbar and choose “Conventional” to get a view where all three views are shown side by side.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bac9164ca366b6a76c29a98534f84bcf848efe16.png" alt="image" data-base62-sha1="qEnDtfSE72B3IAHs30TsC5Lvb0i" width="659" height="489"></p>
<p>You can define any custom layout, with any number of views in any arrangement, as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">here</a>.</p>

---

## Post #3 by @Prashant_Pandey (2019-09-13 23:15 UTC)

<p>Just wondering if there’s an easier way to customize layout than the snippet you linked? It just seems an awkward way to change and customize layout, rather than having a GUI option. For example in the ‘side by side’ option in the layout selector, I think users should be able to directly select which views/slices they want to display side by side, and whether the split should be horizontal or vertical.</p>

---

## Post #4 by @lassoan (2019-09-14 11:57 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="3" data-topic="7646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>It just seems an awkward way to change and customize layout, rather than having a GUI option.</p>
</blockquote>
</aside>
<p>It would be certainly useful to have GUI to dynamically create new layouts but implementation would be significant effort. There are several other areas where investing development time makes bigger impact.</p>
<p>Do you know you can register layouts automatically in your slicerrc.py file? You can probably even make it show up in the layout sensor. Would that help?</p>

---

## Post #5 by @pieper (2019-09-14 14:28 UTC)

<p>You can also try the CompareVolumes module (under Wizards in the menu).</p>
<p>Under the hood the CompareVolumesLogic has some helper code that may handle your use cases.  It’s shipped with Slicer.</p>
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

## Post #6 by @Prashant_Pandey (2019-09-14 20:35 UTC)

<p>Thanks, Ill try CompareVolumes</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> How do I register layouts and make them show up in the layout menu, that sounds useful</p>

---

## Post #7 by @lassoan (2019-09-14 21:48 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="6" data-topic="7646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>How do I register layouts and make them show up in the layout menu, that sounds useful</p>
</blockquote>
</aside>
<p>See this example in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---
