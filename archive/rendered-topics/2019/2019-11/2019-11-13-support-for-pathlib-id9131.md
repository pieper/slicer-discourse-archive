---
topic_id: 9131
title: "Support For Pathlib"
date: 2019-11-13
url: https://discourse.slicer.org/t/9131
---

# Support for pathlib

**Topic ID**: 9131
**Date**: 2019-11-13
**URL**: https://discourse.slicer.org/t/support-for-pathlib/9131

---

## Post #1 by @Fernando (2019-11-13 14:44 UTC)

<p>Hi all,</p>
<p>Now that Python 3 works with Slicer, are there any plans to add support for the standard <a href="https://docs.python.org/3/library/pathlib.html" rel="nofollow noopener"><code>pathlib</code></a> library? Currently I just cast all the paths to str before feeding them to Slicer functions:</p>
<p>Old style:</p>
<pre><code class="lang-python">import os
myDir = '/tmp/images'
for root, dirs, files in os.walk(myDir, topdown=False):
    for name in files:
        _, ext = os.splitext(name)
        if ext == '.nrrd':
            loadVolume(os.path.join(root, name))
</code></pre>
<p>New style:</p>
<pre><code class="lang-python">from pathlib import Path
myDir = Path('/tmp/images')
for file in myDir.glob('**/*.nrrd'):
    loadVolume(str(file))  # need str until pathlib is supported
</code></pre>
<p>Here are some issues from big Python libraries:<br>
<a href="https://github.com/nipy/nibabel/pull/610" rel="nofollow noopener"><code>nibabel</code></a><br>
<a href="https://github.com/pandas-dev/pandas/blob/325dd686de1589c17731cf93b649ed5ccb5a99b4/pandas/io/common.py#L131-L160" rel="nofollow noopener"><code>pandas</code></a><br>
<a href="https://github.com/numpy/numpy/issues/6418" rel="nofollow noopener"><code>numpy</code></a><br>
<a href="https://github.com/python-pillow/Pillow/issues/1368" rel="nofollow noopener"><code>PIL</code></a><br>
<a href="https://github.com/matplotlib/matplotlib/pull/6788" rel="nofollow noopener"><code>matplotlib</code></a></p>
<p>Let me know if I can help.</p>

---

## Post #2 by @lassoan (2019-11-14 02:43 UTC)

<p>It would not be hard to add to slicer.util functions (pull request is welcome), but 99% of the API is C++ wrapped VTK and Qt classes. To add automatic Path&lt;-&gt;str conversion to the C++ API, you could ask dgobbi on the <a href="https://discourse.vtk.org">VTK forum</a> (for updating VTK’s Python wrapper), and submit an issue to <a href="https://github.com/MeVisLab/pythonqt">PythonQt</a> project (for updating Qt wrapping).</p>

---

## Post #3 by @Fernando (2021-02-09 14:49 UTC)

<p>Update on this:</p>
<ol>
<li>PythonQt seems to be ok with <code>pathlib</code>: <a href="https://github.com/MeVisLab/pythonqt/issues/38" class="inline-onebox" rel="noopener nofollow ugc">Feature request: add support for pathlib · Issue #38 · MeVisLab/pythonqt · GitHub</a>
</li>
<li>Support in VTK seems trickier: <a href="https://discourse.vtk.org/t/support-for-pathlib/5085/6?u=fepegar" class="inline-onebox" rel="noopener nofollow ugc">Support for pathlib - Development - VTK</a>
</li>
</ol>

---
