# Annotation in volume rendering

**Topic ID**: 19869
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/annotation-in-volume-rendering/19869

---

## Post #1 by @riep (2021-09-26 14:20 UTC)

<p>Hi everyone,<br>
I am working on a python scripted slicelet where I instantiate/modify several Markups planes and vtk cubes based on several QSpinBox values (volume rendering is active). The process on the signal onValueChanged begins to be long, and I observe side effects: double increment of the QSpinBox when I click a single time on the upper arrow, for instance.</p>
<p>To speed up the process:</p>
<ul>
<li>I disable rendering during process and resume it afterwards.</li>
<li>I modify markups in batch using StartModified() and EndModifed()</li>
</ul>
<p>Still, with these optimizations, I have sometimes the double QSpinBox increment. I would say the best way to definitely solve this problem is to parameter all the Markups in a separate thread, so that the slot function runs very fast (which is probably the best thing to do).<br>
But, I am in python… and I cannot find a proper way to do it… Would you have any advice or example I could adapt?</p>
<p>Cheers,<br>
Pierre</p>

---

## Post #2 by @riep (2021-09-26 17:02 UTC)

<p>Sorry, title is wrong…</p>

---

## Post #3 by @pieper (2021-09-26 19:08 UTC)

<p>In your <code>onValueChanged</code> slot you should be simply modifying the state of mrml nodes and this will trigger <code>requestRender</code> on any of the views where those are displayed.  The views compress these renders automatically and will only display periodically to maintain interactivity.  There shouldn’t be any double increment in this scenario.  I suggest avoiding the idea of threads and work on getting the event mechanism to work smoothly.  Perhaps you need to profile the computation to see where time is being spent.</p>

---

## Post #4 by @lassoan (2021-09-27 02:56 UTC)

<p>I observed double-step of the spinbox in completely unrelated, different use cases. Maybe the slow updates make it more visible. It would be nice if someone could investigate and fix it.</p>
<p>Volume rendering is normally very fast if you use the GPU volume rendering mode. This, combined with event compression should make all the renderings fluid. Maybe somewhere there is a force render call in the loop (that does not request a call but immediately renders).</p>
<p>You may also try pauseRender/resume Render to speed up updates (that prevents even force render calls to take effect).</p>

---

## Post #5 by @riep (2021-09-27 03:17 UTC)

<p>Hi Steve, Andras<br>
After modified event compression, things were visibly better, but still at some point where many markups are handled, double increment happen. We can find usefull info here <a href="https://bugreports.qt.io/browse/QTBUG-14259" class="inline-onebox" rel="noopener nofollow ugc">[QTBUG-14259] QSpinBox increments value multiple times on single mouse click when signal handlers are long-running - Qt Bug Tracker</a>. It seems that an internal timer of about 100ms trigger multiple signals if the slot function is longer than that. I could subclass QSpinBox and change this parameter but it is not possible as far as I know in python.</p>

---

## Post #6 by @lassoan (2021-09-27 03:25 UTC)

<p>No need to subclass QSpinBox. You can always just start a single-shot timer from the QSpinBox callback function and do the update when that timer elapses. See for example <a href="https://github.com/Slicer/Slicer/blob/1035355a9606d761fdb4de5b7f2e0a7b61455972/Modules/Scripted/DICOM/DICOM.py#L659">self.databaseRefreshRequestTimer in the DICOM browser</a>.</p>

---

## Post #7 by @riep (2021-09-27 10:26 UTC)

<p>Well, at first I wanted to avoid it, but it effectively solves the issue… Deal.<br>
Thanks both of you</p>

---
