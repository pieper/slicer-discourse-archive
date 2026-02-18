# Segment initialization

**Topic ID**: 10656
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/segment-initialization/10656

---

## Post #1 by @rprueckl (2020-03-12 09:32 UTC)

<p>I am currently writing a custom segment editor effect. There are two cases:</p>
<ul>
<li>When a segment already has contents (e.g. from a thresholding step) I would like to modify the segment based on those contents.</li>
<li>My effect also works on newly generated segments.</li>
</ul>
<p>The first case works. For the latter case, in the UI I do this:</p>
<ul>
<li>Make sure that the master volume is correctly set</li>
<li>Add a new Segment</li>
<li>Click the Apply button of my effect</li>
</ul>
<p>In code, I have:</p>
<pre><code class="lang-auto">segmentEditorNode = self.scriptedEffect.parameterSetNode()
segmentationNode = segmentEditorNode.GetSegmentationNode()
currentSegmentId = segmentEditorNode.GetSelectedSegmentID()
</code></pre>
<ul>
<li>Then, I call <code>self.scriptedEffect.defaultModifierLabelmap()</code>, which I thought would initialize the labelmap to the geometry of the master volume (via <code>bool qMRMLSegmentEditorWidgetPrivate::resetModifierLabelmapToDefault()</code>), however</li>
<li>the call to <code>segmentArray = slicer.util.arrayFromSegmentInternalBinaryLabelmap(segmentationNode, currentSegmentId)</code> fails with:</li>
</ul>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "D:/Misc/TestProjects/SegmentationTest/SegmentationTest/SegmentationTest/Lib/SegmentEditorEffect.py", line 152, in onApply
    segmentArray = slicer.util.arrayFromSegmentInternalBinaryLabelmap(segmentationNode, currentSegmentId)
  File "D:\Apps\Slicer 4.11.0-2020-02-26\bin\Python\slicer\util.py", line 1201, in arrayFromSegmentInternalBinaryLabelmap
    narray = vtk.util.numpy_support.vtk_to_numpy(vimage.GetPointData().GetScalars()).reshape(nshape)
  File "D:\Apps\Slicer 4.11.0-2020-02-26\bin\Lib\site-packages\vtkmodules\util\numpy_support.py", line 216, in vtk_to_numpy
    typ = vtk_array.GetDataType()
AttributeError: 'NoneType' object has no attribute 'GetDataType'
</code></pre>
<p>What do I have to do to determine whether a segment already has contents, and, if not, to correctly initialize it according to the geometry of the master volume?</p>
<p>Thanks again for your help!</p>

---

## Post #2 by @rprueckl (2020-03-13 16:37 UTC)

<p>I know now how the segmentation infrastructure is meant to be used. While the actual segment was still empty (and therefore caused the error), the defaultModifierLabelmap is meant as a “temporary labelmap” that can be used to store the intermediate results of an effect and has the extents of the master volume (or, at least of the ReferenceGeometryImage; however, I don’t know exactly the difference between those two yet).<br>
So, I manipulate the modifierLabelmap and then apply it with <code>self.scriptedEffect.modifySelectedSegmentByLabelmap(...)</code>. Easy.</p>
<p>However, what I found was, that the function <code>def arrayFromSegmentInternalBinaryLabelmap(segmentationNode, segmentId)</code><br>
does not return a numpy array with the same extents as the master volume, but with extents as large as the content of the segment, which confused me a bit. Moreover, an empty segment causes a crash (see first post) that could be avoided by a small check inside the method.</p>
<p>However, the issue is solved.</p>

---

## Post #3 by @lassoan (2020-03-13 17:43 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="2" data-topic="10656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>has the extents of the master volume (or, at least of the ReferenceGeometryImage; however, I don’t know exactly the difference between those two yet).</p>
</blockquote>
</aside>
<p>Having access to a <code>defaultModifierLabelmap</code> is a convenience feature, it is a blank image data initialized to the reference image geometry. Reference image geometry is determined automatically from the first selected master volume (or, if you created a segmentation from a model then from that).</p>
<aside class="quote no-group" data-username="rprueckl" data-post="2" data-topic="10656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>However, what I found was, that the function <code>def arrayFromSegmentInternalBinaryLabelmap(segmentationNode, segmentId)</code><br>
does not return a numpy array with the same extents as the master volume, but with extents as large as the content of the segment</p>
</blockquote>
</aside>
<p>It gives you low-level access to the internal labelmap - whatever it is. If you need simpler access in a specific volume’s geometry then you can export to a labelmap volume node.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="2" data-topic="10656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>Moreover, an empty segment causes a crash (see first post) that could be avoided by a small check inside the method.</p>
</blockquote>
</aside>
<p>It is not a crash but a nice and clean Python exception. It is a bit safer to raise an exception than just return an invalid value (if just an invalid value is returned then you may realize much later that something went wrong) and in the exception you can also give detailed explanation of what went wrong. In this case, the exception text is not that helpful, that should be fixed, but maybe we should also provide a bit higher level access functions to segmentations in numpy.</p>

---

## Post #4 by @rprueckl (2020-03-13 18:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="10656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It is not a crash but a nice and clean Python exception. It is a bit safer to raise an exception than just return an invalid value (if just an invalid value is returned then you may realize much later that something went wrong) and in the exception you can also give detailed explanation of what went wrong. In this case, the exception text is not that helpful, that should be fixed, but maybe we should also provide a bit higher level access functions to segmentations in numpy.</p>
</blockquote>
</aside>
<p>Sure it is an exception, sorry for the wrong terminology. Maybe I am simply used to the approach of of not using exceptions that Qt (and the rest of Slicer) follows, which I actually like a lot.<br>
If the segment is empty, I probably would have expected to receive an empty NumPy array from this method.<br>
Anyway, thanks for the additional information.</p>

---

## Post #5 by @lassoan (2020-03-13 23:25 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="4" data-topic="10656">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>I am simply used to the approach of of not using exceptions that Qt (and the rest of Slicer) follows</p>
</blockquote>
</aside>
<p>Exceptions are great in Python, but quite disruptive in C++ (it crashes the application if uncaught) and can easily put the application in an inconsistent state (it takes lots of extra effort to write exception-safe code, although with modern C++ it is becoming somewhat easier). So, we will keep using exceptions in Python, but I don’t think we will start using exceptions in C++ code in the near future.</p>

---
