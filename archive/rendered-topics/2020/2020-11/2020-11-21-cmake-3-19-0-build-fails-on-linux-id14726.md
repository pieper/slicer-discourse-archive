---
topic_id: 14726
title: "Cmake 3 19 0 Build Fails On Linux"
date: 2020-11-21
url: https://discourse.slicer.org/t/14726
---

# Cmake 3.19.0 : build fails on Linux

**Topic ID**: 14726
**Date**: 2020-11-21
**URL**: https://discourse.slicer.org/t/cmake-3-19-0-build-fails-on-linux/14726

---

## Post #1 by @chir.set (2020-11-21 20:30 UTC)

<p>Build fails on Arch Linux with cmake 3.19.0 with the errors below. Reverting to cmake 3.18.4 fixes the problem.</p>
<p>Not a fundamental issue, FYI.</p>
<p>Regards.</p>
<p>…<br>
…<br>
CMake Deprecation Warning at Modules/ThirdParty/GoogleTest/src/itkgoogletest/googletest/CMakeLists.txt:56 (cmake_minimum_required):<br>
Compatibility with CMake &lt; 2.8.12 will be removed from a future version of<br>
CMake.</p>
<pre><code>  Update the VERSION argument &lt;min&gt; value or use a ...&lt;max&gt; suffix to tell
  CMake that the project does not need compatibility with older versions.


CMake Deprecation Warning at Modules/ThirdParty/MINC/src/libminc/CMakeLists.txt:25 (CMAKE_MINIMUM_REQUIRED):
  Compatibility with CMake &lt; 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument &lt;min&gt; value or use a ...&lt;max&gt; suffix to tell
  CMake that the project does not need compatibility with older versions.


CMake Error: install(EXPORT "ITKTargets" ...) includes target "gdcmjpeg8" more than once in the export set.
CMake Generate step failed.  Build files cannot be regenerated correctly.
make[3]: *** [CMakeFiles/ITK.dir/build.make:130: ITK-prefix/src/ITK-stamp/ITK-configure] Error 1
make[2]: *** [CMakeFiles/Makefile2:1423: CMakeFiles/ITK.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:223: CMakeFiles/Slicer.dir/rule] Error 2
make: *** [Makefile:137: Slicer] Error 2</code></pre>

---

## Post #2 by @guangxv (2020-11-30 06:53 UTC)

<p>It worked to use CMake-3.18.5 instead.</p>

---
