# Can we navigate through markups control points with keyboard?

**Topic ID**: 20307
**Date**: 2021-10-22
**URL**: https://discourse.slicer.org/t/can-we-navigate-through-markups-control-points-with-keyboard/20307

---

## Post #1 by @chir.set (2021-10-22 20:37 UTC)

<p>I could not find keyboard shortcuts to move through next and previous markups control points. The right click menu items allow this but is more demanding than with keyboard. Is this possible with the keyboard ? All random key combinations I’ve tried failed.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2022-08-04 06:42 UTC)

<p>This is available in Markups module → Control Points section. If you set “Jump slices” to “centered” and click in the control point list then you can jump to the previous/next item using up/down arrow button.</p>
<p>It would be nice to add a keyboard shortcut that can be used anytime (e.g., by adding two new widget events to <code>vtkSlicerMarkupsWidget</code>, such  as <code>WidgetEventJumpToPreviousControlPoint</code> and <code>WidgetEventJumpToNextControlPoint</code> and add a keyboard shortcut for them). If you don’t have the time or expertise to implement it yourself then you can add a feature request in the bugtracker to keep track of it.</p>
<p>Until the feature is implemented in the Slicer core, you can add keyboard shortcuts to any action in Slicer (see examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#keyboard-shortcuts-and-mouse-gestures">script repository</a>).</p>

---
