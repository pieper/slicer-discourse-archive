---
topic_id: 19718
title: "Failed Build Slicer In Windows10 With Visual Studio 2017 Qt"
date: 2021-09-17
url: https://discourse.slicer.org/t/19718
---

# Failed build Slicer in Windows10 with Visual Studio 2017,Qt 5.10.1

**Topic ID**: 19718
**Date**: 2021-09-17
**URL**: https://discourse.slicer.org/t/failed-build-slicer-in-windows10-with-visual-studio-2017-qt-5-10-1/19718

---

## Post #1 by @kookoo9999 (2021-09-17 07:55 UTC)

<p>I wnat to build Slicer ( 4.11 20200930) on Windows10 but build failed repeatedly.<br>
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

## Post #2 by @kookoo9999 (2021-09-17 07:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4.png" data-download-href="/uploads/short-url/coRgFwgrYqLL4rzpvygzKJ9rT3S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_690x373.png" alt="image" data-base62-sha1="coRgFwgrYqLL4rzpvygzKJ9rT3S" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_1380x746.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1038 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13da421558628a74a7e328d29add67b4a51233c7.png" data-download-href="/uploads/short-url/2PCGE4fqEPr9VGhIUJwjeNKTQc7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13da421558628a74a7e328d29add67b4a51233c7.png" alt="image" data-base62-sha1="2PCGE4fqEPr9VGhIUJwjeNKTQc7" width="583" height="500" data-dominant-color="F2F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1101×943 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35ed1c844d607d0ee4d4245aedc2c5b5c417ce94.png" data-download-href="/uploads/short-url/7H3jvUdYwbEgJm42YtbRCYZvj3S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35ed1c844d607d0ee4d4245aedc2c5b5c417ce94.png" alt="image" data-base62-sha1="7H3jvUdYwbEgJm42YtbRCYZvj3S" width="690" height="308" data-dominant-color="484747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1274×570 18.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>S4R is Slicer-4.11.20200930 source code.<br>
All_Build is failed so I can’t find Slicer.exe.<br>
I tried to build this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" rel="noopener nofollow ugc">link</a>.</p>

---

## Post #3 by @lassoan (2021-09-17 17:19 UTC)

<p>First I would recommend to build Slicer by following the exact requirements as described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">build instructions</a>. Once that works, you can try and change the configuration and see if you can use other library versions/compilers.</p>

---

## Post #4 by @kookoo9999 (2021-09-19 07:58 UTC)

<p>Previously, we tried “master” branch source code, but build failed…<br>
And I changed the source code from “master” branch to 4.11 20200930.<br>
nevertheless build failed , I try to build Slicer via Visual Studio 2019. but I couldn’t see Slicer.exe…</p>

---

## Post #5 by @kookoo9999 (2021-09-20 05:12 UTC)

<p>Previously, we tried “master” branch source code, but build failed…<br>
And I changed the source code from “master” branch to 4.11 20200930.<br>
nevertheless build failed , I try to build Slicer via Visual Studio 2019. but I couldn’t see Slicer.exe…<br>
Today I changed the source code version and try to build.<br>
but always I see the this message “Slicer.vcxproj is build failed”.</p>

---

## Post #6 by @lassoan (2021-09-20 14:25 UTC)

<p>We build Slicer master on many Windows computers, every day, without any issues, by following the build instructions described in the documentation. The issue that breaks the build on your computer must be something trivial, but we need to see the actual error message to tell what exactly is that.</p>
<p>Could you copy-paste here the full text of the very first error message that appears when you build the inner <code>Slicer</code> target (<code>c:\D\S4R\Slicer-build\Slicer.sln</code> and not <code>c:\D\S4R\Slicer.sln</code>)?</p>

---

## Post #7 by @kookoo9999 (2021-09-21 06:10 UTC)

<p>This  message is C:\D\S4R\Slicer-build\Slicer.sln.<br>
and I tried upload SlicerTargets.cmake but so long texts…<br>
1&gt;------ 빌드 시작: 프로젝트: CTKResEdit, 구성: Release x64 ------<br>
2&gt;------ 빌드 시작: 프로젝트: LZMA, 구성: Release x64 ------<br>
3&gt;------ 빌드 시작: 프로젝트: OpenSSL, 구성: Release x64 ------<br>
4&gt;------ 빌드 시작: 프로젝트: bzip2, 구성: Release x64 ------<br>
5&gt;------ 빌드 시작: 프로젝트: zlib, 구성: Release x64 ------<br>
6&gt;------ 빌드 시작: 프로젝트: python-source, 구성: Release x64 ------<br>
7&gt;------ 빌드 시작: 프로젝트: sqlite, 구성: Release x64 ------<br>
8&gt;------ 빌드 시작: 프로젝트: tbb, 구성: Release x64 ------<br>
9&gt;------ 빌드 시작: 프로젝트: Swig, 구성: Release x64 ------<br>
10&gt;------ 빌드 시작: 프로젝트: SimpleITK-download, 구성: Release x64 ------<br>
11&gt;------ 빌드 시작: 프로젝트: SimpleFilters, 구성: Release x64 ------<br>
12&gt;------ 빌드 시작: 프로젝트: CompareVolumes, 구성: Release x64 ------<br>
13&gt;------ 빌드 시작: 프로젝트: jqPlot, 구성: Release x64 ------<br>
2&gt;Performing update step for ‘LZMA’<br>
4&gt;Performing update step for ‘bzip2’<br>
14&gt;------ 빌드 시작: 프로젝트: CTKAPPLAUNCHER, 구성: Release x64 ------<br>
15&gt;------ 빌드 시작: 프로젝트: BRAINSTools, 구성: Release x64 ------<br>
16&gt;------ 빌드 시작: 프로젝트: CTKAppLauncherLib, 구성: Release x64 ------<br>
5&gt;Performing update step for ‘zlib’<br>
11&gt;Performing update step for ‘SimpleFilters’<br>
12&gt;Performing update step for ‘CompareVolumes’<br>
7&gt;Performing update step for ‘sqlite’<br>
17&gt;------ 빌드 시작: 프로젝트: DataStore, 구성: Release x64 ------<br>
18&gt;------ 빌드 시작: 프로젝트: JsonCpp, 구성: Release x64 ------<br>
19&gt;------ 빌드 시작: 프로젝트: LandmarkRegistration, 구성: Release x64 ------<br>
20&gt;------ 빌드 시작: 프로젝트: SurfaceToolbox, 구성: Release x64 ------<br>
15&gt;Performing update step for ‘BRAINSTools’<br>
10&gt;Performing update step for ‘SimpleITK-download’<br>
16&gt;Performing update step for ‘CTKAppLauncherLib’<br>
18&gt;Performing update step for ‘JsonCpp’<br>
21&gt;------ 빌드 시작: 프로젝트: qRestAPI, 구성: Release x64 ------<br>
22&gt;------ 빌드 시작: 프로젝트: DCMTK, 구성: Release x64 ------<br>
23&gt;------ 빌드 시작: 프로젝트: curl, 구성: Release x64 ------<br>
24&gt;------ 빌드 시작: 프로젝트: LibArchive, 구성: Release x64 ------<br>
25&gt;------ 빌드 시작: 프로젝트: MultiVolumeExplorer, 구성: Release x64 ------<br>
26&gt;------ 빌드 시작: 프로젝트: MultiVolumeImporter, 구성: Release x64 ------<br>
27&gt;------ 빌드 시작: 프로젝트: vtkAddon, 구성: Release x64 ------<br>
28&gt;------ 빌드 시작: 프로젝트: RapidJSON, 구성: Release x64 ------<br>
17&gt;Performing update step for ‘DataStore’<br>
20&gt;Performing update step for ‘SurfaceToolbox’<br>
21&gt;Performing update step for ‘qRestAPI’<br>
25&gt;Performing update step for ‘MultiVolumeExplorer’<br>
26&gt;Performing update step for ‘MultiVolumeImporter’<br>
27&gt;Performing update step for ‘vtkAddon’<br>
28&gt;Performing update step for ‘RapidJSON’<br>
29&gt;------ 빌드 시작: 프로젝트: python, 구성: Release x64 ------<br>
19&gt;Performing update step for ‘LandmarkRegistration’<br>
24&gt;Creating directories for ‘LibArchive’<br>
22&gt;Performing update step for ‘DCMTK’<br>
23&gt;Performing update step for ‘curl’<br>
29&gt;Performing update step for ‘python’<br>
24&gt;Building Custom Rule C:/D/S4/CMakeLists.txt<br>
30&gt;------ 빌드 시작: 프로젝트: python-ensurepip, 구성: Release x64 ------<br>
31&gt;------ 빌드 시작: 프로젝트: VTK, 구성: Release x64 ------<br>
24&gt;Performing download step (git clone) for ‘LibArchive’<br>
24&gt;-- Avoiding repeated git clone, stamp file is up to date: ‘C:/D/S4R/LibArchive-prefix/src/LibArchive-stamp/LibArchive-gitclone-lastrun.txt’<br>
24&gt;Performing update step for ‘LibArchive’<br>
31&gt;Performing update step for ‘VTK’<br>
32&gt;------ 빌드 시작: 프로젝트: python-setuptools, 구성: Release x64 ------<br>
24&gt;No patch step for ‘LibArchive’<br>
24&gt;Generate version-LibArchive.txt and license-LibArchive.txt<br>
33&gt;------ 빌드 시작: 프로젝트: ITK, 구성: Release x64 ------<br>
34&gt;------ 빌드 시작: 프로젝트: teem, 구성: Release x64 ------<br>
35&gt;------ 빌드 시작: 프로젝트: python-pip, 구성: Release x64 ------<br>
24&gt;Performing configure step for ‘LibArchive’<br>
24&gt;loading initial cache file C:/D/S4R/LibArchive-prefix/tmp/LibArchive-cache-Release.cmake<br>
34&gt;Performing update step for ‘teem’<br>
33&gt;Performing update step for ‘ITK’<br>
24&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19042.<br>
36&gt;------ 빌드 시작: 프로젝트: python-numpy, 구성: Release x64 ------<br>
37&gt;------ 빌드 시작: 프로젝트: python-requests-requirements, 구성: Release x64 ------<br>
38&gt;------ 빌드 시작: 프로젝트: python-wheel, 구성: Release x64 ------<br>
39&gt;------ 빌드 시작: 프로젝트: python-extension-manager-requirements, 구성: Release x64 ------<br>
24&gt;-- Could NOT find LIBB2 (missing: LIBB2_LIBRARY LIBB2_INCLUDE_DIR)<br>
24&gt;-- Could NOT find LZ4 (missing: LZ4_LIBRARY LZ4_INCLUDE_DIR)<br>
24&gt;-- Could NOT find ZSTD (missing: ZSTD_LIBRARY ZSTD_INCLUDE_DIR)<br>
24&gt;-- Could NOT find LIBGCC (missing: LIBGCC_LIBRARY)<br>
24&gt;-- Could NOT find PCREPOSIX (missing: PCREPOSIX_LIBRARY PCRE_INCLUDE_DIR)<br>
24&gt;-- Could NOT find PCRE (missing: PCRE_LIBRARY)<br>
40&gt;------ 빌드 시작: 프로젝트: SimpleITK, 구성: Release x64 ------<br>
41&gt;------ 빌드 시작: 프로젝트: SlicerExecutionModel, 구성: Release x64 ------<br>
42&gt;------ 빌드 시작: 프로젝트: CTK, 구성: Release x64 ------<br>
24&gt;-- Configuring done<br>
43&gt;------ 빌드 시작: 프로젝트: python-dicom-requirements, 구성: Release x64 ------<br>
44&gt;------ 빌드 시작: 프로젝트: python-extension-manager-ssl-requirements, 구성: Release x64 ------<br>
45&gt;------ 빌드 시작: 프로젝트: python-pythonqt-requirements, 구성: Release x64 ------<br>
46&gt;------ 빌드 시작: 프로젝트: python-scipy, 구성: Release x64 ------<br>
24&gt;-- Generating done<br>
24&gt;-- Build files have been written to: C:/D/S4R/LibArchive-build<br>
24&gt;Performing build step for ‘LibArchive’<br>
41&gt;Performing update step for ‘SlicerExecutionModel’<br>
42&gt;Performing update step for ‘CTK’<br>
24&gt;.NET Framework용 Microsoft (R) Build Engine 버전 15.9.21+g9802d43bc3<br>
24&gt;Copyright (C) Microsoft Corporation. All rights reserved.<br>
24&gt;<br>
24&gt;  archive_read_support_format_rar5.c<br>
24&gt;C:\D\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c : error C2220: 경고가 오류로 처리되어 생성된 ‘object’ 파일이 없습니다. [C:\D\S4R\LibArchive-build\libarchive\archive.vcxproj]<br>
24&gt;C:\D\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c : warning C4819: 현재 코드 페이지(949)에서 표시할 수 없는 문자가 파일에 들어 있습니다. 데이터가 손실되지 않게 하려면 해당 파일을 유니코드 형식으로 저장하십시오. [C:\D\S4R\LibArchive-build\libarchive\archive.vcxproj]<br>
24&gt;  archive_read_support_format_rar5.c<br>
24&gt;C:\D\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c : error C2220: 경고가 오류로 처리되어 생성된 ‘object’ 파일이 없습니다. [C:\D\S4R\LibArchive-build\libarchive\archive_static.vcxproj]<br>
24&gt;C:\D\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c : warning C4819: 현재 코드 페이지(949)에서 표시할 수 없는 문자가 파일에 들어 있습니다. 데이터가 손실되지 않게 하려면 해당 파일을 유니코드 형식으로 저장하십시오. [C:\D\S4R\LibArchive-build\libarchive\archive_static.vcxproj]<br>
24&gt;“LibArchive.vcxproj” 프로젝트를 빌드했습니다. - 실패<br>
47&gt;------ 빌드 시작: 프로젝트: Slicer, 구성: Release x64 ------<br>
47&gt;Creating directories for ‘Slicer’<br>
47&gt;Building Custom Rule C:/D/S4/CMakeLists.txt<br>
47&gt;No download step for ‘Slicer’<br>
47&gt;No update step for ‘Slicer’<br>
47&gt;No patch step for ‘Slicer’<br>
47&gt;Performing configure step for ‘Slicer’<br>
47&gt;loading initial cache file C:/D/S4R/Slicer-prefix/tmp/Slicer-cache-Release.cmake<br>
47&gt;-- Setting C++ standard<br>
47&gt;-- Setting C++ standard - C++11<br>
47&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19042.<br>
47&gt;-- Could NOT find Subversion (missing: Subversion_SVN_EXECUTABLE)<br>
47&gt;-- Configuring Slicer organization domain [<a href="http://www.na-mic.org" rel="noopener nofollow ugc">www.na-mic.org</a>]<br>
47&gt;-- Configuring Slicer organization name [NA-MIC]<br>
47&gt;-- Configuring Slicer default home module [Welcome]<br>
47&gt;-- Configuring Slicer default favorite modules [Data, Volumes, Models, Transforms, Markups, SegmentEditor]<br>
47&gt;-- Configuring Slicer text of disclaimer at startup [Thank you for using %1!<br><br>This software is not intended for clinical use.]<br>
47&gt;-- Configuring Slicer requires admin account [OFF]<br>
47&gt;-- Configuring Slicer install root [$LOCALAPPDATA/NA-MIC]<br>
47&gt;-- Configuring Slicer release type [Experimental]<br>
47&gt;CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):<br>
47&gt;  Skipping repository info extraction: directory [C:/D/S4] is not a GIT or<br>
47&gt;  SVN checkout<br>
47&gt;Call Stack (most recent call first):<br>
47&gt;  CMake/SlicerVersion.cmake:55 (SlicerMacroExtractRepositoryInfo)<br>
47&gt;  CMakeLists.txt:182 (include)<br>
47&gt;This warning is for project developers.  Use -Wno-dev to suppress it.<br>
47&gt;<br>
47&gt;-- Configuring Slicer version [4.11.20200930-0000-00-00]<br>
47&gt;-- Configuring Slicer revision [3037]<br>
47&gt;CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):<br>
47&gt;  Skipping repository info extraction: directory [C:/D/S4] is not a GIT or<br>
47&gt;  SVN checkout<br>
47&gt;Call Stack (most recent call first):<br>
47&gt;  CMake/SlicerVersion.cmake:99 (SlicerMacroExtractRepositoryInfo)<br>
47&gt;  CMakeLists.txt:182 (include)<br>
47&gt;This warning is for project developers.  Use -Wno-dev to suppress it.<br>
47&gt;<br>
47&gt;-- Configuring VTK<br>
47&gt;--   Slicer_VTK_RENDERING_BACKEND is OpenGL2<br>
47&gt;--   Slicer_VTK_SMP_IMPLEMENTATION_TYPE is TBB<br>
47&gt;--   Slicer_VTK_VERSION_MAJOR is 8<br>
47&gt;-- Configuring Slicer with Qt 5.10.1 (using modules: Core, Widgets, Multimedia, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, WebEngine, WebEngineWidgets, WebChannel, Script, Test, )<br>
47&gt;-- Setting QT_PLUGINS_DIR: C:/Qt/Qt5.10.1/5.10.1/msvc2017_64/plugins<br>
47&gt;-- Setting QT_BINARY_DIR: C:/Qt/Qt5.10.1/5.10.1/msvc2017_64/bin<br>
47&gt;-- Setting ExternalData_OBJECT_STORES to ‘C:/D/S4R/Slicer-build/ExternalData/Objects’<br>
47&gt;-- Configuring Slicer for [win-amd64]<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
47&gt;-- Configuring Slicer with python 3.6<br>
47&gt;-- Configuring library: ITKFactoryRegistration<br>
47&gt;-- Configuring library: vtkAddon [vtkAddon_SOURCE_DIR: C:/D/S4R/vtkAddon]<br>
47&gt;-- Configuring library: vtkTeem<br>
47&gt;-- Configuring library: vtkITK<br>
47&gt;-- Configuring library: vtkSegmentationCore<br>
47&gt;-- Configuring library: MRML/Core<br>
47&gt;-- Configuring library: MRML/CLI<br>
47&gt;-- Configuring library: RemoteIO<br>
47&gt;-- Configuring library: MRML/Logic<br>
47&gt;-- Configuring library: MRML/DisplayableManager<br>
47&gt;-- Configuring library: MRML/IDImageIO<br>
47&gt;-- Configuring library: MRML/Widgets<br>
47&gt;-- Looking for decorator header qMRMLWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qMRMLWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
47&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTCore<br>
47&gt;-- Looking for decorator header qSlicerBaseQTCorePythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerBaseQTCorePythonQtDecorators.h - Found<br>
47&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTGUI<br>
47&gt;-- Looking for decorator header qSlicerBaseQTGUIPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerBaseQTGUIPythonQtDecorators.h - Found<br>
47&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTCLI<br>
47&gt;-- Looking for decorator header qSlicerBaseQTCLIPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerBaseQTCLIPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring SEM CLI module: CLIModule4Test<br>
47&gt;-- Configuring Slicer Qt base library: qSlicerModulesCore<br>
47&gt;-- Configuring Slicer Qt base library: qSlicerBaseQTApp<br>
47&gt;-- Looking for decorator header qSlicerBaseQTAppPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerBaseQTAppPythonQtDecorators.h - Found<br>
47&gt;-- Configuring Loadable module: Cameras [qSlicerCamerasModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerUnitsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerUnitsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Units [qSlicerUnitsModuleExport.h]<br>
47&gt;-- RapidJSON found. Headers: ./include/Slicer-4.11<br>
47&gt;-- Looking for decorator header qSlicerTerminologiesModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerTerminologiesModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Terminologies [qSlicerTerminologiesModuleExport.h]<br>
47&gt;-- Configuring Loadable module: Colors [qSlicerColorsModuleExport.h]<br>
47&gt;-- Configuring Scripted module: ColorsScalarBarSelfTest<br>
47&gt;-- Looking for decorator header qSlicerSubjectHierarchyModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerSubjectHierarchyModuleWidgetsPythonQtDecorators.h - Found<br>
47&gt;-- Configuring Loadable module: SubjectHierarchy [qSlicerSubjectHierarchyModuleExport.h]<br>
47&gt;-- Configuring Scripted module: SubjectHierarchyCorePluginsSelfTest<br>
47&gt;-- Configuring Scripted module: SubjectHierarchyGenericSelfTest<br>
47&gt;-- Looking for decorator header qSlicerAnnotationsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerAnnotationsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Annotations [qSlicerAnnotationsModuleExport.h]<br>
47&gt;-- RapidJSON found. Headers: ./include/Slicer-4.11<br>
47&gt;-- Looking for decorator header qSlicerMarkupsSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerMarkupsSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerMarkupsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerMarkupsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Scripted module: MarkupsWidgetsSelfTest<br>
47&gt;-- Configuring Loadable module: Markups [qSlicerMarkupsModuleExport.h]<br>
47&gt;-- Configuring Scripted module: AddManyMarkupsFiducialTest<br>
47&gt;-- Configuring Scripted module: NeurosurgicalPlanningTutorialMarkupsSelfTest<br>
47&gt;-- Configuring Scripted module: MarkupsInCompareViewersSelfTest<br>
47&gt;-- Configuring Scripted module: MarkupsInViewsSelfTest<br>
47&gt;-- Looking for decorator header qSlicerTransformsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerTransformsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerTransformsSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerTransformsSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Transforms [qSlicerTransformsModuleExport.h]<br>
47&gt;-- Configuring Loadable module: Data [qSlicerDataModuleExport.h]<br>
47&gt;-- Configuring Loadable module: DoubleArrays [qSlicerDoubleArraysModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerModelsSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerModelsSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerModelsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerModelsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Models [qSlicerModelsModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerPlotsSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerPlotsSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerPlotsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerPlotsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Plots [qSlicerPlotsModuleExport.h]<br>
47&gt;-- Configuring Scripted module: PlotsSelfTest<br>
47&gt;-- Looking for decorator header qSlicerSceneViewsSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerSceneViewsSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: SceneViews [qSlicerSceneViewsModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerSegmentationsEditorEffectsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerSegmentationsEditorEffectsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerSegmentationsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerSegmentationsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerSegmentationsSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerSegmentationsSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Segmentations [qSlicerSegmentationsModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerSequencesModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerSequencesModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Sequences [qSlicerSequencesModuleExport.h]<br>
47&gt;-- Configuring Loadable module: Welcome [qSlicerWelcomeModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerTablesSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerTablesSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerTablesModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerTablesModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Tables [qSlicerTablesModuleExport.h]<br>
47&gt;-- Configuring Scripted module: TablesSelfTest<br>
47&gt;-- Looking for decorator header qSlicerTextsModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerTextsModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerTextsSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerTextsSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Texts [qSlicerTextsModuleExport.h]<br>
47&gt;-- Configuring Loadable module: Reformat [qSlicerReformatModuleExport.h]<br>
47&gt;-- Configuring Loadable module: ViewControllers [qSlicerViewControllersModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerVolumesSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerVolumesSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerVolumesModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerVolumesModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: Volumes [qSlicerVolumesModuleExport.h]<br>
47&gt;-- Looking for decorator header qSlicerVolumeRenderingModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerVolumeRenderingModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: VolumeRendering [qSlicerVolumeRenderingModuleExport.h]<br>
47&gt;VolumeRendering CXX tests: TEMP var: C:/D/S4R/Slicer-build/Testing/Temporary<br>
47&gt;-- Configuring Loadable module: CropVolume [qSlicerCropVolumeModuleExport.h]<br>
47&gt;-- Configuring Scripted module: CropVolumeSelfTest<br>
47&gt;-- Configuring Scripted module: CropVolumeSequence<br>
47&gt;-- Configuring Scripted module: DataProbe<br>
47&gt;-- Configuring Scripted module: Editor<br>
47&gt;-- Configuring Scripted module: EditorLib<br>
47&gt;-- Configuring Scripted module: LabelStatistics<br>
47&gt;-- Configuring Scripted module: PerformanceTests<br>
47&gt;-- Configuring Scripted module: SampleData<br>
47&gt;-- Configuring Scripted module: ScreenCapture<br>
47&gt;-- Configuring Scripted module: SegmentEditor<br>
47&gt;-- Configuring Scripted module: SegmentStatistics<br>
47&gt;-- Configuring Scripted module: SelfTests<br>
47&gt;-- Configuring Scripted module: VectorToScalarVolume<br>
47&gt;-- Configuring Scripted module: DMRIInstall<br>
47&gt;-- Configuring Scripted module: ExtensionWizard<br>
47&gt;-- Configuring Scripted module: Endoscopy<br>
47&gt;-- Configuring Scripted module: DICOM<br>
47&gt;-- Looking for decorator header qSlicerDICOMLibModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerDICOMLibModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Looking for decorator header qSlicerDICOMLibSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerDICOMLibSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Scripted module: DICOMLib<br>
47&gt;-- Configuring Scripted module: DICOMPlugins<br>
47&gt;-- Configuring Scripted module: DICOMPatcher<br>
47&gt;-- Configuring SEM CLI module: ACPCTransform<br>
47&gt;-- Configuring SEM CLI module: AddScalarVolumes<br>
47&gt;-- Configuring SEM CLI module: CastScalarVolume<br>
47&gt;-- Configuring SEM CLI module: CheckerBoardFilter<br>
47&gt;-- Configuring SEM CLI module: CurvatureAnisotropicDiffusion<br>
47&gt;-- Configuring SEM CLI module: ExecutionModelTour<br>
47&gt;-- Configuring SEM CLI module: ExtractSkeleton<br>
47&gt;-- Configuring SEM CLI module: GaussianBlurImageFilter<br>
47&gt;-- Configuring SEM CLI module: GradientAnisotropicDiffusion<br>
47&gt;-- Configuring SEM CLI module: GrayscaleFillHoleImageFilter<br>
47&gt;-- Configuring SEM CLI module: GrayscaleGrindPeakImageFilter<br>
47&gt;-- Configuring SEM CLI module: GrayscaleModelMaker<br>
47&gt;-- Configuring SEM CLI module: HistogramMatching<br>
47&gt;-- Configuring SEM CLI module: ImageLabelCombine<br>
47&gt;-- Configuring SEM CLI module: LabelMapSmoothing<br>
47&gt;-- Configuring SEM CLI module: MaskScalarVolume<br>
47&gt;-- Configuring SEM CLI module: MedianImageFilter<br>
47&gt;-- Configuring SEM CLI module: MergeModels<br>
47&gt;-- Configuring SEM CLI module: ModelMaker<br>
47&gt;-- Configuring SEM CLI module: ModelToLabelMap<br>
47&gt;-- Configuring SEM CLI module: MultiplyScalarVolumes<br>
47&gt;-- Configuring SEM CLI module: N4ITKBiasFieldCorrection<br>
47&gt;-- Configuring SEM CLI module: OrientScalarVolume<br>
47&gt;-- Configuring SEM CLI module: ProbeVolumeWithModel<br>
47&gt;-- Configuring SEM CLI module: ResampleDTIVolume<br>
47&gt;-- Configuring SEM CLI module: ResampleScalarVectorDWIVolume<br>
47&gt;-- Configuring SEM CLI module: RobustStatisticsSegmenter<br>
47&gt;-- Configuring SEM CLI module: SimpleRegionGrowingSegmentation<br>
47&gt;-- Configuring SEM CLI module: SubtractScalarVolumes<br>
47&gt;-- Configuring SEM CLI module: ThresholdScalarVolume<br>
47&gt;-- Configuring SEM CLI module: VotingBinaryHoleFillingImageFilter<br>
47&gt;-- Configuring SEM CLI module: CLIROITest<br>
47&gt;-- Configuring SEM CLI module: CreateDICOMSeries<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
47&gt;-- Configuring SEM CLI module: PETStandardUptakeValueComputation<br>
47&gt;-- Configuring SEM CLI module: ExpertAutomatedRegistration<br>
47&gt;-- Configuring SEM CLI module: FiducialRegistration<br>
47&gt;-- Configuring SEM CLI module: ResampleScalarVolume<br>
47&gt;-- Configuring SEM CLI module: DiffusionTensorTest<br>
47&gt;-- Configuring SEM CLI module: TestGridTransformRegistration<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring Slicer application library: qSlicerApp<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Setting Slicer DESCRIPTION_SUMMARY to ‘Medical Visualization and Processing Environment for Research’<br>
47&gt;-- Setting Slicer DESCRIPTION_FILE to ‘C:/D/S4/README.txt’<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring Slicer application: SlicerApp<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Setting Slicer APPLICATION_NAME to ‘Slicer’<br>
47&gt;-- Setting Slicer LAUNCHER_SPLASHSCREEN_FILE to ‘C:/D/S4/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png’<br>
47&gt;-- Setting Slicer APPLE_ICON_FILE to ‘C:/D/S4/Applications/SlicerApp/Resources/Slicer.icns’<br>
47&gt;-- Setting Slicer WIN_ICON_FILE to ‘C:/D/S4/Applications/SlicerApp/Resources/Slicer.ico’<br>
47&gt;-- Setting Slicer LICENSE_FILE to ‘C:/D/S4/License.txt’<br>
47&gt;-- Setting Slicer executable name to ‘SlicerApp-real.exe’<br>
47&gt;-- Setting Slicer EXECUTABLE to ‘C:/D/S4R/Slicer-build/bin/SlicerApp-real.exe’<br>
47&gt;-- Enabling Slicer build tree launcher option: --VisualStudio<br>
47&gt;-- Enabling Slicer build tree launcher option: --VisualStudioProject<br>
47&gt;-- Enabling Slicer build tree launcher option: --cmd<br>
47&gt;-- Enabling Slicer install tree launcher option: --cmd<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: MultiVolumeExplorer<br>
47&gt;-- Configuring Loadable module: MultiVolumeExplorer [qSlicerMultiVolumeExplorerModuleExport.h]<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: MultiVolumeImporter<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: SimpleFilters<br>
47&gt;-- Checking EXTENSION_NAME variable<br>
47&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED<br>
47&gt;-- Checking MODULE_NAME variable<br>
47&gt;-- Checking MODULE_NAME variable - NOTDEFINED<br>
47&gt;-- Checking PROJECT_NAME variable<br>
47&gt;-- Checking PROJECT_NAME variable - SimpleFilters<br>
47&gt;-- Setting EXTENSION_NAME …: SimpleFilters<br>
47&gt;-- Configuring Scripted module: SimpleFilters<br>
47&gt;-- Skipping extension packaging: SimpleFilters - Slicer_SOURCE_DIR is defined.<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: BRAINSTools<br>
47&gt;CMake Warning at C:/D/S4R/BRAINSTools/Version.cmake:29 (message):<br>
47&gt;  VERSION_MINOR from project not match git tag version: “2” EQUAL “0”<br>
47&gt;Call Stack (most recent call first):<br>
47&gt;  C:/D/S4R/BRAINSTools/CMakeLists.txt:61 (include)<br>
47&gt;<br>
47&gt;<br>
47&gt;-- BUILD_FOR_DASHBOARD: OFF<br>
47&gt;-- BRAINSTools_BUILD_DICOM_SUPPORT: ON<br>
47&gt;-- BRAINSTools_VERSION_MAJOR 5<br>
47&gt;-- BRAINSTools_VERSION_MINOR 2<br>
47&gt;-- BRAINSTools_VERSION_PATCH 0<br>
47&gt;-- BRAINSTools_VERSION_TWEAK<br>
47&gt;-- BRAINSTools_VERSION_RC<br>
47&gt;-- BRAINSTools_VERSION_HASH  de71a<br>
47&gt;-- BRAINSTools_VERSION_POST<br>
47&gt;-- BRAINSTools_VERSION_DEV   379<br>
47&gt;-- Building BRAINSTools version “5.2.0…dev379-gde71a”<br>
47&gt;-- Configuring SEM CLI module: BRAINSFit<br>
47&gt;-- Configuring SEM CLI module: PerformMetricTest<br>
47&gt;-- Configuring SEM CLI module: BRAINSResample<br>
47&gt;-- Configuring SEM CLI module: BRAINSResize<br>
47&gt;-- Configuring SEM CLI module: BRAINSROIAuto<br>
47&gt;-- Configuring SEM CLI module: DWIConvert<br>
47&gt;-- Configuring SEM CLI module: BRAINSLabelStats<br>
47&gt;-- Configuring SEM CLI module: BRAINSDWICleanup<br>
47&gt;-- Configuring SEM CLI module: BRAINSTransformConvert<br>
47&gt;-- Configuring SEM CLI module: BRAINSStripRotation<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: DataStore<br>
47&gt;-- Checking EXTENSION_NAME variable<br>
47&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED<br>
47&gt;-- Checking MODULE_NAME variable<br>
47&gt;-- Checking MODULE_NAME variable - NOTDEFINED<br>
47&gt;-- Checking PROJECT_NAME variable<br>
47&gt;-- Checking PROJECT_NAME variable - DataStore<br>
47&gt;-- Setting EXTENSION_NAME …: DataStore<br>
47&gt;-- Looking for decorator header qSlicerDataStoreModuleWidgetsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerDataStoreModuleWidgetsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: DataStore [qSlicerDataStoreModuleExport.h]<br>
47&gt;-- Skipping extension packaging: DataStore - Slicer_SOURCE_DIR is defined.<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: CompareVolumes<br>
47&gt;-- Configuring Scripted module: CompareVolumes<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: LandmarkRegistration<br>
47&gt;-- Configuring Scripted module: LandmarkRegistration<br>
47&gt;-- --------------------------------------------------<br>
47&gt;-- Configuring remote module: SurfaceToolbox<br>
47&gt;-- Checking EXTENSION_NAME variable<br>
47&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED<br>
47&gt;-- Checking MODULE_NAME variable<br>
47&gt;-- Checking MODULE_NAME variable - NOTDEFINED<br>
47&gt;-- Checking PROJECT_NAME variable<br>
47&gt;-- Checking PROJECT_NAME variable - SurfaceToolbox<br>
47&gt;-- Setting EXTENSION_NAME …: SurfaceToolbox<br>
47&gt;-- Configuring SEM CLI module: BordersOut<br>
47&gt;-- Configuring SEM CLI module: Cleaner<br>
47&gt;-- Configuring SEM CLI module: Connectivity<br>
47&gt;-- Configuring SEM CLI module: Decimation<br>
47&gt;-- Configuring SEM CLI module: FillHoles<br>
47&gt;-- Configuring SEM CLI module: MC2Origin<br>
47&gt;-- Configuring SEM CLI module: Mirror<br>
47&gt;-- Configuring SEM CLI module: Normals<br>
47&gt;-- Configuring SEM CLI module: relaxPolygons<br>
47&gt;-- Configuring SEM CLI module: Smoothing<br>
47&gt;-- Configuring Scripted module: SurfaceToolbox<br>
47&gt;-- Configuring SEM CLI module: scaleMesh<br>
47&gt;-- Configuring SEM CLI module: translateMesh<br>
47&gt;-- Looking for decorator header qSlicerDynamicModelerSubjectHierarchyPluginsPythonQtDecorators.h<br>
47&gt;-- Looking for decorator header qSlicerDynamicModelerSubjectHierarchyPluginsPythonQtDecorators.h - Not found<br>
47&gt;-- Configuring Loadable module: DynamicModeler [qSlicerDynamicModelerModuleExport.h]<br>
47&gt;-- Skipping extension packaging: SurfaceToolbox - Slicer_SOURCE_DIR is defined.<br>
47&gt;CMake Warning at Utilities/Scripts/SlicerWizard/doc/CMakeLists.txt:41 (message):<br>
47&gt;CUSTOMBUILD : warning : sphinx-build not found: Python documentation will not be created<br>
47&gt;<br>
47&gt;<br>
47&gt;-- Setting ‘CTEST_MODEL’ variable with default value ‘Experimental’<br>
47&gt;-- Setting ‘MIDAS_PACKAGE_URL’ variable with default value ‘<a href="http://slicer.kitware.com/midas3" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3</a>’<br>
47&gt;-- Setting ‘MIDAS_PACKAGE_EMAIL’ variable with default value ‘OBFUSCATED’<br>
47&gt;-- Setting ‘MIDAS_PACKAGE_API_KEY’ variable with default value ‘OBFUSCATED’<br>
47&gt;CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):<br>
47&gt;  Skipping repository info extraction: directory [C:/D/S4] is not a GIT or<br>
47&gt;  SVN checkout<br>
47&gt;Call Stack (most recent call first):<br>
47&gt;  CMake/SlicerPackageAndUploadTarget.cmake:100 (SlicerMacroExtractRepositoryInfo)<br>
47&gt;  CMake/LastConfigureStep/CMakeLists.txt:41 (include)<br>
47&gt;This warning is for project developers.  Use -Wno-dev to suppress it.<br>
47&gt;<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake<br>
47&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
47&gt;-- Setting CPACK_PACKAGE_NAME to ‘Slicer’<br>
47&gt;-- Setting CPACK_PACKAGE_VENDOR to ‘NA-MIC’<br>
47&gt;-- Setting CPACK_PACKAGE_VERSION_MAJOR to ‘4’<br>
47&gt;-- Setting CPACK_PACKAGE_VERSION_MINOR to ‘11’<br>
47&gt;-- Setting CPACK_PACKAGE_VERSION_PATCH to ‘20200930’<br>
47&gt;-- Setting CPACK_PACKAGE_VERSION to ‘4.11.20200930-0000-00-00’<br>
47&gt;-- Setting CPACK_PACKAGE_INSTALL_DIRECTORY to ‘Slicer 4.11.20200930-0000-00-00’<br>
47&gt;-- Setting CPACK_PACKAGE_DESCRIPTION_FILE to ‘C:/D/S4/README.txt’<br>
47&gt;-- Setting CPACK_RESOURCE_FILE_LICENSE to ‘C:/D/S4/License.txt’<br>
47&gt;-- Setting CPACK_PACKAGE_DESCRIPTION_SUMMARY to ‘Medical Visualization and Processing Environment for Research’<br>
47&gt;-- Setting CPACK_NSIS_INSTALL_SUBDIRECTORY to ‘’<br>
47&gt;-- Setting CPACK_NSIS_PACKAGE_NAME to ‘Slicer 4.11.20200930-0000-00-00’<br>
47&gt;-- Setting CPACK_PACKAGE_INSTALL_REGISTRY_KEY to ‘Slicer 4.11.20200930-0000-00-00 (Win64)’<br>
47&gt;-- Setting CPACK_NSIS_INSTALL_ROOT to ‘$LOCALAPPDATA\NA-MIC’<br>
47&gt;-- Setting CPACK_PACKAGE_EXECUTABLES to ‘…\Slicer;Slicer 4.11.20200930-0000-00-00’<br>
47&gt;-- Configuring done<br>
47&gt;-- Generating done<br>
47&gt;-- Build files have been written to: C:/D/S4R/Slicer-build<br>
47&gt;Performing build step for ‘Slicer’<br>
47&gt;.NET Framework용 Microsoft (R) Build Engine 버전 15.9.21+g9802d43bc3<br>
47&gt;Copyright (C) Microsoft Corporation. All rights reserved.<br>
47&gt;<br>
47&gt;  ITKFactoryRegistration.vcxproj → C:\D\S4R\Slicer-build\bin\Release\ITKFactoryRegistration.dll<br>
47&gt;  Configuring vtkSlicerVersionConfigure.h<br>
47&gt;  – Configuring Slicer release type [Experimental]<br>
47&gt;  CMake Warning (dev) at C:/D/S4/CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):<br>
47&gt;    Skipping repository info extraction: directory [C:/D/S4] is not a GIT or<br>
47&gt;    SVN checkout<br>
47&gt;  Call Stack (most recent call first):<br>
47&gt;    C:/D/S4/CMake/SlicerVersion.cmake:55 (SlicerMacroExtractRepositoryInfo)<br>
47&gt;    C:/D/S4/CMake/SlicerConfigureVersionHeaderTarget.cmake:131 (include)<br>
47&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
47&gt;<br>
47&gt;  – Configuring Slicer version [4.11.20200930-0000-00-00]<br>
47&gt;  – Configuring Slicer revision [3037]<br>
47&gt;  CMake Warning (dev) at C:/D/S4/CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):<br>
47&gt;    Skipping repository info extraction: directory [C:/D/S4] is not a GIT or<br>
47&gt;    SVN checkout<br>
47&gt;  Call Stack (most recent call first):<br>
47&gt;    C:/D/S4/CMake/SlicerVersion.cmake:99 (SlicerMacroExtractRepositoryInfo)<br>
47&gt;    C:/D/S4/CMake/SlicerConfigureVersionHeaderTarget.cmake:131 (include)<br>
47&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
47&gt;<br>
47&gt;  vtkAddon.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkAddon.dll<br>
47&gt;  vtkITK.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkITK.dll<br>
47&gt;  For vtkSegmentationCore - updating vtkSegmentationCoreHierarchy.txt<br>
47&gt;  vtkOrientedImageData.cxx<br>
47&gt;  vtkOrientedImageDataResample.cxx<br>
47&gt;  vtkSegment.cxx<br>
47&gt;  vtkSegmentation.cxx<br>
47&gt;  vtkSegmentationConverter.cxx<br>
47&gt;  vtkSegmentationConverterFactory.cxx<br>
47&gt;  vtkSegmentationConverterRule.cxx<br>
47&gt;  vtkSegmentationHistory.cxx<br>
47&gt;  vtkSegmentationModifier.cxx<br>
47&gt;  vtkTopologicalHierarchy.cxx<br>
47&gt;  vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx<br>
47&gt;  vtkClosedSurfaceToBinaryLabelmapConversionRule.cxx<br>
47&gt;  vtkCalculateOversamplingFactor.cxx<br>
47&gt;  vtkClosedSurfaceToFractionalLabelmapConversionRule.cxx<br>
47&gt;  vtkFractionalLabelmapToClosedSurfaceConversionRule.cxx<br>
47&gt;  vtkPolyDataToFractionalLabelmapFilter.cxx<br>
47&gt;  코드를 생성하고 있습니다…<br>
47&gt;     C:/D/S4R/Slicer-build/lib/Slicer-4.11/Release/vtkSegmentationCore.lib 라이브러리 및 C:/D/S4R/Slicer-build/lib/Slicer-4.11/Release/vtkSegmentationCore.exp 개체를 생성하고 있습니다.<br>
47&gt;  vtkSegmentationCore.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkSegmentationCore.dll<br>
47&gt;  vtkTeem.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkTeem.dll<br>
47&gt;  For MRMLCore - updating MRMLCoreHierarchy.txt<br>
47&gt;  vtkArchive.cxx<br>
47&gt;C:\D\S4\Libs\MRML\Core\vtkArchive.cxx(17): fatal error C1083: 포함 파일을 열 수 없습니다. ‘archive.h’: No such file or directory [C:\D\S4R\Slicer-build\Libs\MRML\Core\MRMLCore.vcxproj]<br>
47&gt;  SlicerBaseCLI.vcxproj → C:\D\S4R\Slicer-build\bin\Release\SlicerBaseCLI.dll<br>
47&gt;  AddScalarVolumesLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\AddScalarVolumesLib.dll<br>
47&gt;  AddScalarVolumes.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\AddScalarVolumes.exe<br>
47&gt;  Copying XML file ‘AddScalarVolumes.xml’ along side the executable<br>
47&gt;  AddScalarVolumesTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\AddScalarVolumesTest.exe<br>
47&gt;  BRAINSCommonLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\Release\BRAINSCommonLib.lib<br>
47&gt;  BRAINSDWICleanupLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSDWICleanupLib.dll<br>
47&gt;  BRAINSDWICleanup.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSDWICleanup.exe<br>
47&gt;  Copying XML file ‘BRAINSDWICleanup.xml’ along side the executable<br>
47&gt;  BRAINSFitLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSFitLib.dll<br>
47&gt;  BRAINSFit.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSFit.exe<br>
47&gt;  Copying XML file ‘BRAINSFit.xml’ along side the executable<br>
47&gt;  BRAINSLabelStatsLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSLabelStatsLib.dll<br>
47&gt;  BRAINSLabelStats.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSLabelStats.exe<br>
47&gt;  Copying XML file ‘BRAINSLabelStats.xml’ along side the executable<br>
47&gt;  BRAINSROIAutoLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSROIAutoLib.dll<br>
47&gt;  BRAINSROIAuto.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSROIAuto.exe<br>
47&gt;  Copying XML file ‘BRAINSROIAuto.xml’ along side the executable<br>
47&gt;  BRAINSResampleLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSResampleLib.dll<br>
47&gt;  BRAINSResample.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSResample.exe<br>
47&gt;  Copying XML file ‘BRAINSResample.xml’ along side the executable<br>
47&gt;  BRAINSResizeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSResizeLib.dll<br>
47&gt;  BRAINSResize.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSResize.exe<br>
47&gt;  Copying XML file ‘BRAINSResize.xml’ along side the executable<br>
47&gt;  BRAINSStripRotationLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSStripRotationLib.dll<br>
47&gt;  BRAINSStripRotation.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSStripRotation.exe<br>
47&gt;  Copying XML file ‘BRAINSStripRotation.xml’ along side the executable<br>
47&gt;  BRAINSTransformConvertLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSTransformConvertLib.dll<br>
47&gt;  BRAINSTransformConvert.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BRAINSTransformConvert.exe<br>
47&gt;  Copying XML file ‘BRAINSTransformConvert.xml’ along side the executable<br>
47&gt;  BordersOutLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BordersOutLib.dll<br>
47&gt;  BordersOut.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\BordersOut.exe<br>
47&gt;  Copying XML file ‘BordersOut.xml’ along side the executable<br>
47&gt;  CLIModule4TestLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CLIModule4TestLib.dll<br>
47&gt;  SEMCommandLineLibraryWrapper.cxx<br>
47&gt;  CLIModule4Test.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CLIModule4Test.exe<br>
47&gt;  Copying XML file ‘CLIModule4Test.xml’ along side the executable<br>
47&gt;  CastScalarVolumeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CastScalarVolumeLib.dll<br>
47&gt;  CastScalarVolume.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CastScalarVolume.exe<br>
47&gt;  Copying XML file ‘CastScalarVolume.xml’ along side the executable<br>
47&gt;  CastScalarVolumeTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\CastScalarVolumeTest.exe<br>
47&gt;  CheckerBoardFilterLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CheckerBoardFilterLib.dll<br>
47&gt;  CheckerBoardFilter.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CheckerBoardFilter.exe<br>
47&gt;  Copying XML file ‘CheckerBoardFilter.xml’ along side the executable<br>
47&gt;  CheckerBoardFilterTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\CheckerBoardFilterTest.exe<br>
47&gt;  CleanerLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CleanerLib.dll<br>
47&gt;  Cleaner.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\Cleaner.exe<br>
47&gt;  Copying XML file ‘Cleaner.xml’ along side the executable<br>
47&gt;  ConnectivityLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ConnectivityLib.dll<br>
47&gt;  Connectivity.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\Connectivity.exe<br>
47&gt;  Copying XML file ‘Connectivity.xml’ along side the executable<br>
47&gt;  DWIConvertSupportLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\Release\DWIConvertSupportLib.lib<br>
47&gt;  Convert4DImageTo3DSeries.vcxproj → C:\D\S4R\Slicer-build\bin\Release\Convert4DImageTo3DSeries.exe<br>
47&gt;  CreateDICOMSeriesLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CreateDICOMSeriesLib.dll<br>
47&gt;  CreateDICOMSeries.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CreateDICOMSeries.exe<br>
47&gt;  Copying XML file ‘CreateDICOMSeries.xml’ along side the executable<br>
47&gt;  CreateDICOMSeriesTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\CreateDICOMSeriesTest.exe<br>
47&gt;  CurvatureAnisotropicDiffusionLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CurvatureAnisotropicDiffusionLib.dll<br>
47&gt;  CurvatureAnisotropicDiffusion.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\CurvatureAnisotropicDiffusion.exe<br>
47&gt;  Copying XML file ‘CurvatureAnisotropicDiffusion.xml’ along side the executable<br>
47&gt;  DWIConvertLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\DWIConvertLib.lib<br>
47&gt;  DWIConvert.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\DWIConvert.exe<br>
47&gt;  Copying XML file ‘DWIConvert.xml’ along side the executable<br>
47&gt;  DecimationLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\DecimationLib.dll<br>
47&gt;  Decimation.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\Decimation.exe<br>
47&gt;  Copying XML file ‘Decimation.xml’ along side the executable<br>
47&gt;  DiffusionTensorTestLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\DiffusionTensorTestLib.dll<br>
47&gt;  DiffusionTensorTest.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\DiffusionTensorTest.exe<br>
47&gt;  Copying XML file ‘DiffusionTensorTest.xml’ along side the executable<br>
47&gt;  DiffusionTensorTestTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\DiffusionTensorTestTest.exe<br>
47&gt;  For MRMLCore - updating MRMLCoreHierarchy.txt<br>
47&gt;  For vtkSegmentationCore - updating vtkSegmentationCoreHierarchy.txt<br>
47&gt;  ExpertAutomatedRegistrationLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ExpertAutomatedRegistrationLib.dll<br>
47&gt;  ExpertAutomatedRegistration.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ExpertAutomatedRegistration.exe<br>
47&gt;  Copying XML file ‘ExpertAutomatedRegistration.xml’ along side the executable<br>
47&gt;  FiducialRegistrationLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\FiducialRegistrationLib.dll<br>
47&gt;  FiducialRegistration.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\FiducialRegistration.exe<br>
47&gt;  Copying XML file ‘FiducialRegistration.xml’ along side the executable<br>
47&gt;  FiducialRegistrationTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\FiducialRegistrationTest.exe<br>
47&gt;  FillHolesLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\FillHolesLib.dll<br>
47&gt;  FillHoles.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\FillHoles.exe<br>
47&gt;  Copying XML file ‘FillHoles.xml’ along side the executable<br>
47&gt;  GaussianBlurImageFilterLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GaussianBlurImageFilterLib.dll<br>
47&gt;  GaussianBlurImageFilter.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GaussianBlurImageFilter.exe<br>
47&gt;  Copying XML file ‘GaussianBlurImageFilter.xml’ along side the executable<br>
47&gt;  GaussianBlurImageFilterTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\GaussianBlurImageFilterTest.exe<br>
47&gt;  GenerateExpertAutomatedRegistrationTestData.vcxproj → C:\D\S4R\Slicer-build\bin\Release\GenerateExpertAutomatedRegistrationTestData.exe<br>
47&gt;  GradientAnisotropicDiffusionLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GradientAnisotropicDiffusionLib.dll<br>
47&gt;  GradientAnisotropicDiffusion.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GradientAnisotropicDiffusion.exe<br>
47&gt;  Copying XML file ‘GradientAnisotropicDiffusion.xml’ along side the executable<br>
47&gt;  GradientAnisotropicDiffusionTestWithImageSpacingOff.vcxproj → C:\D\S4R\Slicer-build\bin\Release\GradientAnisotropicDiffusionTestWithImageSpacingOff.exe<br>
47&gt;  GradientAnisotropicDiffusionTestWithImageSpacingOn.vcxproj → C:\D\S4R\Slicer-build\bin\Release\GradientAnisotropicDiffusionTestWithImageSpacingOn.exe<br>
47&gt;  GrayscaleFillHoleImageFilterLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GrayscaleFillHoleImageFilterLib.dll<br>
47&gt;  GrayscaleFillHoleImageFilter.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GrayscaleFillHoleImageFilter.exe<br>
47&gt;  Copying XML file ‘GrayscaleFillHoleImageFilter.xml’ along side the executable<br>
47&gt;  GrayscaleFillHoleImageFilterTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\GrayscaleFillHoleImageFilterTest.exe<br>
47&gt;  GrayscaleGrindPeakImageFilterLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GrayscaleGrindPeakImageFilterLib.dll<br>
47&gt;  GrayscaleGrindPeakImageFilter.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\GrayscaleGrindPeakImageFilter.exe<br>
47&gt;  Copying XML file ‘GrayscaleGrindPeakImageFilter.xml’ along side the executable<br>
47&gt;  GrayscaleGrindPeakImageFilterTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\GrayscaleGrindPeakImageFilterTest.exe<br>
47&gt;  HistogramMatchingLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\HistogramMatchingLib.dll<br>
47&gt;  HistogramMatching.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\HistogramMatching.exe<br>
47&gt;  Copying XML file ‘HistogramMatching.xml’ along side the executable<br>
47&gt;  HistogramMatchingTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\HistogramMatchingTest.exe<br>
47&gt;  ImageLabelCombineLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ImageLabelCombineLib.dll<br>
47&gt;  ImageLabelCombine.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ImageLabelCombine.exe<br>
47&gt;  Copying XML file ‘ImageLabelCombine.xml’ along side the executable<br>
47&gt;  ImageLabelCombineTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\ImageLabelCombineTest.exe<br>
47&gt;  LabelMapSmoothingLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\LabelMapSmoothingLib.dll<br>
47&gt;  LabelMapSmoothing.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\LabelMapSmoothing.exe<br>
47&gt;  Copying XML file ‘LabelMapSmoothing.xml’ along side the executable<br>
47&gt;  LabelMapSmoothingTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\LabelMapSmoothingTest.exe<br>
47&gt;  MC2OriginLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MC2OriginLib.dll<br>
47&gt;  MC2Origin.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MC2Origin.exe<br>
47&gt;  Copying XML file ‘MC2Origin.xml’ along side the executable<br>
47&gt;  MaskScalarVolumeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MaskScalarVolumeLib.dll<br>
47&gt;  MaskScalarVolume.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MaskScalarVolume.exe<br>
47&gt;  Copying XML file ‘MaskScalarVolume.xml’ along side the executable<br>
47&gt;  MaskScalarVolumeTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\MaskScalarVolumeTest.exe<br>
47&gt;  MedianImageFilterLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MedianImageFilterLib.dll<br>
47&gt;  MedianImageFilter.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MedianImageFilter.exe<br>
47&gt;  Copying XML file ‘MedianImageFilter.xml’ along side the executable<br>
47&gt;  MedianImageFilterTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\MedianImageFilterTest.exe<br>
47&gt;  MirrorLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MirrorLib.dll<br>
47&gt;  Mirror.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\Mirror.exe<br>
47&gt;  Copying XML file ‘Mirror.xml’ along side the executable<br>
47&gt;  MultiplyScalarVolumesLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MultiplyScalarVolumesLib.dll<br>
47&gt;  MultiplyScalarVolumes.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\MultiplyScalarVolumes.exe<br>
47&gt;  Copying XML file ‘MultiplyScalarVolumes.xml’ along side the executable<br>
47&gt;  MultiplyScalarVolumesTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\MultiplyScalarVolumesTest.exe<br>
47&gt;  N4ITKBiasFieldCorrectionLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\N4ITKBiasFieldCorrectionLib.dll<br>
47&gt;  N4ITKBiasFieldCorrection.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\N4ITKBiasFieldCorrection.exe<br>
47&gt;  Copying XML file ‘N4ITKBiasFieldCorrection.xml’ along side the executable<br>
47&gt;  N4ITKBiasFieldCorrectionTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\N4ITKBiasFieldCorrectionTest.exe<br>
47&gt;  NormalsLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\NormalsLib.dll<br>
47&gt;  Normals.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\Normals.exe<br>
47&gt;  Copying XML file ‘Normals.xml’ along side the executable<br>
47&gt;  OrientScalarVolumeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\OrientScalarVolumeLib.dll<br>
47&gt;  OrientScalarVolume.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\OrientScalarVolume.exe<br>
47&gt;  Copying XML file ‘OrientScalarVolume.xml’ along side the executable<br>
47&gt;  OrientScalarVolumeTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\OrientScalarVolumeTest.exe<br>
47&gt;  PerformMetricTestLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\PerformMetricTestLib.dll<br>
47&gt;  PerformMetricTest.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\PerformMetricTest.exe<br>
47&gt;  Copying XML file ‘PerformMetricTest.xml’ along side the executable<br>
47&gt;  ResampleDTIVolumeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ResampleDTIVolumeLib.dll<br>
47&gt;  ResampleDTIVolume.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ResampleDTIVolume.exe<br>
47&gt;  Copying XML file ‘ResampleDTIVolume.xml’ along side the executable<br>
47&gt;  ResampleDTIVolumeTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\ResampleDTIVolumeTest.exe<br>
47&gt;  ResampleScalarVectorDWIVolumeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ResampleScalarVectorDWIVolumeLib.dll<br>
47&gt;  ResampleScalarVectorDWIVolume.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ResampleScalarVectorDWIVolume.exe<br>
47&gt;  Copying XML file ‘ResampleScalarVectorDWIVolume.xml’ along side the executable<br>
47&gt;  ResampleScalarVectorDWIVolumeTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\ResampleScalarVectorDWIVolumeTest.exe<br>
47&gt;  ResampleScalarVolumeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ResampleScalarVolumeLib.dll<br>
47&gt;  ResampleScalarVolume.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ResampleScalarVolume.exe<br>
47&gt;  Copying XML file ‘ResampleScalarVolume.xml’ along side the executable<br>
47&gt;  ResampleScalarVolumeTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\ResampleScalarVolumeTest.exe<br>
47&gt;  RobustStatisticsSegmenterLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\RobustStatisticsSegmenterLib.dll<br>
47&gt;  RobustStatisticsSegmenter.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\RobustStatisticsSegmenter.exe<br>
47&gt;  Copying XML file ‘RobustStatisticsSegmenter.xml’ along side the executable<br>
47&gt;  SFLSRobustStat3DTestConsole.vcxproj → C:\D\S4R\Slicer-build\bin\Release\SFLSRobustStat3DTestConsole.exe<br>
47&gt;  SimpleRegionGrowingSegmentationLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\SimpleRegionGrowingSegmentationLib.dll<br>
47&gt;  SimpleRegionGrowingSegmentation.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\SimpleRegionGrowingSegmentation.exe<br>
47&gt;  Copying XML file ‘SimpleRegionGrowingSegmentation.xml’ along side the executable<br>
47&gt;  SimpleRegionGrowingSegmentationTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\SimpleRegionGrowingSegmentationTest.exe<br>
47&gt;  SmoothingLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\SmoothingLib.dll<br>
47&gt;  Smoothing.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\Smoothing.exe<br>
47&gt;  Copying XML file ‘Smoothing.xml’ along side the executable<br>
47&gt;  SubtractScalarVolumesLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\SubtractScalarVolumesLib.dll<br>
47&gt;  SubtractScalarVolumes.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\SubtractScalarVolumes.exe<br>
47&gt;  Copying XML file ‘SubtractScalarVolumes.xml’ along side the executable<br>
47&gt;  SubtractScalarVolumesTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\SubtractScalarVolumesTest.exe<br>
47&gt;  TestGridTransformRegistrationLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\TestGridTransformRegistrationLib.dll<br>
47&gt;  TestGridTransformRegistration.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\TestGridTransformRegistration.exe<br>
47&gt;  Copying XML file ‘TestGridTransformRegistration.xml’ along side the executable<br>
47&gt;  TestGridTransformRegistrationTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\TestGridTransformRegistrationTest.exe<br>
47&gt;  ThresholdScalarVolumeLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ThresholdScalarVolumeLib.dll<br>
47&gt;  ThresholdScalarVolume.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\ThresholdScalarVolume.exe<br>
47&gt;  Copying XML file ‘ThresholdScalarVolume.xml’ along side the executable<br>
47&gt;  ThresholdScalarVolumeTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\ThresholdScalarVolumeTest.exe<br>
47&gt;  VTKITKVectorReader.vcxproj → C:\D\S4R\Slicer-build\bin\Release\VTKITKVectorReader.exe<br>
47&gt;  VotingBinaryHoleFillingImageFilterLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\VotingBinaryHoleFillingImageFilterLib.dll<br>
47&gt;  VotingBinaryHoleFillingImageFilter.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\VotingBinaryHoleFillingImageFilter.exe<br>
47&gt;  Copying XML file ‘VotingBinaryHoleFillingImageFilter.xml’ along side the executable<br>
47&gt;  VotingBinaryHoleFillingImageFilterTest.vcxproj → C:\D\S4R\Slicer-build\bin\Release\VotingBinaryHoleFillingImageFilterTest.exe<br>
47&gt;  qSlicerIconEnginePlugin.vcxproj → C:\D\S4R\Slicer-build\bin\iconengines\Release\qSlicerIconEnginePlugin.dll<br>
47&gt;  relaxPolygonsLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\relaxPolygonsLib.dll<br>
47&gt;  relaxPolygons.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\relaxPolygons.exe<br>
47&gt;  Copying XML file ‘relaxPolygons.xml’ along side the executable<br>
47&gt;  scaleMeshLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\scaleMeshLib.dll<br>
47&gt;  scaleMesh.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\scaleMesh.exe<br>
47&gt;  Copying XML file ‘scaleMesh.xml’ along side the executable<br>
47&gt;  translateMeshLib.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\translateMeshLib.dll<br>
47&gt;  translateMesh.vcxproj → C:\D\S4R\Slicer-build\lib\Slicer-4.11\cli-modules\Release\translateMesh.exe<br>
47&gt;  Copying XML file ‘translateMesh.xml’ along side the executable<br>
47&gt;  vtkAddonCxxTests.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkAddonCxxTests.exe<br>
47&gt;  vtkAddonPythonD.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkAddonPythonD.dll<br>
47&gt;  vtkAddonPython.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkAddonPython.pyd<br>
47&gt;  vtkITKPythonD.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkITKPythonD.dll<br>
47&gt;  vtkITKPython.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkITKPython.pyd<br>
47&gt;  vtkSegmentationCoreCxxTests.cxx<br>
47&gt;  vtkSegmentationTest1.cxx<br>
47&gt;  vtkSegmentationTest2.cxx<br>
47&gt;  vtkSegmentationHistoryTest1.cxx<br>
47&gt;  vtkSegmentationConverterTest1.cxx<br>
47&gt;  vtkClosedSurfaceToFractionalLabelMapConversionTest1.cxx<br>
47&gt;  코드를 생성하고 있습니다…<br>
47&gt;  vtkSegmentationCoreCxxTests.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkSegmentationCoreCxxTests.exe<br>
47&gt;  Python Wrapping - generating vtkOrientedImageDataPython.cxx<br>
47&gt;  Python Wrapping - generating vtkOrientedImageDataResamplePython.cxx<br>
47&gt;  Python Wrapping - generating vtkSegmentPython.cxx<br>
47&gt;  Python Wrapping - generating vtkSegmentationPython.cxx<br>
47&gt;  Python Wrapping - generating vtkSegmentationConverterPython.cxx<br>
47&gt;  Python Wrapping - generating vtkSegmentationConverterFactoryPython.cxx<br>
47&gt;  Python Wrapping - generating vtkSegmentationConverterRulePython.cxx<br>
47&gt;  Python Wrapping - generating vtkSegmentationHistoryPython.cxx<br>
47&gt;  Python Wrapping - generating vtkSegmentationModifierPython.cxx<br>
47&gt;  Python Wrapping - generating vtkTopologicalHierarchyPython.cxx<br>
47&gt;  Python Wrapping - generating vtkBinaryLabelmapToClosedSurfaceConversionRulePython.cxx<br>
47&gt;  Python Wrapping - generating vtkClosedSurfaceToBinaryLabelmapConversionRulePython.cxx<br>
47&gt;  Python Wrapping - generating vtkCalculateOversamplingFactorPython.cxx<br>
47&gt;  Python Wrapping - generating vtkClosedSurfaceToFractionalLabelmapConversionRulePython.cxx<br>
47&gt;  Python Wrapping - generating vtkFractionalLabelmapToClosedSurfaceConversionRulePython.cxx<br>
47&gt;  Python Wrapping - generating vtkPolyDataToFractionalLabelmapFilterPython.cxx<br>
47&gt;  vtkOrientedImageDataPython.cxx<br>
47&gt;  vtkOrientedImageDataResamplePython.cxx<br>
47&gt;  vtkSegmentPython.cxx<br>
47&gt;  vtkSegmentationPython.cxx<br>
47&gt;  vtkSegmentationConverterPython.cxx<br>
47&gt;  vtkSegmentationConverterFactoryPython.cxx<br>
47&gt;  vtkSegmentationConverterRulePython.cxx<br>
47&gt;  vtkSegmentationHistoryPython.cxx<br>
47&gt;  vtkSegmentationModifierPython.cxx<br>
47&gt;  vtkTopologicalHierarchyPython.cxx<br>
47&gt;  vtkBinaryLabelmapToClosedSurfaceConversionRulePython.cxx<br>
47&gt;  vtkClosedSurfaceToBinaryLabelmapConversionRulePython.cxx<br>
47&gt;  vtkCalculateOversamplingFactorPython.cxx<br>
47&gt;  vtkClosedSurfaceToFractionalLabelmapConversionRulePython.cxx<br>
47&gt;  vtkFractionalLabelmapToClosedSurfaceConversionRulePython.cxx<br>
47&gt;  vtkPolyDataToFractionalLabelmapFilterPython.cxx<br>
47&gt;  vtkSegmentationCorePythonInitImpl.cxx<br>
47&gt;  코드를 생성하고 있습니다…<br>
47&gt;     C:/D/S4R/Slicer-build/lib/Slicer-4.11/Release/vtkSegmentationCorePythonD.lib 라이브러리 및 C:/D/S4R/Slicer-build/lib/Slicer-4.11/Release/vtkSegmentationCorePythonD.exp 개체를 생성하고 있습니다.<br>
47&gt;  vtkSegmentationCorePythonD.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkSegmentationCorePythonD.dll<br>
47&gt;  vtkSegmentationCorePythonInit.cxx<br>
47&gt;     C:/D/S4R/Slicer-build/lib/Slicer-4.11/Release/vtkSegmentationCorePython.lib 라이브러리 및 C:/D/S4R/Slicer-build/lib/Slicer-4.11/Release/vtkSegmentationCorePython.exp 개체를 생성하고 있습니다.<br>
47&gt;  vtkSegmentationCorePython.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkSegmentationCorePython.pyd<br>
47&gt;  vtkTeemPythonD.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkTeemPythonD.dll<br>
47&gt;  vtkTeemCxxTests.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkTeemCxxTests.exe<br>
47&gt;  vtkTeemPython.vcxproj → C:\D\S4R\Slicer-build\bin\Release\vtkTeemPython.pyd<br>
47&gt;“Slicer.vcxproj” 프로젝트를 빌드했습니다. - 실패<br>
========== 빌드: 성공 45, 실패 2, 최신 1, 생략 0 ==========</p>

---

## Post #8 by @kookoo9999 (2021-09-21 06:23 UTC)

<p>I am using Visual Studio 2017 v141 toolset, Qt 5.10.1 , CMake 3.15. when I try to build for Slicer-Master I can’t configure in CMake. and I changed Slicer Source from Master to 4.11 20200930 I succeeded configure and generate but failed build in Visual Studio …<br>
I am curious about your environment (about source : Slicer-Master, Visual Sutido’s version and toolset,CMake…Qt version)</p>

---

## Post #9 by @lassoan (2021-09-21 12:03 UTC)

<p>It is normal that the build fails if you use older tool or library versions than the required.</p>
<p>As described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">build instructions</a>, you need to use Visual Studio 2019 with toolset v142, Qt-5.15.x.</p>

---

## Post #11 by @kookoo9999 (2021-09-22 10:16 UTC)

<p>I can’t buy a license and use Qt…<br>
So I use and try visual studio 2107, toolset v141, Qt 5.10.1…(5.12.1 …) and every try is failed…</p>

---

## Post #12 by @pieper (2021-09-22 12:25 UTC)

<p>You can get 5.15.2 for free from <a href="https://www.qt.io/download-open-source?hsCtaTracking=9f6a2170-a938-42df-a8e2-a9f0b1d6cdce%7C6cb0de4f-9bb5-4778-ab02-bfb62735f3e5" class="inline-onebox">Open Source Development | Open Source License | Qt</a></p>

---

## Post #14 by @kookoo9999 (2021-09-22 13:30 UTC)

<p>After fail with 5.12 , now I am using 5.10.1 because I saw on the forum that you should write 5.10.1.<br>
Did you succeed to build in Windows10 ??</p>

---

## Post #15 by @pieper (2021-09-22 13:57 UTC)

<p>You need to use the latest Qt (5.15.2) not an old version.  Yes, my build works fine on windows 10 with visual studio 2019.</p>

---

## Post #17 by @kookoo9999 (2021-09-22 17:39 UTC)

<p>I just tried build Slicer-Master via Qt(5.15.1),VisualStudio 2019 (toolset v142) but failed too…</p>

---

## Post #18 by @jamesobutler (2021-09-22 17:42 UTC)

<p>Are you using a recent version of CMake? Your first image showed you were using 3.15.0-rc1? I’ve been successful building a recent Slicer <code>master</code> branch using CMake 3.21.2, Qt 5.15.2, and Visual Studio 2019 (v142).</p>
<p>When you are trying different versions are you clearing out your build tree completely and starting a fresh build?</p>

---

## Post #20 by @kookoo9999 (2021-09-22 17:46 UTC)

<p>ow I will try to build Slicer master branch after change CMake version and for fresh build , I will delete build tree change the Qt 5.15.2 and try again</p>

---

## Post #21 by @kookoo9999 (2021-09-23 06:08 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>  <a class="mention" href="/u/lassoan">@lassoan</a><br>
After I did clear the build tree, then I tried to build Slicer master branch via changed env Visual Studio 2019 (toolset v142) , Qt5.15.2, CMake 3.21.3  but build is failed…<br>
S4R\slicer.sln is can’t build and I can’t find slicer.exe,<br>
I don’t know why I can’t build . Please give me some advice.<br>
Attached is the result CMake txt below.</p>

---

## Post #22 by @kookoo9999 (2021-09-23 06:13 UTC)

<p>C:\D\S4R\slicer-build\CMakeFiles\CMakeError.txt</p>
<p>Determining if the CXX compiler accepts the flag -features=no%anachronisms passed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_04fe8.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_04fe8.dir\Debug\" /Fd"cmTC_04fe8.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  -features=no%%anachronisms “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 warning D9002: 알 수 없는 ‘-features=no%%anachronisms’ 옵션을 무시합니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_04fe8.vcxproj]</p>
<p>cmTC_04fe8.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_04fe8.exe</p>
<p>Source file was:<br>
int main() { return 0;}</p>
<p>Performing C SOURCE FILE Test C_HAS_WARNING-Wno-uninitialized failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_f66fd.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wno-uninitialized” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_f66fd.dir\Debug\" /Fd"cmTC_f66fd.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wno-uninitialized “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-uninitialized’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_f66fd.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wno-unused-parameter failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_4be86.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wno-unused-parameter” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_4be86.dir\Debug\" /Fd"cmTC_4be86.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wno-unused-parameter “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-unused-parameter’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_4be86.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wno-long-double failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_a09aa.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wno-long-double” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_a09aa.dir\Debug\" /Fd"cmTC_a09aa.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wno-long-double “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-long-double’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_a09aa.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wcast-align failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_05260.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wcast-align” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_05260.dir\Debug\" /Fd"cmTC_05260.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wcast-align “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wcast-align’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_05260.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wdisabled-optimization failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_15a34.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wdisabled-optimization” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_15a34.dir\Debug\" /Fd"cmTC_15a34.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wdisabled-optimization “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wdisabled-optimization’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_15a34.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wextra failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_9e748.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wextra” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_9e748.dir\Debug\" /Fd"cmTC_9e748.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wextra “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wextra’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_9e748.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wformat_2 failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_185f0.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wformat_2” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_185f0.dir\Debug\" /Fd"cmTC_185f0.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wformat=2 “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wformat=2’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_185f0.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Winvalid-pch failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_4d589.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Winvalid-pch” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_4d589.dir\Debug\" /Fd"cmTC_4d589.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Winvalid-pch “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Winvalid-pch’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_4d589.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wno-format-nonliteral failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_1efac.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wno-format-nonliteral” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_1efac.dir\Debug\" /Fd"cmTC_1efac.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wno-format-nonliteral “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-format-nonliteral’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_1efac.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wpointer-arith failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_f6a2a.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wpointer-arith” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_f6a2a.dir\Debug\" /Fd"cmTC_f6a2a.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wpointer-arith “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wpointer-arith’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_f6a2a.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wshadow failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_fc650.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wshadow” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_fc650.dir\Debug\" /Fd"cmTC_fc650.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wshadow “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wshadow’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_fc650.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wunused failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_6a0c1.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wunused” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_6a0c1.dir\Debug\" /Fd"cmTC_6a0c1.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wunused “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wunused’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_6a0c1.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wwrite-strings failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_7fccd.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wwrite-strings” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_7fccd.dir\Debug\" /Fd"cmTC_7fccd.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wwrite-strings “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wwrite-strings’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_7fccd.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-funit-at-a-time failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_f1d32.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.c</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-funit-at-a-time” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_f1d32.dir\Debug\" /Fd"cmTC_f1d32.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -funit-at-a-time “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 warning D9002: 알 수 없는 ‘-funit-at-a-time’ 옵션을 무시합니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_f1d32.vcxproj]</p>
<p>cmTC_f1d32.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_f1d32.exe</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C SOURCE FILE Test C_HAS_WARNING-Wno-strict-overflow failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_f1123.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-Wno-strict-overflow” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_f1123.dir\Debug\" /Fd"cmTC_f1123.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj -Wno-strict-overflow “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-strict-overflow’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_f1123.vcxproj]</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wno-long-double failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_a7674.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wno-long-double” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_a7674.dir\Debug\" /Fd"cmTC_a7674.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wno-long-double “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-long-double’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_a7674.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wcast-align failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_1a208.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wcast-align” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_1a208.dir\Debug\" /Fd"cmTC_1a208.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wcast-align “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wcast-align’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_1a208.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wdisabled-optimization failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_7a08f.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wdisabled-optimization” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_7a08f.dir\Debug\" /Fd"cmTC_7a08f.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wdisabled-optimization “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wdisabled-optimization’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_7a08f.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wextra failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_160ad.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wextra” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_160ad.dir\Debug\" /Fd"cmTC_160ad.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wextra “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wextra’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_160ad.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wformat_2 failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_e67af.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wformat_2” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_e67af.dir\Debug\" /Fd"cmTC_e67af.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wformat=2 “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wformat=2’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_e67af.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Winvalid-pch failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_bde73.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Winvalid-pch” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_bde73.dir\Debug\" /Fd"cmTC_bde73.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Winvalid-pch “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Winvalid-pch’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_bde73.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wno-format-nonliteral failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_4fec3.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wno-format-nonliteral” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_4fec3.dir\Debug\" /Fd"cmTC_4fec3.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wno-format-nonliteral “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-format-nonliteral’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_4fec3.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wpointer-arith failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_31f09.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wpointer-arith” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_31f09.dir\Debug\" /Fd"cmTC_31f09.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wpointer-arith “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wpointer-arith’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_31f09.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wshadow failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_7371a.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wshadow” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_7371a.dir\Debug\" /Fd"cmTC_7371a.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wshadow “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wshadow’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_7371a.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wunused failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_11ebd.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wunused” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_11ebd.dir\Debug\" /Fd"cmTC_11ebd.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wunused “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wunused’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_11ebd.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wwrite-strings failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_f1cf0.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wwrite-strings” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_f1cf0.dir\Debug\" /Fd"cmTC_f1cf0.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wwrite-strings “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wwrite-strings’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_f1cf0.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-funit-at-a-time failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_d0faa.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-funit-at-a-time” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_d0faa.dir\Debug\" /Fd"cmTC_d0faa.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -funit-at-a-time “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 warning D9002: 알 수 없는 ‘-funit-at-a-time’ 옵션을 무시합니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_d0faa.vcxproj]</p>
<p>cmTC_d0faa.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_d0faa.exe</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wno-strict-overflow failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_c1891.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wno-strict-overflow” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_c1891.dir\Debug\" /Fd"cmTC_c1891.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wno-strict-overflow “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-strict-overflow’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_c1891.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wno-deprecated failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_164e8.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wno-deprecated” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_164e8.dir\Debug\" /Fd"cmTC_164e8.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wno-deprecated “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-deprecated’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_164e8.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wno-invalid-offsetof failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_8685f.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wno-invalid-offsetof” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_8685f.dir\Debug\" /Fd"cmTC_8685f.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wno-invalid-offsetof “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-invalid-offsetof’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_8685f.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wno-undefined-var-template failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_e43b0.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wno-undefined-var-template” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_e43b0.dir\Debug\" /Fd"cmTC_e43b0.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wno-undefined-var-template “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wno-undefined-var-template’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_e43b0.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Woverloaded-virtual failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_6d091.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Woverloaded-virtual” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_6d091.dir\Debug\" /Fd"cmTC_6d091.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Woverloaded-virtual “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Woverloaded-virtual’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_6d091.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-Wstrict-null-sentinel failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_b934c.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-Wstrict-null-sentinel” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_b934c.dir\Debug\" /Fd"cmTC_b934c.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj -Wstrict-null-sentinel “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cl : 명령줄 error D8021: ‘/Wstrict-null-sentinel’ 숫자 인수가 잘못되었습니다. [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_b934c.vcxproj]</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test CXX_HAS_DISABLE_OPTIMIZATION_FLAG failed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_4497b.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D CXX_HAS_DISABLE_OPTIMIZATION_FLAG /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_4497b.dir\Debug\" /Fd"cmTC_4497b.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue  /bigobj /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx(1,1): error C2059: 구문 오류: ‘/’ [C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\cmTC_4497b.vcxproj]</p>
<p>Source file was:<br>
/Od</p>

---

## Post #23 by @kookoo9999 (2021-09-23 06:14 UTC)

<p>C:\D\S4R\slicer-build\CMakeOutput.txt</p>
<p>The system is: Windows - 10.0.19042 - AMD64<br>
Compiling the C compiler identification source file “CMakeCCompilerId.c” succeeded.<br>
Compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe<br>
Build flags: ;;/DWIN32;/D_WINDOWS;/W2;<br>
Id flags:</p>
<p>The output was:<br>
0<br>
.NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04<br>
Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>빌드 시작: 2021-09-23 오후 2:20:03<br>
1 노드의 “C:\D\S4R\Slicer-build\CMakeFiles\3.21.3\CompilerIdC\CompilerIdC.vcxproj” 프로젝트(기본 대상)입니다.<br>
PrepareForBuild:<br>
“Debug” 디렉터리를 만들고 있습니다.<br>
“Debug\CompilerIdC.tlog” 디렉터리를 만들고 있습니다.<br>
InitializeBuildStatus:<br>
“AlwaysCreate"이(가) 지정되었기 때문에 “Debug\CompilerIdC.tlog\unsuccessfulbuild"을(를) 만들고 있습니다.<br>
ClCompile:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\” /Fd"Debug\vc142.pdb” /external:W0 /Gd /TC /FC /errorReport:queue CMakeCCompilerId.c<br>
CMakeCCompilerId.c<br>
Link:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdC.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:“level=‘asInvoker’ uiAccess=‘false’” /manifest:embed /PDB:".\CompilerIdC.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdC.lib" /MACHINE:X64 Debug\CMakeCCompilerId.obj<br>
CompilerIdC.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\3.21.3\CompilerIdC\CompilerIdC.exe<br>
PostBuildEvent:<br>
for %%i in (cl.exe) do <span class="mention">@echo</span> CMAKE_C_COMPILER=%%~$PATH:i<br>
:VCEnd<br>
CMAKE_C_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe<br>
FinalizeBuildStatus:<br>
“Debug\CompilerIdC.tlog\unsuccessfulbuild” 파일을 삭제하고 있습니다.<br>
"Debug\CompilerIdC.tlog\CompilerIdC.lastbuildstate"에 연결(touching)하고 있습니다.<br>
“C:\D\S4R\Slicer-build\CMakeFiles\3.21.3\CompilerIdC\CompilerIdC.vcxproj” 프로젝트를 빌드했습니다(기본 대상).</p>
<p>빌드했습니다.<br>
경고 0개<br>
오류 0개</p>
<p>경과 시간: 00:00:00.46</p>
<p>Compilation of the C compiler identification source “CMakeCCompilerId.c” produced “CompilerIdC.exe”</p>
<p>Compilation of the C compiler identification source “CMakeCCompilerId.c” produced “CompilerIdC.vcxproj”</p>
<p>The C compiler identification is MSVC, found in “C:/D/S4R/Slicer-build/CMakeFiles/3.21.3/CompilerIdC/CompilerIdC.exe”</p>
<p>Compiling the CXX compiler identification source file “CMakeCXXCompilerId.cpp” succeeded.<br>
Compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.29.30133/bin/Hostx64/x64/cl.exe<br>
Build flags: ;;/DWIN32;/D_WINDOWS;/W2;/GR;/EHsc;<br>
Id flags:</p>
<p>The output was:<br>
0<br>
.NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04<br>
Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>빌드 시작: 2021-09-23 오후 2:20:03<br>
1 노드의 “C:\D\S4R\Slicer-build\CMakeFiles\3.21.3\CompilerIdCXX\CompilerIdCXX.vcxproj” 프로젝트(기본 대상)입니다.<br>
PrepareForBuild:<br>
“Debug” 디렉터리를 만들고 있습니다.<br>
“Debug\CompilerIdCXX.tlog” 디렉터리를 만들고 있습니다.<br>
InitializeBuildStatus:<br>
“AlwaysCreate"이(가) 지정되었기 때문에 “Debug\CompilerIdCXX.tlog\unsuccessfulbuild"을(를) 만들고 있습니다.<br>
ClCompile:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\CL.exe /c /nologo /W0 /WX- /diagnostics:column /Od /D _MBCS /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"Debug\” /Fd"Debug\vc142.pdb” /external:W0 /Gd /TP /FC /errorReport:queue CMakeCXXCompilerId.cpp<br>
CMakeCXXCompilerId.cpp<br>
Link:<br>
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\HostX64\x64\link.exe /ERRORREPORT:QUEUE /OUT:".\CompilerIdCXX.exe" /INCREMENTAL:NO /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:“level=‘asInvoker’ uiAccess=‘false’” /manifest:embed /PDB:".\CompilerIdCXX.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:".\CompilerIdCXX.lib" /MACHINE:X64 Debug\CMakeCXXCompilerId.obj<br>
CompilerIdCXX.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\3.21.3\CompilerIdCXX\CompilerIdCXX.exe<br>
PostBuildEvent:<br>
for %%i in (cl.exe) do <span class="mention">@echo</span> CMAKE_CXX_COMPILER=%%~$PATH:i<br>
:VCEnd<br>
CMAKE_CXX_COMPILER=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64\cl.exe<br>
FinalizeBuildStatus:<br>
“Debug\CompilerIdCXX.tlog\unsuccessfulbuild” 파일을 삭제하고 있습니다.<br>
"Debug\CompilerIdCXX.tlog\CompilerIdCXX.lastbuildstate"에 연결(touching)하고 있습니다.<br>
“C:\D\S4R\Slicer-build\CMakeFiles\3.21.3\CompilerIdCXX\CompilerIdCXX.vcxproj” 프로젝트를 빌드했습니다(기본 대상).</p>
<p>빌드했습니다.<br>
경고 0개<br>
오류 0개</p>
<p>경과 시간: 00:00:00.48</p>
<p>Compilation of the CXX compiler identification source “CMakeCXXCompilerId.cpp” produced “CompilerIdCXX.exe”</p>
<p>Compilation of the CXX compiler identification source “CMakeCXXCompilerId.cpp” produced “CompilerIdCXX.vcxproj”</p>
<p>The CXX compiler identification is MSVC, found in “C:/D/S4R/Slicer-build/CMakeFiles/3.21.3/CompilerIdCXX/CompilerIdCXX.exe”</p>
<p>Detecting C compiler ABI info compiled with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_88ea8.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>CMakeCCompilerABI.c</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_88ea8.dir\Debug\" /Fd"cmTC_88ea8.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue “C:\Program Files\CMake\share\cmake-3.21\Modules\CMakeCCompilerABI.c”</p>
<p>cmTC_88ea8.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_88ea8.exe</p>
<p>Detecting CXX compiler ABI info compiled with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_61cdc.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>CMakeCXXCompilerABI.cpp</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_61cdc.dir\Debug\" /Fd"cmTC_61cdc.dir\Debug\vc142.pdb" /external:W2 /Gd /TP /errorReport:queue “C:\Program Files\CMake\share\cmake-3.21\Modules\CMakeCXXCompilerABI.cpp”</p>
<p>cmTC_61cdc.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_61cdc.exe</p>
<p>Determining if files stdint.h exist passed with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_8cc03.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>HAVE_STDINT_H.c</p>
<p>cl /c /Zi /W2 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_8cc03.dir\Debug\" /Fd"cmTC_8cc03.dir\Debug\vc142.pdb" /external:W2 /Gd /TC /errorReport:queue  /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CheckIncludeFiles\HAVE_STDINT_H.c”</p>
<p>cmTC_8cc03.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_8cc03.exe</p>
<p>Performing C SOURCE FILE Test C_HAS_WARNING-W3 succeeded with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_4c557.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.c</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “C_HAS_WARNING-W3” /D “CMAKE_INTDIR=“Debug”” /Gm- /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"cmTC_4c557.dir\Debug\" /Fd"cmTC_4c557.dir\Debug\vc142.pdb" /external:W3 /Gd /TC /errorReport:queue  /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.c”</p>
<p>cmTC_4c557.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_4c557.exe</p>
<p>Source file was:<br>
int main(void) { return 0; }<br>
Performing C++ SOURCE FILE Test CXX_HAS_WARNING-W3 succeeded with the following output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_65398.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D “CXX_HAS_WARNING-W3” /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_65398.dir\Debug\" /Fd"cmTC_65398.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue  /bigobj /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cmTC_65398.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_65398.exe</p>
<p>Source file was:<br>
int main() { return 0;}<br>
Performing C++ SOURCE FILE Test have_avx_extensions_var succeeded with the following compile output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_eee97.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D have_avx_extensions_var /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /arch:AVX /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_eee97.dir\Debug\" /Fd"cmTC_eee97.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue  /bigobj /bigobj /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cmTC_eee97.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_eee97.exe</p>
<p>…and run output:</p>
<p>Return value: 1<br>
Source file was:</p>
<pre><code>#include &lt;immintrin.h&gt;
int main()
{
  __m256 a, b, c;
  const float src[8] = { 1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f };
  float dst[8];
  a = _mm256_loadu_ps( src );
  b = _mm256_loadu_ps( src );
  c = _mm256_add_ps( a, b );
  _mm256_storeu_ps( dst, c );

  for( int i = 0; i &lt; 8; i++ ){
    if( ( src[i] + src[i] ) != dst[i] ){
      return -1;
    }
  }

  return 0;
}
</code></pre>
<p>Performing C++ SOURCE FILE Test have_avx2_extensions_var succeeded with the following compile output:<br>
Change Dir: C:/D/S4R/Slicer-build/CMakeFiles/CMakeTmp</p>
<p>Run Build Command(s):C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/MSBuild/Current/Bin/MSBuild.exe cmTC_7000e.vcxproj /p:Configuration=Debug /p:Platform=x64 /p:VisualStudioVersion=16.0 /v:m &amp;&amp; .NET Framework용 Microsoft (R) Build Engine 버전 16.11.0+0538acc04</p>
<p>Copyright (C) Microsoft Corporation. All rights reserved.</p>
<p>Microsoft (R) C/C++ 최적화 컴파일러 버전 19.29.30133(x64)</p>
<p>Copyright (c) Microsoft Corporation. All rights reserved.</p>
<p>src.cxx</p>
<p>cl /c /Zi /W3 /WX- /diagnostics:column /Od /Ob0 /D _MBCS /D WIN32 /D _WINDOWS /D have_avx2_extensions_var /D “CMAKE_INTDIR=“Debug”” /Gm- /EHsc /RTC1 /MDd /GS /arch:AVX2 /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /Fo"cmTC_7000e.dir\Debug\" /Fd"cmTC_7000e.dir\Debug\vc142.pdb" /external:W3 /Gd /TP /errorReport:queue  /bigobj /bigobj /bigobj “C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”</p>
<p>cmTC_7000e.vcxproj → C:\D\S4R\Slicer-build\CMakeFiles\CMakeTmp\Debug\cmTC_7000e.exe</p>
<p>…and run output:</p>
<p>Return value: 1<br>
Source file was:</p>
<pre><code>#include &lt;immintrin.h&gt;
int main()
{
  __m256i a, b, c;
  const int src[8] = { 1, 2, 3, 4, 5, 6, 7, 8 };
  int dst[8];
  a =  _mm256_loadu_si256( (__m256i*)src );
  b =  _mm256_loadu_si256( (__m256i*)src );
  c = _mm256_add_epi32( a, b );
  _mm256_storeu_si256( (__m256i*)dst, c );

  for( int i = 0; i &lt; 8; i++ ){
    if( ( src[i] + src[i] ) != dst[i] ){
      return -1;
    }
  }

  return 0;
}</code></pre>

---

## Post #24 by @kookoo9999 (2021-09-23 06:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe01573b5773c03ca416a687f451dc8e3b8f65ec.png" data-download-href="/uploads/short-url/Af29iJMVmuuI5JbDptlXZNjvhIE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe01573b5773c03ca416a687f451dc8e3b8f65ec_2_690x418.png" alt="image" data-base62-sha1="Af29iJMVmuuI5JbDptlXZNjvhIE" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe01573b5773c03ca416a687f451dc8e3b8f65ec_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe01573b5773c03ca416a687f451dc8e3b8f65ec_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe01573b5773c03ca416a687f451dc8e3b8f65ec_2_1380x836.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1387×842 47.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/211ab880f725997cac73f49a4013183e6fc8c936.png" data-download-href="/uploads/short-url/4IR0kKGqHiir00jWot6fQTJYQAu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/211ab880f725997cac73f49a4013183e6fc8c936_2_690x426.png" alt="image" data-base62-sha1="4IR0kKGqHiir00jWot6fQTJYQAu" width="690" height="426" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/211ab880f725997cac73f49a4013183e6fc8c936_2_690x426.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/211ab880f725997cac73f49a4013183e6fc8c936_2_1035x639.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/211ab880f725997cac73f49a4013183e6fc8c936_2_1380x852.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1466×907 53.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/876544852abbf74fcf44e80a7afe3ae2ff2a83c6.png" data-download-href="/uploads/short-url/jjLqfNzIHp7lqFXKF3fLJceLp30.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/876544852abbf74fcf44e80a7afe3ae2ff2a83c6_2_690x428.png" alt="image" data-base62-sha1="jjLqfNzIHp7lqFXKF3fLJceLp30" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/876544852abbf74fcf44e80a7afe3ae2ff2a83c6_2_690x428.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/876544852abbf74fcf44e80a7afe3ae2ff2a83c6_2_1035x642.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/876544852abbf74fcf44e80a7afe3ae2ff2a83c6_2_1380x856.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1460×907 41.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60ed330def094de582c426426c7fd0c9d6131292.png" data-download-href="/uploads/short-url/dPs290oiYQf5uLM0NqVljNgt4X0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ed330def094de582c426426c7fd0c9d6131292_2_690x421.png" alt="image" data-base62-sha1="dPs290oiYQf5uLM0NqVljNgt4X0" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ed330def094de582c426426c7fd0c9d6131292_2_690x421.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ed330def094de582c426426c7fd0c9d6131292_2_1035x631.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/60ed330def094de582c426426c7fd0c9d6131292_2_1380x842.png 2x" data-dominant-color="F6F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1389×849 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’am trying again…</p>

---

## Post #25 by @kookoo9999 (2021-09-23 06:49 UTC)

<p>This text message is after configuration and generate via CMake.</p>
<p>Setting C++ standard<br>
Setting C++ standard - C++11<br>
Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19042.<br>
Could NOT find Subversion (missing: Subversion_SVN_EXECUTABLE)<br>
Configuring Slicer organization domain [<a href="http://www.na-mic.org" rel="noopener nofollow ugc">www.na-mic.org</a>]<br>
Configuring Slicer organization name [NA-MIC]<br>
Configuring Slicer default home module [Welcome]<br>
Configuring Slicer default favorite modules [Data, Volumes, Models, Transforms, Markups, SegmentEditor]<br>
Configuring Slicer text of disclaimer at startup [Thank you for using %1!</p>
<p>This software is not intended for clinical use.]<br>
Configuring Slicer requires admin account [OFF]<br>
Configuring Slicer install root [$LOCALAPPDATA/NA-MIC]<br>
Configuring Slicer release type [Experimental]<br>
CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):<br>
Skipping repository info extraction: directory [C:/D/S4] is not a GIT or<br>
SVN checkout<br>
Call Stack (most recent call first):<br>
CMake/SlicerVersion.cmake:55 (SlicerMacroExtractRepositoryInfo)<br>
CMakeLists.txt:193 (include)<br>
This warning is for project developers.  Use -Wno-dev to suppress it.</p>
<p>Configuring Slicer version [4.13.0-0000-00-00]<br>
Configuring Slicer revision [3037]<br>
CMake Warning (dev) at CMake/SlicerMacroExtractRepositoryInfo.cmake:94 (message):<br>
Skipping repository info extraction: directory [C:/D/S4] is not a GIT or<br>
SVN checkout<br>
Call Stack (most recent call first):<br>
CMake/SlicerVersion.cmake:99 (SlicerMacroExtractRepositoryInfo)<br>
CMakeLists.txt:193 (include)<br>
This warning is for project developers.  Use -Wno-dev to suppress it.</p>
<p>Configuring VTK<br>
Slicer_VTK_RENDERING_BACKEND is OpenGL2<br>
Slicer_VTK_SMP_IMPLEMENTATION_TYPE is TBB<br>
Slicer_VTK_VERSION_MAJOR is 9<br>
Configuring Slicer with Qt 5.15.2 (using modules: Core, Widgets, Multimedia, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, WebEngine, WebEngineWidgets, WebChannel, Script, LinguistTools, Test, )<br>
Setting QT_PLUGINS_DIR: C:/Qt/5.15.2/msvc2019_64/plugins<br>
Setting QT_BINARY_DIR: C:/Qt/5.15.2/msvc2019_64/bin<br>
Setting ExternalData_OBJECT_STORES to ‘C:/D/S4R/ExternalData/Objects’<br>
Configuring Slicer for [win-amd64]<br>
Checking if CMake supports https<br>
Checking if CMake supports https - ok<br>
Remote - vtkAddon [OK]<br>
Remote - jqPlot [OK]<br>
Remote - MultiVolumeExplorer [OK]<br>
Remote - MultiVolumeImporter [OK]<br>
Remote - SimpleFilters [OK]<br>
Remote - BRAINSTools [OK]<br>
Remote - DataStore [OK]<br>
Remote - CompareVolumes [OK]<br>
Remote - LandmarkRegistration [OK]<br>
Remote - SurfaceToolbox [OK]<br>
SuperBuild - First pass<br>
SuperBuild - TBB_INSTALL_DIR:C:/D/S4R/tbb-install<br>
SuperBuild - First pass - done<br>
SuperBuild - Slicer =&gt; Requires curl, CTKAppLauncherLib, teem, VTK, ITK, CTK, LibArchive, RapidJSON, SimpleITK, SlicerExecutionModel, qRestAPI, DCMTK, CTKAPPLAUNCHER, python, python-pythonqt-requirements, python-scipy, python-numpy, python-dicom-requirements, python-extension-manager-requirements, python-extension-manager-ssl-requirements, tbb[INCLUDED], JsonCpp,<br>
SuperBuild -   curl =&gt; Requires zlib, OpenSSL,<br>
SuperBuild -     zlib[OK]<br>
SuperBuild -     ZLIB_INCLUDE_DIR:C:/D/S4R/zlib-install/include<br>
SuperBuild -     ZLIB_LIBRARY:C:/D/S4R/zlib-install/lib/zlib.lib<br>
SuperBuild -     ZLIB_ROOT:C:/D/S4R/zlib-install<br>
SuperBuild -     OpenSSL[OK]<br>
SuperBuild -     LIB_EAY_DEBUG:C:/D/S4R/OpenSSL-install/Debug/lib/libcrypto.lib<br>
SuperBuild -     LIB_EAY_RELEASE:C:/D/S4R/OpenSSL-install/Release/lib/libcrypto.lib<br>
SuperBuild -     SSL_EAY_DEBUG:C:/D/S4R/OpenSSL-install/Debug/lib/libssl.lib<br>
SuperBuild -     SSL_EAY_RELEASE:C:/D/S4R/OpenSSL-install/Release/lib/libssl.lib<br>
SuperBuild -     OpenSSL 1.1.1g<br>
SuperBuild -     OPENSSL_LIBRARY_DIR:C:/D/S4R/OpenSSL-install/$(Configuration)/lib<br>
SuperBuild -     OPENSSL_EXPORT_LIBRARY_DIR:C:/D/S4R/OpenSSL-install/$(Configuration)/bin<br>
SuperBuild -     OPENSSL_INCLUDE_DIR:C:/D/S4R/OpenSSL-install/$(Configuration)/include<br>
SuperBuild -     OPENSSL_LIBRARIES:optimized;C:/D/S4R/OpenSSL-install/Release/lib/libssl.lib;debug;C:/D/S4R/OpenSSL-install/Debug/lib/libssl.lib;optimized;C:/D/S4R/OpenSSL-install/Release/lib/libcrypto.lib;debug;C:/D/S4R/OpenSSL-install/Debug/lib/libcrypto.lib<br>
SuperBuild -   curl[OK]<br>
SuperBuild -   CURL_INCLUDE_DIR:C:/D/S4R/curl-install/include<br>
SuperBuild -   CURL_LIBRARY:C:/D/S4R/curl-install/lib/libcurl.lib<br>
SuperBuild -   CTKAppLauncherLib[OK]<br>
SuperBuild -   teem =&gt; Requires zlib[INCLUDED], VTK,<br>
SuperBuild -     VTK =&gt; Requires zlib[INCLUDED], python, tbb[INCLUDED],<br>
SuperBuild -       python =&gt; Requires bzip2, CTKAPPLAUNCHER, LZMA, zlib[INCLUDED], sqlite, OpenSSL[INCLUDED],<br>
SuperBuild -         bzip2[OK]<br>
SuperBuild -         BZIP2_INCLUDE_DIR:C:/D/S4R/bzip2<br>
SuperBuild -         BZIP2_LIBRARIES:C:/D/S4R/bzip2-install/lib/libbz2.lib<br>
SuperBuild -         CTKAPPLAUNCHER =&gt; Requires CTKResEdit,<br>
SuperBuild -           CTKResEdit[OK]<br>
SuperBuild -         CTKAPPLAUNCHER[OK]<br>
SuperBuild -         LZMA[OK]<br>
SuperBuild -         sqlite[OK]<br>
SuperBuild -       python[OK]<br>
SuperBuild -       PYTHON_EXECUTABLE:C:/D/S4R/python-install/bin/PythonSlicer.exe<br>
SuperBuild -       PYTHON_INCLUDE_DIR:C:/D/S4R/python-install/include<br>
SuperBuild -       PYTHON_LIBRARY:C:/D/S4R/python-install/libs/python36.lib<br>
SuperBuild -       PYTHON_DEBUG_LIBRARY:C:/D/S4R/python-install/libs/python36.lib<br>
SuperBuild -       Python3_ROOT_DIR:C:/D/S4R/python-install<br>
SuperBuild -       Python3_INCLUDE_DIR:C:/D/S4R/python-install/include<br>
SuperBuild -       Python3_LIBRARY:C:/D/S4R/python-install/libs/python36.lib<br>
SuperBuild -       Python3_LIBRARY_DEBUG:C:/D/S4R/python-install/libs/python36.lib<br>
SuperBuild -       Python3_LIBRARY_RELEASE:C:/D/S4R/python-install/libs/python36.lib<br>
SuperBuild -       Python3_EXECUTABLE:C:/D/S4R/python-install/bin/PythonSlicer.exe<br>
SuperBuild -     VTK[OK]<br>
SuperBuild -   teem[OK]<br>
SuperBuild -   ITK =&gt; Requires zlib[INCLUDED], VTK[INCLUDED], DCMTK, Swig[INCLUDED], python[INCLUDED], tbb[INCLUDED],<br>
SuperBuild -     DCMTK =&gt; Requires zlib[INCLUDED],<br>
SuperBuild -     DCMTK[OK]<br>
SuperBuild -   ITK[OK]<br>
SuperBuild -   CTK =&gt; Requires VTK[INCLUDED], ITK[INCLUDED], python[INCLUDED], DCMTK[INCLUDED],<br>
SuperBuild -   CTK[OK]<br>
SuperBuild -   LibArchive =&gt; Requires zlib[INCLUDED], zlib[INCLUDED],<br>
SuperBuild -   LibArchive[OK]<br>
SuperBuild -   RapidJSON[OK]<br>
SuperBuild -   SimpleITK =&gt; Requires ITK[INCLUDED], Swig[INCLUDED], python[INCLUDED], python-setuptools,<br>
SuperBuild -     python-setuptools =&gt; Requires python[INCLUDED], python-ensurepip,<br>
SuperBuild -       python-ensurepip =&gt; Requires python[INCLUDED],<br>
SuperBuild -       python-ensurepip[OK]<br>
SuperBuild -     python-setuptools[OK]<br>
SuperBuild -   SimpleITK[OK]<br>
SuperBuild -   SlicerExecutionModel =&gt; Requires ITK[INCLUDED], tbb[INCLUDED], JsonCpp, ParameterSerializer,<br>
SuperBuild -     JsonCpp[OK]<br>
SuperBuild -     ParameterSerializer =&gt; Requires JsonCpp[INCLUDED], ITK[INCLUDED],<br>
SuperBuild -     ParameterSerializer[OK]<br>
SuperBuild -   SlicerExecutionModel[OK]<br>
SuperBuild -   qRestAPI[OK]<br>
SuperBuild -   python-pythonqt-requirements =&gt; Requires python[INCLUDED], python-ensurepip[INCLUDED], python-pip, python-setuptools[INCLUDED], python-wheel,<br>
SuperBuild -     python-pip =&gt; Requires python[INCLUDED], python-ensurepip[INCLUDED], python-setuptools[INCLUDED],<br>
SuperBuild -     python-pip[OK]<br>
SuperBuild -     python-wheel =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED],<br>
SuperBuild -     python-wheel[OK]<br>
SuperBuild -   python-pythonqt-requirements[OK]<br>
SuperBuild -   python-scipy =&gt; Requires python[INCLUDED], python-ensurepip[INCLUDED], python-numpy, python-pip[INCLUDED], python-setuptools[INCLUDED], python-wheel[INCLUDED],<br>
SuperBuild -     python-numpy =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED],<br>
SuperBuild -     python-numpy[OK]<br>
SuperBuild -   python-scipy[OK]<br>
SuperBuild -   python-dicom-requirements =&gt; Requires python[INCLUDED], python-numpy[INCLUDED], python-pip[INCLUDED], python-requests-requirements, python-setuptools[INCLUDED],<br>
SuperBuild -     python-requests-requirements =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED],<br>
SuperBuild -     python-requests-requirements[OK]<br>
SuperBuild -   python-dicom-requirements[OK]<br>
SuperBuild -   python-extension-manager-requirements =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-setuptools[INCLUDED],<br>
SuperBuild -   python-extension-manager-requirements[OK]<br>
SuperBuild -   python-extension-manager-ssl-requirements =&gt; Requires python[INCLUDED], python-pip[INCLUDED], python-requests-requirements[INCLUDED], python-setuptools[INCLUDED],<br>
SuperBuild -   python-extension-manager-ssl-requirements[OK]<br>
SuperBuild - Slicer[OK]<br>
Configuring done<br>
Generating done</p>

---

## Post #26 by @kookoo9999 (2021-09-23 08:33 UTC)

<p>I can’t build this list.<br>
22&gt; “LibArchive.vcxproj”<br>
43&gt; “ITK.vcxproj”<br>
47&gt; “CTK.vcxproj”<br>
48&gt; “SlicerExecutionModel.vcxproj”<br>
49&gt; “Slicer.vcxproj”</p>

---

## Post #27 by @kookoo9999 (2021-09-23 16:13 UTC)

<p>I just tried to build using CMD, but it failed…I think there were more errors than using CMake-GUI.</p>

---

## Post #28 by @kookoo9999 (2021-09-25 06:38 UTC)

<p>I fixed the error of LibArchive for delete line in C:\D\S4R\LibArchive\libarchive\archive_read_support_format_rar5.c line 74.</p>
<p>And now, I can’t fix this error (MSB8066 , when I build the SimpleITK)<br>
I read <a href="https://github.com/Slicer/Slicer/issues/5498" rel="noopener nofollow ugc">here</a> and I try to fix but I can’t understand add these and can’t find the External_SimpleITK.cmake.<br>
Do you mean to add these before configure via CMake-GUI ??<br>
I can find External_SImpleITKExamples.cmake in directory C:\D\S4R\SimpleITK\SuperBuild .</p>
<pre><code class="lang-auto"> if(Slicer_VTK_VERSION_MAJOR STREQUAL "9")
      list(APPEND EXTERNAL_PROJECT_OPTIONAL_CMAKE_CACHE_ARGS
        # Required by FindPython3 CMake module used by VTK
        -DPython3_ROOT_DIR:PATH=${Python3_ROOT_DIR}
        -DPython3_INCLUDE_DIR:PATH=${Python3_INCLUDE_DIR}
        -DPython3_LIBRARY:FILEPATH=${Python3_LIBRARY}
        -DPython3_LIBRARY_DEBUG:FILEPATH=${Python3_LIBRARY_DEBUG}
        -DPython3_LIBRARY_RELEASE:FILEPATH=${Python3_LIBRARY_RELEASE}
        -DPython3_EXECUTABLE:FILEPATH=${Python3_EXECUTABLE}
        )
    endif()
</code></pre>
<div class="md-table">
<table>
<thead>
<tr>
<th>심각도</th>
<th>코드</th>
<th>설명</th>
<th>프로젝트</th>
<th>파일</th>
<th>줄</th>
<th>비표시 오류(Suppression) 상태</th>
</tr>
</thead>
<tbody>
<tr>
<td>오류</td>
<td>MSB8066</td>
<td>'C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-configure.rule;C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-build.rule;C:\D\S4R\CMakeFiles\b2bcbfa553be6b76f5311151bbb771b6\SimpleITK-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\SimpleITK-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\SimpleITK.rule’에 대한 사용자 지정 빌드가 종료되었습니다(코드 1).</td>
<td>SimpleITK</td>
<td>C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets</td>
<td>241</td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #29 by @lassoan (2021-09-26 04:03 UTC)

<p>This build error and solution (workaround) is discussed <a href="https://github.com/Slicer/Slicer/issues/5498">here</a>.</p>

---

## Post #30 by @kookoo9999 (2021-09-26 04:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Thanks for reply.<br>
Do you mean to add these lines into S4\Super-build\External_SImpleITK.cmake and then configure via CMake-GUI and build again??<br>
if(Slicer_VTK_VERSION_MAJOR STREQUAL “9”)<br>
list(APPEND EXTERNAL_PROJECT_OPTIONAL_CMAKE_CACHE_ARGS<br>
# Required by FindPython3 CMake module used by VTK<br>
-DPython3_ROOT_DIR:PATH=${Python3_ROOT_DIR}<br>
-DPython3_INCLUDE_DIR:PATH=${Python3_INCLUDE_DIR}<br>
-DPython3_LIBRARY:FILEPATH=${Python3_LIBRARY}<br>
-DPython3_LIBRARY_DEBUG:FILEPATH=${Python3_LIBRARY_DEBUG}<br>
-DPython3_LIBRARY_RELEASE:FILEPATH=${Python3_LIBRARY_RELEASE}<br>
-DPython3_EXECUTABLE:FILEPATH=${Python3_EXECUTABLE}<br>
)<br>
endif()</p>

---

## Post #31 by @lassoan (2021-09-26 04:33 UTC)

<p>Please keep the discussion of this error at one place, the <a href="https://github.com/Slicer/Slicer/issues/5498">issue tracker</a>.</p>

---

## Post #33 by @2733845631 (2024-04-15 10:48 UTC)

<p>/fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /GR /std:c++17 /Fo"cmTC_1ecf8.dir\Debug\" /Fd"cmTC_1ecf8.dir\Debug\vc143.pdb" /external:W1 /Gd /TP /errorReport:queue  /bigobj /bigobj “D:\D\SR\Slicer-build\CMakeFiles\CMakeTmp\src.cxx”<br>
src.cxx<br>
D:\D\SR\Slicer-build\CMakeFiles\CMakeTmp\src.cxx(1,1): error C2059: 语法错误:“/” [D:\D\SR\Slicer-build\CMakeFiles\CMakeTmp\cmTC_1ecf8.vcxproj]</p>
<p>Source file was:<br>
/Od<br>
Hello, I encountered the same problem. May I ask how you resolved it?</p>

---
