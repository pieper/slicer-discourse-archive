---
topic_id: 24461
title: "Visual Studio 2022 Project Never Up To Date After Build"
date: 2022-07-22
url: https://discourse.slicer.org/t/24461
---

# Visual studio 2022 project never up-to-date after build

**Topic ID**: 24461
**Date**: 2022-07-22
**URL**: https://discourse.slicer.org/t/visual-studio-2022-project-never-up-to-date-after-build/24461

---

## Post #1 by @PaulMartinMurphy (2022-07-22 21:33 UTC)

<p>Hi all,</p>
<p>I am trying to build Slicer for Windows 10 with Visual Studio Community 2022 version 17.2.6, after configuring it in CMake 3.23.2 with Qt 5.15.2, according to the directions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" rel="noopener nofollow ugc">here</a></p>
<p>The build for target ALL_BUILDS succeeds initially, and I’m able to run Slicer.</p>
<p>However, when I build for a second time, with no changes to the code, with no intervening clean, and with build (rather than rebuild), almost every component is reported to be “not up-to-date”, and is recompiled in its entirety.</p>
<p>This is a problem, since it takes quite a while to recompile every component of Slicer.</p>
<p>Does anyone know why that’s happening and how to fix it?</p>
<p>I tried to figure out why this is happening by setting Tools &gt; Options &gt; Projects and Solutions &gt; Build and Run &gt; MSBuild project build output verbosity = “Diagnostic” in Visual Studio and and running the build again. The first few lines of the output from the build are below:</p>
<p>Build started…<br>
1&gt;------ Up-To-Date check: Project: ZERO_CHECK.vcxproj, Configuration: Debug x64 ------<br>
1&gt;All outputs are up-to-date.<br>
1&gt;Time Elapsed 6 ms<br>
2&gt;------ Up-To-Date check: Project: zlib.vcxproj, Configuration: Debug x64 ------<br>
2&gt;Project is not up-to-date: build input ‘d:\d\s5r\zlib-prefix\src\zlib-stamp\debug\zlib-update’ is missing.<br>
2&gt;------ Build started: Project: zlib, Configuration: Debug x64 ------<br>
3&gt;------ Up-To-Date check: Project: vtkAddon.vcxproj, Configuration: Debug x64 ------<br>
3&gt;Project is not up-to-date: build input ‘d:\d\s5r\vtkaddon-prefix\src\vtkaddon-stamp\debug\vtkaddon-update’ is missing.<br>
3&gt;------ Build started: Project: vtkAddon, Configuration: Debug x64 ------<br>
4&gt;------ Up-To-Date check: Project: tbb.vcxproj, Configuration: Debug x64 ------<br>
4&gt;Project is not up-to-date: build output ‘d:\d\s5r\cmakefiles\tbb’ is missing<br>
4&gt;------ Build started: Project: tbb, Configuration: Debug x64 ------<br>
5&gt;------ Up-To-Date check: Project: sqlite.vcxproj, Configuration: Debug x64 ------<br>
5&gt;Project is not up-to-date: build input ‘d:\d\s5r\sqlite-prefix\src\sqlite-stamp\debug\sqlite-update’ is missing.<br>
5&gt;------ Build started: Project: sqlite, Configuration: Debug x64 ------<br>
6&gt;------ Up-To-Date check: Project: qRestAPI.vcxproj, Configuration: Debug x64 ------<br>
6&gt;Project is not up-to-date: build input ‘d:\d\s5r\qrestapi-prefix\src\qrestapi-stamp\debug\qrestapi-update’ is missing.<br>
6&gt;------ Build started: Project: qRestAPI, Configuration: Debug x64 ------<br>
7&gt;------ Up-To-Date check: Project: python-source.vcxproj, Configuration: Debug x64 ------<br>
7&gt;Project is not up-to-date: build output ‘d:\d\s5r\cmakefiles\python-source’ is missing<br>
7&gt;------ Build started: Project: python-source, Configuration: Debug x64 ------<br>
8&gt;------ Up-To-Date check: Project: bzip2.vcxproj, Configuration: Debug x64 ------<br>
8&gt;Project is not up-to-date: build input ‘d:\d\s5r\bzip2-prefix\src\bzip2-stamp\debug\bzip2-update’ is missing.</p>
<p>Many of these files are in fact missing when I look for them in the filesystem. I read that there can be issues with case sensitivity of paths in Windows, but I don’t think that’s the issue here since my build directory is not case sensitive:</p>
<blockquote>
<p>fsutil.exe file queryCaseSensitiveInfo D:\D\S5R<br>
Case sensitive attribute on directory D:\D\S5R\ is disabled.</p>
</blockquote>
<p>Thanks for any input on this topic!<br>
-Paul</p>

---

## Post #2 by @adamrankin (2022-07-22 21:40 UTC)

<p>Once the superbuild is complete, could you work only in the inner build? If you’re modifying Slicer source code, then that’s the way to go.</p>

---

## Post #3 by @PaulMartinMurphy (2022-07-25 03:43 UTC)

<p>Thanks! I didn’t realize there was an inner build, but I see that in the instructions now.</p>

---
