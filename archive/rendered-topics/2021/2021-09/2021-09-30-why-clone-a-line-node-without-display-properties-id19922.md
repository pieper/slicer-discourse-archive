---
topic_id: 19922
title: "Why Clone A Line Node Without Display Properties"
date: 2021-09-30
url: https://discourse.slicer.org/t/19922
---

# Why clone a line node without display properties?

**Topic ID**: 19922
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/why-clone-a-line-node-without-display-properties/19922

---

## Post #1 by @jumbojing (2021-09-30 04:10 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69d7ea198515b33164a452caee809669176e90b1.png" alt="image" data-base62-sha1="f6kJcbBqAHAARxOI5M681jblsm5" width="574" height="430"></p>
<p>Why clone a line node without display properties?<br>
克隆一条直线为啥不带显示属性呢?</p>

---

## Post #2 by @cpinter (2021-09-30 08:51 UTC)

<p>What do you do, what do you expect, and what happens instead? What Slicer version?</p>

---

## Post #3 by @jumbojing (2021-09-30 21:36 UTC)

<p>slicer 4.13<br>
我画了一条直线如图, 并且设置了显示属性加粗和颜色…</p>
<blockquote>
<p>I drew a straight line as shown in the figure, and set the display attributes bold and color…</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9198492ddc2e91035f65a6a7ce48d3d361a0da6d.png" data-download-href="/uploads/short-url/kLZvfYHAfnqssl8G68WfCbw2WRv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9198492ddc2e91035f65a6a7ce48d3d361a0da6d_2_582x500.png" alt="image" data-base62-sha1="kLZvfYHAfnqssl8G68WfCbw2WRv" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9198492ddc2e91035f65a6a7ce48d3d361a0da6d_2_582x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9198492ddc2e91035f65a6a7ce48d3d361a0da6d_2_873x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9198492ddc2e91035f65a6a7ce48d3d361a0da6d_2_1164x1000.png 2x" data-dominant-color="2B2B35"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1726×1482 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then clone it… get this result<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb0b3618687299afce7937abc13b50ac8ea4641a.png" data-download-href="/uploads/short-url/qGFj2tgWJwvGzor9DpJBIaN7lI6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb0b3618687299afce7937abc13b50ac8ea4641a_2_690x407.png" alt="image" data-base62-sha1="qGFj2tgWJwvGzor9DpJBIaN7lI6" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb0b3618687299afce7937abc13b50ac8ea4641a_2_690x407.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb0b3618687299afce7937abc13b50ac8ea4641a_2_1035x610.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb0b3618687299afce7937abc13b50ac8ea4641a_2_1380x814.png 2x" data-dominant-color="555762"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2152×1270 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why clone a line node without display properties?</p>

---

## Post #4 by @lassoan (2021-09-30 21:47 UTC)

<p>I guess the cloned node is using default markups properties, which make sense, but probably copying display properties would be a more desirable behavior. You can submit a bug report to <a href="https://issues.slicer.org">https://issues.slicer.org</a> and we’ll try to get to it soon.</p>
<p>If you copy the node programmatically then after cloning you can simply copy the content of the original node’s display node to the cloned node’s display node.</p>

---

## Post #5 by @jumbojing (2022-05-12 23:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="19922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you copy the node programmatically then after cloning you can simply copy the content of the original node’s display node to the cloned node’s display node.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Howto <em>copy the content of the original node’s display node to the cloned node’s display node</em> <strong>except those that have been modified display properties</strong>, such as the line diameter and color of the lineNode display properties, etc. programmatically (py)?</p>

---

## Post #6 by @lassoan (2022-05-13 00:50 UTC)

<p>You can copy all content of a node into another, using the <code>CopyContent</code> method.</p>

---

## Post #7 by @jumbojing (2022-05-13 02:05 UTC)

<pre><code class="lang-py">def cloneNode(modNode):
  """Create a copy from input nodes and return the new instance"""
  modClass = modNode.GetClassName()
  modCopy = slicer.mrmlScene.AddNewNodeByClass(modClass)
  modCopy.CopyContent(modNode, False)
  modCopy.SetName(f"{modNode.GetName()}_copy")
  modCopy.GetDisplayNode().CopyContent(modNode.GetDisplayNode(), False)
  modCopy.GetDisplayNode().SetVisibility3D(True)
  modCopy.GetDisplayNode().SetVisibility2D(True)
  return modCopy
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bcc174f93ba8d1f760fdd97144b96056b29ce05.png" data-download-href="/uploads/short-url/d64IckGX7hMumNHtvVeFTmgzBJz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcc174f93ba8d1f760fdd97144b96056b29ce05_2_690x390.png" alt="image" data-base62-sha1="d64IckGX7hMumNHtvVeFTmgzBJz" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcc174f93ba8d1f760fdd97144b96056b29ce05_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcc174f93ba8d1f760fdd97144b96056b29ce05_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bcc174f93ba8d1f760fdd97144b96056b29ce05_2_1380x780.png 2x" data-dominant-color="787B82"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2866×1624 373 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks</p>

---

## Post #8 by @lassoan (2022-05-13 17:06 UTC)

<p>The <code>cloneNode</code> function that you created takes a MRML node object as input. It fails because you passed a string as input.</p>

---

## Post #9 by @jumbojing (2022-05-21 00:56 UTC)

<pre><code class="lang-auto">def cloneNode(modName="None",modNode=None):
  """Create a copy from input nodes and return the new instance"""
  if modName!="None":
    modNode=slicer.util.getNode(modName)
  else:
    modName=modNode.GetName()
  modClass = modNode.GetClassName()
  modCopy = slicer.mrmlScene.AddNewNodeByClass(modClass)
  modCopy.CopyContent(modNode,False)
  modCopy.SetName(f"{modNode.GetName()}_copy")
  modCopyDn=slicer.mrmlScene.CreateNodeByClass(modNode.GetDisplayNode().GetClassName())
  modCopyDn.CopyContent(modNode.GetDisplayNode(),False)
  modCopyDn.SetVisibility3D(True)
  modCopyDn.SetVisibility2D(True)
  return modCopy
</code></pre>
<p>这样似乎可以了, 只是不知道为啥颜色属性没有copy过来…</p>
<blockquote>
<p>This seems to work, but I don’t know why the color attribute is not copied…</p>
</blockquote>

---

## Post #10 by @lassoan (2022-05-21 02:04 UTC)

<p><code>CopyContent</code> copies color:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/43e8f5b2407b4c83509406b1acf266e25412eb49/Libs/MRML/Core/vtkMRMLDisplayNode.cxx#L272-L273">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/43e8f5b2407b4c83509406b1acf266e25412eb49/Libs/MRML/Core/vtkMRMLDisplayNode.cxx#L272-L273" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/43e8f5b2407b4c83509406b1acf266e25412eb49/Libs/MRML/Core/vtkMRMLDisplayNode.cxx#L272-L273" target="_blank" rel="noopener">Slicer/Slicer/blob/43e8f5b2407b4c83509406b1acf266e25412eb49/Libs/MRML/Core/vtkMRMLDisplayNode.cxx#L272-L273</a></h4>



    <pre class="onebox">      <code class="lang-cxx">
        <ol class="start lines" start="272" style="counter-reset: li-counter 271 ;">
            <li>this-&gt;SetColor(node-&gt;Color);</li>
            <li>this-&gt;SetSelectedColor(node-&gt;SelectedColor);</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you can provide an example (source code and data) that behaves differently than you expect then we can have a look.</p>
<p>Your code snippet above looks good, except I would recommend only use <code>slicer.util.getNode</code> for testing and debugging, not for any production code. Instead, when you create or read a node, store the returned node variable or node ID. A node name does not uniquely identify a node, because many nodes can have the same name.</p>
<p>If you want to clone any node that shows up in the subject hierarchy tree (for example, in Data module) then you can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-node">this code snippet</a>.</p>

---
