---
topic_id: 8028
title: "Error Building Slicer On Windows 10 Ctk Problem"
date: 2019-08-14
url: https://discourse.slicer.org/t/8028
---

# Error building slicer on Windows 10 (CTK problem?)

**Topic ID**: 8028
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/error-building-slicer-on-windows-10-ctk-problem/8028

---

## Post #1 by @aalarcon96 (2019-08-14 15:19 UTC)

<p>Hi,</p>
<p>I am trying to build slicer on Windows 10, using Visual Studios 2019 and Qt 5.10. I came across this error after building “ALL_BUILD” in release mode. Could it be that I needed to download some package beforehand?</p>
<p>47&gt;CMake Error at CMakeLists.txt:792 (find_package):<br>
47&gt;  By not providing “FindCTK.cmake” in CMAKE_MODULE_PATH this project has<br>
47&gt;  asked CMake to find a package configuration file provided by “CTK”, but<br>
47&gt;  CMake did not find one.<br>
47&gt;<br>
47&gt;  Could not find a package configuration file provided by “CTK” with any of<br>
47&gt;  the following names:<br>
47&gt;<br>
47&gt;    CTKConfig.cmake<br>
47&gt;    ctk-config.cmake<br>
47&gt;<br>
47&gt;  Add the installation prefix of “CTK” to CMAKE_PREFIX_PATH or set “CTK_DIR”<br>
47&gt;  to a directory containing one of the above files.  If “CTK” provides a<br>
47&gt;  separate development package or SDK, be sure it has been installed.<br>
47&gt;<br>
47&gt;<br>
47&gt;-- Configuring incomplete, errors occurred!<br>
47&gt;See also “C:/Angela/S4/S4-Superbuild/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
47&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(220,5): error MSB6006: “cmd.exe” exited with code 1.<br>
47&gt;Done building project “Slicer.vcxproj” – FAILED.<br>
48&gt;------ Build started: Project: ALL_BUILD, Configuration: Release x64 ------<br>
48&gt;Building Custom Rule C:/Angela/S4/S4-s/CMakeLists.txt<br>
========== Build: 41 succeeded, 7 failed, 0 up-to-date, 0 skipped ==========</p>
<p>Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2019-08-14 16:04 UTC)

<p>When configuring Slicer with CMake did you set to use the v140 toolset since you are using Visual Studio 2019?</p>
<p>It would be part of this section in the build instructions:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Experimental.2Fdeprecated_build_environments" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Experimental.2Fdeprecated_build_environments</a></p>

---

## Post #3 by @aalarcon96 (2019-08-14 16:10 UTC)

<p>I am not sure if I did. Is there a way to check? Sorry, I am very new to this.</p>

---

## Post #4 by @jamesobutler (2019-08-14 16:26 UTC)

<p>If you open up the main solution where you have ALL_BUILD and all of the other projects it should have “(Visual Studio 2015)” next to the project names if you have set the toolset correctly.</p>
<p>If you are using a recent CMakeGUI you would’ve specified Visual Studio 2019 as your generator, then you define platform and toolset below. So “X64” and then “v140”.</p>

---

## Post #5 by @aalarcon96 (2019-08-14 16:44 UTC)

<p>They don’t have “(Visual Studio 2015)” next to the project names.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/834c1dcd108b7b308d19648882049f36d814ed47.png" data-download-href="/uploads/short-url/iJvCThL76cGHmLQcxPFJjjXPT5Z.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/834c1dcd108b7b308d19648882049f36d814ed47.png" alt="Capture" data-base62-sha1="iJvCThL76cGHmLQcxPFJjjXPT5Z" width="210" height="500" data-dominant-color="ECEDF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">472×1121 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I chose Visual Studios 2019 as my generator, but I did not define the platform nor toolset.</p>

---
