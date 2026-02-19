---
topic_id: 16761
title: "Use Different Python Interpreter With Slicer 3D"
date: 2021-03-25
url: https://discourse.slicer.org/t/16761
---

# Use different python interpreter with Slicer 3d

**Topic ID**: 16761
**Date**: 2021-03-25
**URL**: https://discourse.slicer.org/t/use-different-python-interpreter-with-slicer-3d/16761

---

## Post #1 by @oren (2021-03-25 11:26 UTC)

<p>Hi<br>
I wish Slicer 3D to run with my local anaconda interpreter instead of the default Slicer3D python environment<br>
Is is possible ?  how should I configure this change ?</p>
<p>I have many packages that are already installed on my conda interpreter and I do not wish to reinstall them all again on Slicer 3D</p>
<p>Operating system is Windows 10, and Pycharm with python 3.7 - 3.6</p>
<p>thanks</p>

---

## Post #2 by @pieper (2021-03-25 19:17 UTC)

<p>Unfortunately that’s not an easy thing to support.  You /might/ be able to build slicer from source and point to your anaconda install, but that hasn’t always worked in the past.  Much better to just install what you need in Slicer.</p>

---
