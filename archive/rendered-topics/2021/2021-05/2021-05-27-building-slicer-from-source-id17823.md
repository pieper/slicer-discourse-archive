---
topic_id: 17823
title: "Building Slicer From Source"
date: 2021-05-27
url: https://discourse.slicer.org/t/17823
---

# Building Slicer from source

**Topic ID**: 17823
**Date**: 2021-05-27
**URL**: https://discourse.slicer.org/t/building-slicer-from-source/17823

---

## Post #1 by @mau_igna_06 (2021-05-27 10:57 UTC)

<p>I was able to build Slicer following <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" rel="noopener nofollow ugc">this tutorial</a></p>
<p>I have not tested if all the functionalities work without crash but at least the sliceViews and the 3D View work.</p>
<p>I had to change one line of the instructions a little bit for it to work. Here it is in case some one needs it:</p>
<pre><code class="lang-auto">"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 16 2019" -A x64 -DQt5_DIR:PATH=C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5 C:\D\S4\Slicer
</code></pre>

---

## Post #2 by @jamesobutler (2021-05-27 15:21 UTC)

<p>You are correct that the “Visual Studio 16 2019 Win64” is not an appropriate generator name.<br>
See <a href="https://cmake.org/cmake/help/latest/release/3.14.html#generators" rel="noopener nofollow ugc">CMake 3.14 Release Notes</a> where the CMake generator platform must be set with the “-A” command line option starting with the VS 2019 generator which was introduced in this version.</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> That documentation can be changed in the following file which is located in the Slicer GitHub repo. Could you issue a PR to fix this? Thanks! <a href="https://github.com/Slicer/Slicer/blob/master/Docs/developer_guide/build_instructions/windows.md" class="inline-onebox" rel="noopener nofollow ugc">Slicer/windows.md at master · Slicer/Slicer · GitHub</a></p>

---
