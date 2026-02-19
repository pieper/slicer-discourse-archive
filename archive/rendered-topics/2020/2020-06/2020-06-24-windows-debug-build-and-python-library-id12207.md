---
topic_id: 12207
title: "Windows Debug Build And Python Library"
date: 2020-06-24
url: https://discourse.slicer.org/t/12207
---

# Windows debug build and python library

**Topic ID**: 12207
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/windows-debug-build-and-python-library/12207

---

## Post #1 by @finetjul (2020-06-24 22:33 UTC)

<p>Hi all,</p>
<p>What is the status with debug build of Slicer on Windows ? I am trying to build Slicer master (without SimpleITK) on MSVC2017 x64 in Debug with no luck.<br>
I saw some recent changes from <a class="mention" href="/u/lassoan">@lassoan</a>. e.g. <a href="https://github.com/Slicer/Slicer/commit/49f3f0b8c02621baf6bad4e98c0b45c2ef30cd52" rel="nofollow noopener">49f3f0b8</a>.</p>
<p>As I am about to stop trying, I would like to share with you my findings:</p>
<details>
<summary>
I have these kinds of warnings...</summary>
<pre><code>CMake Warning (dev) at C:/Work/R-b/vtkAddon/CMake/vtkMacroKitPythonWrap.cmake:242 (target_link_libraries):
Link library type specifier "optimized" is followed by specifier
"optimized" instead of a library name.  The first specifier will be ignored.
Call Stack (most recent call first):
C:/Work/R-b/vtkAddon/CMakeLists.txt:206 (vtkMacroKitPythonWrap)
This warning is for project developers.  Use -Wno-dev to suppress it.
</code></pre>
</details>
<details>
<summary>
and these kinds of errors...</summary>
<pre><code>1&gt;CMake Error at C:/Work/R-b/slicersources-src/CMake/SlicerMacroBuildApplication.cmake:462 (get_filename_component):
get_filename_component unknown component
C:/Work/R-b/python-install/libs/python36.lib
Call Stack (most recent call first):
C:/Work/RFC/RFCo/Src/rfviewer/Applications/RFViewerApp/CMakeLists.txt:87 (slicerMacroBuildApplication)
</code></pre>
</details>
<p>This is because the variable <code>PYTHON_LIBRARY</code> is equal to:<br>
<code>optimized;C:/Work/R-b/python-install/libs/python36.lib;debug;C:/Work/Python/Python36/libs/python36_d.lib</code></p>
<p>According to the following 3 interesting links…<br>
<a href="https://cmake.org/pipermail/cmake/2016-April/063150.html" rel="nofollow noopener">https://cmake.org/pipermail/cmake/2016-April/063150.html</a><br>
<a href="https://github.com/Slicer/VTK/pull/24" rel="nofollow noopener">https://github.com/Slicer/VTK/pull/24</a><br>
<a href="https://gitlab.kitware.com/cmake/cmake/-/commit/a12d8a03af8430d0a570c97deb200e16830568eb" rel="nofollow noopener">https://gitlab.kitware.com/cmake/cmake/-/commit/a12d8a03af8430d0a570c97deb200e16830568eb</a></p>
<p>… it seems (at least according to the last commit message) that it is ok to have <code>PYTHON_LIBRARY=optimized;...;debug;...</code></p>
<p>Do you confirm ? Therefore should the fix done on <code>FindPythonLibs</code> be applied everywhere  ? If so, what about the warnings ? And what about the erroneous debug python path found on system ?</p>
<p>For information, when configuring <code>Slicer/CMakeLists.txt</code> (inner build, not superbuild), it seems that <code>PYTHON_LIBRARY</code> is fine (i.e. <code>C:/Work/R-b/python-install/libs/python36.lib</code>) until <code>find_package(CTK REQUIRED)</code> is called. It is then equal to <code>optimized;...;debug;...</code></p>

---

## Post #2 by @jcfr (2020-06-24 22:55 UTC)

<p>Thanks for the detailed report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>Could you try with this patch applied to CTK: <a href="https://github.com/commontk/CTK/pull/901">https://github.com/commontk/CTK/pull/901</a> ?</p>

---

## Post #3 by @jcfr (2020-06-24 22:57 UTC)

<p>The PR referenced above will be integrated while finalizing the update to VTK9 (tracked in <a href="https://github.com/Slicer/Slicer/issues/4696">https://github.com/Slicer/Slicer/issues/4696</a>)</p>
<p>I expect to work on this in the next t weeks.</p>

---
