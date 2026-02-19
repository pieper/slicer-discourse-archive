---
topic_id: 16100
title: "Slicer Classes Api Documentation In Code Editor"
date: 2021-02-19
url: https://discourse.slicer.org/t/16100
---

# Slicer classes API documentation in code editor

**Topic ID**: 16100
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/slicer-classes-api-documentation-in-code-editor/16100

---

## Post #1 by @rbumm (2021-02-19 19:56 UTC)

<p>Hi,</p>
<p>Is there context-sensitive help (something like IntelliSense) available for Slicer classes when editing Python or C++ code?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e1b88350a6b23690dd202e6c3b33810072d01f8.png" alt="image" data-base62-sha1="myGqvih1USt9V3cUtBv6f5x22s8" width="438" height="47"></p>
<p>Thank you</p>
<p>Rudolf</p>

---

## Post #2 by @lassoan (2021-02-19 20:11 UTC)

<p>Yes, but not with static analysis (we can revisit that after VTK9 upgrade in a few weeks) but with a running Slicer. If you put a breakpoint in the function that you want to edit and you use a good IDE (such as PyCharm) then you should be able to get auto-complete and documentation.</p>
<p>Or, you can use <a href="https://github.com/Slicer/SlicerJupyter">Jupyter</a> to develop new functions and - you get syntax-highlighting, autocomplete, and API documentation, etc.</p>

---
