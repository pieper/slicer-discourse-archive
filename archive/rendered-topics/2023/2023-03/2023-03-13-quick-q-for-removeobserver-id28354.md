# Quick Q for RemoveObserver

**Topic ID**: 28354
**Date**: 2023-03-13
**URL**: https://discourse.slicer.org/t/quick-q-for-removeobserver/28354

---

## Post #1 by @aiden.zhu (2023-03-13 18:33 UTC)

<p>Hi all,<br>
quick question about “RemoveObserver”==&gt;<br>
After I did the following to add one observer<br>
“”"<br>
crosshairNode=slicer.util.getNode(“Crosshair”)<br>
crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)<br>
“”"<br>
I did try<br>
crosshairNode.RemoveObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent)<br>
but no effect from this line.</p>
<p>how to remove the observer?</p>

---

## Post #2 by @smrolfe (2023-03-13 19:46 UTC)

<p>You can remove an observer using the tag generated when the observer was added. See the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-mouse-pointer-coordinates-in-alternative-coordinate-system" rel="noopener nofollow ugc">this example</a> in the script repository.</p>

---

## Post #3 by @aiden.zhu (2023-03-13 20:08 UTC)

<p>Thanks a lot for the solution.<br>
It worked after taking all parameters to the root “self”.</p>

---
