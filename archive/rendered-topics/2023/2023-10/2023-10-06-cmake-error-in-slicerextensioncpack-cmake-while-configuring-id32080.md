# CMake error in SlicerExtensionCPack.cmake while configuring extension

**Topic ID**: 32080
**Date**: 2023-10-06
**URL**: https://discourse.slicer.org/t/cmake-error-in-slicerextensioncpack-cmake-while-configuring-extension/32080

---

## Post #1 by @fedorov (2023-10-06 18:30 UTC)

<p>I am getting the error below while trying to configure the build for the <a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser/">SlicerIDCBrowser extension</a>. The error seems to be unrelated to the extension. Does anyone know how to work around it?</p>
<p>I am using the latest, and the same, CMake 3.27.6 for both Slicer and my extension.</p>
<pre><code class="lang-auto">$ ~/cmake-3.27.6-linux-x86_64/bin/cmake -DSlicer_DIR:PATH=../Slicer-SuperBuild/Slicer-build ../SlicerIDCBrowser
[...]
-- Checking if CPACK_INSTALL_CMAKE_PROJECTS is defined
-- Checking if CPACK_INSTALL_CMAKE_PROJECTS is defined - no
CMake Error at /home/exouser/Slicer-SuperBuild/CTKAPPLAUNCHER/CMake/ctkAppLauncher.cmake:409 (file):
  file RELATIVE_PATH must be passed a full path to the file:
  ../Slicer-SuperBuild/Slicer-build
Call Stack (most recent call first):
  /home/exouser/Slicer/CMake/SlicerExtensionCPack.cmake:324 (ctkAppLauncherConfigureForExecutable)
  CMakeLists.txt:21 (include)


-- Setting 'CTEST_MODEL' variable with default value 'Experimental'
-- Setting 'SLICER_EXTENSION_
</code></pre>
<p>All I want to do is to confirm I can build and package the extension to make sure build/package succeeds for the next nightly.</p>

---

## Post #2 by @fedorov (2023-10-06 21:42 UTC)

<p>The solution was trivial - I needed to use the absolute path instead of relative!</p>
<pre><code class="lang-bash">$ ~/cmake-3.27.6-linux-x86_64/bin/cmake \
  -DSlicer_DIR:PATH=`pwd`/../Slicer-SuperBuild/Slicer-build \
  `pwd`/../SlicerIDCBrowser
</code></pre>

---
