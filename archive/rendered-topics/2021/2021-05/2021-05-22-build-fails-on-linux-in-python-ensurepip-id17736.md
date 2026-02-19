---
topic_id: 17736
title: "Build Fails On Linux In Python Ensurepip"
date: 2021-05-22
url: https://discourse.slicer.org/t/17736
---

# Build fails on Linux in python-ensurepip

**Topic ID**: 17736
**Date**: 2021-05-22
**URL**: https://discourse.slicer.org/t/build-fails-on-linux-in-python-ensurepip/17736

---

## Post #1 by @chir.set (2021-05-22 16:13 UTC)

<p>Build fails on Linux in python-ensurepip</p>
<p>I having this error since 9be0308d2 while building in Arch Linux :</p>
<blockquote>
<p>CMake Error at /home/arc/src/Slicer-SuperBuild/python-ensurepip-prefix/src/python-ensurepip-stamp/python-ensurepip-install-Release.cmake:49 (message):<br>
Command failed: 1</p>
<p>‘/home/arc/src/Slicer-SuperBuild/python-install/bin/PythonSlicer’ ‘-m’ ‘ensurepip’ ‘–default-pip’</p>
</blockquote>
<p>python-ensurepip-stamp/python-ensurepip-install-*.log do not provide any clue.</p>
<p>SLicer is configured as such :</p>
<blockquote>
<p>export CFLAGS=“-I/usr/include/tirpc”; export CXXFLAGS=“-I/usr/include/tirpc”; cmake -DSlicer_VTK_VERSION_MAJOR:INT=8 -DQt5_DIR:PATH=/usr/lib/cmake/Qt5 -DBUILD_TESTING:BOOL=OFF -DCMAKE_BUILD_TYPE:STRING=Release -DADDITIONAL_CXX_FLAGS:STRING=-I/usr/include/tirpc …/Slicer</p>
</blockquote>
<p>Removing lsb_release as in <a href="https://discourse.slicer.org/t/build-fails-in-python-ensurepip-on-linux/12023">here</a> doesn’t resolve the issue.</p>
<p>It has been building for years. What could be the problem ? How to research it further ? What could be a fix ?</p>
<p>Thanks and regards.</p>

---

## Post #2 by @chir.set (2021-05-23 16:39 UTC)

<p>Could finally build and run Slicer on Arch (with VTK8).</p>
<p>I had to :<br>
downgrade GCC from 11.0 to previous 10.2, else Python 3.6.7 fails at runtime with assigned tasks (ensurepip, setuptools),<br>
revert qt5-base to the previous one not built by GCC 11.0, else CTKAppLauncher would not link to QtCore.</p>
<pre><code> [ 96%] Linking CXX executable bin/CTKAppLauncher
/usr/bin/ld: /usr/lib/libQt5Core.so.5.15.2: undefined reference to `std::__exception_ptr::exception_ptr::_M_release()@CXXABI_1.3.13'
/usr/bin/ld: /usr/lib/libQt5Widgets.so.5.15.2: undefined reference to `std::__throw_bad_array_new_length()@GLIBCXX_3.4.29'
/usr/bin/ld: /usr/lib/libQt5Core.so.5.15.2: undefined reference to `std::__exception_ptr::exception_ptr::_M_addref()@CXXABI_1.3.13'
</code></pre>
<p>I tend to forget that Arch moves on very fast, and hope that built SlicerPython, of whatever version, becomes functional again with latest compilers.</p>
<p>Regards.</p>

---

## Post #3 by @ButuiHu (2021-06-21 11:59 UTC)

<p>It’s a temporary solution. ArchLinux would keep updating to the latest gcc. Other distribution will also update gcc soon or later.<br>
I also encounter compiling error trigger by gdcm, which is needed in ITK subproject.<br>
see also <a href="https://gcc.gnu.org/gcc-11/porting_to.html#header-dep-changes" class="inline-onebox" rel="noopener nofollow ugc">Porting to GCC 11 - GNU Project - Free Software Foundation (FSF)</a> for gcc 10 → gcc 11 upgrade porting changes.</p>

---
