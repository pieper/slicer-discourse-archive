# Python scripted module code organization

**Topic ID**: 6339
**Date**: 2019-03-30
**URL**: https://discourse.slicer.org/t/python-scripted-module-code-organization/6339

---

## Post #1 by @michalikthomas (2019-03-30 23:04 UTC)

<p>What is the recommended way to distribute and initiate source code in a scripted module - separating code into multiple files?</p>
<p>I am not sure about importing files. When I add <code>__init__.py</code> into a scripted module folder to import all files within the module folder, then during the Slicer startup appears following error:</p>
<pre><code>SystemError: /work/Stable/Slicer-4101-build/Python-2.7.13/Objects/classobject.c:521: bad argument to internal function
</code></pre>
<p>Slicer version: Slicer-4.10.1-linux-amd64</p>

---

## Post #2 by @lassoan (2019-03-31 04:36 UTC)

<p>Python modules must be in subfolder(s). See for example how it is done in <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted/DataProbe" rel="nofollow noopener">DataProbe module</a>.</p>

---
