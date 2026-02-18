# Could I see different staff in different 3D window？

**Topic ID**: 7873
**Date**: 2019-08-05
**URL**: https://discourse.slicer.org/t/could-i-see-different-staff-in-different-3d-window/7873

---

## Post #1 by @Zhao_Su (2019-08-05 00:03 UTC)

<p>like i want one window shows the man’s blood vessel and another shows the skull.</p>

---

## Post #2 by @lassoan (2019-08-05 00:08 UTC)

<p>Yes. You can choose which node is shown in which view. If you have segmented these structures then export them to model nodes and in Models module Display section you can set for each model where you want to see it.</p>

---

## Post #4 by @Zhao_Su (2019-08-05 00:22 UTC)

<p>Oh! I get it. My English is so bad:sweat_smile:,And i want to know is there possible two different window have two rendering with different shift.</p>

---

## Post #5 by @lassoan (2019-08-05 00:33 UTC)

<p>Each displayed object has the same 3D position in all viewers, so if you want to show the “same” object in different positions then you need to clone it (in Data module, by right-clicking on it) and apply a transform on it (in Transforms module).</p>

---
