---
topic_id: 18657
title: "Cli Start 3D Slicer With Specific Module Loaded"
date: 2021-07-13
url: https://discourse.slicer.org/t/18657
---

# CLI start 3d slicer with specific module loaded

**Topic ID**: 18657
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/cli-start-3d-slicer-with-specific-module-loaded/18657

---

## Post #1 by @talmazov (2021-07-13 05:10 UTC)

<p>Hey,<br>
I am trying to start 3D Slicer from another script via CLI. the slicer instance should be windowed and startup w/ specific module showing, instead of the ‘welcome’ UI. Is this possible?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-07-13 15:17 UTC)

<p>You can easily do this by passing the appropriate Python commands using <code>--python-code</code> argument. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-slicer">script repository</a>. You can set the window size and position using standard Qt commands and switch module using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#switch-to-a-different-module"><code>selectModule()</code> function</a>.</p>

---
