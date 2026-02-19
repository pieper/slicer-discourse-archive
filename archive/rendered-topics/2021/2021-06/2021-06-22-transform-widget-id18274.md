---
topic_id: 18274
title: "Transform Widget"
date: 2021-06-22
url: https://discourse.slicer.org/t/18274
---

# Transform Widget

**Topic ID**: 18274
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/transform-widget/18274

---

## Post #1 by @Loc_Tran (2021-06-22 17:46 UTC)

<p>Hello.</p>
<p>I would like to display transformation fields and manipulate some visualization features of the fields such as spacing, scale factor. I tried writing a program to do that based on <a href="https://apidocs.slicer.org/master/classqMRMLTransformDisplayNodeWidget.html#a17c6de69a1f76958684f6b90e94e22bd" rel="noopener nofollow ugc">this document</a> but it does not work.</p>
<p>Below is my code:<br>
<span class="hashtag-raw">#get</span> a field node<br>
field = getNode(“Transform_field”)</p>
<h1><a name="p-61772-get-the-transforms-widget-1" class="anchor" href="#p-61772-get-the-transforms-widget-1" aria-label="Heading link"></a>get the transforms widget</h1>
<p>displacement_widget = slicer.qMRMLTransformDisplayNodeWidget()<br>
displacement_widget.setMRMLTransformNode(field)<br>
displacement_widget.setVisibility(True)<br>
displacement_widget.setVisibility2d(True)<br>
<span class="hashtag-raw">#set</span> spacing and scale factors<br>
displacement_widget.setGlyphSpacingMm(3)<br>
displacement_widget.setGlyphScalePercent(250)</p>
<p>I realized that when I check and uncheck the “visible” or “visible in slice view” checkbox inside visualization section, my program works. It would be great if you could correct my code.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-06-25 20:31 UTC)

<p>You created a GUI widget that you can use to edit properties of a transform display node. The widget is useful if you want to allow users to modify transform display properties in your module’s GUI. It probably does not work if you don’t set the MRML scene in the widget and/or the widget is not displayed.</p>
<p>If you just want to modify a transform’s appearance then you can edit the <a href="https://apidocs.slicer.org/master/classvtkMRMLTransformDisplayNode.html">transform display node</a> properties directly:</p>
<pre><code class="lang-python">transformNode = getNode('LinearTransform_3')
transformNode.CreateDefaultDisplayNodes()
transformDisplayNode = transformNode.GetDisplayNode()
transformDisplayNode.SetVisibility(True)
transformDisplayNode.SetVisibility2D(True)
transformDisplayNode.SetAndObserveRegionNode(getNode('MRHead'))
</code></pre>

---

## Post #3 by @Loc_Tran (2021-06-28 20:26 UTC)

<p>Thank you so much! It works perfectly</p>

---
