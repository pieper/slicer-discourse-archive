---
topic_id: 45473
title: "Segmentation In Windows 11 Extremely Slow"
date: 2025-12-13
url: https://discourse.slicer.org/t/45473
---

# Segmentation in Windows 11 extremely slow

**Topic ID**: 45473
**Date**: 2025-12-13
**URL**: https://discourse.slicer.org/t/segmentation-in-windows-11-extremely-slow/45473

---

## Post #1 by @NSLight (2025-12-13 17:52 UTC)

<p><strong>Operating System</strong> - Windows 11<br>
<strong>Slicer 3D Version</strong> - 5.8.1</p>
<p>I have been everywhere on the forum, tried different solutions but nothing seems to work.</p>
<p>I am working on a dataset (Brain Angio-CT) and trying to segment vessels. On windows (AMD Rysen 5 5600X, 16Gb RAM), the segmentation takes a very long time (talking in minutes here) to do a simple cut with the scisor module. Task Manager shows available memory, I’ve turned off surface smoothing.</p>
<p>On the other hand when I use my Macbook Air (2020, intel silicon, 8Gb RAM) it works beautifully.</p>
<p>Is there any known bug reagarding this issue?</p>
<p>Best regards</p>

---

## Post #2 by @pieper (2025-12-13 18:51 UTC)

<p>If you are doing the same operation on the same data there shouldn’t be much difference between mac and windows.  Many of us do this all the time so there must be something misconfigured on your windows machine.  Sometimes there are issues such as using the right GPU for the app.</p>

---
