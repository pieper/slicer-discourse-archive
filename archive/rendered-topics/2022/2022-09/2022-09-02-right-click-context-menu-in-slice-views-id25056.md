# Right-click context menu in slice views

**Topic ID**: 25056
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/right-click-context-menu-in-slice-views/25056

---

## Post #1 by @giovform (2022-09-02 19:58 UTC)

<p>How can I programatically disable (and enable again) the right-click context menu in slice views?</p>

---

## Post #2 by @lassoan (2022-09-02 21:40 UTC)

<p>You can configure this at multiple levels. If you just want to disable all actions in all views then you can set an empty list for the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-allowlist-to-customize-view-menu">allowed context menu action names</a>. If you just want to disable right-click action in certain views then you can remove the right-click GUI event translation (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#custom-shortcut-for-moving-crosshair-in-a-slice-view">assign the right-click GUI event</a> to <code>vtk.vtkWidgetEvent.NoEvent</code> widget event).</p>

---
