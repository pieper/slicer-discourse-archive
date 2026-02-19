---
topic_id: 42472
title: "Issues Related To The Python Environment In 3D Slicer Softwa"
date: 2025-04-07
url: https://discourse.slicer.org/t/42472
---

# Issues Related to the Python Environment in 3D Slicer Software

**Topic ID**: 42472
**Date**: 2025-04-07
**URL**: https://discourse.slicer.org/t/issues-related-to-the-python-environment-in-3d-slicer-software/42472

---

## Post #1 by @lirongyaoper (2025-04-07 16:18 UTC)

<p>Why does 3D Slicer bundle its own Python environment instead of using a user-configured Python environment? Can we modify settings to make 3D Slicer use a custom Python environment?</p>

---

## Post #2 by @muratmaga (2025-04-07 16:39 UTC)

<p>Short answer is this: think of slicer as the system, as a system it uses its own system installed python.</p>
<p>Slightly long answer is because it would be impossible to maintain functionality across different oses, python versions, package managers, virtual environments and such, and it would break things.</p>

---

## Post #3 by @lassoan (2025-04-08 15:20 UTC)

<p>Slicer application’s Python environment is your “user-configured Python environment”. You can configure it as any other Python environments. As <a class="mention" href="/u/muratmaga">@muratmaga</a> described, it would be impractical for you to set up and maintain a custom Python environment that is compatible with the Slicer application.</p>
<p>However, if you just want to import Slicer as a library into your Python environment and use some Slicer features from there (some widgets, algorithms, etc.) then you will be able to use <a href="https://discourse.slicer.org/t/trame-slicer-and-slicerlib-wheel/41388">SlicerLib</a>. It is planned to be released around the end of this year.</p>

---

## Post #4 by @Narges_Olia (2025-07-18 06:47 UTC)

<p>Hello,</p>
<p>I am facing a similar issue. I attempted to install the parallelproj package using SlicerPython, but it seems that I cannot install it via pip. I decided to create a virtual environment using conda, but I am unable to run it in 3D Slicer. Do you have any suggestions in this case? I need this package, and the default Python in 3D Slicer does not support conda.</p>

---

## Post #5 by @lassoan (2025-07-18 11:26 UTC)

<p>The <code>parallelproj</code> package is not available on PyPI at all. This is a huge red flag telling that its developers have very limited resources or intent for making their software widely available to users. Conda is heavy, opinionated, and does not mix reliably with pip, so it does not help much if the package is available only via conda.</p>
<p><a class="mention" href="/u/lukepolson">@lukepolson</a> do you have any advice?</p>

---
