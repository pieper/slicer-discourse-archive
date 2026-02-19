---
topic_id: 11126
title: "Can 3D Slicer Modules Be Used In Python Code External To 3D"
date: 2020-04-15
url: https://discourse.slicer.org/t/11126
---

# Can 3d slicer modules be used in python code external to 3d slicer?

**Topic ID**: 11126
**Date**: 2020-04-15
**URL**: https://discourse.slicer.org/t/can-3d-slicer-modules-be-used-in-python-code-external-to-3d-slicer/11126

---

## Post #1 by @LisaDuff (2020-04-15 13:31 UTC)

<p>The particular module I am interested in does have a CLI (command line interface) counterpart, am I able to use it in a separate piece of code without having to open 3d slicer?</p>

---

## Post #2 by @pieper (2020-04-15 14:58 UTC)

<p>If it’s just a CLI (as in a C++ executable) then yes, you can call it from python using the <code>subprocess</code> module.  Most of the other Slicer code has dependencies that make it impossible to use in the normal interpreter, but we’ve been talking about migrating as many libraries as possible into packages that could be distributed via pypi.</p>

---
