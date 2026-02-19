---
topic_id: 29604
title: "C1001 Internal Compiler Error"
date: 2023-05-23
url: https://discourse.slicer.org/t/29604
---

# C1001: Internal compiler error

**Topic ID**: 29604
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/c1001-internal-compiler-error/29604

---

## Post #1 by @Ngo_Minh_Toan (2023-05-23 13:37 UTC)

<p>I tried to build the latest Slicer  on Windows using CMake 3.26.3 and Visual Studio 2022 17.6.1 with the prerequisites have met (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#install-prerequisites" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>)<br>
CMake configure and generate the Release build were done without any error<br>
However, during the Release by Visual Studio there was an error</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>12:18:40:263</th>
<th>13&gt;E:\S\B\VTK\ThirdParty\ioss\vtkioss\private_copy_fmt\fmt/ostream.h(32,1): fatal error C1001: Internal compiler error. [E:\S\B\VTK-build\ThirdParty\ioss\vtkioss\ioss.vcxproj]</th>
</tr>
</thead>
<tbody>
<tr>
<td>12:18:40:263</td>
<td>13&gt;  (compiler file ‘msc1.cpp’, line 1589)</td>
</tr>
<tr>
<td>then</td>
<td></td>
</tr>
<tr>
<td>12:34:22:973</td>
<td>13&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(248,5): error MSB8066: Custom build for ‘E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-mkdir.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-download.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-update.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-patch.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-configure.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-build.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-create_egg_info.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-generate_project_description.rule;E:\S\B\CMakeFiles\2f3b8b1f079799e3ffdef766991c1db2\VTK-install.rule;E:\S\B\CMakeFiles\37951788506b17b75cca77d1d45f0dfb\VTK-complete.rule;E:\S\B\CMakeFiles\9e8337cb89344f33c6ac88b23a164fd9\VTK.rule;E:\S\S\CMakeLists.txt’ exited with code 1.</td>
</tr>
<tr>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>12:34:22:985</td>
<td>13&gt;Done building project VTK.vcxproj – FAILED.</td>
</tr>
<tr>
<td>Is there any way to overcome this problem?</td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @lassoan (2023-05-23 13:55 UTC)

<p>I’ve built Slicer on Windows thousands of times but I haven’t run into this issue.</p>
<p>Are you building the latest Slicer <code>main</code> branch?</p>
<p>What is the build toolset version?<br>
Mine is <code>14.34.31933</code>, as in the top-level CMakeCache.txt I have a line like this:<br>
<code>CMAKE_AR:FILEPATH=C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.34.31933/bin/Hostx64/x64/lib.exe</code></p>

---

## Post #3 by @Ngo_Minh_Toan (2023-05-23 15:32 UTC)

<p>Thank for the quick response<br>
I used the git for the Slicer according to the guide <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#install-prerequisites" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a> which is <a href="https://github.com/Slicer/Slicer.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a><br>
The toolset I used is C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.36.32532/bin/Hostx64/x64/lib.exe</p>

---

## Post #4 by @lassoan (2023-05-23 17:01 UTC)

<p>New compiler versions often need some time to get stable, so it is usually better not to use the very latest version. You can downgrade to toolset version 14.34, by opening the Visual Studio Installer application, choose Modify, choose “Individual components” tab, and unselect MSVC… build tools (Latest)" and select a 14.34 instead.</p>
<p>You can also open VTK build settings in CMake and disable all modules that refer to IOSS.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> It seems that this problematic private copy of the <code>fmt</code> library has been removed in VTK-9.2.0 (in September 2022). Could we rebase Slicer’s VTK on a recent VTK version? The amount of backported fixes (and the lots more fixes that we have not backported) is becoming a bit worrying.</p>

---

## Post #5 by @Ngo_Minh_Toan (2023-05-23 19:14 UTC)

<p>I have disabled all modules referring to the IOSS and have successfully built the Slicer without any error<br>
Thank you</p>

---

## Post #7 by @lassoan (2023-05-30 19:24 UTC)

<p>We got another report at <a href="https://github.com/Slicer/Slicer/issues/6990" class="inline-onebox">faild to install the debug and release version of slicer multipy times · Issue #6990 · Slicer/Slicer · GitHub</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> we’ll probably get just more and more reports like this (unless Microsoft very quickly releases a new compiler revision). To avoid frustrating many developers, could we upgrade Slicer’s VTK? Recent VTK versions don’t contain the file that crashes the MSVC compiler.</p>

---

## Post #8 by @jcfr (2023-05-30 19:27 UTC)

<blockquote>
<p>Could we rebase Slicer’s VTK on a recent VTK version?</p>
</blockquote>
<p>Indeed, a pull-request is being worked on.</p>

---

## Post #9 by @slicer365 (2023-07-17 04:54 UTC)

<p>Can you tell me how to disable all modules referring to the IOSS?<br>
I met the same problems during rebuilding.</p>

---

## Post #10 by @lassoan (2023-07-17 17:07 UTC)

<p>I would recommend to not mess with the configuration but instead update to the latest Slicer main version.</p>

---

## Post #11 by @slicer365 (2023-07-18 00:18 UTC)

<p>Thank you ,I solved the problem after I changed the  MSVC tool to  version 14.34</p>

---
