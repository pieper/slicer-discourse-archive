# How to display the PolyData independently?

**Topic ID**: 1700
**Date**: 2017-12-21
**URL**: https://discourse.slicer.org/t/how-to-display-the-polydata-independently/1700

---

## Post #1 by @spring (2017-12-21 10:03 UTC)

<p>Operating system: Windows 10 64bit<br>
Slicer version:4.9.0 2017-10-23<br>
Expected behavior: display the polydata independently<br>
Actual behavior: displayed one polydata in all of  scenes.</p>
<p>Hi SlicerExperts,</p>
<pre><code>I have setted the Slicer's layout with two scenes(view1,view2),then I want to  draw one PolyData(rectangle) in view1,but this rectangle also showed in view2,pls see below screenshot,
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf7a7ab1981549295706159ab9549290b381d02.jpeg" alt="image" data-base62-sha1="xFsNPZBx0tmg75KR6w4Xnxps6FI" width="680" height="310"></p>
<pre><code>I just want to show the created rectangle in the scene which I drawed,could you give me some suggestions ?
</code></pre>
<p>Thanks,<br>
Chunbo</p>

---

## Post #2 by @spring (2017-12-21 10:33 UTC)

<p>BTW,I am using Python script to implement it.I guess there are some funtions from Slicer can set the model which added the Polydata to each view/scenes?</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #3 by @cpinter (2017-12-21 12:21 UTC)

<p>I assume you want to do this programmatically as well. After you get the display node for the model node (or segmentation node) using GetDisplayNode, you can change what views it appears in like this<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLDisplayNodeViewComboBox.cxx#L167-L181" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLDisplayNodeViewComboBox.cxx#L167-L181" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLDisplayNodeViewComboBox.cxx#L167-L181</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="167" style="counter-reset: li-counter 166 ;">
<li>if (this-&gt;allChecked() || this-&gt;noneChecked())</li>
<li>  {</li>
<li>  d-&gt;MRMLDisplayNode-&gt;RemoveAllViewNodeIDs();</li>
<li>  }</li>
<li>else</li>
<li>  {</li>
<li>  foreach (vtkMRMLAbstractViewNode* viewNode, this-&gt;checkedViewNodes())</li>
<li>    {</li>
<li>    d-&gt;MRMLDisplayNode-&gt;AddViewNodeID(viewNode ? viewNode-&gt;GetID() : 0);</li>
<li>    }</li>
<li>  foreach (vtkMRMLAbstractViewNode* viewNode, this-&gt;uncheckedViewNodes())</li>
<li>    {</li>
<li>    d-&gt;MRMLDisplayNode-&gt;RemoveViewNodeID(viewNode ? viewNode-&gt;GetID() : 0);</li>
<li>    }</li>
<li>  }</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @spring (2017-12-23 15:05 UTC)

<p>Thanks for your answer，cpinter.</p>
<p>One thing is not very sure:I have two sliceWidgets(likes View1,View2),how to link the viewNode to related sliceWidgets?</p>
<p>Thanks,<br>
Chunbo</p>

---

## Post #5 by @lassoan (2017-12-23 16:50 UTC)

<aside class="quote no-group" data-username="spring" data-post="4" data-topic="1700">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ee59a6/48.png" class="avatar"> spring:</div>
<blockquote>
<p>how to link the viewNode to related sliceWidgets?</p>
</blockquote>
</aside>
<p>See examples for that in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Accessing_views.2C_renderers.2C_and_cameras" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #6 by @spring (2017-12-25 01:22 UTC)

<p>Thanks Lassoan and cpinter,</p>
<pre><code>Merry Christmas!
</code></pre>
<p>Thanks,<br>
Chunbo</p>

---
