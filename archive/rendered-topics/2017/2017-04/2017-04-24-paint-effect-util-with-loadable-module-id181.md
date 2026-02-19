---
topic_id: 181
title: "Paint Effect Util With Loadable Module"
date: 2017-04-24
url: https://discourse.slicer.org/t/181
---

# Paint Effect Util with loadable module

**Topic ID**: 181
**Date**: 2017-04-24
**URL**: https://discourse.slicer.org/t/paint-effect-util-with-loadable-module/181

---

## Post #1 by @basti (2017-04-24 15:04 UTC)

<p>I’m new with slicer and I’m trying to build a module which includes the paint effect. Right now I have two problems:</p>
<ul>
<li>
<p>I don’t know how to create and link a label map. The code below just works when I create a Label Map using the Editor Module.</p>
</li>
<li>
<p>When I change the radius of the sphere it creates a new circle, but on painting the size stays the same.</p>
<pre><code>  # TODO: Create/Link Labelmap!!
  editUtil = EditorLib.EditUtil.EditUtil()
  parameterNode = editUtil.getParameterNode()
  lm = slicer.app.layoutManager()
  paintEffect = EditorLib.PaintEffectOptions()
  paintEffect.setMRMLDefaults()
  parameterNode.SetParameter('PaintEffect,radius', str(sphereSize))
  parameterNode.SetParameter('PaintEffect,sphere', '1')
  sliceWidget = lm.sliceWidget('Red')
  paintTool = EditorLib.PaintEffectTool(sliceWidget)
  sliceWidget = lm.sliceWidget('Green')
  paintTool = EditorLib.PaintEffectTool(sliceWidget)
  sliceWidget = lm.sliceWidget('Yellow')
  paintTool = EditorLib.PaintEffectTool(sliceWidget)
  editUtil.setLabel(3)
</code></pre>
</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/bf5c4cef2e5e467f2993f5325a8b11850f3cb600.jpg" width="657" height="379"></p>

---

## Post #2 by @pieper (2017-04-24 15:28 UTC)

<p>Hi - we’ve moved active development to the Segment Editor module, particularly for segmentation tools embedding inside other modules.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentEditor" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentEditor</a></p>
<p>I think <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/cpinter">@cpinter</a> or <a class="mention" href="/u/che85">@che85</a> can point to some examples of how to do the embedding.</p>

---

## Post #3 by @lassoan (2017-04-24 15:40 UTC)

<p>The simplest embedding example is the SegmentEditor module itself.<br>
For a more complex example, have a look at <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting.py">https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting.py</a>.</p>
<p>You can customize which effects are displayed in what order. You can also hide node selectors, etc.</p>

---
