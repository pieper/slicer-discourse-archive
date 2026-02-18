# Building Slicer with gcc 6

**Topic ID**: 1422
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/building-slicer-with-gcc-6/1422

---

## Post #1 by @franklinwk (2017-11-09 15:38 UTC)

<p>I am currently running Debian 9 and I’m trying to rebuild Slicer with gcc 6 which is the default in Debian 9.</p>
<p>I was originally trying to rebuild the stable Slicer 4.6.2 build but came across the issues that were mentioned here resolving all except the issue with ITK and ctk+11: <a href="https://issues.slicer.org/view.php?id=4268" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4268</a></p>
<p>I then tried building stable Slicer 4.8 but was unable to do so with Qt 4.8.7, and I must be doing something wrong building Qt5 because QtWebEngine remains unbuilt.</p>
<p>Is there a recommended/known revision of Slicer/Qt/Vtk that is known to work with Debian and gcc 6? I’m not particularly picky as long as it’s around 4.5 and up.</p>
<p>Thanks in advance</p>

---

## Post #2 by @gcsharp (2017-11-09 16:41 UTC)

<p>Hi Franklin,</p>
<p>Here is how I managed to build Slicer on Debian 9.  (This is git HEAD<br>
rather than stable, so YMMV.)</p>
<p>First, edit the top of CMakeLists.txt to be this:</p>
<pre><code class="lang-auto">set(_msg "Setting C++ standard")
message(STATUS "${_msg} - C++")
if(NOT DEFINED CMAKE_CXX_STANDARD)
  if("${Slicer_VTK_VERSION_MAJOR}" STREQUAL "8" OR DEFINED Qt5_DIR)
    set(CMAKE_CXX_STANDARD 11)
  else()
    set(CMAKE_CXX_STANDARD 98)
  endif()
endif()
# Since SimpleITK requires CMP0067 to properly support C++11, requires
# the corresponding CMake version.
if(CMAKE_CXX_STANDARD EQUAL 11 AND CMAKE_VERSION VERSION_LESS "3.8.2")
  if (NOT DEFINED Slicer_USE_SimpleITK OR Slicer_USE_SimpleITK)
    message(FATAL_ERROR "CMake &gt;= 3.8.2 is required to enable C++11
support")
  endif()
endif()
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
message(STATUS "${_msg} - C++${CMAKE_CXX_STANDARD}")
</code></pre>
<p>Next, edit External_OpenSSL.cmake to be this:</p>
<pre><code class="lang-auto">    set(OPENSSL_DOWNLOAD_VERSION "1.0.2l" CACHE STRING "Version of
OpenSSL source package to download")
    set(OpenSSL_1.0.2l_URL https://www.openssl.org/source/openssl-1.0.2
l.tar.gz)
    set(OpenSSL_1.0.2l_MD5 f85123cd390e864dfbe517e7616e6566)
</code></pre>
<p>Finally, configure like this:</p>
<pre><code class="lang-auto">cmake \
    -DQt5_DIR:PATH=/usr/lib/x86_64-linux-gnu/cmake/Qt5/ \
    -DSlicer_VTK_VERSION_MAJOR=8 \
    -DCMAKE_CXX_STANDARD=11 \
    -DSlicer_USE_SimpleITK:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING:BOOL=OFF \
    ../Slicer
</code></pre>
<p>Good luck!<br>
Greg</p>

---

## Post #3 by @cpinter (2017-11-09 17:04 UTC)

<p>Also please use 4.8 instead, as 4.6.2 is more than a year old, and there is no point trying anything with such an old version.</p>

---

## Post #4 by @franklinwk (2017-11-09 17:43 UTC)

<p>Hi Greg,</p>
<p>Thanks, I’ll try that out! Did you use Qt5 built from source (and if so via JC’s <a href="https://github.com/jcfr/qt-easy-build/tree/5.9.1#readme" rel="nofollow noopener">easy build</a>?) or another package?</p>

---

## Post #5 by @gcsharp (2017-11-09 18:19 UTC)

<p>Hi Franklin,</p>
<p>No.  I use Debian’s qt5 packages.  In Debian 9 it is Qt 5.7.1.</p>
<p>Update 2017-11-16.  Following packages are needed:</p>
<p>qt5-qmake<br>
libqt5webkit5-dev<br>
qtmultimedia5-dev<br>
qttools5-dev-tools<br>
qttools5-dev<br>
libqt5xmlpatterns5-dev<br>
libqt5svg5-dev<br>
qtwebengine5-dev<br>
qtscript5-dev<br>
libqt5x11extras5-dev<br>
qtbase5-private-dev<br>
qtpositioning5-dev</p>
<p>Greg</p>

---
