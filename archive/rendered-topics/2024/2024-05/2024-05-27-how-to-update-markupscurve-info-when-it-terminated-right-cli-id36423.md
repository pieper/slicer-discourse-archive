# How to update markupsCurve info when it terminated right-click end?

**Topic ID**: 36423
**Date**: 2024-05-27
**URL**: https://discourse.slicer.org/t/how-to-update-markupscurve-info-when-it-terminated-right-click-end/36423

---

## Post #1 by @park (2024-05-27 19:28 UTC)

<p>Hi all,</p>
<p>I am using the PointModifiedEvent to update curve information when drawing a curve.</p>
<p>When I end the curve drawing interaction with a right-click, I noticed that information from undefined parts remains.</p>
<p>To address this, I tried using the PointEndInteractionEvent, but I found that it is not called when ending the curve drawing with a right-click.</p>
<p>What can I do to solve this issue?</p>
<p>(I want to update only the information defined up to the last point when ending the curve drawing with a right-click</p>

---

## Post #2 by @park (2024-05-28 01:24 UTC)

<p>I found solution about this, through simply added ‘vtk.vtkCommand.ModifiedEvent’</p>
<p><code>self.addObserver(self.node, vtk.vtkCommand.ModifiedEvent, self.function)</code></p>

---
