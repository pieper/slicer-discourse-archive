---
topic_id: 10370
title: "Build Slicer In Windows Subsystem Complaining Rename Permiss"
date: 2020-02-20
url: https://discourse.slicer.org/t/10370
---

# Build Slicer in Windows subsystem complaining rename permission denied

**Topic ID**: 10370
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/build-slicer-in-windows-subsystem-complaining-rename-permission-denied/10370

---

## Post #1 by @Zhiy (2020-02-20 19:53 UTC)

<p>I tried to build Slicer nightly code in Ubuntu 18 (subsystem of windows 10). The cmake version is 3.13.4. The gcc/g++ versions are both 7.4. I ran cmake  -DCMAKE_BUILD_TYPE:STRING=Debug <br>
-DQt5_DIR:PATH=/home/me/Qt/5.14.0/gcc_64/lib/cmake/Qt5 <br>
-DSlicer_USE_SYSTEM_QT:BOOL=1 <br>
…/Slicer and configured it successfully. Then I ran sudo make. The building process complains that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> CMake Error at python-source-prefix/src/python-source-stamp/extract-python-source.cmake:51 (file):</p>
<p>file RENAME failed to rename</p>
<pre><code>/home/me/MyProjects/Slicer-SuperBuild-Debug/ex-python-source1234/Python-3.6.7
</code></pre>
<p>to</p>
<pre><code>/home/me/MyProjects/Slicer-SuperBuild-Debug/Python-3.6.7
</code></pre>
<p>because: Permission denied</p>
<p>Any help is appreciate.</p>

---

## Post #2 by @lassoan (2020-02-21 01:41 UTC)

<p>It does not look like an error specific to Slicer. Can you do the rename manually?</p>

---
