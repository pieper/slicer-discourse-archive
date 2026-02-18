# Extract centerline Python scripting

**Topic ID**: 21275
**Date**: 2021-12-30
**URL**: https://discourse.slicer.org/t/extract-centerline-python-scripting/21275

---

## Post #1 by @bserrano (2021-12-30 12:28 UTC)

<p>Hi,</p>
<p>I am trying to automatize the process of extracting a centerline.<br>
I want an automatic configuration that looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea204f3dd0b9a634922bf229e5a3442ae10e0e9.png" data-download-href="/uploads/short-url/klMVocJHuEQlwIOKIuz3nD3aTZ7.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ea204f3dd0b9a634922bf229e5a3442ae10e0e9_2_349x499.png" alt="imagen" data-base62-sha1="klMVocJHuEQlwIOKIuz3nD3aTZ7" width="349" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ea204f3dd0b9a634922bf229e5a3442ae10e0e9_2_349x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ea204f3dd0b9a634922bf229e5a3442ae10e0e9_2_523x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea204f3dd0b9a634922bf229e5a3442ae10e0e9.png 2x" data-dominant-color="3C3C3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">540×773 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have some lines of code based on:<br>
import ExtractCenterline</p>
<p>slicer.util.selectModule(‘ExtractCenterline’)<br>
ec = ExtractCenterline.ExtractCenterlineLogic()<br>
s = segmentationNode.GetSegmentation()<br>
ss = s.GetSegment(s.GetSegmentIdBySegmentName(“aortaCompleta”)).GetRepresentation(‘Closed surface’)<br>
fids = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsFiducialNode”)<br>
centerlinePolyData,voronoiDiagramPolyData = ec.extractCenterline(ss, fids)<br>
But I can’t find the centerline after this</p>
<p>I also tryied to modify the ParameterNode<br>
ec.getParameterNode().SetParameter(“InputSurface”, segmentID)<br>
but I don’t know how to see changes on GUI and modify the “Tree” section.</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @chir.set (2021-12-30 14:48 UTC)

<p>You seem to mix up things here.</p>
<p>\1. If you wish to work with the logic class of ‘ExtractCenterline’ module, <a href="https://discourse.slicer.org/t/automatic-centerline/14829/22">this</a> post is very instructive. The logic class won’t modify the UI in itself.</p>
<p>\2. If you wish to work with the ‘ExtractCenterline’ module’s GUI, you can access all UI widgets this way :</p>
<pre><code class="lang-auto">ecWidgetRepresentation = slicer.modules.extractcenterline.widgetRepresentation()
ecUI = ecWidgetRepresentation.ui
</code></pre>
<p>For example, to get a handle to the output curve combobox, you would use <em>ecUI.outputCenterlineCurveSelector</em>.</p>

---

## Post #3 by @bserrano (2021-12-31 08:52 UTC)

<p>Hi,</p>
<p>This gives me an error</p>
<pre><code class="lang-auto">ecWidgetRepresentation = slicer.modules.extractcenterline.widgetRepresentation()
ecUI = ecWidgetRepresentation.ui
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/023e214afc48cb46397f699437162095271b896c.png" alt="imagen" data-base62-sha1="jQ4deMxi6gUlKRYwdWYZfV6lm4" width="653" height="86"></p>
<p>But I tryied with this and seems to work fine</p>
<pre><code class="lang-auto">ecUI = slicer.modules.ExtractCenterlineWidget.ui
</code></pre>
<p>However I don’t know how to change options. Could you give me an example of how to change (for instance) the input surface? I am quite noob with slicer.</p>
<p>Thanks</p>

---

## Post #4 by @chir.set (2021-12-31 11:16 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="3" data-topic="21275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>This gives me an error</p>
<pre><code class="lang-auto">ecWidgetRepresentation = slicer.modules.extractcenterline.widgetRepresentation()
ecUI = ecWidgetRepresentation.ui
</code></pre>
</blockquote>
</aside>
<p>You’re right, it should be :<br>
<code>ecUI = ecWidgetRepresentation.self().ui</code></p>
<p>As for <em>slicer.modules.ExtractCenterlineWidget.ui</em>, <em>slicer.modules.ExtractCenterlineWidget</em> is available only if you have shown the ‘ExtractCenterline’ module once, or if you have run <em>slicer.modules.extractcenterline.widgetRepresentation()</em> once. That is, the widget representation needs to be created.</p>
<aside class="quote no-group" data-username="bserrano" data-post="3" data-topic="21275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>Could you give me an example of how to change (for instance) the input surface?</p>
</blockquote>
</aside>
<pre><code class="lang-auto">segmentation = slicer.util.getNode("Segmentation")
ecUI.inputSurfaceSelector.setCurrentNode(segmentation)
</code></pre>
<p>In a real application, you won’t use getNode() of course. Either you create a node, or you get it from a UI widget following its API.</p>

---
