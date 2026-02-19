---
topic_id: 22488
title: "When Building Custom Template In Release Mode Getting Error"
date: 2022-03-14
url: https://discourse.slicer.org/t/22488
---

# When building custom template in release mode getting error

**Topic ID**: 22488
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/when-building-custom-template-in-release-mode-getting-error/22488

---

## Post #1 by @Dwij_Mistry (2022-03-14 02:42 UTC)

<p>I am following all build steps mentioned in [readthedocs] for release (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#configure-and-build-slicer" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>)</p>
<p>I have tried both the way command line build and GUI build. but getting same error as bellow.</p>
<pre><code class="lang-auto">    Couldn't open file 'C:/BR/LibFFI-build/objlib.dir/Release/debug.obj' with CreateFile()
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: The command "setlocal [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibFFI.vcx
proj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: cd C:\BR\LibFFI-build [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibFFI.vcx
proj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-buil
d\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: C: [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-buil
d\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: "C:\Program Files\CMake\bin\cmake.exe" -E __create_def C:/BR/LibFFI-build/ffi_shared.dir/Release/ex
ports.def C:/BR/LibFFI-build/ffi_shared.dir/Release//objects.txt [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicers
ources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-buil
d\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: :cmEnd [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone [C:\BR\LibFFI-build\ffi_shared.vcxproj] [
C:\BR\slicersources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: :cmErrorLevel [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: exit /b %1 [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: :cmDone [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: if %errorlevel% neq 0 goto :VCEnd [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-buil
d\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(150
,5): error MSB3073: :VCEnd" exited with code 1. [C:\BR\LibFFI-build\ffi_shared.vcxproj] [C:\BR\slicersources-build\LibF
FI.vcxproj]
    Building Custom Rule C:/BR/LibFFI/CMakeLists.txt
LINK : fatal error LNK1181: cannot open input file 'C:\BR\LibFFI-build\objlib.dir\Release\debug.obj' [C:\BR\LibFFI-buil
d\ffi_static.vcxproj] [C:\BR\slicersources-build\LibFFI.vcxproj]
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241
,5): error MSB8066: Custom build for 'C:\BR\CMakeFiles\53e8e00795af948a1cf7ab505f262965\LibFFI-mkdir.rule;C:\BR\CMakeFi
les\53e8e00795af948a1cf7ab505f262965\LibFFI-download.rule;C:\BR\CMakeFiles\53e8e00795af948a1cf7ab505f262965\LibFFI-upda
te.rule;C:\BR\CMakeFiles\53e8e00795af948a1cf7ab505f262965\LibFFI-patch.rule;C:\BR\CMakeFiles\53e8e00795af948a1cf7ab505f
262965\LibFFI-configure.rule;C:\BR\CMakeFiles\53e8e00795af948a1cf7ab505f262965\LibFFI-build.rule;C:\BR\CMakeFiles\53e8e
00795af948a1cf7ab505f262965\LibFFI-install.rule;C:\BR\CMakeFiles\53e8e00795af948a1cf7ab505f262965\LibFFI-generate_proje
ct_description.rule;C:\BR\CMakeFiles\3d8e95d19201056634839aa69f03021d\LibFFI-complete.rule;C:\BR\CMakeFiles\14e8e525956
9794af3c37f023dd5c921\LibFFI.rule' exited with code 1. [C:\BR\slicersources-build\LibFFI.vcxproj]
  Creating directories for 'OpenSSL'
  Performing download step (download, verify and extract) for 'OpenSSL'
  -- Downloading...
     dst='C:/BR/OpenSSL_1_1_1g-install-msvc1900-64.tar.gz'
     timeout='none'
  -- Using src='https://github.com/Slicer/Slicer-OpenSSL/releases/download/1.1.1g/OpenSSL_1_1_1g-install-msvc1900-64.ta
  r.gz'
  -- [download 100% complete]
</code></pre>
<p><a href="https://gist.github.com/dwijmistry11/580d4fcd0a9077b7532aea6d8ce767c1" rel="noopener nofollow ugc">full build log file is here.</a></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> Can you please help me to solve this error. Thank you</p>

---

## Post #2 by @lassoan (2022-03-14 13:32 UTC)

<p>The full build log shows that the first error is this:</p>
<blockquote>
<p>Couldn’t open file ‘C:/BR/LibFFI-build/objlib.dir/Release/debug.obj’ with CreateFile()</p>
</blockquote>
<p>I’ve checked my Slicer builds and in the debug-mode build tree <code>debug.obj</code> is available at <code>c:\D\S4D\LibFFI-build\objlib.dir\Debug\debug.obj</code>, but there is no such file in the release-mode build tree.</p>
<p>Have you ever attempted to build this Slicer in this build tree in debug mode? If yes, configuring the build in debug-mode first may have enabled some debug build options that did not disappear when you switched to release mode.</p>
<p>You can try removing LibFFI-build, LibFFI-install, and LibFFI-prefix folders and restart the build. If that does not fix the issue then it may be easier to do a full rebuild of Slicer (removing the entire C:\BR folder) rather than try to debug it further.</p>
<p>Are you using the very latest Slicer master version? If you do a full rebuild it could make sense to update to the latest version.</p>

---

## Post #3 by @Dwij_Mistry (2022-03-21 05:42 UTC)

<p>in CMAKE we are having this two entry for build type and missing <strong>CMAKE_CONFIGURATION_TYPES</strong> entry</p>
<pre><code class="lang-auto">#adding default build type
if(NOT DEFINED CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()


if(NOT CMAKE_CONFIGURATION_TYPES)
  set(Slicer_DEFAULT_BUILD_TYPE "Release")
endif()
</code></pre>
<p>When Configuring project using CMAKE<br>
it is taking default entry of</p>
<pre><code class="lang-auto">CMAKE_CONFIGURATION_TYPES : Debug;Release;MinSizeRel;RelWithDebInfo
</code></pre>
<p>To solve this we have to add this entry</p>
<pre><code class="lang-auto">CMAKE_CONFIGURATION_TYPES : Release 
</code></pre>

---

## Post #4 by @Sam_Horvath (2022-07-13 19:05 UTC)

<p>So, I also encountered this error, and updating to CMake 2.22.1 (from 3.17.1) fixed it.</p>

---
