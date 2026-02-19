---
topic_id: 28463
title: "Using Curvedplanarreformat Without 3D Slicer Gui"
date: 2023-03-20
url: https://discourse.slicer.org/t/28463
---

# Using CurvedPlanarReformat without 3D Slicer GUI

**Topic ID**: 28463
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/using-curvedplanarreformat-without-3d-slicer-gui/28463

---

## Post #1 by @aalihashemi (2023-03-20 04:48 UTC)

<p>Hi,<br>
I want to straighten some arteries using the curved planar reformat algorithm but I don’t want to use 3D Slicer GUI because my code has its own GUI and other parts. Now my question is which way is preferred for this purpose? Should I use Slicelet? If I wanted to just run a python script to use the Slicer’s CPR functions, I have to compile both Slicer and also the Sandbox extension and after that, will I be able to use those functions?</p>

---

## Post #2 by @lassoan (2023-03-21 03:47 UTC)

<p>There are many ways to do this. For example, you can use run Slicer in a docker container and access its features as a web service using its <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">REST API</a>.</p>

---
