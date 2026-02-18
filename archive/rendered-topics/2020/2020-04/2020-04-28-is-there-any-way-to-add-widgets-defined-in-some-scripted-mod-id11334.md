# Is there any way to add widgets defined in some scripted module to a new scripted module?

**Topic ID**: 11334
**Date**: 2020-04-28
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-add-widgets-defined-in-some-scripted-module-to-a-new-scripted-module/11334

---

## Post #1 by @xlucox (2020-04-28 21:47 UTC)

<p>Hi !!!</p>
<p>I’m developing a new scripted module and I would like to add to it some widgets with the same functionality that these have in another module. I wonder if there is any way to do this without copping and pasting all the code.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2020-04-28 22:00 UTC)

<p>Module user interfaces are mostly built from reusable high-level widgets. You can drag-and-drop them into your own module GUI in Qt Designer, so you don’t even need to write any code to create your GUI (only to specify the behavior). See step-by-step tutorial here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---
