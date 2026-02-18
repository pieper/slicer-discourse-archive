# Build Slicer in apple silicon - error "arm64"

**Topic ID**: 39549
**Date**: 2024-10-05
**URL**: https://discourse.slicer.org/t/build-slicer-in-apple-silicon-error-arm64/39549

---

## Post #1 by @park (2024-10-05 18:48 UTC)

<p>Hi all,</p>
<p>During the build process as per Steve’s advice, <a href="https://github.com/Slicer/Slicer/issues/5944" rel="noopener nofollow ugc">#5944</a><br>
I encountered the following issue. Has anyone resolved this?</p>
<p><strong>Computer Specifications:</strong></p>
<ul>
<li>CPU: M1 Pro</li>
<li>OS: macOS Ventura</li>
<li>Xcode: 13.0</li>
</ul>
<p><strong>Process:</strong></p>
<ol>
<li>Installed Qt5 and CMake using Homebrew.</li>
</ol>
<pre><code class="lang-auto">brew install qt@5
brew install cmake
</code></pre>
<ol start="2">
<li>Build OpenSSL:</li>
</ol>
<pre><code class="lang-auto">git clone https://github.com/openssl/openssl.git openssl-git
cd openssl-git
./Configure darwin64-arm64-cc --prefix="/tmp/openssl-arm" no-asm
make &amp;&amp; make install
mv OpenSSL-install OpenSSL-install-orig
ln -s /tmp/openssl-arm ./OpenSSL-install
</code></pre>
<p>3.Configured using CMake command:</p>
<pre><code class="lang-auto">sudo cmake \
  -DCMAKE_OSX_ARCHITECTURES=arm64 \
  -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DSlicer_USE_SYSTEM_OpenSSL:BOOL=ON \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DSlicer_BUILD_DICOM_SUPPORT:BOOL=OFF \
  -DQt5_DIR:PATH=/opt/homebrew/Cellar/qt@5/5.15.13_1/lib/cmake/Qt5 \
  /opt/T/S
</code></pre>
<ol start="4">
<li>Change cmakelists relates to <code>ffi</code></li>
</ol>
<pre><code class="lang-auto">+       message("skipping ctypes on mac")
+        #add_python_extension(_ctypes
+            #SOURCES ${ctypes_COMMON_SOURCES}
+                    #_ctypes/malloc_closure.c
+                    #_ctypes/darwin/dlfcn_simple.c
+                    #_ctypes/libffi_osx/ffi.c
+                    #_ctypes/libffi_osx/x86/darwin64.S
+                    #_ctypes/libffi_osx/x86/x86-darwin.S
+                    #_ctypes/libffi_osx/x86/x86-ffi_darwin.c
+                    #_ctypes/libffi_osx/x86/x86-ffi64.c
+            #INCLUDEDIRS ${SRC_DIR}/Modules/_ctypes/libffi_osx/include
+                        #${SRC_DIR}/Modules/_ctypes/darwin
</code></pre>
<p><strong>Then, I got the error like this</strong></p>
<pre><code class="lang-auto">"tbb::detail::r1::terminate(tbb::detail::d1::task_arena_base&amp;)", referenced from:
    tbb::detail::d1::task_arena::terminate() in vtkSMPToolsImpl.cxx.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
</code></pre>

---

## Post #2 by @pieper (2024-10-05 19:18 UTC)

<p>I haven’t tried building on mac arm in a long time, so more recent changes in the dependencies may have broken things.</p>
<p>One idea is to turn off this flag:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/SuperBuild/External_VTK.cmake#L9">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/SuperBuild/External_VTK.cmake#L9" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/SuperBuild/External_VTK.cmake#L9" target="_blank" rel="noopener">Slicer/Slicer/blob/main/SuperBuild/External_VTK.cmake#L9</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li></li>
          <li>set(proj VTK)</li>
          <li></li>
          <li># Set dependency list</li>
          <li>set(${proj}_DEPENDENCIES "zlib")</li>
          <li>if (Slicer_USE_PYTHONQT)</li>
          <li>  list(APPEND ${proj}_DEPENDENCIES python)</li>
          <li>endif()</li>
          <li class="selected">if(Slicer_USE_TBB)</li>
          <li>  list(APPEND ${proj}_DEPENDENCIES tbb)</li>
          <li>endif()</li>
          <li></li>
          <li># Include dependent projects if any</li>
          <li>ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDENCIES)</li>
          <li></li>
          <li>if(Slicer_USE_SYSTEM_${proj})</li>
          <li>  unset(VTK_DIR CACHE)</li>
          <li>  unset(VTK_SOURCE_DIR CACHE)</li>
          <li>  find_package(VTK REQUIRED NO_MODULE)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @pieper (2025-05-05 01:43 UTC)

<p><a class="mention" href="/u/park">@park</a> - did you ever have luck getting this build to work?  Do you have an updated build script you can share that works with current Slicer? Thanks in advance.</p>

---

## Post #4 by @park (2025-05-05 07:12 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> .<br>
No I haven’t succeeded yet, I am sorry couldn’t be of help.</p>

---

## Post #5 by @MJamal (2025-07-22 08:06 UTC)

<p>Hello,</p>
<p>I am also encountering this same error. I have attached the logs:</p>
<pre><code class="lang-auto">  "tbb::detail::r1::terminate(tbb::detail::d1::task_arena_base&amp;)", referenced from:
      vtk::detail::smp::vtkSMPToolsImplTBBInitialize::~vtkSMPToolsImplTBBInitialize() in vtkSMPToolsImpl.cxx.o
      vtk::detail::smp::vtkSMPToolsImpl&lt;(vtk::detail::smp::BackendType)2&gt;::Initialize(int) in vtkSMPToolsImpl.cxx.o
      vtk::detail::smp::vtkSMPToolsImpl&lt;(vtk::detail::smp::BackendType)2&gt;::Initialize(int) in vtkSMPToolsImpl.cxx.o
ld: symbol(s) not found for architecture arm64
c++: error: linker command failed with exit code 1 (use -v to see invocation)
make[5]: *** [lib/libvtkCommon-9.5.9.5.dylib] Error 1
make[4]: *** [CMakeFiles/Common.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [VTK-prefix/src/VTK-stamp/VTK-build] Error 2
make[1]: *** [CMakeFiles/VTK.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>Any solution on how to fix this?</p>
<p>System: mac os version sequoia v15.5</p>

---

## Post #6 by @chir.set (2025-07-22 08:21 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="5" data-topic="39549">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Any solution on how to fix this?</p>
</blockquote>
</aside>
<p>I don’t build on Mac but tried once for aarch64 on an x86_64 system.</p>
<p>TBB is not available for aarch64 so you should configure without this option:</p>
<p><code>Slicer_VTK_SMP_IMPLEMENTATION_TYPE:STRING=Sequential</code></p>

---
