# Paring a needle model with a vtktransform through python code

**Topic ID**: 2827
**Date**: 2018-05-16
**URL**: https://discourse.slicer.org/t/paring-a-needle-model-with-a-vtktransform-through-python-code/2827

---

## Post #1 by @lgroves (2018-05-16 15:52 UTC)

<p>I am trying to pair an already existing needle model with tracking data streaming in through the Plus server to view the needle in the 3D view. Currently I am performing this through using the data module and dragging my needle model on top of the appropriate transform, however I would like to code this to happen automatically as part of my module.</p>
<p>Any help is appreciated!</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2018-05-16 20:15 UTC)

<p>You can call <code>transformableNode.SetAndObserveTransformNodeID(transformNode.GetID())</code>. See more examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Examples">Transforms module documentation</a>.</p>

---
