---
topic_id: 21544
title: "Vmtkcenterlinegeometry Cant View Output File"
date: 2022-01-20
url: https://discourse.slicer.org/t/21544
---

# vmtkcenterlinegeometry - can't view output file

**Topic ID**: 21544
**Date**: 2022-01-20
**URL**: https://discourse.slicer.org/t/vmtkcenterlinegeometry-cant-view-output-file/21544

---

## Post #1 by @fsneden (2022-01-20 13:55 UTC)

<p>Hi,</p>
<p>Have used vmtkcenterline geometry to calculate tortuousity of a carotid artery. Output runs fine; the file is written under .vtp extension as in tutorial. However, I want numbers that relate to tortuousity, curvature etc, and no idea how to get these data.</p>

---

## Post #2 by @ramtingh (2022-01-21 09:19 UTC)

<p>If you want tortuosity, you should use <code>vmtkbranchgeometry</code>.<br>
vmtkcenterlinegeometry produces pointwise curvature and torsion as point data arrays. Easiest way of accessing these is probably through the python/numpy interface.</p>
<p>You can convert it to a .dat file as well which will be a spreadsheet of these values, but unless you have a simple geometry this is going to be difficult to process.</p>

---
