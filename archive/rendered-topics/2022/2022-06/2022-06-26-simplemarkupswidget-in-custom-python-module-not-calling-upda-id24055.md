---
topic_id: 24055
title: "Simplemarkupswidget In Custom Python Module Not Calling Upda"
date: 2022-06-26
url: https://discourse.slicer.org/t/24055
---

# SimpleMarkupsWidget in custom python module not calling updateParameterNodeFromGUI()

**Topic ID**: 24055
**Date**: 2022-06-26
**URL**: https://discourse.slicer.org/t/simplemarkupswidget-in-custom-python-module-not-calling-updateparameternodefromgui/24055

---

## Post #1 by @koeglfryderyk (2022-06-26 22:47 UTC)

<p>In my Python Scripted Module I have an instance of a <em>SimpleMarkupsWidget</em>.</p>
<p>When I change the selected Point List (as depicted in the screenshot below) <code>updateParameterNodeFromGUI()</code> is not called:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ced195d285b6cb03dbd683d0b64292cbb7cb1651.jpeg" data-download-href="/uploads/short-url/tvBonyKk0yfBfFZ2P1k2G3MCj8B.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ced195d285b6cb03dbd683d0b64292cbb7cb1651_2_345x156.jpeg" alt="image" data-base62-sha1="tvBonyKk0yfBfFZ2P1k2G3MCj8B" width="345" height="156" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ced195d285b6cb03dbd683d0b64292cbb7cb1651_2_345x156.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ced195d285b6cb03dbd683d0b64292cbb7cb1651_2_517x234.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ced195d285b6cb03dbd683d0b64292cbb7cb1651_2_690x312.jpeg 2x" data-dominant-color="E0E4EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1018×462 82.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I already read in <a href="https://discourse.slicer.org/t/slicer-scripted-module-not-calling-updateparameternodefromgui-when-ui-is-updated/20122" class="inline-onebox">Slicer Scripted Module not calling updateParameterNodeFromGUI when UI is updated</a> that I have <em>“connect each GUI element with the callback to updateParameterNodeFromGUI”</em>, so I added this to <code>setup()</code>:</p>
<pre><code class="lang-auto">self.ui.SimpleMarkupsWidget.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
</code></pre>
<p>but this did not solve the problem.<br>
<br>
What am I missing? Does changing the Point List not trigger <code>currentNodeChanged()</code>?</p>

---

## Post #2 by @lassoan (2022-06-28 03:15 UTC)

<p><code>qSlicerSimpleMarkupsWidget</code> is not related to parameter nodes, so I’m not sure what <code>updateParameterNodeFromGUI</code> signal you expect it to emit. You can find what signals this widget emits in its <a href="http://apidocs.slicer.org/master/classqSlicerSimpleMarkupsWidget.html#Signals">documentation</a>.</p>

---

## Post #3 by @koeglfryderyk (2022-07-01 22:09 UTC)

<p>Thanks! I wanted to get the currently selected node, I managed to do this by connecting <code>markupsFiducialNodeChanged</code> (which I found in the documentation you linked) like so:</p>
<pre><code class="lang-auto">self.ui.SimpleMarkupsWidget.connect("markupsFiducialNodeChanged()", self.foo)
</code></pre>

---
