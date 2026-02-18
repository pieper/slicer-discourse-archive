# View multiple axial slices in the 3D view blue window

**Topic ID**: 33049
**Date**: 2023-11-27
**URL**: https://discourse.slicer.org/t/view-multiple-axial-slices-in-the-3d-view-blue-window/33049

---

## Post #1 by @zzzzzzzz (2023-11-27 04:48 UTC)

<p>Hi,</p>
<p>I got an image with 60 slices and I would like to view multiple axial slices aligned in 3D,but I can only view one slice at a time. Is a way to achieve that?</p>
<p>Thanks</p>

---

## Post #2 by @mikebind (2023-11-28 18:56 UTC)

<p>If three slices is enough, you can use, for example, the Four Up layout, and change the green and yellow slice views to also be axial slices, which can also be shown in the 3D view (see the buttons labeled “Slice orientation” and “Show in 3D” <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">here</a>).  If you want more than three axial slices shown, then you can set up as many slice views as you would like using a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout">custom layout</a> .</p>

---
