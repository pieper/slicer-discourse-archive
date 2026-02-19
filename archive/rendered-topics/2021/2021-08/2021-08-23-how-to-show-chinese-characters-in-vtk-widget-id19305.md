---
topic_id: 19305
title: "How To Show Chinese Characters In Vtk Widget"
date: 2021-08-23
url: https://discourse.slicer.org/t/19305
---

# How to show chinese characters in vtk widget

**Topic ID**: 19305
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/how-to-show-chinese-characters-in-vtk-widget/19305

---

## Post #1 by @wycstar (2021-08-23 07:17 UTC)

<p>i want to show chinese characters in 3d view widget using this code</p>
<pre><code class="lang-auto">view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,"Something")
</code></pre>
<p>but can only show ascii characters, the non ascii part is missing</p>

---

## Post #2 by @lassoan (2021-08-23 13:50 UTC)

<p>You need to choose a font that has Chinese characters. See a complete example here: <a href="https://github.com/liwind/VTK-Chinese-Font">https://github.com/liwind/VTK-Chinese-Font</a></p>

---
