---
topic_id: 17832
title: "Interactive Zoom Mouse Drag Direction"
date: 2021-05-27
url: https://discourse.slicer.org/t/17832
---

# Interactive Zoom Mouse Drag Direction

**Topic ID**: 17832
**Date**: 2021-05-27
**URL**: https://discourse.slicer.org/t/interactive-zoom-mouse-drag-direction/17832

---

## Post #1 by @spycolyf (2021-05-27 22:34 UTC)

<p>Currently, when you interactively zoom with the mouse, dragging the mouse up zooms out, and dragging down zooms in. I’m using my slicer module as an extension to a main app that zooms in the opposite direction. This confuses the users making them zoom in the wrong direction when in the slicer module UI.</p>
<p>Is there a way to make mouse drag up zoom in and mouse drag down zoom out?</p>
<p>Thanks</p>

---

## Post #2 by @jamesobutler (2021-05-27 22:52 UTC)

<p>Reviewing the current state of your <a href="https://github.com/KitwareMedical/SlicerQReads" rel="noopener nofollow ugc">SlicerQReads</a> custom app, it appears you are using a <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L15-L16" rel="noopener nofollow ugc">modified Slicer version</a> that has already swapped some zoom/pan functionality for mouse clicks by way of <a href="https://github.com/KitwareMedical/Slicer/commit/9acdfe886eac90326c3a7075d2ae91c846eecccd" rel="noopener nofollow ugc">this commit</a>. For inverting zoom in/out based on those mouse interactions I would suggest to look in those same files as that commit to then invert some more logic.</p>

---

## Post #4 by @spycolyf (2021-06-10 19:50 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p>Here’s how I attempted to reverse the zoom mouse drag direction…</p>
<ol>
<li>Changed the following code in vtkMRMLSliceIntersectionWidget.cxx (MouseWheelForward = Zoom In  /  MouseWheelBackward = Zoom out) …</li>
</ol>
<pre><code class="lang-auto">    this-&gt;SetEventTranslation(WidgetStateIdle, vtkCommand::MouseWheelForwardEvent, vtkEvent::ControlModifier, WidgetEventZoomInSlice); // DVP swapped Zoom In and Zoom Out
    this-&gt;SetEventTranslation(WidgetStateIdle, vtkCommand::MouseWheelBackwardEvent, vtkEvent::ControlModifier, WidgetEventZoomOutSlice); // DVP swapped Zoom In and Zoom Out
</code></pre>
<p>… And these lines in the PyObject *PyvtkMRMLSliceIntersectionWidget_ClassNew() method in vtkMRMLSliceIntersectionWidgetPython.cxx</p>
<pre><code>    { "WidgetEventZoomInSlice", vtkMRMLSliceIntersectionWidget::WidgetEventZoomOutSlice },
    { "WidgetEventZoomOutSlice", vtkMRMLSliceIntersectionWidget::WidgetEventZoomInSlice },
</code></pre>
<ol>
<li>Does this look correct?</li>
<li>Will this require a full rebuild?</li>
</ol>
<p>Thanks</p>

---

## Post #5 by @spycolyf (2021-06-21 17:29 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc93bffd574e944fde21215fe735608ccd9e2d4b.png" data-download-href="/uploads/short-url/vtjAYhpdylEhdYp8rJJ8uSCGXiP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc93bffd574e944fde21215fe735608ccd9e2d4b.png" alt="image" data-base62-sha1="vtjAYhpdylEhdYp8rJJ8uSCGXiP" width="690" height="222" data-dominant-color="ECEAE5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">740×239 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I made the above changes. I simply swapped the zoom in/out Signals slots so that in calls out and out calls in. For instance…</p>
<p>The WidgetEventZoom<strong>In</strong>Slice (Zoom In) signal calls the opposite (Zoom Out) function, vtkMRMLSliceIntersectionWidget::WidgetEventZoom<strong>Out</strong>Slice, and visa versa.</p>
<p>This is obviously the wrong way to do it, right?</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=12" title=":expressionless:" class="emoji only-emoji" alt=":expressionless:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2021-06-21 21:34 UTC)

<p>Changing the mapping like this is fine, but it would be a bit more future-proof if you did not change the Slicer core source code but instead you would run some Python code at startup to change the mapping. See example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-mouse-gestures-in-viewers">here</a>.</p>

---

## Post #7 by @spycolyf (2021-06-22 01:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, I disagree that it’s fine. I’d like your way much better if I can now figure out the correct parameters to use for the Zoom mouse drag and mouse wheel direction.</p>
<p>I’ll search for it. Thanks</p>

---

## Post #8 by @spycolyf (2021-06-23 15:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="17832" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Changing the mapping like this is fine, but it would be a bit more future-proof if you did not change the Slicer core source code but instead you would run some Python code at startup to change the mapping. See example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-mouse-gestures-in-viewers" rel="noopener nofollow ugc">here </a>.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>, I stayed up till past 2 in the morning trying to figure out the secret formula for changing the zoom in/out mouse drag direction using Python. Then I began to wonder why <a class="mention" href="/u/jcfr">@jcfr</a> did not use Python <a href="https://github.com/KitwareMedical/Slicer/commit/9acdfe886eac90326c3a7075d2ae91c846eecccd" rel="noopener nofollow ugc">here</a></p>
<p>Also, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>  commented <a href="https://discourse.slicer.org/t/interactive-zoom-mouse-drag-direction/17832/2">here</a>.</p>
<p>So why did my code <a href="https://discourse.slicer.org/t/interactive-zoom-mouse-drag-direction/17832/5">here</a> not work? Shouldn’t the mouse wheel at least be working in the opposite direction. Maybe I’m building incorrectly.</p>
<p>Should I continue to try to implement this in Python?</p>
<p>Thanks</p>

---

## Post #9 by @spycolyf (2021-06-28 14:32 UTC)

<p>Good morning <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a>,</p>
<p>Could someone please tell me why making these changes (swapping slots) would have no effect on mouse actions Zoom events after rebuilding?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc93bffd574e944fde21215fe735608ccd9e2d4b.png" data-download-href="/uploads/short-url/vtjAYhpdylEhdYp8rJJ8uSCGXiP.png?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc93bffd574e944fde21215fe735608ccd9e2d4b.png" alt="" data-base62-sha1="vtjAYhpdylEhdYp8rJJ8uSCGXiP" role="presentation" width="690" height="222" data-dominant-color="ECEAE5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">740×239 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I’m totally lost…</p>
<p>Thanks</p>

---

## Post #10 by @lassoan (2021-06-28 14:55 UTC)

<p>It should not be necessary to look into the generated Python wrapper. It is the exact translation of the corresponding header file to a Python object. It contains no additional information compared to the header file.</p>
<p>Changing the translation from GUI event to widget event in the constructor should work well. Changing it in Python is more flexible, but you need to do it for each view (and if you switch layout then you need to do it for the newly created view, too). Also make sure to remove the old mapping before trying to add a new one.</p>

---
