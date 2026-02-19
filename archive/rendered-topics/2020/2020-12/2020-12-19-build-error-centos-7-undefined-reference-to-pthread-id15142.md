---
topic_id: 15142
title: "Build Error Centos 7 Undefined Reference To Pthread"
date: 2020-12-19
url: https://discourse.slicer.org/t/15142
---

# [Build Error] [CentOS 7] undefined reference to pthread_*

**Topic ID**: 15142
**Date**: 2020-12-19
**URL**: https://discourse.slicer.org/t/build-error-centos-7-undefined-reference-to-pthread/15142

---

## Post #1 by @tbillah (2020-12-19 04:51 UTC)

<p>Hi,</p>
<p>VTK builds independently in my CentOS 7 machine but appears not to as part of Slicer:</p>
<p>Console log:</p>
<pre><code class="lang-auto">[ 50%] Building CXX object Interaction/Widgets/CMakeFiles/vtkInteractionWidgetsObjects.dir/vtkContourLineInterpolator.cxx.o
[ 50%] Linking CXX executable ../../bin/vtkProbeOpenGLVersion
../../lib/libvtkexodusII-8.2.so.1: error: undefined reference to 'pthread_setspecific'
../../lib/libvtkexodusII-8.2.so.1: error: undefined reference to 'pthread_getspecific'
../../lib/libvtkexodusII-8.2.so.1: error: undefined reference to 'pthread_key_create'
../../lib/libvtkexodusII-8.2.so.1: error: undefined reference to 'pthread_mutexattr_settype'
../../lib/libvtkexodusII-8.2.so.1: error: undefined reference to 'pthread_mutexattr_init'
../../lib/libvtkexodusII-8.2.so.1: error: undefined reference to 'pthread_once'
../../lib/libvtkhdf5-8.2.so.1: error: undefined reference to 'dlerror'
../../lib/libvtkhdf5-8.2.so.1: error: undefined reference to 'dlopen'
../../lib/libvtkhdf5-8.2.so.1: error: undefined reference to 'dlsym'
../../lib/libvtkhdf5-8.2.so.1: error: undefined reference to 'dlclose'
collect2: error: ld returned 1 exit status
make[5]: *** [bin/vtkProbeOpenGLVersion] Error 1
make[4]: *** [Rendering/OpenGL2/CMakeFiles/vtkProbeOpenGLVersion.dir/all] Error 2
make[4]: *** Waiting for unfinished jobs....
[ 50%] Building CXX object Interaction/Widgets/CMakeFiles/vtkInteractionWidgetsObjects.dir/vtkContourWidget.cxx.o
...
...
[ 57%] Building CXX object Wrapping/Python/CMakeFiles/vtkCommonKitPythonD.dir/vtkCommonKitPythonInitImpl.cxx.o
[ 57%] Linking CXX shared library ../../lib/libvtkCommonKitPython36D-8.2.so
[ 57%] Built target vtkCommonKitPythonD
make[3]: *** [all] Error 2
make[2]: *** [VTK-prefix/src/VTK-stamp/VTK-build] Error 2
make[1]: *** [CMakeFiles/VTK.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>CMakeError.log:</p>
<pre><code class="lang-auto">Run Build Command(s):/usr/bin/gmake cmTC_f23cb/fast
gmake[3]: Entering directory `/data/pnl/soft/pnlpipe3/Slicer-4.11/build/VTK-build/ThirdParty/libxml2/vtklibxml2/CMakeFiles/CMakeTmp'
/usr/bin/gmake -f CMakeFiles/cmTC_f23cb.dir/build.make CMakeFiles/cmTC_f23cb.dir/build
gmake[4]: Entering directory `/data/pnl/soft/pnlpipe3/Slicer-4.11/build/VTK-build/ThirdParty/libxml2/vtklibxml2/CMakeFiles/CMakeTmp'
Building C object CMakeFiles/cmTC_f23cb.dir/platformTestsC.c.o
/apps/software-compiled/GCCcore/7.3.0/bin/cc -DTEST_HAVE_SYS_NDIR_H  -w -w    -o CMakeFiles/cmTC_f23cb.dir/platformTestsC.c.o   -c /data/pnl/soft/pnlpipe3/Slicer-4.11/build/VTK/ThirdParty/libxml2/vtklibxml2/platformTestsC.c
/data/pnl/soft/pnlpipe3/Slicer-4.11/build/VTK/ThirdParty/libxml2/vtklibxml2/platformTestsC.c:82:10: fatal error: sys/ndir.h: No such file or directory
 #include &lt;sys/ndir.h&gt;
          ^~~~~~~~~~~~
compilation terminated.
gmake[4]: *** [CMakeFiles/cmTC_f23cb.dir/platformTestsC.c.o] Error 1
gmake[4]: Leaving directory `/data/pnl/soft/pnlpipe3/Slicer-4.11/build/VTK-build/ThirdParty/libxml2/vtklibxml2/CMakeFiles/CMakeTmp'
gmake[3]: *** [cmTC_f23cb/fast] Error 2
gmake[3]: Leaving directory `/data/pnl/soft/pnlpipe3/Slicer-4.11/build/VTK-build/ThirdParty/libxml2/vtklibxml2/CMakeFiles/CMakeTmp'
</code></pre>
<p>I have cmake 3.14.2, gcc 7.3.0, and Mesa/18.1.1-foss-2018b. I am trying to build the default configuration with my own <code>Qt5_DIR</code>. Do the above errors look familiar? Any tip is appreciated.</p>

---

## Post #2 by @pieper (2020-12-20 19:49 UTC)

<p>Probably the default vtk build doesn’t enable features that lead to the build issue.  You can try enabling the same <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_VTK.cmake">features that the superbuild does</a> and isolate what leads to the error.  If you can reproduce it at the VTK level you can try reporting on their discourse.</p>

---

## Post #3 by @shangguan (2021-12-10 03:00 UTC)

<p>I have same errors. And I tried to add pthread and dl in vtk-cmakelists, but the errors still exists.Have you solve them?really appreciate for your help.</p>

---

## Post #4 by @shangguan (2021-12-14 02:36 UTC)

<p>I’ve fixed the bugs by modify the CmakeLists in /build/VTK.</p>

---

## Post #5 by @lassoan (2021-12-14 05:25 UTC)

<p>Could you describe the changes that solved the issue for you? Just in case someone else runs into the same problem.</p>

---

## Post #6 by @Alex_Vergara (2021-12-14 09:34 UTC)

<p>I have ran the same issues when preparin the docker image for Gate.I solved in the moment with</p>
<pre><code class="lang-auto">RUN if [ "$Centos_Version" = "centos:7" ]; then \
     yum install -y devtoolset-7-gcc-c++ \
  fi
</code></pre>
<p>But Centos7 proves to be very non friendly with modern packages.So I must move to Centos8 and that’s the current base for <a href="https://github.com/OpenGATE/Gate/pull/414" rel="noopener nofollow ugc">dockerized Gate</a></p>

---

## Post #7 by @shangguan (2021-12-16 08:53 UTC)

<p>Add<br>
set(CMAKE_CXX_FLAGS “${CMAKE_CXX_FLAGS} -pthread”)<br>
set(CMAKE_CXX_FLAGS “${CMAKE_CXX_FLAGS} -ldl”)<br>
after project(VTK) in build/VTK/CmakeLists.txt could solve the issues in my ubuntu20 machine.</p>

---
