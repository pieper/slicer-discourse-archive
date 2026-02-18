# Typing custom coordinates to edit a fiducial

**Topic ID**: 18442
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/typing-custom-coordinates-to-edit-a-fiducial/18442

---

## Post #1 by @Rahulsabharwal (2021-06-30 20:26 UTC)

<p>Can we type custom r,a,s coordinates and edit a placed fiducial markup ?</p>

---

## Post #2 by @Juicy (2021-07-01 20:39 UTC)

<p>Yes this can be done in the markups module. Expand the control points drop down from memory.</p>

---

## Post #3 by @Rahulsabharwal (2023-02-02 15:11 UTC)

<p>I can see the r,a,s coordinates in the drop down . But how can I edit them ? For eg . I have placed a point F1 at (4,5,6). How can I place this point exactly at (0,0,0). ?</p>

---

## Post #4 by @jamesobutler (2023-02-02 19:22 UTC)

<p>In the Markups module, double left-click to edit the values.</p>
<p>This is not Slicer defined behavior, but how the Qt GUI framework handles editable/selectable cells in a table.</p>

---
