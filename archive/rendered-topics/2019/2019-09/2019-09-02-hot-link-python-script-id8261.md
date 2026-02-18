# Hot Link Python Script

**Topic ID**: 8261
**Date**: 2019-09-02
**URL**: https://discourse.slicer.org/t/hot-link-python-script/8261

---

## Post #1 by @bsmarine (2019-09-02 15:04 UTC)

<p>Does anyone know of python script that activates hot-link mode between different windows/studies?</p>

---

## Post #2 by @pieper (2019-09-02 18:58 UTC)

<p>You’d just need to convert this code to python:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L2077-L2094" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L2077-L2094" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L2077-L2094</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="2077" style="counter-reset: li-counter 2076 ;">
<li>//---------------------------------------------------------------------------</li>
<li>void qMRMLSliceControllerWidget::setHotLinked(bool linked)</li>
<li>{</li>
<li>  vtkCollection* sliceCompositeNodes = this-&gt;mrmlScene() ?</li>
<li>    this-&gt;mrmlScene()-&gt;GetNodesByClass("vtkMRMLSliceCompositeNode") : nullptr;</li>
<li>  if (!sliceCompositeNodes)</li>
<li>    {</li>
<li>    return;</li>
<li>    }</li>
<li>  vtkMRMLSliceCompositeNode* sliceCompositeNode = nullptr;</li>
<li>  for(sliceCompositeNodes-&gt;InitTraversal();</li>
<li>      (sliceCompositeNode = vtkMRMLSliceCompositeNode::SafeDownCast(</li>
<li>        sliceCompositeNodes-&gt;GetNextItemAsObject()));)</li>
<li>    {</li>
<li>    sliceCompositeNode-&gt;SetHotLinkedControl(linked);</li>
<li>    }</li>
<li>  sliceCompositeNodes-&gt;Delete();</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @JoostJM (2019-09-03 05:30 UTC)

<p>it’ll be something like</p>
<pre><code class="lang-auto">compositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
for node in compositeNodes:
  node.SetHotLinkedControl(linked)
</code></pre>

---

## Post #4 by @bsmarine (2019-09-03 19:03 UTC)

<p>Thanks for the help!</p>
<p>This will automatically turn on hot link for all views in Python:</p>
<pre><code class="lang-auto">compositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
for node in compositeNodes:
  node.SetHotLinkedControl(1)
  node.SetLinkedControl(1)</code></pre>

---
