---
topic_id: 4173
title: "Where Is Slicerconfig Cmake"
date: 2018-09-23
url: https://discourse.slicer.org/t/4173
---

# Where is Slicerconfig.cmake

**Topic ID**: 4173
**Date**: 2018-09-23
**URL**: https://discourse.slicer.org/t/where-is-slicerconfig-cmake/4173

---

## Post #1 by @rasoul (2018-09-23 14:21 UTC)

<p>Hi every one,<br>
I wana building an extension(MABMIS) for slicer by CMake but I get this Error:</p>
<pre><code>CMake Error at CMakeLists.txt:12 (find_package):
By not providing &amp;quot;FindSlicer.cmake&amp;quot; in CMAKE_MODULE_PATH this project has
asked CMake to find a package configuration file provided by &amp;quot;Slicer&amp;quot;, but
CMake did not find one.
Could not find a package configuration file provided by &amp;quot;Slicer&amp;quot; with any
of the following names:

SlicerConfig.cmake
slicer-config.cmake

Add the installation prefix of &amp;quot;Slicer&amp;quot; to CMAKE_PREFIX_PATH or set
&amp;quot;Slicer_DIR&amp;quot; to a directory containing one of the above files. If &amp;quot;Slicer&amp;quot;
provides a separate development package or SDK, be sure it has been
installed.
</code></pre>
<p>So I build the slicer from sources but these files did not created, Where does they build usually?</p>

---

## Post #2 by @darekdev (2018-09-23 20:06 UTC)

<p>Hi,</p>
<p>what is the cmake command you are using for your extension? You need to specify Slicer-build folder location.</p>

---

## Post #3 by @rasoul (2018-09-24 05:26 UTC)

<p>I am using cmake GUI, so I just specify source and build folders. (so I do not use any command). I specify slicer build location but it said to me it can not find:</p>
<p>SlicerConfig.cmake<br>
slicer-config.cmake</p>

---

## Post #4 by @darekdev (2018-09-24 11:03 UTC)

<p>What version of cmake are you using? I suggest to use the newest version for example 3.12.0.</p>

---

## Post #5 by @lassoan (2018-09-24 12:14 UTC)

<p>Is your Slicer build completed successfully? Does Slicer start if you run Slicer.exe in your build tree?</p>
<p>Make sure you specify Slicer-build subfolder and not the top-level build directory.</p>

---

## Post #7 by @rasoul (2018-09-29 14:36 UTC)

<p>No I found that it did not completed successfully, I have this error in slicer configuration step:</p>
<p>CMake Error at CMake/SlicerBlockFindQtAndCheckVersion.cmake:45 (message):<br>
error: Qt 4.7.4 was not found on your system.You probably need to set the<br>
QT_QMAKE_EXECUTABLE variable.<br>
Call Stack (most recent call first):<br>
CMake/SlicerBlockFindQtAndCheckVersion.cmake:110 (__SlicerBlockFindQtAndCheckVersion_find_qt)<br>
CMakeLists.txt:602 (include)</p>
<p>I am building slicer with its <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">proposed steps</a>. It proposed Qt version 5.1.0, which I downloaded and install successfully. I changed QT_QMAKE_EXECUTABLE to</p>
<p>D:/Qt_Online/5.10.0/msvc2015_64/bin/qmake.exe</p>
<p>and still I have that error.</p>

---

## Post #8 by @lassoan (2018-09-29 17:18 UTC)

<p>You need to set Qt5_DIR as described in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build instructions</a>.</p>

---

## Post #9 by @rasoul (2018-09-30 06:34 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I set it but now it does not find some sub directories:</p>
<p>Qt5PHONON_DIR-NOTFOUND<br>
Qt5QTCORE_DIR-NOTFOUND<br>
Qt5QTGUI_DIR-NOTFOUND</p>
<p>and ten others. I installed Qt5 by [qt-unified-windows-x86-online.exe].<br>
(<a href="https://download.qt.io/official_releases/online_installers/qt-unified-windows-x86-online.exe" rel="nofollow noopener">https://download.qt.io/official_releases/online_installers/qt-unified-windows-x86-online.exe</a>).</p>

---

## Post #10 by @darekdev (2018-09-30 08:45 UTC)

<p>Did you remove build directory before running cmake? Clean up build directory (delete it and create new empty) and then set Qt5_DIR according to this <a href="https://discourse.slicer.org/t/build-error-pythonqt-visual-studio-2015-qt-5-9-2/1411/4?u=darekdev">Build Error PythonQt Visual Studio 2015 Qt 5.9.2</a>.</p>

---

## Post #11 by @rasoul (2018-09-30 09:42 UTC)

<p>Yes I built in a completely new folder. You know, there is no such a folder with those names(Qt5PHONON , Qt5QTCORE , Qt5QTGUI) in that directory.</p>

---

## Post #12 by @lassoan (2018-09-30 12:43 UTC)

<p>It seems that you have partially configured your the CMake project before provided Qt5 directory. You need to start again from scratch and follow configuration instructions very accurately, especially the bold part: do not click configure before specifying Qt5_DIR.</p>
<p>It is difficult to pay attention to all details each time you rebuild Slicer, therefore I always build Slicer using a batch file. In the .bat file you can specify CMake options using command-line options. I’ve added a few examples to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Configure#Windows">Windows configuration instructions</a>.</p>

---

## Post #13 by @rasoul (2018-09-30 14:39 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, It now configured completely without any error.</p>

---

## Post #14 by @rasoul (2018-10-09 13:24 UTC)

<p>After I configured it successfully by CMake, I generated slicer.sln and then built it using vs2015 x64. But it configured with 50 succeeded and 2 failed which I do not understand them. I see in error list just this description:</p>
<p>Error	MSB6006	“cmd.exe” exited with code 1.	Slicer	C:\Program Files<br>
(x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets	171</p>
<p>What is wrong with my building?</p>

---

## Post #15 by @fedorov (2018-10-09 15:21 UTC)

<p>Did you follow the advice below, as described in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Configure#Windows">windows-specific instructions</a>?</p>
<blockquote>
<p>In case of  <em>any</em>  build error, use very short directory names: C:\S4 for source directory, C:\S4D for debug build, C:\S4R for release build.</p>
</blockquote>

---

## Post #17 by @rasoul (2018-10-10 05:49 UTC)

<p>Yes I think that was too short, but now I am building it again using exactly the same directories you said (but in drive D!). Thanks <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #18 by @lassoan (2018-10-10 14:40 UTC)

<aside class="quote no-group" data-username="rasoul" data-post="14" data-topic="4173">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rasoul/48/1493_2.png" class="avatar"> rasoul:</div>
<blockquote>
<p>Error MSB6006 “cmd.exe” exited with code 1. Slicer C:\Program Files<br>
(x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets 171</p>
</blockquote>
</aside>
<p>This indicates that some of the targets were failed to build, but does not tell what was the problem. You should find the actual error message in the full build log (c:\D\S4D\Testing\Temporary\LastBuild_YYYMMDD-HHMM.log).</p>

---

## Post #19 by @rasoul (2018-10-11 08:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, The folder you mentioned is empty. I built it again and now I can see the slicer.exe and SlicerConfig.cmake in slicer-build folder (but it has 2 failed again).<br>
Thank you so much</p>

---

## Post #20 by @lassoan (2018-10-11 12:21 UTC)

<p>Build logs should be in similarly named files. You can also just scroll up to see which project failed and open .sln file of that project and build it. Make sure to choose correct project configuration (Debug/Release) before start building.</p>

---
