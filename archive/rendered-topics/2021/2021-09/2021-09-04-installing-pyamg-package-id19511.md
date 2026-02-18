# Installing pyamg package

**Topic ID**: 19511
**Date**: 2021-09-04
**URL**: https://discourse.slicer.org/t/installing-pyamg-package/19511

---

## Post #1 by @shatz (2021-09-04 19:45 UTC)

<p>When installing the pyamg package, I get the error <code>RuntimeError: Unsupported compiler -- at least C++11 support is needed!</code>.</p>
<p>OS: linux<br>
Slicer Ver: 4.13.0</p>
<p>Any advice?</p>

---

## Post #2 by @lassoan (2021-09-04 20:30 UTC)

<p>As you can <a href="https://pypi.org/project/pyamg">see on PyPI</a>, the pyamg 4.0 has wheels (binary install package) for all platforms. However, this 4.0 is 3 years old. There is a 4.1.0 version released 5 months ago, but it only has a single macOS wheel (that’s why your Python tries to build the package on your computer). It indicates that something is not entirely right with this package (not enough maintainers?), so I would recommend to check if it is is still active, quality is good, developers are responsive, etc. before investing too much time into learning to use it.</p>
<p>You can get started by installing the 4.0 release (that has wheels):</p>
<pre><code>pip_install('pyamg==4.0.0')
</code></pre>
<p>And if it looks promising then ask the developers to provide wheels for the current release.</p>

---
