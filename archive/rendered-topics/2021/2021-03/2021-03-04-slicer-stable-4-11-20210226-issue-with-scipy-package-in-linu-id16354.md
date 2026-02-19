---
topic_id: 16354
title: "Slicer Stable 4 11 20210226 Issue With Scipy Package In Linu"
date: 2021-03-04
url: https://discourse.slicer.org/t/16354
---

# Slicer Stable 4.11.20210226 issue with scipy package in Linux

**Topic ID**: 16354
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/slicer-stable-4-11-20210226-issue-with-scipy-package-in-linux/16354

---

## Post #1 by @Alex_Vergara (2021-03-04 11:05 UTC)

<p>There is a problem with scipy package in linux in the new Slicer stable:</p>
<pre><code class="lang-auto">from scipy import signal
  File "/home/alex/Programas/Slicer3D/lib/Python/lib/python3.6/site-packages/scipy/signal/__init__.py", line 289, in &lt;module&gt;
    from . import sigtools, windows
  File "/home/alex/Programas/Slicer3D/lib/Python/lib/python3.6/site-packages/scipy/signal/windows/__init__.py", line 41, in &lt;module&gt;
    from .windows import *
  File "/home/alex/Programas/Slicer3D/lib/Python/lib/python3.6/site-packages/scipy/signal/windows/windows.py", line 7, in &lt;module&gt;
    from scipy import linalg, special, fft as sp_fft
  File "/home/alex/Programas/Slicer3D/lib/Python/lib/python3.6/site-packages/scipy/linalg/__init__.py", line 194, in &lt;module&gt;
    from .misc import *
  File "/home/alex/Programas/Slicer3D/lib/Python/lib/python3.6/site-packages/scipy/linalg/misc.py", line 3, in &lt;module&gt;
    from .blas import get_blas_funcs
  File "/home/alex/Programas/Slicer3D/lib/Python/lib/python3.6/site-packages/scipy/linalg/blas.py", line 213, in &lt;module&gt;
    from scipy.linalg import _fblas
ImportError: /home/alex/Programas/Slicer3D/lib/Python/lib/python3.6/site-packages/scipy/linalg/_fblas.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned
</code></pre>
<p>Reinstalling scipy from python console solves the issue</p>
<pre><code class="lang-auto">from slicer.util import pip_install
pip_install('scipy -U')
</code></pre>

---

## Post #2 by @Sam_Horvath (2021-03-04 14:47 UTC)

<p>This is an issue we are working on addressing: <a href="https://github.com/Slicer/Slicer/issues/5474" class="inline-onebox" rel="noopener nofollow ugc">Importing the numpy C-extensions failed. [slicer 4.11.20200930, archlinux] · Issue #5474 · Slicer/Slicer · GitHub</a></p>
<p>It affects a number of python packages that are bundled with Slicer.  See <a href="https://discourse.slicer.org/t/slicer-4-11-20200930-cant-import-pip-installed-pillow-on-linux/14448" class="inline-onebox">Slicer-4.11.20200930: Can't import pip-installed Pillow on Linux</a></p>

---

## Post #3 by @Alex_Vergara (2021-06-24 19:28 UTC)

<p>Hey, Are there any news on solving this issue? I have several users complaining on this</p>

---

## Post #4 by @Sam_Horvath (2021-06-24 19:31 UTC)

<p>As noted in the GitHub issue linked above, a fix has been pushed to Slicer as of March.  Are you still having the same issue with newer packages?</p>

---

## Post #5 by @Alex_Vergara (2021-06-24 19:48 UTC)

<p>Sorry, the issue is present in the latest stable version. So the question shall be rewritten as: when a new stable version will contain the solution to this issue?</p>

---

## Post #6 by @Sam_Horvath (2021-06-24 20:18 UTC)

<p>Sure, we should be putting out another stable snapshot in the next few weeks, most likely after the switch to the new extension manager.</p>

---
