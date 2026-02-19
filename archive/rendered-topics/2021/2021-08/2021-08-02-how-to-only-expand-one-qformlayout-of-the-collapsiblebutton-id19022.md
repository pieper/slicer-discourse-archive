---
topic_id: 19022
title: "How To Only Expand One Qformlayout Of The Collapsiblebutton"
date: 2021-08-02
url: https://discourse.slicer.org/t/19022
---

# How to only expand one QFormLayout of the CollapsibleButton which is operating?

**Topic ID**: 19022
**Date**: 2021-08-02
**URL**: https://discourse.slicer.org/t/how-to-only-expand-one-qformlayout-of-the-collapsiblebutton-which-is-operating/19022

---

## Post #1 by @jumbojing (2021-08-02 10:44 UTC)

<p>How to only expand one QFormLayout of the CollapsibleButton which is operating?</p>

---

## Post #2 by @jumbojing (2021-08-02 13:08 UTC)

<p>就像@lassoan做的很多插件那样,要用ctk.ctkWorkflow(), stepbystep 不错,可是参数的传递有点麻烦,可能我理解的不够啊,我问这个问题是想实现单一GUI实现我的插件,我觉得这个CollapsibleButton或者可以实现我的想法,哪位大神帮帮忙呢?</p>
<blockquote>
<p>Just like some plugins made by my great god <a class="mention" href="/u/lassoan">@lassoan</a>, you need to use ctk.ctkWorkflow(), stepbystep is good, but the parameter transfer is a bit troublesome, maybe I don’t understand enough, I asked this question to implement a single GUI to implement my plugin, I  I think this CollapsibleButton can perhaps realize my idea, which great god can help me?<br>
–from Google translator</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a>  <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #3 by @lassoan (2021-08-02 14:46 UTC)

<p>I would recommend placing the collapsible buttons into a <code>QButtonGroup</code> and enable <code>exclusive</code> property. See for example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/5b02b00ea3cb618c74e3e21485c8a0f61bc739a9/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L214-L215">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/5b02b00ea3cb618c74e3e21485c8a0f61bc739a9/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L214-L215" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5b02b00ea3cb618c74e3e21485c8a0f61bc739a9/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L214-L215" target="_blank" rel="noopener">Slicer/Slicer/blob/5b02b00ea3cb618c74e3e21485c8a0f61bc739a9/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L214-L215</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="214" style="counter-reset: li-counter 213 ;">
          <li>self.histogramBrushButtonGroup = qt.QButtonGroup()</li>
          <li>self.histogramBrushButtonGroup.setExclusive(True)</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I don’t particularly like <code>ctkWorkflowWidget</code> because it is complicated yet it is not powerful or flexible enough. The main problem is that the widget does not let users to jump to any step but forces them to click Back/Next many times, which can be frustrating. It is also quite complicated for developers to define all the state transitions; and it does not support hierarchical state machines, while in reality most workflows are like that (you have states and sub-states within them). In contrast, while using a set of collapsible buttons is not very sophisticated, it is very simple for both users and developers.</p>

---

## Post #4 by @jumbojing (2021-08-03 01:11 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c14f5d462c447f6028b88bf7bb00fbf21dce83e.gif" alt="5y0o0-d7e81" data-base62-sha1="8zvyqXZllzOuwHbAdKNPpfCEBf8" width="480" height="480" class="animated"></p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="19022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">self.histogramBrushButtonGroup = qt.QButtonGroup()
self.histogramBrushButtonGroup.setExclusive(True)
</code></pre>
</blockquote>
</aside>
<p>Great! Thank you very much!<br>
太棒了, 谢谢大神!!</p>

---
