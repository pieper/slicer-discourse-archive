---
topic_id: 17265
title: "Access 3D Renderer For Multiple View"
date: 2021-04-23
url: https://discourse.slicer.org/t/17265
---

# Access 3d renderer for multiple view

**Topic ID**: 17265
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/access-3d-renderer-for-multiple-view/17265

---

## Post #1 by @pj-rit (2021-04-23 03:01 UTC)

<p>Hi, I am wondering if it is possible to access the renderer that is associated with a view node. I am currently grabbing the view node using</p>
<p><code>slicer.util.getFirstNodeByName('View1')</code>, but I don’t know know how to grab the renderer that is associated with that view or rather what threeDwidget the view belongs to.</p>
<p>I am creating a script where more than one 3d views can be created, but I need to keep track of the first one and it seems that I can’t just assume that idx = 0 in</p>
<blockquote>
<p>slicer.app.layoutmanager().threeDWidget(idx).threeDView().renderWindow().GetRenderers().GetFirstRenderer()</p>
</blockquote>
<p>I am using the imagedata from one of the 3d views to capture the image and create an AR overlay in the slice view.<br>
Thank you for any help.<br>
Peter</p>

---

## Post #2 by @pieper (2021-04-23 21:26 UTC)

<p>You should be able to iterate over the threeDWidgets and find the one that matches your view node with this call:</p>
<pre><code class="lang-auto">slicer.app.layoutManager().threeDWidget(0).threeDView().mrmlViewNode()
</code></pre>

---

## Post #3 by @pj-rit (2021-04-26 15:26 UTC)

<p>Thanks, I think that makes sense. I hadn’t thought of doing it that way, because I was thinking there was a direct reference between the two</p>

---

## Post #4 by @pieper (2021-04-26 20:00 UTC)

<aside class="quote no-group" data-username="pj-rit" data-post="3" data-topic="17265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pj-rit/48/10760_2.png" class="avatar"> pj-rit:</div>
<blockquote>
<p>I was thinking there was a direct reference between the two</p>
</blockquote>
</aside>
<p>You’re right, this is cleaner:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; v = getNode('*View*')
&gt;&gt;&gt; v
(MRMLCore.vtkMRMLViewNode)0x253dc1648
&gt;&gt;&gt; slicer.app.layoutManager().viewWidget(v)
qMRMLThreeDWidget(0x7fce8970bfd0, name="ThreeDWidget1") 
</code></pre>

---

## Post #5 by @pj-rit (2021-05-10 14:18 UTC)

<p>Thanks,<br>
That’s so much easier to use.</p>

---
