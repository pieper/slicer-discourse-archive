---
topic_id: 19724
title: "Faild Build Slicer In Windows10 With Visual Studio 2017 Qt 5"
date: 2021-09-17
url: https://discourse.slicer.org/t/19724
---

# Faild build Slicer in Windows10 with Visual Studio 2017,Qt 5.10.1

**Topic ID**: 19724
**Date**: 2021-09-17
**URL**: https://discourse.slicer.org/t/faild-build-slicer-in-windows10-with-visual-studio-2017-qt-5-10-1/19724

---

## Post #1 by @kookoo9999 (2021-09-17 13:29 UTC)

<p>Hello thanks for reading.<br>
I wnat to build Slicer ( 4.11 20200930) on Windows10 but  build failed repeatedly.<br>
In the past , I tried to build Slicer Source(from git “master” branch) but I saw the CMake configuration error occured.(env : Visual Studio 2017,Qt5.15 include Web Engine &amp; Script,CMake 3.15) and then I changed the environment as follows.<br>
My env is<br>
Visual Studio 2017<br>
Qt 5.10.1(include WebEngine,Script)<br>
CMake 3.15.0-rc1 and Source Code is changed from “master” branch to Slicer-4.11.20200930.<br>
So I did success to do configuration in CMake.</p>
<p>There is no problem with Configuration in CMake(option Visual Studio 2017,x64) and generate too.<br>
but when I build the ALL_BUILD in Slicer.sln , I see the Message of Build Fail 48 out of 54 …</p>
<p>And I can’t find Slicer.exe in directory of Slicer_build\build\ or Slicer_build.</p>
<p>Did I do anything wrong?</p>

---

## Post #2 by @lassoan (2021-09-26 04:03 UTC)

<p>This build error and solution (workaround) is discussed <a href="https://github.com/Slicer/Slicer/issues/5498">here</a>.</p>

---
