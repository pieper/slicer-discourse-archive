# Slicer build crash on Qt creator in Window11

**Topic ID**: 39900
**Date**: 2024-10-28
**URL**: https://discourse.slicer.org/t/slicer-build-crash-on-qt-creator-in-window11/39900

---

## Post #1 by @tobi9952 (2024-10-28 20:38 UTC)

<p>Dear concern,</p>
<p>While trying to build Slicer in QtCreator, I got the following error message (CreateProcess failed. Command attempted: ~ninja build logs~<br>
ninja: fatal: CreateProcess: ~crashed language in korean~<br>
(is the command line too long?)</p>
<p><strong>FAILED</strong>: Slicer-prefix/src/Slicer-stamp/Slicer-build C:/D/SDebug/Slicer-prefix/src/Slicer-stamp/Slicer-build<br>
C:\Windows\system32\cmd.exe /C “cd /D C:\D\SDebug\Slicer-build &amp;&amp; C:\Qt\Tools\CMake_64\bin\cmake.exe --build . &amp;&amp; C:\Qt\Tools\CMake_64\bin\cmake.exe -E touch C:/D/SDebug/Slicer-prefix/src/Slicer-stamp/Slicer-build”</p>
<p>Note: I am using Qt 5.14.17 and MSVC 2022<br>
I didn’t make any code change and try to build with the defaults.</p>
<p>Can anyone kindly assist me solving this issue?</p>

---

## Post #2 by @lassoan (2024-10-29 16:36 UTC)

<p>We don’t support building using QtCreator or ninja generator. It may work, but we don’t test it and if the build fails then we may not be able to help you. You can build Slicer without problems if you follow the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">build instructions</a>.</p>

---
