# is PointClickedEvent still supported in slicer 4.11.0?

**Topic ID**: 10962
**Date**: 2020-04-01
**URL**: https://discourse.slicer.org/t/is-pointclickedevent-still-supported-in-slicer-4-11-0/10962

---

## Post #1 by @TiphaineJh (2020-04-01 19:54 UTC)

<p>Operating system: windows10<br>
Slicer version: slicer 4.11.0<br>
Expected behavior: trigger an event when the markup is clicked (used here <a href="https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository#Show_a_context_menu_when_a_markup_point_is_clicked_in_a_slice_or_3D_view" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/ScriptRepository#Show_a_context_menu_when_a_markup_point_is_clicked_in_a_slice_or_3D_view</a>)<br>
Actual behavior:  type object ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsNode’ has no attribute ‘PointClickedEvent’</p>

---

## Post #2 by @lassoan (2020-04-01 22:38 UTC)

<p>Recent Slicer-4.11 releases have built-in right-click menu. You can customize the menu by creating a subject hierarchy plugin and overriding <code>viewContextMenuActions</code> and <code>showViewContextMenuActionsForItem</code> methods.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> do you have a working example in Python?</p>

---

## Post #3 by @cpinter (2020-04-02 12:58 UTC)

<p>Yes, but it’s in a private repository. Should I “sanitize” it and upload it as example somewhere?</p>

---

## Post #4 by @lassoan (2020-04-02 15:22 UTC)

<p>Yes, it would be great if you could upload it to the script repository (replace <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_context_menu_when_a_markup_point_is_clicked_in_a_slice_or_3D_view">this example</a>).</p>

---

## Post #5 by @cpinter (2020-04-02 15:35 UTC)

<p>Done, let me know if it’s fine.</p>

---

## Post #6 by @lassoan (2020-04-04 21:03 UTC)

<p>Awesome, thanks a lot! <a class="mention" href="/u/tiphainejh">@TiphaineJh</a> let us know if you need more help with setting up a custom menu for your markups.</p>

---
