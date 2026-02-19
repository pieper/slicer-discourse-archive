---
topic_id: 17356
title: "Change Axis Labels From Ras To Xyz Or Something Else Custom"
date: 2021-04-27
url: https://discourse.slicer.org/t/17356
---

# Change Axis Labels from RAS to XYZ (or something else custom)

**Topic ID**: 17356
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/change-axis-labels-from-ras-to-xyz-or-something-else-custom/17356

---

## Post #1 by @Jonathan_Lesage (2021-04-27 14:59 UTC)

<p>I was wondering if it is possible to change the RAS labels on the axes to XYZ? I am attempting to make using slicer more attractive to folks in the Nondestructive Testing world and being able to change RAS to XYZ will make the direction markers easier for us non-medical users more straightforward.</p>
<p>Many thanks!</p>

---

## Post #2 by @pieper (2021-04-27 18:44 UTC)

<p>Yes, that’s configurable.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; v = getNode('*View*')
&gt;&gt;&gt; v.SetAxisLabel(0, "Hello")
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/322c21c89f69f6f41015cfd80d4bb8ca6539aff1.png" alt="image" data-base62-sha1="79QqoSrs51MGpca4Vd9io1lvmP7" width="102" height="53"></p>

---

## Post #3 by @Jonathan_Lesage (2021-04-27 19:05 UTC)

<p>Hi pieper,</p>
<p>Thanks for the swift reply!</p>
<p>Is this also configurable for the axis arrows (see below):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea84c481524df384e4637fa1c7cd9bfc5bc4b9a.png" alt="image" data-base62-sha1="rcDimkV4OSNOysSOHUWNwPTEooq" width="145" height="167"></p>
<ul>
<li>Jon</li>
</ul>

---

## Post #4 by @Jonathan_Lesage (2021-04-27 19:06 UTC)

<p>… also on the slice views</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de32dc20f5bc32af36c4f5e5ff4fcf8cc92d6cce.png" alt="image" data-base62-sha1="vHEXQkhNOx47D4P2iZmPki0NmMu" width="339" height="228"></p>

---

## Post #5 by @pieper (2021-04-27 19:23 UTC)

<p>Yes, both Slice and ThreeD view nodes are subclasses of <code>vtkMRMLAbstractViewNode</code>.  Probably you should look at <a href="https://github.com/Punzo/SlicerAstro">SlicerAstro</a> to get ideas for removing the human-specific parts of the Slicer interface.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLAbstractViewNode.h#L268-L278" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLAbstractViewNode.h#L268-L278" target="_blank" rel="noopener">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/Core/vtkMRMLAbstractViewNode.h#L268-L278</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="268" style="counter-reset: li-counter 267 ;">
<li>/// Get/Set labels of coordinate system axes.</li>
<li>/// Order of labels: -X, +X, -Y, +Y, -Z, +Z.</li>
<li>/// Default: L, R, P, A, I, S</li>
<li>/// Note that these labels are used for display only (for example, showing organ specific</li>
<li>/// directions, such as "Temporal" and "Nasal" instead of "Left" and "Right").</li>
<li>/// Therefore, changing labels will not change orientation of displayed data in the view.</li>
<li>const char* GetAxisLabel(int labelIndex);</li>
<li>void SetAxisLabel(int labelIndex, const char* label);</li>
<li>
</li>
<li>/// Total number of coordinate system axis labels</li>
<li>static const int AxisLabelsCount;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Jonathan_Lesage (2021-04-28 15:54 UTC)

<p>Thank you so much! I will look into this.</p>

---
