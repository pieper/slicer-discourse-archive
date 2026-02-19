---
topic_id: 5706
title: "How To Enable Editin3Dviews Via Python Module Code"
date: 2019-02-08
url: https://discourse.slicer.org/t/5706
---

# How to Enable "Editin3DViews" via python module code

**Topic ID**: 5706
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/how-to-enable-editin3dviews-via-python-module-code/5706

---

## Post #1 by @coolsocks (2019-02-08 21:59 UTC)

<p>Hi I’m new to slicer development and I wanted to update my code to the 4.10 version. I just had a question of how to enable the “edit in 3D view” section using the qMRMLSegmentEditorWidget?</p>
<p>I got to this point:<br>
self.segmentEditorWidget.setActiveEffectByName(“Erase”)<br>
effect = self.segmentEditorWidget.activeEffect()<br>
effect.setParameter(“Editin3DViews”,“1”)<br>
effect.self().onApply()<br>
But whenever I attempt to erase, it will only rotate/displace the volume.</p>
<p>Thanks</p>

---

## Post #2 by @jamesobutler (2019-02-08 22:25 UTC)

<p>Hi Amanda,</p>
<p>I see you have posted this twice in less than an hour. Please, keep it contained to one post and someone on the forum will respond to you likely within the day.</p><aside class="quote" data-post="2" data-topic="5701">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coolsocks/48/3299_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/enable-edit-in-3d-view-via-qmrmlsegmenteditorwidget/5701/2">Enable "Edit in 3D View" Via qMRMLSegmentEditorWidget</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I got to this point: 
self.segmentEditorWidget.setActiveEffectByName(“Erase”) 
effect = self.segmentEditorWidget.activeEffect() 
effect.setParameter(“Editin3DViews”,“1”) 
effect.self().onApply() 
But whenever I attempt to erase, it will only rotate/displace the volume.
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2019-02-08 23:06 UTC)

<p>Parameter names are case sensitive (<code>EditIn3DViews</code> is correct, <code>Editin3DViews</code> is incorrect). Also, this parameter is shared between paint and erase effects, therefore you need to set it using <code>setCommonParameter</code>.</p>
<p>So, you need to change</p>
<pre><code>effect.setParameter("Editin3DViews","1")
</code></pre>
<p>to</p>
<pre><code>effect.setCommonParameter("EditIn3DViews","1")</code></pre>

---

## Post #4 by @coolsocks (2019-02-09 07:12 UTC)

<p>Sorry about that, will keep that in mind for next time</p>

---
