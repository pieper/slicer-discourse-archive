---
topic_id: 20049
title: "How To Enlarge Zoom In Out The Volume Of A Slice With Python"
date: 2021-10-07
url: https://discourse.slicer.org/t/20049
---

# How to enlarge(zoom in/out) the volume of a slice with python code?

**Topic ID**: 20049
**Date**: 2021-10-07
**URL**: https://discourse.slicer.org/t/how-to-enlarge-zoom-in-out-the-volume-of-a-slice-with-python-code/20049

---

## Post #1 by @jumbojing (2021-10-07 09:50 UTC)

<p>如何用python代码放大某个slice的volume呢?</p>
<blockquote>
<p>How to enlarge(zoom in/out) the volume of a slice with python code?</p>
</blockquote>

---

## Post #2 by @pieper (2021-10-07 11:40 UTC)

<p>This should help:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465">
  <header class="source">

      <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465" target="_blank" rel="noopener">pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="447" style="counter-reset: li-counter 446 ;">
          <li>def zoom(self,factor,sliceNodes=None):</li>
          <li>  """Zoom slice nodes by factor.</li>
          <li>  factor: "Fit" or +/- amount to zoom</li>
          <li>  sliceNodes: list of slice nodes to change, None means all.</li>
          <li>  """</li>
          <li>  if not sliceNodes:</li>
          <li>    sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')</li>
          <li>  layoutManager = slicer.app.layoutManager()</li>
          <li>  for sliceNode in list(sliceNodes.values()):</li>
          <li>    if factor == "Fit":</li>
          <li>      sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())</li>
          <li>      if sliceWidget:</li>
          <li>        sliceWidget.sliceLogic().FitSliceToAll()</li>
          <li>    else:</li>
          <li>      newFOVx = sliceNode.GetFieldOfView()[0] * factor</li>
          <li>      newFOVy = sliceNode.GetFieldOfView()[1] * factor</li>
          <li>      newFOVz = sliceNode.GetFieldOfView()[2]</li>
          <li>      sliceNode.SetFieldOfView( newFOVx, newFOVy, newFOVz )</li>
          <li>      sliceNode.UpdateMatrices()</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jumbojing (2021-10-09 00:13 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="20049">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<pre><code class="lang-auto">def zoom(self,factor,sliceNodes=None):
            """Zoom slice nodes by factor.
            factor: "Fit" or +/- amount to zoom
            sliceNodes: list of slice nodes to change, None means all.
            """
            if not sliceNodes:
              sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')
            layoutManager = slicer.app.layoutManager()
            for sliceNode in list(sliceNodes.values()):
              if factor == "Fit":
                sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())
                if sliceWidget:
                  sliceWidget.sliceLogic().FitSliceToAll()
              else:
                newFOVx = sliceNode.GetFieldOfView()[0] * factor
                newFOVy = sliceNode.GetFieldOfView()[1] * factor
                newFOVz = sliceNode.GetFieldOfView()[2]
                sliceNode.SetFieldOfView( newFOVx, newFOVy, newFOVz )
                sliceNode.UpdateMatrices()
</code></pre>
</blockquote>
</aside>
<p>谢谢老师! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465">
  <header class="source">

      <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465" target="_blank" rel="noopener nofollow ugc">pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="447" style="counter-reset: li-counter 446 ;">
          <li>def zoom(self,factor,sliceNodes=None):</li>
          <li>  """Zoom slice nodes by factor.</li>
          <li>  factor: "Fit" or +/- amount to zoom</li>
          <li>  sliceNodes: list of slice nodes to change, None means all.</li>
          <li>  """</li>
          <li>  if not sliceNodes:</li>
          <li>    sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')</li>
          <li>  layoutManager = slicer.app.layoutManager()</li>
          <li>  for sliceNode in list(sliceNodes.values()):</li>
          <li>    if factor == "Fit":</li>
          <li>      sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())</li>
          <li>      if sliceWidget:</li>
          <li>        sliceWidget.sliceLogic().FitSliceToAll()</li>
          <li>    else:</li>
          <li>      newFOVx = sliceNode.GetFieldOfView()[0] * factor</li>
          <li>      newFOVy = sliceNode.GetFieldOfView()[1] * factor</li>
          <li>      newFOVz = sliceNode.GetFieldOfView()[2]</li>
          <li>      sliceNode.SetFieldOfView( newFOVx, newFOVy, newFOVz )</li>
          <li>      sliceNode.UpdateMatrices()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
[/quote]</p>

---

## Post #4 by @jumbojing (2021-10-09 03:22 UTC)

<p>根据老师的代码和我的需求我加了这些, 感觉不够简洁…您有没有更简洁的建议呢?</p>
<blockquote>
<p>[quote=“pieper, post:2, topic:20049”]<br>
<a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465" class="inline-onebox" rel="noopener nofollow ugc">CompareVolumes/CompareVolumes.py at master · pieper/CompareVolumes · GitHub</a><br>
[/quote]</p>
</blockquote>
<blockquote>
<p>According to the teacher’s code and my needs, I added these codes, which is not concise enough… Do you have any more concise suggestions?</p>
</blockquote>
<pre><code class="lang-auto">def zoomplus(factor,sliceNodes=None):
  """Zoom slice nodes by factor.
  factor: "Fit" or +/- amount to zoom
  sliceNodes: list of slice nodes to change, None means all.
  """
  layoutManager = slicer.app.layoutManager()
  if sliceNodes==None:
    sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')
    for sliceNode in list(sliceNodes.values()):
      if factor == "Fit":
        sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())
        if sliceWidget:
          sliceWidget.sliceLogic().FitSliceToAll()
      else:
        newFOVx = sliceNode.GetFieldOfView()[0] * factor
        newFOVy = sliceNode.GetFieldOfView()[1] * factor
        newFOVz = sliceNode.GetFieldOfView()[2]
        sliceNode.SetFieldOfView( newFOVx, newFOVy, newFOVz )
  else:          
    if sliceNodes == "R":
      sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")
    elif sliceNodes == "Y":
      sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeYellow")
    elif sliceNodes == "G":
      sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeGreen")
    if factor == "Fit":
      sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())      
      if sliceWidget:
          sliceWidget.sliceLogic().FitSliceToAll()
    else:   
      newFOVx = sliceNode.GetFieldOfView()[0] * factor
      newFOVy = sliceNode.GetFieldOfView()[1] * factor
      newFOVz = sliceNode.GetFieldOfView()[2]
      sliceNode.SetFieldOfView( newFOVx, newFOVy, newFOVz )
  sliceNode.UpdateMatrices() 
</code></pre>

---

## Post #5 by @pieper (2021-10-09 22:12 UTC)

<p>The original idea of the <code>sliceNodes</code> argument would that it’s a list of nodes to which the zoom operation should be applied, so it would be better to keep the node ids out of the function.  Instead you would invoke it like this an you wouldn’t need to change the function at all.</p>
<pre><code class="lang-auto">sliceNodes = [slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")]
zoom('fit', sliceNodes)
</code></pre>

---

## Post #6 by @jumbojing (2021-10-10 00:35 UTC)

<p>I see, thanks.</p>
<p>like that:</p>
<pre><code class="lang-auto">def zoomSlice(factor,sliceNodes=None):
  """Zoom slice nodes by factor.
  factor: "Fit" or +/- amount to zoom
  sliceNodes: list of slice nodes to change, None means all.
  """
  layoutManager = slicer.app.layoutManager()
  
  if sliceNodes==None:
    sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')
  else:
    if sliceNodes == "R":
      sliceNodes = slicer.util.getNodes('vtkMRMLSliceNodeR*')
    elif sliceNodes == "Y":
      sliceNodes = slicer.util.getNodes('vtkMRMLSliceNodeY*')
    elif sliceNodes == "G":
      sliceNodes = slicer.util.getNodes('vtkMRMLSliceNodeG*')
    for sliceNode in list(sliceNodes.values()):
      sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())      
      if factor == "Fit":
        sliceWidget.sliceLogic().FitSliceToAll()
      else:
        sliceWidget.sliceLogic().FitSliceToAll()        
        newFOVx = sliceNode.GetFieldOfView()[0] * factor
        newFOVy = sliceNode.GetFieldOfView()[1] * factor
        newFOVz = sliceNode.GetFieldOfView()[2]
        sliceNode.SetFieldOfView( newFOVx, newFOVy, newFOVz )
  sliceNode.UpdateMatrices() 
</code></pre>

---

## Post #7 by @jumbojing (2021-10-20 03:27 UTC)

<h1><a name="p-68308-h-1" class="anchor" href="#p-68308-h-1" aria-label="Heading link"></a>最终解决方案:</h1>
<pre><code class="lang-auto">def zoomSlice(factor, sliceNode=None):
  """Zoom slice nodes by factor.
  factor: "Fit" or +/- amount to zoom
  sliceNode:"R";"Y";"G":"None"
  sliceNodes: list of slice nodes to change, None means all.
  """
  layoutManager = slicer.app.layoutManager()    
  if sliceNode==None:
    sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')
  else:      
    sliceNodes = {"R": "vtkMRMLSliceNodeRed", "Y": "vtkMRMLSliceNodeYellow", "G": "vtkMRMLSliceNodeGreen"}
    sliceNodes = slicer.util.getNodes(sliceNodes[sliceNode])      
  for sliceNode in list(sliceNodes.values()):
    sliceWidget = layoutManager.sliceWidget(sliceNode.GetLayoutName())
    sliceWidget.sliceLogic().FitSliceToAll()        
    newFOVx = sliceNode.GetFieldOfView()[0] / factor
    newFOVy = sliceNode.GetFieldOfView()[1] / factor
    newFOVz = sliceNode.GetFieldOfView()[2]
    sliceNode.SetFieldOfView( newFOVx, newFOVy, newFOVz )
    sliceNode.UpdateMatrices()
</code></pre>

---
