---
topic_id: 21013
title: "Event When Node Visibility Is Changed"
date: 2021-12-11
url: https://discourse.slicer.org/t/21013
---

# Event when node visibility is changed

**Topic ID**: 21013
**Date**: 2021-12-11
**URL**: https://discourse.slicer.org/t/event-when-node-visibility-is-changed/21013

---

## Post #1 by @keri (2021-12-11 02:41 UTC)

<p>Hi,</p>
<p>Can’t find an event that is triggered when node visibility is changed. Does <code>vtkMRMLDisplayableNode</code> triggers such event?</p>

---

## Post #2 by @Mik (2021-12-11 03:59 UTC)

<p>The vtkCommand::ModifiedEvent is envoked when you change visibility of a corresponding <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html" rel="noopener nofollow ugc">display node</a>.</p>
<p>For example</p>
<pre><code class="lang-auto">vtkMRMLDisplayNode* dispNode = scalarVolumeNode-&gt;GetDisplayNode(); // get vtkMRMLScalarVolumeDisplayNode
if (dispNode)
{
  dispNode-&gt;VisibilityOff();
  // do some work
  dispNode-&gt;VisibilityOn();
}
</code></pre>

---

## Post #3 by @keri (2021-12-11 14:28 UTC)

<p>Thank you for the help, I didn’t know that.</p>
<p>I guess if displayable node doesn’t have the display node then I can’t add an observer watches the visibility of my displayable node?</p>
<p>I just tried as you proposed and it seems that <code>displayableNode-&gt;GetDisplayNode();</code> sometimes returns <code>nullptr</code> even if the <code>displayableNode</code> is on the scene and it is shown (as in my case).</p>

---

## Post #4 by @lassoan (2021-12-11 15:25 UTC)

<aside class="quote no-group" data-username="keri" data-post="3" data-topic="21013">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I just tried as you proposed and it seems that <code>displayableNode-&gt;GetDisplayNode();</code> sometimes returns <code>nullptr</code> even if the <code>displayableNode</code> is on the scene and it is shown (as in my case).</p>
</blockquote>
</aside>
<p>A node cannot be displayed without a display node. It will not appear in any views.</p>
<aside class="quote no-group" data-username="keri" data-post="1" data-topic="21013">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Can’t find an event that is triggered when node visibility is changed. Does <code>vtkMRMLDisplayableNode</code> triggers such event?</p>
</blockquote>
</aside>
<p>You can observe the <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayableNode.html#a3b90d8fb984ac35e8ac919d6371a1ca1a8482bd3445607cf6ec6590466edd5436">vtkMRMLDisplayableNode::DisplayModifiedEvent</a> of the displayable node to get notified about display property changes (when a display node is added or modified).</p>

---

## Post #5 by @keri (2021-12-11 20:57 UTC)

<p>thank you, <code>vtkMRMLDisplayableNode::DisplayModifiedEvent</code> works fine for me</p>

---

## Post #6 by @keri (2021-12-25 02:14 UTC)

<p>I just figured out that if I try to <code>vtkMRMLScalarVolumeNode::SetDisplayVisibility(0)</code> (from both Python and C++) I’m still able to see that  volume node is displayed in 3D view and in Slice views.</p>
<p>Is there something special with scalar volume nodes? Or how can I manage the visibility of volume nodes?</p>

---

## Post #7 by @pieper (2021-12-29 04:36 UTC)

<p>Yes, volumes are a special case for historic reasons based on common uses and hardware/software limitations.  Slice views are handled by slice composite nodes (background and foreground cross-fading only) and 3D view is based on volume rendering nodes (only one could be visible at a time).  We might generalize this in the future and make volumes more like other displayables.</p>

---

## Post #8 by @lassoan (2022-01-02 02:06 UTC)

<p>I would just add that recent Slicer Preview Releases can render any number of volumes in 3D views. For correct 3D compositing you need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#panels-and-their-use">choose the experimental “VTK Multi-Volume” rendering method</a>.</p>

---
