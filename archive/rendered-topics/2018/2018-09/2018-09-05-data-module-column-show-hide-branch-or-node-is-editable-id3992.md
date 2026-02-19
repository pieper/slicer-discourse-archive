---
topic_id: 3992
title: "Data Module Column Show Hide Branch Or Node Is Editable"
date: 2018-09-05
url: https://discourse.slicer.org/t/3992
---

# Data Module: column show/hide branch or node is editable

**Topic ID**: 3992
**Date**: 2018-09-05
**URL**: https://discourse.slicer.org/t/data-module-column-show-hide-branch-or-node-is-editable/3992

---

## Post #1 by @phcerdan (2018-09-05 16:42 UTC)

<p>Using a recent Slicer <a href="https://github.com/Slicer/Slicer/tree/c88b17d38acf99c66892f867aff163a9c07d073a" rel="noopener nofollow ugc">c88b17d38</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c76b84b0ecefdd99ac8d8207869d2ce27547565.gif" data-download-href="/uploads/short-url/hL3ySoCrKpchACTnen76gzFa3XL.gif?dl=1" title="Peek%202018-09-05%2012-31" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c76b84b0ecefdd99ac8d8207869d2ce27547565_2_690x319.gif" alt="Peek%202018-09-05%2012-31" data-base62-sha1="hL3ySoCrKpchACTnen76gzFa3XL" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c76b84b0ecefdd99ac8d8207869d2ce27547565_2_690x319.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c76b84b0ecefdd99ac8d8207869d2ce27547565_2_1035x478.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c76b84b0ecefdd99ac8d8207869d2ce27547565_2_1380x638.gif 2x" data-dominant-color="C0C1D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Peek%202018-09-05%2012-31</span><span class="informations">1436×664 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is this expected? Thanks</p>

---

## Post #2 by @lassoan (2018-09-05 16:57 UTC)

<p>This seems to be a bug. Can you give it a try and fix it? I think edit triggers need to be changed. It would be nicer to not show the editable part at all, though.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #3 by @phcerdan (2018-09-05 20:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3992">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you give it a try and fix it?</p>
</blockquote>
</aside>
<p>I would love it, but not much time right now. That’s why I opened an “issue” and not a PR directly.</p>

---

## Post #4 by @cpinter (2018-09-06 15:34 UTC)

<p>I spent quite a bit of time trying to figure out why the ItemIsEditable flag seems to have no effect in Subject hierarchy, as opposed to the regular qMRMLSceneModel, where it works.</p>
<p>This line is supposed to selectively enable the editable flag which is off by default, I confirmed it with debugging:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyModel.cxx#L777" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyModel.cxx#L777" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyModel.cxx#L777</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="767" style="counter-reset: li-counter 766 ;">
<li>
</li>
<li>if (!d-&gt;SubjectHierarchyNode)</li>
<li>  {</li>
<li>  qCritical() &lt;&lt; Q_FUNC_INFO &lt;&lt; ": Invalid subject hierarchy";</li>
<li>  return flags;</li>
<li>  }</li>
<li>
</li>
<li>// Name and transform columns are editable</li>
<li>if (column == this-&gt;nameColumn() || column == this-&gt;transformColumn())</li>
<li>  {</li>
<li class="selected">  flags |= Qt::ItemIsEditable;</li>
<li>  }</li>
<li>
</li>
<li>if (this-&gt;canBeAChild(itemID))</li>
<li>  {</li>
<li>  flags |= Qt::ItemIsDragEnabled;</li>
<li>  }</li>
<li>if (this-&gt;canBeAParent(itemID))</li>
<li>  {</li>
<li>  flags |= Qt::ItemIsDropEnabled;</li>
<li>  }</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
However it doesn’t matter what this flag says, the cell is always editable.</p>
<p>The same thing is happening here, but in this case the editable flag works as expected.<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSceneModel.cxx#L936" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSceneModel.cxx#L936" target="_blank">Slicer/Slicer/blob/master/Libs/MRML/Widgets/qMRMLSceneModel.cxx#L936</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="926" style="counter-reset: li-counter 925 ;">
<li>QFlags&lt;Qt::ItemFlag&gt; qMRMLSceneModel::nodeFlags(vtkMRMLNode* node, int column)const</li>
<li>{</li>
<li>QFlags&lt;Qt::ItemFlag&gt; flags = Qt::ItemIsEnabled</li>
<li>                           | Qt::ItemIsSelectable;</li>
<li>if (column == this-&gt;checkableColumn() &amp;&amp; node-&gt;GetSelectable())</li>
<li>  {</li>
<li>  flags = flags | Qt::ItemIsUserCheckable;</li>
<li>  }</li>
<li>if (column == this-&gt;nameColumn())</li>
<li>  {</li>
<li class="selected">  flags = flags | Qt::ItemIsEditable;</li>
<li>  }</li>
<li>if (this-&gt;canBeAChild(node))</li>
<li>  {</li>
<li>  flags = flags | Qt::ItemIsDragEnabled;</li>
<li>  }</li>
<li>if (this-&gt;canBeAParent(node))</li>
<li>  {</li>
<li>  flags = flags | Qt::ItemIsDropEnabled;</li>
<li>  }</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I implemented a workaround to prevent editing of the visibility and ID columns. I committed it, so the symptom you reported doesn’t come up any more. If anybody has any idea about the ItemIsEditable mistery, I’d be glad to hear it.</p>

---

## Post #5 by @cpinter (2018-09-06 17:05 UTC)

<p>We teamed up with Andras and with some painful Qt debugging we managed to find the reason why the flag was not used properly. I committed the real fix and removed the previous workaround.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/e5a5efbe6a9982ee0dc8f12c45a35e1c96f6e617" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    
<h4>
  <a href="https://github.com/Slicer/Slicer/commit/e5a5efbe6a9982ee0dc8f12c45a35e1c96f6e617" target="_blank">BUG: Proper fix for subject hierarchy editable bug</a>
</h4>

  <pre class="message" style="white-space: normal;">The column index was not propagated in the proxy model, so always the first column's flags were used. The previous workaround...</pre>

<div class="date">
  by <a href=""></a>
  on <a href="https://github.com/Slicer/Slicer/commit/e5a5efbe6a9982ee0dc8f12c45a35e1c96f6e617" target="_blank">05:04PM - 06 Sep 18</a>
</div>

<div class="github-commit-stats">
  changed <strong>4 files</strong>
  with <strong>2 additions</strong>
  and <strong>14 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @phcerdan (2018-09-06 18:13 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a>! <img src="https://emoji.discourse-cdn.com/twitter/sparkles.png?v=6" title=":sparkles:" class="emoji" alt=":sparkles:"></p>

---
