# Dual view with the segment editor

**Topic ID**: 1413
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/dual-view-with-the-segment-editor/1413

---

## Post #1 by @muratmaga (2017-11-09 05:52 UTC)

<p>Hi,</p>
<p>I am using scissors tool a lot to trim unwanted data. I do this in the side view of the specimen, but I also need to see how the specimen looks front on, so that I do not cut into it at an angle. I can turn on the dual 3D, but I can’t find a way to link them so view1 e.g., shows A view, while view2 show the Left view, and rotating in the volume in either of the views updates the other.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d819228c889a93e2dc8bbb127263ad109f67b513.jpeg" data-download-href="/uploads/short-url/uPGZ4olULMKwJngKQdGuwwkeubx.jpg?dl=1" title="Capture"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d819228c889a93e2dc8bbb127263ad109f67b513_2_590x500.jpg" alt="Capture" data-base62-sha1="uPGZ4olULMKwJngKQdGuwwkeubx" width="590" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d819228c889a93e2dc8bbb127263ad109f67b513_2_590x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d819228c889a93e2dc8bbb127263ad109f67b513_2_885x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d819228c889a93e2dc8bbb127263ad109f67b513_2_1180x1000.jpg 2x" data-dominant-color="B3B8BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1662×1407 514 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is it possible to do this?</p>

---

## Post #2 by @lassoan (2017-11-09 14:50 UTC)

<p>I think the closest you can get to this without writing any script is the following:</p>
<ul>
<li>Switch to dual 3D view (this makes sure you have 2 camera nodes), rotate the camera views to be orthogonal</li>
<li>In Transforms module, create a transform and apply it to all nodes named “Default Scene Camera” (there should be at least two)</li>
<li>Move the Rotation / IS slider to rotate the camera views in sync.</li>
</ul>
<p>To make rotation available while you are in another module, type these into the python console to show a widget where you can adjust IS rotation:</p>
<pre><code>sliders=slicer.qMRMLTransformSliders()
sliders.setMRMLScene(slicer.mrmlScene)
sliders.TypeOfTransform = slicer.qMRMLTransformSliders.ROTATION
sliders.TypeOfTransform = slicer.qMRMLTransformSliders.TRANSLATION
sliders.TypeOfTransform = slicer.qMRMLTransformSliders.ROTATION
sliders.setMRMLTransformNode(getNode('LinearTransform_3'))
sliders.show()</code></pre>

---

## Post #3 by @mukatyz (2018-11-18 15:16 UTC)

<p>Hi,</p>
<p>how i can make this script generic for any transform from python console. instead of getNode(‘LinearTransform_3’)</p>

---

## Post #4 by @lassoan (2018-11-18 15:24 UTC)

<p>Typically you create the transform node, so you don’t need to call <code>getNode</code>. If you want the user to select it then you typically add a <code>slicer.qMRMLNodeComboBox()</code> to your GUI (or you get the transform node associated with another node using <code>someNode.GetParentTransformNode()</code>.</p>

---
