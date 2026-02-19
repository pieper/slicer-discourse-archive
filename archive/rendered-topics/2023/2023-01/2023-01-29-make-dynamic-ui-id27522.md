---
topic_id: 27522
title: "Make Dynamic Ui"
date: 2023-01-29
url: https://discourse.slicer.org/t/27522
---

# Make dynamic UI

**Topic ID**: 27522
**Date**: 2023-01-29
**URL**: https://discourse.slicer.org/t/make-dynamic-ui/27522

---

## Post #1 by @SH4096 (2023-01-29 00:59 UTC)

<p>I want to make a dynamic interface in slicer with QML, but I can’t find this library, how can I do it</p>

---

## Post #2 by @lassoan (2023-01-29 09:22 UTC)

<p><a href="https://mevislab.github.io/pythonqt/Features.html">PythonQt</a> is bundled with Slicer and it supports QML and has experimental support for Qt Quick, so it should all work, but I don’t know if anyone has tried to use these in Slicer.</p>
<p>As an experiment, you can also pip_install “Qt for Python” in Slicer and use QML via that wrapping.</p>
<p>Note that you can create dynamic GUI using classic Qt widgets, too. Qt Designer is bundled with Slicer, so you can very quickly and conveniently design your module GUI in a visual editor (and you can further dynamically modify it using Python scripting).</p>

---
