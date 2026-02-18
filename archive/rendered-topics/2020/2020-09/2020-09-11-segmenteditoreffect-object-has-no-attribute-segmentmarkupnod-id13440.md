# 'SegmentEditorEffect' object has no attribute 'segmentMarkupNode'

**Topic ID**: 13440
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/segmenteditoreffect-object-has-no-attribute-segmentmarkupnode/13440

---

## Post #1 by @Anand_Mulay (2020-09-11 14:25 UTC)

<p>I’m trying to use Nvidia Ai using the sample script (<a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5" rel="nofollow noopener">https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5</a>)<br>
First I got an internal error for the study which is running successfully in the editor but not with the script, so I updated the slicer to the latest nightly build, then I got this error.</p>
<pre><code>slicer.util.updateMarkupsControlPointsFromArray(effect.self().segmentMarkupNode, inputPoints)

AttributeError: 'SegmentEditorEffect' object has no attribute 'segmentMarkupNode'
</code></pre>
<p>I tried to uninstall and install the MarkupTomodel extension.<br>
any changes in SegmentEditorEffect class for the latest nightly build??</p>

---

## Post #2 by @lassoan (2020-09-11 20:14 UTC)

<p>For some reason, NVidia developers renamed <code>segmentMarkupNode</code> to <code>annotationFiducialNode</code>. Make the change in the script accordingly and let me know if it fixed the issue.</p>

---

## Post #3 by @Anand_Mulay (2020-09-14 08:25 UTC)

<p>Thanks, that error is gone now.<br>
But that unexpected error window came up,  <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"><br>
let me share the log file and traceback window error message with you,<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://textuploader.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://textuploader.com/1p063" target="_blank" rel="noopener nofollow ugc">textuploader.com - Untitled Post</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="20" height="20">

<h3><a href="https://textuploader.com/1p063" target="_blank" rel="noopener nofollow ugc">Untitled Post</a></h3>

<p>[DEBUG][Qt] 14.09.2020 13:32:27 [] (unknown:0) - Session start time .......: 2020-09-14 13:32:27
[DEBUG][Qt] 14.09.20...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://textuploader.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://textuploader.com/1p06b" target="_blank" rel="noopener nofollow ugc">textuploader.com - Untitled Post</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="20" height="20">

<h3><a href="https://textuploader.com/1p06b" target="_blank" rel="noopener nofollow ugc">Untitled Post</a></h3>

<p>Traceback (most recent call last):
  File "C:/Users/anand.mulay/AppData/Roaming/NA-MIC/Extensions-29363/NvidiaAI...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>the same study works in the editor though.</p>

---

## Post #4 by @Anand_Mulay (2020-09-17 08:54 UTC)

<p>hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Am i missing somthing here? <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"><br>
i’m trying but not geting the result , same error message all time.</p>

---

## Post #5 by @lassoan (2020-09-18 00:03 UTC)

<p>NVidia develepers changed the module so that input points are now cleared when a model is selected the first time, so now you need to select the model before you set the points. I’ve updated the example gist accordingly.</p>

---
