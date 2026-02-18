# Slicer 4.11 crash when switch to a layout with standard quantitave

**Topic ID**: 8598
**Date**: 2019-09-27
**URL**: https://discourse.slicer.org/t/slicer-4-11-crash-when-switch-to-a-layout-with-standard-quantitave/8598

---

## Post #1 by @g.belmonte (2019-09-27 22:18 UTC)

<p>Hi everybody,</p>
<p>since the last update when I switch to a layout with standard quantitative Slicer crashes (both manual switch and from python script). The error I have is</p>
<p>An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
ASSERT: “ctxt == nullptr || surface != nullptr” in file /home/gina/lavoro/AOUS/src/Slicer-SuperBuild-Release/VTK/GUISupport/Qt/QVTKOpenGLNativeWidget.cxx, line 127</p>
<p>I’m using Slicer on Linux Ubuntu compiled from master branch, version 4.11.0-2016-04-23 r25018.</p>
<p>Thank you a lot,<br>
Gina</p>

---

## Post #2 by @lassoan (2019-09-28 12:46 UTC)

<p>This view uses Qt webview to draw plots using a JavaScript library, so there are a number of things that can go wrong.</p>
<p>Which Qt version do you use? What CPU and graphics card do you have?</p>
<p>These JavaScript based plotting views will be deprecated soon and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="nofollow noopener">VTK native plotting views</a> should be used instead. If you don’t need real-time updates from MRML nodes then python plotting libraries may be used too (but these are still in experimental phase).</p>

---

## Post #3 by @g.belmonte (2019-10-04 14:55 UTC)

<p>Hi thanks for the answer,</p>
<p>Qt version is 5.13.1. I have a Intel Core i7-4500U and a yIntel Corporation Haswell-ULT Integrated Graphics Controller.</p>
<p>Unfortunately I wrote a Slicer Extension to quantify some quality control parameters in MR that use this kind of plot but I will try to update to a new version using VTK. But it seems to me that also some Slicer integrated modules keep using this, such as Label Statistics. Is it possible?</p>
<p>Gina</p>

---

## Post #4 by @lassoan (2019-10-04 15:32 UTC)

<p>This is a very old computer (6 generations behind current chipsets), which can cause compatibility issues.</p>
<p>Label statistics will be deprecated soon. It is replaced by Segment statistics module.</p>

---
