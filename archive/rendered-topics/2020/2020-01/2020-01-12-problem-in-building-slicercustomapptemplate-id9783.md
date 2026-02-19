---
topic_id: 9783
title: "Problem In Building Slicercustomapptemplate"
date: 2020-01-12
url: https://discourse.slicer.org/t/9783
---

# Problem in building SlicerCustomAppTemplate

**Topic ID**: 9783
**Date**: 2020-01-12
**URL**: https://discourse.slicer.org/t/problem-in-building-slicercustomapptemplate/9783

---

## Post #1 by @Pooja_Virkar (2020-01-12 17:11 UTC)

<p>Hello,</p>
<p>I am trying to build SlicerCustomAppTemplate to create customized Slicer application. I am following the tutorial of <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="nofollow noopener">https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a><br>
and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files</a>.</p>
<p>While creating the directory in github, when I clone it, it is showing empty repository which has no CMakeLists.txt. I don’t understand the procedure for cloning it.</p>
<p>Also If I copy the CMakeLists.txt in my folder and configure it using CMake-gui, it shows me following errors -<br>
CMake Warning at SlicerApp-rel/slicersources-src/CMake/SlicerBlockFindQtAndCheckVersion.cmake:22 (find_package):<br>
Found package configuration file:</p>
<pre><code>C:/Qt2/5.12.5/msvc2017_64/lib/cmake/Qt5/Qt5Config.cmake
</code></pre>
<p>but it set Qt5_FOUND to FALSE so package “Qt5” is considered to be NOT<br>
FOUND.  Reason given by package:</p>
<p>Failed to find Qt5 component “WebEngine” config file at<br>
“C:/Qt2/5.12.5/msvc2017_64/lib/cmake/Qt5WebEngine/Qt5WebEngineConfig.cmake”</p>
<p>Failed to find Qt5 component “WebEngineWidgets” config file at<br>
“C:/Qt2/5.12.5/msvc2017_64/lib/cmake/Qt5WebEngineWidgets/Qt5WebEngineWidgetsConfig.cmake”</p>
<p>Call Stack (most recent call first):<br>
SlicerApp-rel/slicersources-src/CMake/SlicerBlockFindQtAndCheckVersion.cmake:67 (__SlicerBlockFindQtAndCheckVersion_find_qt)<br>
SlicerApp-rel/slicersources-src/CMakeLists.txt:600 (include)</p>
<p>CMake Error at SlicerApp-rel/slicersources-src/CMake/SlicerBlockFindQtAndCheckVersion.cmake:30 (message):<br>
error: Qt 5.6.0 was not found on your system.You probably need to set the<br>
Qt5_DIR variable.<br>
Call Stack (most recent call first):<br>
SlicerApp-rel/slicersources-src/CMake/SlicerBlockFindQtAndCheckVersion.cmake:67 (__SlicerBlockFindQtAndCheckVersion_find_qt)<br>
SlicerApp-rel/slicersources-src/CMakeLists.txt:600 (include)</p>
<p>I am using Windows with Visual Studio 2019 and QT 5.12.5.<br>
Can someone please help me to solve the error and provide me steps in detail?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @jamesobutler (2020-01-12 20:51 UTC)

<p>Make sure to follow<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Prerequisites/Qt5" rel="nofollow noopener">these instructions</a> to make sure you’ve selected the QWebEngine and Qt Script components whenever you selected to install the MSVC2017 x64 version of Qt 5.12. You can have a successful build with Qt 5.12 building Slicer with the VS2017 toolset (v141).</p>
<p>The rest of the Windows instructions can be found here -&gt; <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows_2" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows_2</a></p>

---

## Post #3 by @Pooja_Virkar (2020-01-15 11:59 UTC)

<p>I have Visual Studio 2019 x64 version. Will it not work in it to build SlicerCustomAppTemplate?<br>
Is MSVC 2017 mandatory for this installation?</p>
<p>Also, when we clone the repository, should it have CMakeLists.txt ? From where I can get it?<br>
Could you please tell me exact procedure for this installation?</p>
<p>Thanks in advance.</p>

---

## Post #4 by @Sam_Horvath (2020-01-15 16:08 UTC)

<p>Hi:</p>
<p>Using the Custom app template generation procedure (these are commands that should go into a bash shell or command prompt, you will need to have python installed):</p>
<pre><code class="lang-bash">pip install cookiecutter jinja2-github
cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate
</code></pre>
<p>and following the prompts should create a directory contains the CMakeLists for your custom slicer build.  You do no need to do a separate checkout of Slicer, or copy anything else in. Once you have that directory, you can configure and build starting from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CONFIGURE_and_generate_Slicer_solution_files" rel="nofollow noopener">this</a> point in the Slicer instructions.</p>
<p>This will require an appropriate Qt installation.  When installing Qt you should enable QtWebEngine and Qt Script for the version of Qt you are installing.  We currently test/build slicer with VS2015 and VS2017.  However, Qt binaries for VS2017 should work in VS2019</p>

---

## Post #5 by @Pooja_Virkar (2020-01-18 18:08 UTC)

<p>Thank you for this information.<br>
I followed the steps (without modifying any CMake variables from CMakeLists.txt) and it took lot of time to build All_Build project.<br>
But after it, I observed there was no Slicer-superbuild directory in my bin folder, only Slicer-build directory was there. So I built the Slicer.sln from Slicer-build and it was succeeded, run the Slicer.exe successfully.<br>
But In my application,I can not load Dicom data (maybe because Slicer_BUILD_DICOM_SUPPORT is OFF).<br>
So what should I do now to turn some modules ON without doing this whole procedure of build again?</p>

---

## Post #6 by @lassoan (2020-01-19 21:22 UTC)

<aside class="quote no-group" data-username="Pooja_Virkar" data-post="5" data-topic="9783">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pooja_virkar/48/3902_2.png" class="avatar"> Pooja_Virkar:</div>
<blockquote>
<p>But after it, I observed there was no Slicer-superbuild directory in my bin folder</p>
</blockquote>
</aside>
<p>“Slicer-superbuild directory” refers to your top-level binary folder (e.g., “C:\S4R”). It is not created automatically but it exists by the name that you give to it.</p>
<aside class="quote no-group" data-username="Pooja_Virkar" data-post="5" data-topic="9783">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pooja_virkar/48/3902_2.png" class="avatar"> Pooja_Virkar:</div>
<blockquote>
<p>what should I do now to turn some modules ON without doing this whole procedure of build again?</p>
</blockquote>
</aside>
<p>You can go on and change any CMake options and when you build again, only impacted parts will be rebuilt, so it will be much faster than the first build from scratch.</p>

---

## Post #7 by @Pooja_Virkar (2020-01-20 09:36 UTC)

<p>Okay. Thanks.<br>
But after making changes in CMakeLists.txt, do I have to build solution file from top-level build directory or  build Slicer.sln file directly from Slicer-superbuild/Slicer-build directory?</p>

---

## Post #8 by @Sam_Horvath (2020-01-20 10:17 UTC)

<p>You will need to rebuild from the solution in the top level build directory, as enabling DICOM adds DICOM specific dependencies that need to be built.</p>

---

## Post #9 by @Pooja_Virkar (2020-01-20 10:38 UTC)

<p>Sorry for asking it again, but it is really confusing me.<br>
I did changes in CMakeLists.txt.<br>
So now first Do I need to configure again using CMake-gui and then rebuild from the solution (All_Build) in the top-level build directory? After that I can directly open Slicer.exe from Slicer-superbuild/Slicer-build. Is it correct?<br>
Please tell me the procedure in steps.<br>
Thanks in advance.</p>

---

## Post #10 by @Sam_Horvath (2020-01-20 10:45 UTC)

<p>Yes, that is correct.</p>
<ol>
<li>Change the CMakeLists file</li>
<li>Configure and generate using cmake-gui.  Make sure that the source and build directories are set to the folder you have already used for the first build.</li>
<li>Open the .sln file in the to level build directory</li>
<li>Build the ALL_BUILD target</li>
<li>Run Slicer.exe from the Slicer-build directory.</li>
</ol>

---
