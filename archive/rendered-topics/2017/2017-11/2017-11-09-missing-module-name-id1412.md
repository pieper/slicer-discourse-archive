---
topic_id: 1412
title: "Missing Module Name"
date: 2017-11-09
url: https://discourse.slicer.org/t/1412
---

# Missing module name

**Topic ID**: 1412
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/missing-module-name/1412

---

## Post #1 by @Zoe_Goey (2017-11-09 00:09 UTC)

<p>If I create a Python extension in Slicer 4.6.2 using the extension wizard and load a module that has been created within this extension, then the module name is not automatically added to slicer.moduleNames. This results in an AttributeError when Slicer is closed (line 191 of Slicer-4.6.2-linux-amd64/bin/Python/slicer/slicerqt.py, in unsetSlicerModule, delattr(slicer.moduleNames, moduleName)). Is this a bug, or should I be doing something to get the module name added?</p>

---

## Post #2 by @lassoan (2017-11-09 02:41 UTC)

<p>You only get this error if you register a module using module manager manually. You can safely ignore it.</p>
<p>I’ve just committed a fix to suppress this error (available in tomorrow’s nightly build).</p>

---
