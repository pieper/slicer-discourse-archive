---
topic_id: 47476
title: "How to turn a python extension into a C++ one?"
date: 2026-06-27
url: https://discourse.slicer.org/t/47476
last_bumped: 2026-07-01T14:17:01.307Z
---

# How to turn a python extension into a C++ one?

**Topic ID**: 47476
**Date**: 2026-06-27
**URL**: https://discourse.slicer.org/t/how-to-turn-a-python-extension-into-a-c-one/47476

---

## Post #1 by @Long_Zhang (2026-06-27 11:51 UTC)

<p>I want to speedup the extension, and I wonder if this is a feasible way. and how to do it.</p>

---

## Post #2 by @shai-ikko (2026-07-01 14:17 UTC)

<p>It depends on which extension you are looking at, and what it does. Many extensions just invoke ITK algorithms and/or VTK visualizations, and then there’s little to gain from a compiled extension. Others do relatively simple mathematical operations on volumes, and are sometimes written to do this by looping on arrays in Python – and then can be sped up by orders of magnitude by using numpy array operations instead, while staying in Python.</p>
<p>To turn a Python extension into a C++ one, you essentially need to rewrite it. This also requires building your extension, which may not be trivial (depending on your familiarity with creating C++ extensions for Slicer).</p>
<p>To summarize: It can be done, but – unless you are doing something extremely special – I would recommend looking at other options first.</p>

---
