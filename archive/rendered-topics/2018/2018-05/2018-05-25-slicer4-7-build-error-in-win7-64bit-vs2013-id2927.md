# Slicer4.7 build error in Win7-64bit Vs2013

**Topic ID**: 2927
**Date**: 2018-05-25
**URL**: https://discourse.slicer.org/t/slicer4-7-build-error-in-win7-64bit-vs2013/2927

---

## Post #1 by @brotherher (2018-05-25 04:37 UTC)

<p>Hi all,<br>
I tried to build Slicer 4.7  in debug mode with the  VS 2013, and I got the following  errors:<br>
19&gt;------ Rebuild All started: Project: EMSegment, Configuration: Debug x64 ------<br>
19&gt;  Building Custom Rule D:/myProject/Slicer/CMakeLists.txt<br>
19&gt;  CMake does not need to re-run because D:\S4D\CMakeFiles\generate.stamp is up-to-date.<br>
19&gt;  Creating directories for ‘EMSegment’<br>
19&gt;  Performing download step (SVN checkout) for ‘EMSegment’<br>
19&gt;  svn: E155004: Run“svn cleanup”to remove locks (type ‘svn help cleanup’ for details)<br>
19&gt;  svn: E155004: Working copy ‘D:\S4D\EMSegment’ locked.<br>
19&gt;  svn: E155004: ‘D:\S4D\EMSegment’ is already locked.<br>
19&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: “cmd.exe” exited with code 1.<br>
By the way,my qt is  qt4.8.7.<br>
I don’t know where it went wrong,according to the compiler hints.</p>
<p>Can any body  help me?<br>
Any idea on how to proceed??</p>
<p>Waiting for your reply.<br>
Thanks so much!</p>

---
