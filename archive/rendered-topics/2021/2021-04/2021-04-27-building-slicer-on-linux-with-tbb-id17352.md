# Building Slicer on Linux with TBB

**Topic ID**: 17352
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/building-slicer-on-linux-with-tbb/17352

---

## Post #1 by @chir.set (2021-04-27 14:17 UTC)

<p>Following this <a href="https://discourse.slicer.org/t/why-the-the-tool-of-scissor-become-slower-after-i-undated-my-computer/10887/11">discussion</a>.</p>
<p>Slicer builds on Arch Linux with TBB by passing Slicer_VTK_SMP_IMPLEMENTATION_TYPE:STRING=TBB to cmake.</p>
<p>However, VTK failed initially :</p>
<pre><code>[  7%] Built target vtkCommonComputationalGeometryObjects
make[2]: *** No rule to make target '/home/arc/src/Slicer4138-SuperBuild/tbb-install/tbb2019_20191006oss/lib/intel64/gcc4.4/libtbb.so', needed by 'lib/libvtkCommon-8.2.so.1'.  Stop.
make[1]: *** [CMakeFiles/Makefile2:3342: CMakeFiles/vtkCommon.dir/all] Error 2
make: *** [Makefile:136: all] Error 2
</code></pre>
<p>It is easily fixed in SuperBuild/External_tbb.cmake :</p>
<p>-  set(tbb_libdir “lib/${tbb_archdir}/gcc4.4”)<br>
+  set(tbb_libdir “lib/${tbb_archdir}/gcc4.8”)</p>
<p>Packaging succeeds, but with a console error message :</p>
<pre><code>CPack: - Run preinstall target for: Slicer
CPack: - Install project: Slicer []
/usr/bin/strip: « /home/arc/src/Slicer4138-SuperBuild/Slicer-build/_CPack_Packages/linux-amd64/TGZ/Slicer-4.13.0-2021-04-25-linux-amd64/./lib/Slicer-4.13/libtbb.so.2;./lib/Slicer-4.13/libtbbmalloc.so.2;./lib/Slicer-4.13/libtbbmalloc_proxy.so.2 »: no such file
CPack: Create package
</code></pre>
<p>corresponding to instructions in Slicer4138-SuperBuild/Slicer-build/CMake/LastConfigureStep/cmake_install.cmake</p>
<pre><code>if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xRuntimex" OR NOT CMAKE_INSTALL_COMPONENT)
  message(STATUS "Stripping: $ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/./lib/Slicer-4.13/libtbb.so.2;./lib/Slicer-4.13/libtbbmalloc.so.2;./lib/Slicer-4.13/libtbbmalloc_proxy.so.2")
execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/./lib/Slicer-4.13/libtbb.so.2;./lib/Slicer-4.13/libtbbmalloc.so.2;./lib/Slicer-4.13/libtbbmalloc_proxy.so.2")
endif()
</code></pre>
<p>Slicer runs normally.</p>
<p>How can one notice an increased performance due to parallel tasking ? In which modules and at which steps ? Is there some python script that would allow to compare things ? A quick test in Segment Editor does not seem to trigger all CPU cores.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-04-28 01:20 UTC)

<p>Update of 3D view after editing a segment is a good test, because both flying edge surface extraction and surface smoothing are faster with TBB.</p>
<p>The main motivation for enabling TBB was that image reslicing was very slow on Windows with systems that had good NVidia GPU in them (due to some conflict of threaded optimization heuristics in the NVidia driver and creation&amp;destroying of many threads in VTK’s default SMP backend). So, if you use a desktop computer with a strong NVidia GPU then you might see performance improvement in reslicing (browsing slice views).</p>

---
