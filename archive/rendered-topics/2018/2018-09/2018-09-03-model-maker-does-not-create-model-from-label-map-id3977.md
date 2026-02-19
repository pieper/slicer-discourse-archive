---
topic_id: 3977
title: "Model Maker Does Not Create Model From Label Map"
date: 2018-09-03
url: https://discourse.slicer.org/t/3977
---

# Model Maker does not create model from label map

**Topic ID**: 3977
**Date**: 2018-09-03
**URL**: https://discourse.slicer.org/t/model-maker-does-not-create-model-from-label-map/3977

---

## Post #1 by @chir.set (2018-09-03 16:40 UTC)

<p>Slicer built at commit af5f294fb on Linux using GCC 8.2, Python 2.7.15</p>
<p>I just noticed that Model Maker fails to create a model from a label map generated in Simple Growing Segmentation module with a few fiducial points. There’s only one label value.</p>
<p>The error log is <a href="https://pastebin.com/393zfDBv" rel="nofollow noopener">here</a>.</p>
<p>Thanks for considering.</p>

---

## Post #2 by @pieper (2018-09-03 19:32 UTC)

<p>Thanks for reporting this.</p>
<p>The error messages from the log:</p>
<pre><code class="lang-auto">vtkMRMLColorTableNode::SetColor: ERROR: can't set a colour if not a user defined colour table, reset the type first to User or File
</code></pre>
<p>Make me wonder if it’s related to this commit:</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/a694b040df3b44eb2dd3cc7d3b116d4bbac0e947" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    
<h4>
  <a href="https://github.com/Slicer/Slicer/commit/a694b040df3b44eb2dd3cc7d3b116d4bbac0e947" target="_blank">BUG: Fixed User color node reverting to File on scene reload</a>
</h4>

  <pre class="message" style="white-space: normal;">When a "User" color node type was saved to scene and then reloaded from scene
then its type was always set to...</pre>

<div class="date">
  by <a href=""></a>
  on <a href="https://github.com/Slicer/Slicer/commit/a694b040df3b44eb2dd3cc7d3b116d4bbac0e947" target="_blank">02:16PM - 29 Aug 18</a>
</div>

<div class="github-commit-stats">
  changed <strong>1 files</strong>
  with <strong>12 additions</strong>
  and <strong>1 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2018-09-03 19:49 UTC)

<p>It may be related. I can have a look at this later tonight or tomorrow.</p>

---

## Post #4 by @lassoan (2018-09-05 03:35 UTC)

<p>I’ve fixed the issue - it was a regression caused by the commit mentioned above. See details <a href="https://github.com/Slicer/Slicer/commit/c88ee87ef2c1864fc5d737ef3654b64c2998dd91">here</a>. Nightly builds that are downloaded on Thursday or later should work well.</p>

---

## Post #5 by @chir.set (2018-09-05 13:48 UTC)

<p>Model Maker now works as expected.</p>
<p>Thanks.</p>

---

## Post #6 by @lassoan (2018-09-06 05:28 UTC)

<p>By the way, are you still using Model Maker? Maybe you even use the legacy Editor module? I would recommend to switch to Segment editor, which makes Model Maker module irrelevant, since conversion between various representations happens automatically.</p>

---

## Post #7 by @chir.set (2018-09-06 08:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="3977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By the way, are you still using Model Maker?</p>
</blockquote>
</aside>
<p>My daily tool in vascular surgery for surgical planning is in fact Volume Rendering. When I need to create an arterial blood flow model from contrast enhanced CT scan, I use Simple Region Growing because I need only one segment and it’s fast.</p>
<p>I have thouroughly explored the new Segmentation Editor and it’s definitely an invaluable tool. Prior painting is rather time consuming however, and this does not suit my workflow.</p>
<p>For instance, with just one fiducial point in the aorta of the CT-Cardio sample dataset, Simple Region Growing does a fabulous job to isolate the arterial lumen as a label map.</p>
<p>Of course, this are many other cases where the new Segment Editor is best suited.</p>

---
