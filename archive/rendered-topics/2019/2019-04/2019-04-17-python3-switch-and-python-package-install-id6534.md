# Python3 switch and python package install

**Topic ID**: 6534
**Date**: 2019-04-17
**URL**: https://discourse.slicer.org/t/python3-switch-and-python-package-install/6534

---

## Post #1 by @muratmaga (2019-04-17 21:54 UTC)

<p>Does switching to Python3 changed anything regarding install python packages with Slicer? I.e, is the preferred way still:<br>
<code>PythonSlicer -m pip install something</code> .</p>

---

## Post #2 by @lassoan (2019-04-17 22:39 UTC)

<p>The main difference is that you can install any Python3 package in Slicer’s Python environment, even on Windows.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> is still working out the details of how to automatically install Python packages required by extensions. Users will not need to manually pip install any Python packages but the extension manager will take care of that.</p>

---

## Post #3 by @muratmaga (2019-04-18 07:04 UTC)

<p>ok. That’s great.<br>
While the previous method worked, it required admin rights which is challenging to obtain at certain environments. An automatic install, without admin privileges  will be great.<br>
Looking forward to it.</p>

---
