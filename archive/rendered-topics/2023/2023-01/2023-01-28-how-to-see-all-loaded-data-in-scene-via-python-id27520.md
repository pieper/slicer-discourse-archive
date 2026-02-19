---
topic_id: 27520
title: "How To See All Loaded Data In Scene Via Python"
date: 2023-01-28
url: https://discourse.slicer.org/t/27520
---

# How to see all loaded data in Scene via Python

**Topic ID**: 27520
**Date**: 2023-01-28
**URL**: https://discourse.slicer.org/t/how-to-see-all-loaded-data-in-scene-via-python/27520

---

## Post #1 by @michabermoy (2023-01-28 21:32 UTC)

<p>How can I obtain all loaded data in the scene via python, if such data exists? I need to create a conditional that only runs a certain function if the scene already has some data, otherwise the user is prompted to load data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfef96e83335011b85ae85dc5f7f4e2e07224b4a.png" data-download-href="/uploads/short-url/vX1Ne9BiS4OHXgqb5tZFHMbxJUu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfef96e83335011b85ae85dc5f7f4e2e07224b4a_2_329x500.png" alt="image" data-base62-sha1="vX1Ne9BiS4OHXgqb5tZFHMbxJUu" width="329" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfef96e83335011b85ae85dc5f7f4e2e07224b4a_2_329x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfef96e83335011b85ae85dc5f7f4e2e07224b4a_2_493x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfef96e83335011b85ae85dc5f7f4e2e07224b4a_2_658x1000.png 2x" data-dominant-color="F1F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">908×1378 60.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also what are the different data types that can be loaded by the user? For example, scene, volume, sequence, and transforms can be loaded by the user via the slicer.util.load… function, but I do not know all the possible types/functions</p>

---

## Post #2 by @ebrahim (2023-01-29 16:15 UTC)

<aside class="quote no-group" data-username="michabermoy" data-post="1" data-topic="27520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michabermoy/48/16003_2.png" class="avatar"> michabermoy:</div>
<blockquote>
<p>Also what are the different data types that can be loaded by the user? For example, scene, volume, sequence, and transforms can be loaded by the user via the slicer.util.load… function, but I do not know all the possible types/functions</p>
</blockquote>
</aside>
<p>See the inheritance diagram at the top of this page which shows all the descendants of <code>vtkMRMLStorableNode</code>:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLStorableNode.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classvtkMRMLStorableNode.html</a><br>
There are other nodes that can be in a scene that serve various purposes, but I guess the storable nodes are “data types” that could be saved/loaded.<br>
Another possibility is to look at all <code>vtkMRMLDisplayableNode</code>s:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLDisplayableNode.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classvtkMRMLDisplayableNode.html</a><br>
which includes only the ones the user can “see” in the scene.<br>
To summarize: Markups, models, volumes, segmentations, and transforms.</p>
<aside class="quote no-group" data-username="michabermoy" data-post="1" data-topic="27520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michabermoy/48/16003_2.png" class="avatar"> michabermoy:</div>
<blockquote>
<p>How can I obtain all loaded data in the scene via python, if such data exists? I need to create a conditional that only runs a certain function if the scene already has some data, otherwise the user is prompted to load data.</p>
</blockquote>
</aside>
<p>For checking if the subject hierarchy (the list displayed in your screenshot) has any items in it, I think this works:</p>
<pre data-code-wrap="py"><code class="lang-py">slicer.mrmlScene.GetSubjectHierarchyNode().GetNumberOfItems()
</code></pre>
<p>For listing all nodes in the scene of a certain type (which includes many that don’t show up in the subject hierarchy) you can do something like</p>
<pre data-code-wrap="py"><code class="lang-py">list(slicer.mrmlScene.GetNodesByClass('vtkMRMLDisplayableNode'))
</code></pre>
<p>for example to get a list of all the <code>vtkMRMLDisplayableNode</code>s</p>

---

## Post #3 by @RafaelPalomar (2023-02-01 11:37 UTC)

<aside class="quote no-group" data-username="michabermoy" data-post="1" data-topic="27520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michabermoy/48/16003_2.png" class="avatar"> michabermoy:</div>
<blockquote>
<p>How can I obtain all loaded data in the scene via python, if such data exists? I need to create a conditional that only runs a certain function if the scene already has some data, otherwise the user is prompted to load data.</p>
</blockquote>
</aside>
<p>For this use case, I would rather observe the MRML scene for new nodes added and react to the first addition (you can also filter the type of nodes you want to consider), then you can remove the observer or simply ignore subsequent event triggers.</p>
<aside class="quote no-group" data-username="michabermoy" data-post="1" data-topic="27520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michabermoy/48/16003_2.png" class="avatar"> michabermoy:</div>
<blockquote>
<p>Also what are the different data types that can be loaded by the user? For example, scene, volume, sequence, and transforms can be loaded by the user via the slicer.util.load… function, but I do not know all the possible types/functions</p>
</blockquote>
</aside>
<p>There are a lot of data types that the user can load, and this also depends on the extensions installed by the user. <code>slicer.util.load..</code> are utility functions to load the most commonly used types, but they don’t represent the whole extent of possibilities. In the approach described (observing the MRML Scene) above you will be “notified” for any data type loaded, even data supported by other modules.</p>

---
