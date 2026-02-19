---
topic_id: 41633
title: "Build Slicer With The System Python"
date: 2025-02-11
url: https://discourse.slicer.org/t/41633
---

# Build Slicer with the system Python

**Topic ID**: 41633
**Date**: 2025-02-11
**URL**: https://discourse.slicer.org/t/build-slicer-with-the-system-python/41633

---

## Post #1 by @martin-g (2025-02-11 15:58 UTC)

<p>Hi,</p>
<p>I am trying to build Slicer and I want to use as many <code>-DSlicer_USE_SYSTEM_***=1</code> as possible.<br>
I provide all the dependencies with conda.</p>
<p>My conda environment is activated and there I have Python 3.13.1 installed, together with <code>packaging</code> and many more packages.</p>
<p>I use the following command to generate the build files:</p>
<pre><code class="lang-auto">cmake -S . -B build  \
    -DCMAKE_C_COMPILER=$CC \
    -DCMAKE_CXX_COMPILER=$CXX \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS $LDFLAGS" \
    -DCMAKE_C_FLAGS="$CFLAGS $LDFLAGS" \
    -DSlicer_FORCED_REVISION="12345678" \
    -Wno-dev \
    -DSlicer_USE_SYSTEM_LZMA=1 \
    -DSlicer_USE_SYSTEM_zlib=1 \
    -DSlicer_USE_SYSTEM_bzip2=1 \
    -DSlicer_USE_SYSTEM_curl=1 \
    -DSlicer_USE_SYSTEM_LibFFI=1 \
    -DSlicer_USE_SYSTEM_DCMTK=1 \
    -DSlicer_USE_SYSTEM_OpenSSL=1 \
    -DSlicer_USE_SYSTEM_LibArchive=1 \
    -DSlicer_USE_SYSTEM_Swig=1 \
    -DSlicer_USE_SimpleITK_SHARED="ON" \
    -DSlicer_VTK_SMP_IMPLEMENTATION_TYPE="TBB" \
    -DBUILD_TESTING="OFF" \
    -DCMAKE_MESSAGE_LOG_LEVEL=ERROR \
    -DSlicer_USE_SYSTEM_python=1 \
    -DPYTHON_EXECUTABLE:FILEPATH="/home/mgrigorov/git/slicer/.pixi/envs/default/bin/python3" \
    -DSlicer_USE_SYSTEM_python-pythonqt-requirements=1
</code></pre>
<p>But it fails with:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'packaging'
CMake Error at CMake/ExternalProjectDependencyForPython.cmake:111 (message):
  Could not import module for required dependency 'packaging' using
  '/usr/bin/python3.9' interpreter.
Call Stack (most recent call first):
  SuperBuild/External_python-pythonqt-requirements.cmake:24 (ExternalProject_FindPythonPackage)
  CMake/ExternalProjectDependency.cmake:890 (include)
  CMake/ExternalProjectDependency.cmake:964 (ExternalProject_Include_Dependencies)
  SuperBuild.cmake:473 (ExternalProject_Include_Dependencies)
  CMakeLists.txt:779 (include)


-- Configuring incomplete, errors occurred!
</code></pre>
<p>It seems it ignores the PYTHON_EXECUTABLE setting…<br>
<code>/home/mgrigorov/git/slicer/.pixi/envs/default/bin/</code> is the first entry in $PATH, so both <code>python</code> and <code>python3</code> are used from there.</p>
<p>Any idea why cmake tries to use <code>/usr/bin/python3.9</code> instead ?</p>
<p>P.S. If I try to use the vendored Python, i.e. <code>-DSlicer_USE_SYSTEM_python=0</code> then it installs SlicerPython that is for x86_64 while I run it on Linux aarch64 system.</p>

---
