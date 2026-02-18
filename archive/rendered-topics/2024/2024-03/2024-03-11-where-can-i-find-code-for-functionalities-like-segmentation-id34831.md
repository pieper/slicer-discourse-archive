# Where can I find code for functionalities like segmentation, registration etc

**Topic ID**: 34831
**Date**: 2024-03-11
**URL**: https://discourse.slicer.org/t/where-can-i-find-code-for-functionalities-like-segmentation-registration-etc/34831

---

## Post #1 by @Arun03Kumar (2024-03-11 17:46 UTC)

<p>Dear 3D slicer family.</p>
<p>I am learning the codebase for learning purpose, I learned some UI implementation techniques, but I want to create a toggle button in segmentation or in functionality tools section so that it initially hides some of the tools. so can anyone please tell me where can I find the code for same, also an idea to complete the task?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2024-03-12 04:04 UTC)

<p>It is a very common need to customize the Slicer GUI to make it easy to perform specific workflows. Slicer uses Qt as GUI toolkit, so all you need to do is to learn how to hide widgets in Qt (basically get the widget and call <code>hide()</code> method) or design custom GUI layouts (you can use Qt designer for this - it is bundled with 3D Slicer).</p>
<p>I would recommend to get started with programming Slicer using the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab bootcamp Slicer programming tutorial</a> and complete a few online Qt tutorials.</p>

---
