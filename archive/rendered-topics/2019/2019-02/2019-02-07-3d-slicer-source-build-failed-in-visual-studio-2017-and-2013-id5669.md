---
topic_id: 5669
title: "3D Slicer Source Build Failed In Visual Studio 2017 And 2013"
date: 2019-02-07
url: https://discourse.slicer.org/t/5669
---

# 3D Slicer source Build failed in Visual studio 2017 and 2013

**Topic ID**: 5669
**Date**: 2019-02-07
**URL**: https://discourse.slicer.org/t/3d-slicer-source-build-failed-in-visual-studio-2017-and-2013/5669

---

## Post #1 by @smaatze (2019-02-07 06:12 UTC)

<p>Hello<br>
i have a couple of week trying to build 3d slicer in visual studio 2017 and 2013. i tried qt v5.12 but it failed with so many errors. after that tried qt-4.8.7-x64-msvc2013 with vs 2013 x64 build, it was successful but it failed to open Extension Manager in order to install IGT Module.</p>
<p>Software’s Version:<br>
Windows 10   64 bit<br>
3d Slicer 4.10.1</p>

---

## Post #2 by @jamesobutler (2019-02-07 06:39 UTC)

<p>Make sure to follow the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">build instructions</a> very closely. The document explains what Qt components to install and that for Windows you must use 5.10.x or older versions. You had a lot of errors because you were using 5.12. Qt4 builds are possible, build Qt5 builds are preferred now. Let us know if any instructions need clarification.</p>
<p>If you want to use the IGT module, you can always download the pre-built Slicer versions from the main website and install the extension using the extension manager.</p>

---

## Post #3 by @pieper (2019-02-07 12:40 UTC)

<p>In addition note that as a general rule, if you build your own Slicer from source, you won’t be able to add factory-built extensions.</p>

---

## Post #4 by @smaatze (2019-02-09 20:04 UTC)

<p>i used cmake 3.11.1 GUI with QT_QMAKE_EXECUTABLE variable set to C:/Qt/Qt5.10.1/5.10.1/msvc2017_64/bin/qmake.exe and configure set to visual studio 2017.  cmake failed with this error:<br>
CMake Error at CMake/SlicerBlockFindQtAndCheckVersion.cmake:45 (message):<br>
error: Qt 4.7.4 was not found on your system.You probably need to set the<br>
QT_QMAKE_EXECUTABLE variable.<br>
Call Stack (most recent call first):<br>
CMake/SlicerBlockFindQtAndCheckVersion.cmake:110 (__SlicerBlockFindQtAndCheckVersion_find_qt)<br>
CMakeLists.txt:610 (include)</p>

---

## Post #5 by @jamesobutler (2019-02-09 20:36 UTC)

<p>You’ve overlooked a few instructions. I’ve pointed out some things below which I’ve noticed you’ve done incorrectly. Remember to read the instructions carefully. There are several important steps which if not followed will cause the build to fail with a lot of errors. If there is a specific thing in the instructions that is unclear please let us know so it can be updated. Thanks!</p>
<ul>
<li>Getting the correct Qt5 (msvc 2015 64 bit). See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt5" rel="nofollow noopener">these</a> instructions.</li>
</ul>
<ul>
<li>
<p>For Visual Studio 2017: Make sure you enable installation of component  <em>Programming languages / Visual C++ / Common Tools for Visual C++ 2015</em>  (in some distributions, this option is not enabled by default)</p>
</li>
<li>
<p>Visual Studio 2015 toolset must be set in CMake:  <em>Optional toolset to use (argument to -T)</em>  need to be set to  <em>v140</em></p>
</li>
<li>
<p>Select your compiler: Visual Studio 14 2015 Win64</p>
</li>
<li>
<p><strong>Do not configure yet.</strong></p>
</li>
<li>
<p>Add  <code>Qt5_DIR</code>  variable pointing to Qt5 folder such as  <code>C:\Qt\5.10.0\msvc2015_64\lib\cmake\Qt5</code> .</p>
</li>
</ul>

---

## Post #6 by @pdeman (2019-08-28 14:50 UTC)

<p>using visual studio 2017, even after installing the common tools for visual c++ 2015. cmake doesn’t find the c and cxx compiler corresponding to v140.</p>

---

## Post #7 by @lassoan (2019-08-28 15:02 UTC)

<p>This configuration works well for me. You can use commands described at “Visual Studio 2017 with VS2015 toolset in Release mode” on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">build instructions page</a>. Make sure to follow all the instructions (correct CMake version, Qt version, etc.).</p>

---
