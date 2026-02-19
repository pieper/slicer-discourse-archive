---
topic_id: 37028
title: "Cannot Install Pyacvd Python Package In 3Dslicer 5 7 0 2024"
date: 2024-06-26
url: https://discourse.slicer.org/t/37028
---

# Cannot install pyacvd Python package in 3Dslicer 5.7.0-2024-06-24

**Topic ID**: 37028
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/cannot-install-pyacvd-python-package-in-3dslicer-5-7-0-2024-06-24/37028

---

## Post #1 by @lv_xiao (2024-06-26 03:22 UTC)

<p>I am using the Surface Toolbox module in 3Dslicer 5.7.0-2024-06-24 on Win11 and I want to use the surface model uniform remeshing function to remesh my surface model in ply format loaded into 3Dslicer.</p>
<p>However, I got the error message after being prompted that pyacvd is required:<br>
Failed to compute output model: Command ‘[‘C:/ProgramData/slicer.org/Slicer 5.7.0-2024-06-24/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pyacvd’]’ returned non-zero exit status 1.</p>
<p>How should I solve this issue?</p>
<p>Best,<br>
Xiao</p>

---

## Post #2 by @muratmaga (2024-06-26 05:52 UTC)

<aside class="quote no-group" data-username="lv_xiao" data-post="1" data-topic="37028">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lv_xiao/48/8224_2.png" class="avatar"> lv_xiao:</div>
<blockquote>
<p>[‘C:/ProgramData/slicer.org/Slicer 5.7.0-2024-06-24/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pyacvd’]’</p>
</blockquote>
</aside>
<p>Your slicer installation seems in the folder which you may not have write permission. Were you able to install any extension or other python packages to this Slicer installation? Are you getting this error message only for this package?</p>
<p>What happens you type<br>
<code>pip_install("pandas")</code></p>
<p>in python console?</p>

---
