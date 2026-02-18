# Slicer latest preview release not working on Ubuntu 20?

**Topic ID**: 25361
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/slicer-latest-preview-release-not-working-on-ubuntu-20/25361

---

## Post #1 by @mau_igna_06 (2022-09-20 17:55 UTC)

<p>Hi. I execute Slicer and get this error message:</p>
<pre><code class="lang-auto">mauro@mauro:~/Escritorio/Slicer-5.1.0-2022-09-19-linux-amd64$ ./Slicer
/home/mauro/Escritorio/Slicer-5.1.0-2022-09-19-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libitkhdf5_hl-shared-5.3.so.1: cannot open shared object file: No such file or directory
</code></pre>

---

## Post #2 by @chir.set (2022-09-20 19:02 UTC)

<p>I got this same error after building Slicer this weekend on Arch. Copying the missing library from the build tree fixed the issue. There was a major ITK upgrade, the packaging script should perhaps be optimized.</p>

---

## Post #3 by @pieper (2022-09-20 20:00 UTC)

<p>Thanks for the report <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> and the suggested fix <a class="mention" href="/u/chir.set">@chir.set</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">   I agree this sounds like a packaging script issue.</p>
<p>FWIW, Slicer-5.1.0-2022-09-19-macosx-amd64 runs for me on mac.</p>

---

## Post #4 by @chir.set (2022-09-24 19:47 UTC)

<p>This patch allows to include the missing ITK library in the package :</p>
<pre><code class="lang-auto">diff --git a/CMake/SlicerBlockInstallCMakeProjects.cmake b/CMake/SlicerBlockInstallCMakeProjects.cmake
index b98f948e8f..6fca3cb21e 100644
--- a/CMake/SlicerBlockInstallCMakeProjects.cmake
+++ b/CMake/SlicerBlockInstallCMakeProjects.cmake
@@ -26,6 +26,8 @@ if(NOT "${ITK_DIR}" STREQUAL "" AND EXISTS "${ITK_DIR}/CMakeCache.txt")
   set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${ITK_DIR};ITK;libraries;/")
   # HDF5 - hdf5_cpp
   set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${ITK_DIR};ITK;cpplibraries;/")
+  # HDF5 - hdf5_hl
+  set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${ITK_DIR};ITK;hllibraries;/")
   # HDF5 until ITK4. final, then it can be removed
   set(CPACK_INSTALL_CMAKE_PROJECTS "${CPACK_INSTALL_CMAKE_PROJECTS};${ITK_DIR};ITK;Unspecified;/")
</code></pre>
<p>Hopefully, it may get fixed in master.</p>

---
