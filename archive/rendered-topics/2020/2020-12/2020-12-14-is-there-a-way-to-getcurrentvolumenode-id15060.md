---
topic_id: 15060
title: "Is There A Way To Getcurrentvolumenode"
date: 2020-12-14
url: https://discourse.slicer.org/t/15060
---

# Is there a way to getCurrentVolumeNode?

**Topic ID**: 15060
**Date**: 2020-12-14
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-getcurrentvolumenode/15060

---

## Post #1 by @Justin (2020-12-14 21:10 UTC)

<p>Dear all,<br>
I’ve been using Slicer for a time now and am really happy with it.<br>
However, there is one thing I have not found out.</p>
<p>When I’m using a script right now, I manually change the volumeNode name to a certain name.<br>
I always only load one volumenode, never two scans at a time.</p>
<p>My code then uses</p>
<p><code>masterVolumeNode = getNode('name')</code></p>
<p>to get the volumeNode by name.</p>
<p>However, is there a way to let slicer get the currently loaded node? Independent of the name? (by selecting the only available volume node in the hierarchy?)<br>
Something like</p>
<p><code>masterVolumeNode = getActiveNode()</code></p>
<p>In example scripts I always see examples that manually get volumeNode by name, so I wonder whether it is available at all.</p>
<p>Thanks a lot in advance!<br>
Best,<br>
Justin</p>

---

## Post #2 by @lassoan (2020-12-14 21:22 UTC)

<p>If you have only a single volume loaded then you can use <code>slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')</code>.</p>
<p>If you work with multiple nodes (which is most of the time) then you add node selectors to your module GUI to let the user choose inputs and outputs.</p>

---

## Post #3 by @Justin (2020-12-15 10:36 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="15060">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.mrmlScene.GetFirstNodeByClass(‘vtkMRMLScalarVolumeNode’)</p>
</blockquote>
</aside>
<p>Thanks, that’s indeed the solution to my problem!</p>

---
