# How do you get the slice view your cursor is over?

**Topic ID**: 11542
**Date**: 2020-05-14
**URL**: https://discourse.slicer.org/t/how-do-you-get-the-slice-view-your-cursor-is-over/11542

---

## Post #1 by @mjg (2020-05-14 19:14 UTC)

<p>Hello,</p>
<p>How do you get the slice view (Red, Yellow, Green) your cursor is over?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2020-05-14 19:34 UTC)

<p>Hi - Something like this should work for you:</p>
<pre><code class="lang-auto">c = getNode("*Crosshair*")
c.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, lambda callee, event: print(c.GetCursorPositionXYZ([0]*3).GetName()))
</code></pre>
<p>Look in Modules/Scripted/DataProbe/DataProbe.py for more details.</p>

---

## Post #3 by @mjg (2020-05-14 19:51 UTC)

<p>Great, thank you so much!</p>

---
