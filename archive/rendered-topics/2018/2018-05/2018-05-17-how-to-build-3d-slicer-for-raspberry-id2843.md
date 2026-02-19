---
topic_id: 2843
title: "How To Build 3D Slicer For Raspberry"
date: 2018-05-17
url: https://discourse.slicer.org/t/2843
---

# How to build 3D Slicer for Raspberry?

**Topic ID**: 2843
**Date**: 2018-05-17
**URL**: https://discourse.slicer.org/t/how-to-build-3d-slicer-for-raspberry/2843

---

## Post #1 by @AhmadHossam10 (2018-05-17 15:19 UTC)

<p>How to build slicer on raspberri Pi having rasbpian OS?</p>

---

## Post #2 by @lassoan (2018-05-17 15:54 UTC)

<p>Follow Linux <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build instructions</a>. Complete build takes several hours on a desktop PC, so on a raspberry Pi it may take days, but it’ll be interesting to see if it is feasible.</p>

---

## Post #3 by @jcfr (2018-05-18 15:52 UTC)

<p>Instead of compiling Slicer directly on the Raspberry, I suggest to look at using “cross-compilation” approaches.</p>
<p>In the past, we successfully cross-compiled ITK and VTK:</p>
<ul>
<li><a href="https://blog.kitware.com/cross-compile-itks-python-wrapping-for-the-raspberry-pi-2/">Kitware Blog: Cross-compile ITK’s Python Wrapping for the Raspberry Pi 2</a></li>
<li><a href="https://blog.kitware.com/raspberry-pi-likes-vtk/">Kitware Blog: Raspberry Pi likes VTK</a></li>
</ul>
<p>With the improvement to CMake (e.g support for cross-compiling emulator) as well as the work put into the dockcross project, it should be easier today.</p>
<ul>
<li>Cross compiling toolchains in Docker images : <a href="https://github.com/dockcross/dockcross">https://github.com/dockcross/dockcross</a>
</li>
<li><a href="https://blog.kitware.com/cross-compiling-for-the-raspberry-pi-evolved/">Kitware Blog: Cross-compiling for the Raspberry Pi, Evolved</a></li>
</ul>
<p>Further experiments would be needed to compile Qt5. Here are some pointers:</p>
<ul>
<li><a href="https://wiki.qt.io/Native_Build_of_Qt5_on_a_Raspberry_Pi">https://wiki.qt.io/Native_Build_of_Qt5_on_a_Raspberry_Pi</a></li>
<li><a href="https://visualgdb.com/tutorials/raspberry/qt/embedded/">https://visualgdb.com/tutorials/raspberry/qt/embedded/</a></li>
</ul>
<p>At first, I would also suggest to try to compile Slicer with the following options disabled:</p>
<pre><code class="lang-nohighlight">-DSlicer_USE_PYTHONQT:BOOL=OFF
-DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF
-DSlicer_BUILD_DICOM_SUPPORT:BOOL=OFF
-DSlicer_BUILD_DIFFUSION_SUPPORT:BOOL=OFF
-DSlicer_BUILD_EXTENSIONMANAGER_SUPPORT:BOOL=OFF
-DSlicer_BUILD_CLI:BOOL=OFF
-DBUILD_TESTING:BOOL=OFF
-DSlicer_BUILD_QTLOADABLEMODULES:BOOL=OFF
-DSlicer_BUILD_QTSCRIPTEDMODULES:BOOL=OFF
</code></pre>
<p>Also, since options like <a href="https://cmake.org/cmake/help/v3.11/variable/CMAKE_CROSSCOMPILING.html">CMAKE_CROSSCOMPILING</a> and <a href="https://cmake.org/cmake/help/v3.11/variable/CMAKE_CROSSCOMPILING_EMULATOR.html">CMAKE_CROSSCOMPILING_EMULATOR</a> are not propagated down to external projects, I suggest to first build dependent libraries by starting with VTK, then ITK, …</p>
<p>To find in which order to build the dependency, you could look at the topological order displayed when configuring Slicer using a regular toolchain:</p>
<pre><code class="lang-bash">$ cmake ...
[...]
-- SuperBuild - First pass
-- SuperBuild - First pass - done
-- SuperBuild - Slicer =&gt; Requires curl, CTKAppLauncherLib, teem, VTKv9, ITKv4, CTK, LibArchive, RapidJSON, SimpleITK, SlicerExecutionModel, qRestAPI, DCMTK, python-pydicom, python-chardet, python-couchdb, python-GitPython, python-pip, python-PyGithub, CTKAPPLAUNCHER, python, NUMPY, incrTcl,
[...]
</code></pre>
<p>All project listed after <strong>– SuperBuild - Slicer =&gt; Requires</strong> are listed in topological order. (Note that in the case of building for Raspberry, less projects would  be listed because of the disabled options.)</p>
<p>After all required projects are cross-compiled independently (e.g using dockcross), you could then configure Slicer also using dockcross with option like these ones:</p>
<pre><code class="lang-auto">cmake -DVTK_DIR:PATH= ... -DITK_DIR=PATH= ...  -DSlicer_SUPERBUILD:BOOL=OFF ../Slicer
</code></pre>
<p>Also, since there are no prebuilt binaries of the launcher available for Raspberry, you could set <code>Slicer_USE_CTKAPPLAUNCHER</code> to <code>OFF</code> and use a shell script to set the startup environment.</p>
<p>Let us know if you have any questions,<br>
J-Christophe</p>

---

## Post #4 by @chir.set (2018-05-20 14:03 UTC)

<p>I built Slicer on <a href="http://www.hardkernel.com/main/products/prdt_info.php?g_code=G135341370451" rel="noopener nofollow ugc">Odroid-U2</a> out of technical interest on Arch Linux for ARM. There was just one more step to do :</p>
<p>build CTKAPPLAUNCHER,<br>
download <a href="https://github.com/commontk/AppLauncher/releases/download/v0.1.21/CTKAppLauncher-0.1.21-linux-amd64.tar.gz" rel="noopener nofollow ugc">CTKAppLauncher pre-compiled for amd64</a>,<br>
replace the x86_64 blob by the locally compiled ARM binary,<br>
rename the package and patch the cmake file :</p>
<blockquote>
<pre><code> diff --git a/SuperBuild/External_CTKAPPLAUNCHER.cmake b/SuperBuild/External_CTKAPPLAUNCHER.cmake
index dda4e1a54..911cdb428 100644
--- a/SuperBuild/External_CTKAPPLAUNCHER.cmake
+++ b/SuperBuild/External_CTKAPPLAUNCHER.cmake
@@ -30,7 +30,8 @@ if(Slicer_USE_CTKAPPLAUNCHER)
       set(CTKAPPLAUNCHER_ARCHITECTURE "i386")
       set(md5 "9fa2acb7d934a43720a0bee8679cbeff")
     elseif("${CTKAPPLAUNCHER_OS}" STREQUAL "linux")
-      set(md5 "57d9e6fc1fdfe42d78fc4e277b9559ba")
+      set(CTKAPPLAUNCHER_ARCHITECTURE "armv7l")
+      set(md5 "783455a7ee0bea086082f64da6adda1d")
     elseif("${CTKAPPLAUNCHER_OS}" STREQUAL "macosx")
       set(md5 "1f0d86b1eeb386d6892a76db7b111280")
     endif()
</code></pre>
</blockquote>
<p>Please not that if CTKAPPLAUNCHER_ARCHITECTURE is not explicitely set, it defaults to i386. There’s probably a simpler way to build it automatically, I’m eager to learn about it.</p>
<p>It takes about 24 hours to build using all 4 cores with lowest nice priority. Here is a <a href="https://mega.nz/#!lZ1lWDxS!txUyRsslaxzGvKWgKcBY9EGlQ_i2wWv0TmlO0Qacl8Y" rel="noopener nofollow ugc">video</a> captured with Slicer freshly started after rebooting the build device. (You may advance the video with the mouse, some simple steps are very long). Slices are never displayed in the viewers.</p>
<p>Of course it’s not for routine use.  Just a curious thing to do in the background.</p>

---

## Post #5 by @jcfr (2018-05-30 14:06 UTC)

<p>Well done.</p>
<p>Out of curiosity, did you have to apply any other patch to Slicer/VTK/ITK/… or it “just worked” ?</p>
<blockquote>
<p>AppLauncher for ARM</p>
</blockquote>
<p>If you could look at <a href="https://github.com/dockcross/dockcross#cross-compilers">dockcross</a> identify the cross-compiler corresponding to Odroid-U2, it should be possible to have the corresponding launcher binaries automatically built and available AppLauncher <a href="https://github.com/commontk/AppLauncher/releases">release</a> assets.</p>

---

## Post #6 by @chir.set (2018-05-30 15:15 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="2843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>did you have to apply any other patch to Slicer/VTK/ITK/… or it “just worked” ?</p>
</blockquote>
</aside>
<p>I applied the patches mentioned <a href="https://discourse.slicer.org/t/fyi-building-slicer-with-gcc-8-1/2830">here</a> because I used GCC 8.1 on the Odroid-U2 SoC too. I guess these three patches would not be needed for GCC &lt; 8, and it would just work.</p>
<p>Concerning cross-compiling, it’s certainly a good idea, I’ll dig into that when I find some time.</p>
<p>Concerning AppLauncher to be built locally, I understand that both with native or cross-compiling, the current cmake file does not build AppLauncher yet, it should be modified to download sources etc… and this is well beyond my skills.</p>

---
