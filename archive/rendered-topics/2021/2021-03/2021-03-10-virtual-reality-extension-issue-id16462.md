---
topic_id: 16462
title: "Virtual Reality Extension Issue"
date: 2021-03-10
url: https://discourse.slicer.org/t/16462
---

# Virtual Reality extension issue

**Topic ID**: 16462
**Date**: 2021-03-10
**URL**: https://discourse.slicer.org/t/virtual-reality-extension-issue/16462

---

## Post #1 by @eduardo.ecamargo (2021-03-10 00:01 UTC)

<p>I checked out tag v4.11.20210226 from the Slicer repo, which is the latest stable version, and built the source in release mode (Windows 10) as a result Slicer loads as expected (running from Slicer-build\Slicer.exe). Now I would like to add the Virtual reality extension. I opened up the extension manager and install the extension (no errors here). I close the manager and Slicer. When re-opening Slicer I get the following error “cannot load library …/NA-MIC/Extensions-29738/SlicerVirtualReality/lib/Slicer-4.11/qt-loadable-modules\qSlicerVirtualRealityModule.dll: The specific module could not be found.”. If I download the installer from Slicer’s website everything works. No changes to the source code at all. What am I missing here?</p>

---

## Post #2 by @lassoan (2021-03-10 00:34 UTC)

<p>In general, you cannot mix binaries built on different computers due to potential ABI incompatibilities. It is not just that you need to build from the exact same source code but use the exact same build environment (built tools, build options, etc.).</p>
<p>In practice this should not cause any problem, as you can only build an extension if you have already built Slicer.</p>

---

## Post #3 by @eduardo.ecamargo (2021-03-10 17:19 UTC)

<p>Hi Andras,</p>
<p>Thank you for answering my question although it doesn’t make much sense to me yet, please correct me if I’m wrong.</p>
<p>I would expect a Slicer build (any build, any machine, any OS) to be able to download and use any extension using the manager. Please, if I’m wrong please correct me but your answer sounded like Slicer and all extensions need to be built in the same machine for all platforms prior to becoming available for download.</p>
<p>Everything was working (my own Slicer build + downloaded VR Extension) when building from tag v4.11.20200930. Anyway, I will download and build the VR extension too.</p>

---

## Post #4 by @lassoan (2021-03-10 21:12 UTC)

<aside class="quote no-group" data-username="eduardo.ecamargo" data-post="3" data-topic="16462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/9fc29f/48.png" class="avatar"> eduardo.ecamargo:</div>
<blockquote>
<p>Slicer and all extensions need to be built in the same machine for all platforms prior to becoming available for download.</p>
</blockquote>
</aside>
<p>This is correct.</p>
<aside class="quote no-group" data-username="eduardo.ecamargo" data-post="3" data-topic="16462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/9fc29f/48.png" class="avatar"> eduardo.ecamargo:</div>
<blockquote>
<p>Everything was working (my own Slicer build + downloaded VR Extension) when building from tag v4.11.20200930. Anyway, I will download and build the VR extension too.</p>
</blockquote>
</aside>
<p>If your build environment on your machine happens to completely match the build environment on the factory machine then the you can use your custom-built extension with a factory-built Slicer. If there are slight differences then the extension will be loaded but it will randomly crash, and if there are major differences then the extension will not be even loaded.</p>

---

## Post #5 by @eduardo.ecamargo (2021-03-16 21:10 UTC)

<p>Hi Andras,</p>
<p>I would appreciate any help on this issue. I checked out the 3D Slicer tag v4.11.20210226 and have it built (default CMake parameters) as release x64. Now I checked out Slicer’s Virtual Reality extension source code and I am trying to build it against my Slicer’s build (setting up Slicer_build_Dir on CMake). I have followed the exact same steps for Slicer tag v4.11.20200930 and Virtual Realy extension built without problems. I am pasting below the output I got (Windows). Thanks in advance for any help.</p>
<pre><code class="lang-auto">Rebuild started...
1&gt;------ Rebuild All started: Project: ZERO_CHECK, Configuration: Release x64 ------
1&gt;Checking Build System
2&gt;------ Rebuild All started: Project: OpenVR, Configuration: Release x64 ------
2&gt;Creating directories for 'OpenVR'
2&gt;Building Custom Rule C:/source/repos/SlicerVirtualReality/CMakeLists.txt
2&gt;Performing download step (download, verify and extract) for 'OpenVR'
2&gt;-- verifying file...
2&gt;       file='C:/source/repos/SlicerVirtualReality/build/v1.12.5.tar.gz'
2&gt;-- File already exists and hash match (skip download):
2&gt;  file='C:/source/repos/SlicerVirtualReality/build/v1.12.5.tar.gz'
2&gt;  MD5='fabbc1ad83d7c382080ca00b878e6209'
2&gt;-- extracting...
2&gt;     src='C:/source/repos/SlicerVirtualReality/build/v1.12.5.tar.gz'
2&gt;     dst='C:/source/repos/SlicerVirtualReality/build/OpenVR'
2&gt;-- extracting... [tar xfz]
2&gt;cmake -E tar : warning : skipping symbolic link "openvr-1.12.5/bin/osx64/OpenVR.framework/Headers" -&gt; "Versions/Current/Headers".
2&gt;cmake -E tar : warning : skipping symbolic link "openvr-1.12.5/bin/osx64/OpenVR.framework/OpenVR" -&gt; "Versions/Current/OpenVR".
2&gt;cmake -E tar : warning : skipping symbolic link "openvr-1.12.5/bin/osx64/OpenVR.framework/Resources" -&gt; "Versions/Current/Resources".
2&gt;cmake -E tar : warning : skipping symbolic link "openvr-1.12.5/bin/osx64/OpenVR.framework/Versions/Current" -&gt; "A".
2&gt;-- extracting... [analysis]
2&gt;-- extracting... [rename]
2&gt;-- extracting... [clean up]
2&gt;-- extracting... done
2&gt;No update step for 'OpenVR'
2&gt;No patch step for 'OpenVR'
2&gt;Generate version-OpenVR.txt and license-OpenVR.txt
2&gt;No configure step for 'OpenVR'
2&gt;No build step for 'OpenVR'
2&gt;No install step for 'OpenVR'
2&gt;Completed 'OpenVR'
2&gt;Done building project "OpenVR.vcxproj".
3&gt;------ Rebuild All started: Project: VTKRenderingOpenVR, Configuration: Release x64 ------
3&gt;Creating directories for 'VTKRenderingOpenVR'
3&gt;Building Custom Rule C:/source/repos/SlicerVirtualReality/CMakeLists.txt
3&gt;No download step for 'VTKRenderingOpenVR'
3&gt;No update step for 'VTKRenderingOpenVR'
3&gt;No patch step for 'VTKRenderingOpenVR'
3&gt;Performing configure step for 'VTKRenderingOpenVR'
3&gt;loading initial cache file C:/source/repos/SlicerVirtualReality/build/VTKRenderingOpenVR-prefix/tmp/VTKRenderingOpenVR-cache-Release.cmake
3&gt;CMake Warning (dev) in CMakeLists.txt:
3&gt;  No project() command is present.  The top-level CMakeLists.txt file must
3&gt;  contain a literal, direct call to the project() command.  Add a line of
3&gt;  code such as
3&gt;
3&gt;    project(ProjectName)
3&gt;
3&gt;  near the top of the file, but after cmake_minimum_required().
3&gt;
3&gt;  CMake is pretending there is a "project(Project)" command on the first
3&gt;  line.
3&gt;This warning is for project developers.  Use -Wno-dev to suppress it.
3&gt;
3&gt;-- Selecting Windows SDK version 10.0.18362.0 to target Windows 10.0.19042.
3&gt;CMake Error at CMakeLists.txt:1 (vtk_module_find_package):
3&gt;  Unknown CMake command "vtk_module_find_package".
3&gt;
3&gt;
3&gt;CMake Warning (dev) in CMakeLists.txt:
3&gt;  No cmake_minimum_required command is present.  A line of code such as
3&gt;
3&gt;    cmake_minimum_required(VERSION 3.15)
3&gt;
3&gt;  should be added at the top of the file.  The version specified may be lower
3&gt;  if you wish to support older CMake versions for this project.  For more
3&gt;  information run "cmake --help-policy CMP0000".
3&gt;This warning is for project developers.  Use -Wno-dev to suppress it.
3&gt;
3&gt;-- Configuring incomplete, errors occurred!
3&gt;See also "C:/source/repos/SlicerVirtualReality/build/VTKRenderingOpenVR-build/CMakeFiles/CMakeOutput.log".
3&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(238,5): error MSB8066: Custom build for 'C:\source\repos\SlicerVirtualReality\build\CMakeFiles\39885bf821a71085a35f68fd677577b1\VTKRenderingOpenVR-mkdir.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\39885bf821a71085a35f68fd677577b1\VTKRenderingOpenVR-download.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\39885bf821a71085a35f68fd677577b1\VTKRenderingOpenVR-update.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\39885bf821a71085a35f68fd677577b1\VTKRenderingOpenVR-patch.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\39885bf821a71085a35f68fd677577b1\VTKRenderingOpenVR-configure.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\39885bf821a71085a35f68fd677577b1\VTKRenderingOpenVR-build.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\39885bf821a71085a35f68fd677577b1\VTKRenderingOpenVR-install.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\87df6f4498ed6ba2fa495718a2168dc1\VTKRenderingOpenVR-complete.rule;C:\source\repos\SlicerVirtualReality\build\CMakeFiles\5670f373fbe193eb89979bfb7c29ee58\VTKRenderingOpenVR.rule;C:\source\repos\SlicerVirtualReality\CMakeLists.txt' exited with code 1.
3&gt;Done building project "VTKRenderingOpenVR.vcxproj" -- FAILED.
========== Rebuild All: 2 succeeded, 1 failed, 0 skipped ==========
</code></pre>

---

## Post #6 by @jcfr (2021-03-16 21:23 UTC)

<aside class="quote no-group" data-username="eduardo.ecamargo" data-post="5" data-topic="16462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/9fc29f/48.png" class="avatar"> eduardo.ecamargo:</div>
<blockquote>
<p>I checked out the 3D Slicer tag v4.11.20210226 and have it built (default CMake parameters) as release x64.</p>
</blockquote>
</aside>
<p>Instead you should build <a href="https://github.com/Slicer/Slicer">Slicer@master</a> setting CMake option <code>Slicer_VTK_VERSION_MAJOR</code> to <code>9</code></p>

---

## Post #7 by @eduardo.ecamargo (2021-03-16 21:32 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="16462">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Slicer_VTK_VERSION_MAJOR</p>
</blockquote>
</aside>
<p>Hi Jean.<br>
Thanks for replying. I forgot to mention that I set Slicer_VTK_VERSION_MAJOR to 9. That was the reason I updated to the lastest tag. I just checked out master and still the same. I think it might be something within a CMakeFile. Please feel free to share your ideas.</p>

---

## Post #8 by @jcfr (2021-03-16 21:45 UTC)

<p>Build errors are not specific to your setup and are also reported on the dashboard <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2021-03-16&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VirtualReality">here</a></p>
<p>We will follow up when this is fixed.</p>

---

## Post #9 by @eduardo.ecamargo (2021-03-16 21:56 UTC)

<p>Thanks.<br>
I’ll wait for the fix.</p>

---
