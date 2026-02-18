# How to create a Collapsible button in a python 3.7 GUI

**Topic ID**: 12177
**Date**: 2020-06-23
**URL**: https://discourse.slicer.org/t/how-to-create-a-collapsible-button-in-a-python-3-7-gui/12177

---

## Post #1 by @xlucox (2020-06-23 15:08 UTC)

<p>Hi !!!</p>
<p>I’m developing an application in python 3.7 using qt and I would like to create a collapsible button as the used in 3D slicer (ctk.ctkCollapsibleButton()). I tried to download ctk but it seems to don’t have this class inside. Does anyone can help me?</p>
<p>Thanks.</p>

---

## Post #2 by @Sam_Horvath (2020-06-23 15:25 UTC)

<p>The ctk pypi package is built off of an old version of CTK that is no longer supported.  Slicer builds and python wraps CTK itself to provide that functionality.  It is not currently available outside of Slicer.</p>

---
