---
topic_id: 6459
title: "Slicer For Ubuntu Arm64"
date: 2019-04-10
url: https://discourse.slicer.org/t/6459
---

# Slicer for Ubuntu arm64

**Topic ID**: 6459
**Date**: 2019-04-10
**URL**: https://discourse.slicer.org/t/slicer-for-ubuntu-arm64/6459

---

## Post #1 by @adamrankin (2019-04-10 21:30 UTC)

<p>Notes on compilation efforts for compiling Slicer for arm64:</p>
<p><strong>Problem</strong>: VTK does not compile.<br>
<em>Solution</em>:</p>
<ul>
<li>Set VTK_OPENGL_HAS_EGL and VTK_OPENGL_HAS_ES</li>
<li>In <code>&lt;SlicerDir&gt;/SuperBuild/External_VTK.cmake</code> remove section that has <code>-DModule_vtkGUISupportQtOpenGL:BOOL=ON</code> in it</li>
<li>Edit <code>QVTKOpenGLNativeWidget.cxx</code> to use <code>QOpenGLExtraFunctions</code> instead of <code>QOpenGLFunctions_3_2_Core</code>
</li>
</ul>
<p><strong>Problem</strong>: CTKAPPLAUNCHER is a download of amd64<br>
<em>Solution</em>: Overwrite executable <code>&lt;Slicer-build&gt;/CTKAPPLAUNCHER/bin/CTKAppLauncher</code> with compiled executable from <code>&lt;Slicer-build&gt;/CTKAppLauncherLib-build/bin/CTKAppLauncher</code></p>

---

## Post #2 by @jcfr (2019-04-11 14:41 UTC)

<p>Thanks for the report.</p>
<p>Could you describe here:</p>
<ul>
<li>how you setup the build environment / toolchain ?</li>
<li>in addition of the change described above, build options used ?</li>
</ul>
<p>This would help improve the build system.</p>
<p>To enable others to reproduce the build, do you think a docker image could be added to <a href="https://github.com/Slicer/SlicerBuildEnvironment/" rel="nofollow noopener">https://github.com/Slicer/SlicerBuildEnvironment/</a> ?</p>

---

## Post #3 by @adamrankin (2019-04-11 15:53 UTC)

<p>For sure, I’m expect it to be a slog, so this post is just for my notes as well as other googlers. Build options are all default unless a note is present in the main post.</p>
<blockquote>
<p>To enable others to reproduce the build, do you think a docker image could be added to <a href="https://github.com/Slicer/SlicerBuildEnvironment/" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a> ?</p>
</blockquote>
<p>Of course, how can I create a docker image?</p>
<p>Platform is <a href="http://wiki.friendlyarm.com/wiki/index.php/FriendlyDesktop_18.04_for_RK3399" rel="noopener nofollow ugc">FriendlyDesktop</a> for <a href="http://wiki.friendlyarm.com/wiki/index.php/NanoPC-T4" rel="noopener nofollow ugc">NanoPC-T4</a>.</p>
<p>Details:<br>
<strong>Qt</strong><br>
Qt 5.10.0, provided in image.<br>
qtchooser cleaned up:</p>
<blockquote>
<p>pi@NanoPC-T4:~/devel/S4R$ qtchooser -qt=5.10 -print-env<br>
QT_SELECT=“5.10”<br>
QTTOOLDIR=“/usr/local/Trolltech/Qt-5.10.0-rk64one-sdk/bin”<br>
QTLIBDIR=“/usr/local/Trolltech/Qt-5.10.0-rk64one/lib”</p>
</blockquote>
<p><strong>CMake</strong><br>
CMake 3.14.1 built from source (<code>make &amp;&amp; sudo make install</code>)</p>
<p><strong>GCC</strong></p>
<blockquote>
<p>Using built-in specs.<br>
COLLECT_GCC=gcc<br>
COLLECT_LTO_WRAPPER=/usr/lib/gcc/aarch64-linux-gnu/7/lto-wrapper<br>
Target: aarch64-linux-gnu<br>
Configured with: …/src/configure -v --with-pkgversion=‘Ubuntu/Linaro 7.3.0-27ubuntu1~18.04’ --with-bugurl=file:///usr/share/doc/gcc-7/README.Bugs --enable-languages=c,ada,c++,go,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-7 --program-prefix=aarch64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --with-sysroot=/ --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-libquadmath --disable-libquadmath-support --enable-plugin --enable-default-pie --with-system-zlib --enable-multiarch --enable-fix-cortex-a53-843419 --disable-werror --enable-checking=release --build=aarch64-linux-gnu --host=aarch64-linux-gnu --target=aarch64-linux-gnu<br>
Thread model: posix<br>
gcc version 7.3.0 (Ubuntu/Linaro 7.3.0-27ubuntu1~18.04)</p>
</blockquote>

---

## Post #4 by @adamrankin (2019-04-11 16:56 UTC)

<p><strong>Problem</strong>: CTK fails to build<br>
Issue:</p>
<ul>
<li>QtOpenGLTimeMonitor is not available under GL ES2 (at least in 5.10.0)</li>
</ul>

---

## Post #5 by @adamrankin (2019-04-16 13:40 UTC)

<p>PythonQt version under Slicer does not support OpenGL ES build.</p>
<p><em>Solution</em>:<br>
Workaround by manually removing non-OpenGL ES classes. Future fix upgrade PythonQt version.</p>

---

## Post #6 by @chir.set (2019-04-16 14:43 UTC)

<p>Once I built Slicer on arm32. Please see <a href="https://discourse.slicer.org/t/how-to-build-3d-slicer-for-raspberry/2843/4">here</a>. I 'm surprised it 's so hard for arm64. Unfortunately, I don 't have any arm64 machine and can 't join in this effort. Good luck.</p>

---

## Post #7 by @adamrankin (2019-04-16 21:17 UTC)

<p>With OpenGL (ES) hardware acceleration?</p>

---

## Post #8 by @chir.set (2019-04-17 07:02 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="7" data-topic="6459" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>With OpenGL (ES) hardware acceleration</p>
</blockquote>
</aside>
<p>I doubt it, didn 't even pay attention to that. The build was not usable in practice, VTK GPU rendering did not work, even the slices were not shown in the views. I 'll try a new build paying attention to OpenGL ES some weekend.</p>

---

## Post #9 by @adamrankin (2019-04-17 13:27 UTC)

<p>Yeah, that’s the kicker. I’m looking to produce a usable Slicer, hopefully.</p>

---

## Post #10 by @adamrankin (2019-04-17 20:28 UTC)

<p>For VTK, enable VTK_USE_SYSTEM_PNG, otherwise VTK builds libpng with NEON enabled.</p>

---

## Post #11 by @adamrankin (2019-04-18 14:12 UTC)

<p><strong>Problem</strong>: libarchive fails to build<br>
<em>Solution</em>: Add <code>#include &lt;sys/sysmacros.h&gt;</code> to <code>&lt;SlicerBuild&gt;/LibArchive/libarchive/archive_pack_dev.c</code></p>

---

## Post #12 by @adamrankin (2019-04-18 14:12 UTC)

<p><strong>Problem</strong>: zlib relocation errors<br>
<em>Solution</em>: where present, use system zlib (via <code>CMAKE_USE_SYSTEM_ZLIB</code>, <code>USE_BUILTIN_ZLIB</code>, <code>Slicer_USE_SYSTEM_zlib</code> depending on project)</p>

---

## Post #13 by @adamrankin (2019-04-18 15:47 UTC)

<p><strong>Problem</strong>: python-setuptools fails</p>
<pre><code class="lang-auto">/opt/dev/S4R/python-install/bin/PythonSlicer: 5: /opt/dev/S4R/python-install/bin/PythonSlicer: Syntax error: Unterminated quoted string

CMake Error at /opt/dev/S4/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  python-setuptools: bootstrap step failed with exit code '2'.
</code></pre>
<p><em>Solution</em>: Just another effect of CTKAppLauncher being the wrong architecture. See solution for <code>CTKAPPLAUNCHER is a download of amd64</code></p>

---

## Post #14 by @adamrankin (2019-04-19 22:18 UTC)

<p><strong>Problem</strong> : CTK fails to build<br>
Issue:<br>
PythonQt version under Slicer does not support OpenGL ES build.</p>
<ul>
<li>QtOpenGLTimeMonitor is not available under GL ES2 (at least in 5.10.0)</li>
</ul>
<p><em>Solution</em> :<br>
In <code>CTK/CMakeExternals/PythonQt.cmake:34</code>, remove <code>gui</code> from the list of wrapped modules</p>
<p><em>Hint</em>:<br>
Set <code>OpenGL_GL_PREFERENCE:STRING="GLVND"</code> in PythonQt project</p>
<p><em>Notes</em>:<br>
My setup did not have Qt Designer built, so I disabled designer plugins in CTK.</p>

---

## Post #15 by @adamrankin (2019-04-19 23:30 UTC)

<p><strong>Problem</strong><br>
SimpleITK compilation crashes (NanoPC-T4, 4GB ram, gcc 7.3)</p>
<p><em>Solution</em>:<br>
Disable SimpleITK<br>
Possibly cross-compile if it’s a memory issue?</p>

---

## Post #16 by @adamrankin (2019-04-20 02:36 UTC)

<p>Disable all designer plugins for Slicer if designer is not available. <code>-DSlicer_BUILD_QT_DESIGNER_PLUGINS:BOOL=OFF</code></p>

---

## Post #17 by @adamrankin (2019-04-20 02:44 UTC)

<p>Slicer wants <code>vtkGUISupportQtOpenGL</code>, see if workaround <code>vtkGUISupportQt</code> is enough</p>

---

## Post #18 by @chir.set (2019-04-20 14:29 UTC)

<p>Just for information</p>
<p>I rebuilt Slicer on Odroid XU4 with a 32-bit ARM CPU. A clean build succeeded with this cmake config line :</p>
<blockquote>
<p>#! Setting -DADDITIONAL_CXX_FLAGS -DCMAKE_C_FLAGS -DCMAKE_CXX_FLAGS is not sufficient.<br>
#! export is required for python to build here<br>
export CFLAGS=-I/usr/include/tirpc<br>
export CXXFLAGS=-I/usr/include/tirpc; cmake -DSlicer_VTK_VERSION_MAJOR:INT=8 -DQt5_DIR:PATH=/usr/lib/cmake/Qt5 -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=0 -DBUILD_TESTING:BOOL=0 -DCMAKE_BUILD_TYPE:STRING=Release -DSlicer_USE_SimpleITK:BOOL=0 …/Slicer</p>
</blockquote>
<p>With a quick test, only one functionality is missing : viewing slices in 2D slice views ! With or without mali drivers. Volume rendering, segmention models show up. Slice data is visible in the 3D view, in the zoom preview (bottom left) but not in the RYG views. Would it really be an OpenGL ES problem ? I won’t insist of course, was just an experiment.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de738f6dc9870f318d5b744ff831500ceb5efb5c.png" data-download-href="/uploads/short-url/vJTAhpn7Bc0tbPA9W9J2SiMTRNy.png?dl=1" title="slicer_odroid_xu4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de738f6dc9870f318d5b744ff831500ceb5efb5c_2_690x382.png" alt="slicer_odroid_xu4" data-base62-sha1="vJTAhpn7Bc0tbPA9W9J2SiMTRNy" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de738f6dc9870f318d5b744ff831500ceb5efb5c_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de738f6dc9870f318d5b744ff831500ceb5efb5c_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de738f6dc9870f318d5b744ff831500ceb5efb5c.png 2x" data-dominant-color="787878"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_odroid_xu4</span><span class="informations">1332×739 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @adamrankin (2019-04-20 14:49 UTC)

<p>Does that machine/setup have OpenGL drivers for the Mali? If so, that simplifies things tremendously. Otherwise your setup is doing Mesa (software) rendering.</p>

---

## Post #20 by @adamrankin (2019-04-20 15:11 UTC)

<p>Looks like no, OpenGL ES 3.1. Would you check your VTK build to see if <code>VTK_USE_OPENGL_ES</code> is <code>ON</code>?</p>

---

## Post #21 by @chir.set (2019-04-20 15:16 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="19" data-topic="6459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>OpenGL drivers for the Mali</p>
</blockquote>
</aside>
<p>This Arch Linux for ARM (gcc 8.2) setup provides the following mali drivers :</p>
<blockquote>
<p>libEGL.so.1.4, libGLESv1_CM.so.1.1, libGLESv2.so.2.0, libOpenCL.so.1.1, libmali.so</p>
</blockquote>
<p>They are installed, nevertheless, the 2D views remain black. Didn’t find any OpenGL ES 3.x driver.</p>
<p>I tried to specify VTK_OPENGL_HAS_EGL, but VTK-build/CMakeCache.txt reported :</p>
<blockquote>
<p>//The OpenGL library being used supports EGL<br>
VTK_OPENGL_HAS_EGL:BOOL=OFF</p>
</blockquote>
<p>So I just removed that flag during configure.</p>
<p>Perhaps this system is missing some library during build or at runtime.</p>

---

## Post #22 by @adamrankin (2019-04-20 23:03 UTC)

<p>Compiled! Trying to run, and the install for libs is <code>&lt;prefix&gt;/lib/Slicer-4.11/libXYZ.so</code>. If I configure <code>&lt;prefix&gt;/lib</code> (I have other programs installed in that prefix) under <code>/etc/ld.so.conf.d/myconf.conf</code>, it doesn’t seem to pickup subdirectories. Do I have to add Slicer-4.11 as a folder in my ld config?</p>

---

## Post #23 by @adamrankin (2019-04-20 23:33 UTC)

<p>And CTK libs are not installed… <a class="mention" href="/u/jcfr">@jcfr</a> to install Slicer from build tree is it simply <code>make install</code> from <code>&lt;SlicerSuperBuild&gt;\Slicer-build</code> ?</p>

---

## Post #24 by @lassoan (2019-04-20 23:46 UTC)

<p>Do not install. Slicer can be launched from the build tree or you can create a self-contained package by building the PACKAGE target.</p>

---

## Post #25 by @adamrankin (2019-04-22 16:02 UTC)

<p>Somehow I broke my GPU driver installation. Trying to sort that out, but then I think it will work!</p>

---

## Post #26 by @adamrankin (2019-04-22 17:55 UTC)

<p>Driver installation was not the problem. I don’t understand the linux graphics cluster&amp;#!^%.</p>
<p>I am down to<br>
<code>QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled</code></p>

---

## Post #27 by @chir.set (2019-04-22 18:11 UTC)

<p>Does Slicer start at least ? Can you load a volume ? See the slices ? Do a quick volume rendering ? A segmentation ? Not that I’ll be able to help, just to know your actual results.</p>

---

## Post #28 by @adamrankin (2019-04-22 18:17 UTC)

<p>No, Slicer doesn’t even start. abnormal exit (may make a Debug build to get more information).</p>

---

## Post #29 by @adamrankin (2019-04-22 18:34 UTC)

<p>I am investigating my VTK build. <code>OPENGL_gl_PREFERENCE</code> was set to <code>LEGACY</code>. Switching to <code>GLVND</code> now (no idea what this does, but hey!).</p>
<p>Also, updated VTK include and libs to use vendor provided EGL/GLES libraries (libmali.so symlinked)</p>

---

## Post #30 by @jcfr (2019-04-22 18:47 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="29" data-topic="6459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>my VTK build. <code>OPENGL_gl_PREFERENCE</code> was set to <code>LEGACY</code> . Switching to <code>GLVND</code> now (no idea what this does, but hey!).</p>
</blockquote>
</aside>
<p>Reading the message associated with this commit should help understand: <a href="https://github.com/Slicer/Slicer/commit/245097a63c7e24eed5db95fa89b15c227b6f6ccb">https://github.com/Slicer/Slicer/commit/245097a63c7e24eed5db95fa89b15c227b6f6ccb</a></p>
<p>Also copied below for convenience:</p>
<pre><code class="lang-plaintext"> BUG: Fix linux package removing dependency to GLVND libraries

By setting OpenGL_GL_PREFERENCE to LEGACY, this commit ensures that
the applications and libraries are linked against libGL.so (legacy) instead
of libOpenGL.so and libGLX.so (GL Vendor Neutral Dispatch library). It allows
to run the application on system where only libGL is available.

It fixes a regression introduced in r27988 (COMP: Update CMake minimum required
version from 3.5 to 3.13) after which one CMP0072 was set to NEW and led to
have the GLVND libraries being used by default.

Detailed explanation about GLVND (thanks @chuckatkins):
libOpenGL.so and libGLX.so are actually just the stub GLVND interface
libraries with no implementation behind them. GLVND uses a config file
to locate and dlopen the implementation at runtime like a plugin
(/usr/lib64/libGLX_nvidia.so.418.39 for instance).
So it's not really suitable for redistribution unless an implementation
like a glvnd-enabled mesa and associated config files are also packaged.
For broad redistributability, it is preferable to use use the legacy libGL
for now so at runtime it will be available on most systems.
That will likely need to be the case for the next few years until
the non-glvnd implementations are much less common.

Co-authored-by: Chuck Atkins &lt;chuck.atkins@kitware.com&gt;
</code></pre>

---

## Post #31 by @adamrankin (2019-04-23 01:55 UTC)

<p>Removing any mention of <code>libGL.so</code> in VTK cmake. gl2ps (and related projects) have to be removed by editing their <code>CMakeLists.txt</code> or <code>module.cmake</code>. Currently VTK checks for <code>if(ANDROID or IOS)</code> which isn’t correct.</p>
<p>Remaining undefined references</p>
<pre><code class="lang-nohighlight">/opt/dev/S4R/VTK-build/lib/libvtkOpenGL-8.2.so.1: undefined reference to `glGetTexImage'
/opt/dev/S4R/VTK-build/lib/libvtkOpenGL-8.2.so.1: undefined reference to `glTexImage1D'
/opt/dev/S4R/VTK-build/lib/libvtkOpenGL-8.2.so.1: undefined reference to `glGetDoublev'
/opt/dev/S4R/VTK-build/lib/libvtkOpenGL-8.2.so.1: undefined reference to `glClearDepth'
/opt/dev/S4R/VTK-build/lib/libvtkOpenGL-8.2.so.1: undefined reference to `glDrawBuffer'
</code></pre>

---

## Post #32 by @adamrankin (2019-04-23 03:37 UTC)

<p>Disabling <code>BUILD_TESTING</code> in Slicer removes more undefined references.</p>

---

## Post #33 by @adamrankin (2019-04-23 15:02 UTC)

<p>To expand, you can simplify this by changing<br>
<code>&lt;Slicer-build&gt;VTK\CMake\vtkOpenGL.cmake:134</code></p>
<p>from</p>
<p><code>find_library(OPENGL_gl_LIBRARY NAMES GLESv3)</code><br>
to<br>
<code>find_library(OPENGL_gl_LIBRARY NAMES GLESv3 GLESv2)</code><br>
(GLESv3 is an android specific library name, libGLESv2 on linux actually contains v3 functions)</p>
<p>To disable gl2ps:<br>
<code>&lt;Slicer-build&gt;\VTK\ThirdParty\gl2ps\module.cmake</code><br>
<code>&lt;Slicer-build&gt;\VTK\Rendering\GL2PSOpenGL2\module.cmake</code><br>
<code>&lt;Slicer-build&gt;\VTK\IO\ExportOpenGL2\module.cmake</code><br>
have them return immediately, up to you if you change the if condition or just remove the if condition.</p>
<p><code>&lt;Slicer-build&gt;VTK\IO\Export\module.cmake</code><br>
change/remove the if condition so that the depends variable is left blank (equivalent to ANDROID or APPLE_IOS condition met)<br>
<code>&lt;Slicer-build&gt;VTK\IO\Export\CMakeLists.txt</code><br>
comment out or remove vtkGL2PSExporter.cxx</p>

---

## Post #34 by @adamrankin (2019-04-23 16:01 UTC)

<p>Docker image (I think):<br>
<a href="https://cloud.docker.com/u/adamrankin/repository/docker/adamrankin/slicer4arm" class="onebox" target="_blank" rel="nofollow noopener">https://cloud.docker.com/u/adamrankin/repository/docker/adamrankin/slicer4arm</a></p>
<p>Edit: wait for next tag, many dependencies I mounted to local drives. Moving into container now.</p>

---

## Post #35 by @chir.set (2019-04-23 17:44 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="26" data-topic="6459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled</p>
</blockquote>
</aside>
<p>After reading the above, I installed qt5-xcb-private-headers and xcb-util-cursor, then rebuilt everything. Now the slices are displayed in the 2D views.</p>
<p>Nice hint, thanks.</p>

---

## Post #36 by @adamrankin (2019-04-27 22:44 UTC)

<p>Ok, so trying to build VTK with GLES doesn’t seem to work. I have no idea how they do it for Android.</p>
<p>vtkRenderingContextOpenGL2 relies on OpenGL defines and functions. <a class="mention" href="/u/jcfr">@jcfr</a> do you think anyone at Kitware would have any use for this use-case (single-board computers with GPU acceleration)?</p>

---

## Post #37 by @adamrankin (2019-04-28 20:41 UTC)

<p>Did some workarounds by substituting closest GLES equivalent (GL_LINE vs GL_LINES, etc…) and commenting out some gl points logic/functions.</p>

---

## Post #38 by @adamrankin (2019-04-29 00:54 UTC)

<p>In <code>&lt;Slicer&gt;/Libs/vtkAddon/CMakeLists.txt</code><br>
remove section that includes OpenGL classes</p>
<p>In Slicer CMake, disable tests <code>BUILD_TESTING:BOOL=OFF</code></p>
<p>In VTK, defined OPENGL_ES_VERSION:STRING=3.0 (maybe 3.2 would work? my system has headers for 3.2)</p>

---

## Post #39 by @adamrankin (2019-04-29 02:54 UTC)

<p>in <code>&lt;Slicer&gt;/Libs/MRML/Widgets/qMRMLPlotView.cxx::saveAsSVG</code> comment out contents of function</p>

---

## Post #40 by @adamrankin (2019-04-30 15:42 UTC)

<p>Developer provided docker image</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/friendlyarm/friendlyelec-ubuntu18-docker">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/friendlyarm/friendlyelec-ubuntu18-docker" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://opengraph.githubassets.com/ffcecbe6d43ec7136178b2f47b28808d3c76be36e8388f94fd85ff385d5eab13/friendlyarm/friendlyelec-ubuntu18-docker" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://github.com/friendlyarm/friendlyelec-ubuntu18-docker" target="_blank" rel="noopener nofollow ugc">GitHub - friendlyarm/friendlyelec-ubuntu18-docker: This docker image is used...</a></h3>

  <p>This docker image is used to cross-compile Qt application for FriendlyELEC RK3399 platform. - GitHub - friendlyarm/friendlyelec-ubuntu18-docker: This docker image is used to cross-compile Qt applic...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #41 by @Jonatron (2021-06-13 15:54 UTC)

<p>Adam,<br>
I Thank you for the word you have been doing, I have been looking for someone compiling something like this for a while. I got the Galaxy Book S as soon as it dropped thinking that I was gonna step into the future and have a bad-ass 8 core processor computer. Little did I know about software limitations…  Anyways bro man, could you please allow me to get a copy of your software. Pretty please. Id even cash app you or bit coin you some funds !! Please let me know <a href="mailto:confidentconstruction@live.com">confidentconstruction@live.com</a></p>

---

## Post #42 by @adamrankin (2021-06-13 19:34 UTC)

<p>Hey Jonatron,</p>
<p>Unfortunately there is no 64 bit ARM build for Slicer with hardware GPU acceleration.</p>
<p>Adam</p>

---

## Post #43 by @lassoan (2021-06-17 01:26 UTC)

<p>If you want to run Slicer on a tablet then the simplest and cheapest solution is to get a Windows tablet. Slicer works nicely on a Microsoft Surface Pro.</p>

---

## Post #44 by @klchtsk (2024-10-05 10:57 UTC)

<p>Dear Adam,<br>
Recently I put my hands on a NVIDIA Jetson Orin Nano with an arm64 chip in it. Do I understand it wight, even if I successfully build a Slicer on arm64, it won’t still support the GPU acceleration?<br>
Thanks!<br>
Bohdan</p>

---

## Post #45 by @adamrankin (2024-10-05 11:10 UTC)

<p>Someone with more knowledge of OpenGLES and the mobile graphics stack will probably be able to get it working. If I remember correctly the key problem was that OpenGLES assumes a single context to render in, whereas Slicer uses many.</p>
<p>Eventually I gave up</p>

---

## Post #46 by @chir.set (2024-10-05 14:48 UTC)

<aside class="quote no-group" data-username="klchtsk" data-post="44" data-topic="6459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klchtsk/48/77849_2.png" class="avatar"> klchtsk:</div>
<blockquote>
<p>it won’t still support the GPU acceleration</p>
</blockquote>
</aside>
<p>I don’t know if this answers your question, but here is a <a href="https://disk.yandex.com/i/nz8uSwEK3AuAzA" rel="noopener nofollow ugc">video</a> of an aarch64 build of Slicer.</p>
<p>It is not running on bare metal, rather in Arch, itself in a chroot environment on my phone. There’s an additional delay in every display update because of X11 forwarding over WiFi, and because my laptop’s screen’s resolution is rather high at 2560x1440.</p>
<p>The phone’s CPU is Qualcomm® Snapdragon™ 778G:<br>
CPU: Qualcomm® Kryo™ 670, octa-core CPU, up to 2.4GHz<br>
GPU: Qualcomm® Adreno™ 642L GPU</p>
<p>As I see, volume rendering seems to work, not as fluid as on x86_64, it is expected.</p>
<p>I don’t have all the details of the build in mind, but may find some in the build tree.</p>

---

## Post #47 by @klchtsk (2024-10-05 22:10 UTC)

<p>Thank you for your answer!</p>
<p>In the meantime I have made some progress in <code>cmake</code>-ing a Slicer build on NVIDIA Jetson Orin.</p>
<p>Unfortunately it’s stuck on:</p>
<pre><code class="lang-auto">...
[ 40%] Performing build step for 'teem'
Consolidate compiler generated dependencies of target teem
[  0%] Linking C shared library bin/libteem.so
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__length_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): in function `slicer_zlib__tr_tally':
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1040:(.text+0x3414): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1041:(.text+0x3470): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1041:(.text+0x3494): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__length_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): in function `compress_block':
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1091:(.text+0x3728): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1099:(.text+0x3ac4): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1099:(.text+0x3ae4): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(zutil.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib_z_errmsg' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(zutil.c.o): in function `slicer_zlib_zError':
/home/bohdan/Slicer-SuperBuild/zlib/zutil.c:136:(.text+0x74): dangerous relocation: unsupported relocation
collect2: error: ld returned 1 exit status
make[5]: *** [CMakeFiles/teem.dir/build.make:5346: bin/libteem.so.1.12.0] Error 1
make[4]: *** [CMakeFiles/Makefile2:118: CMakeFiles/teem.dir/all] Error 2
make[3]: *** [Makefile:136: all] Error 2
make[2]: *** [CMakeFiles/teem.dir/build.make:90: teem-prefix/src/teem-stamp/teem-build] Error 2
make[1]: *** [CMakeFiles/Makefile2:299: CMakeFiles/teem.dir/all] Error 2
make: *** [Makefile:101: all] Error 2
</code></pre>
<p>VTK didn’t want to be complied either with the same mistake, but under <code>sudo make</code> VTK compilation ran successfully without any change in <code>cmake</code>.</p>
<p>However it doesn’t want to suppress the building of <code>teem</code> so that I can proceed. Any ideas?</p>
<p>Thank you!</p>

---

## Post #48 by @klchtsk (2024-10-06 00:44 UTC)

<p>UPDATE:</p>
<p><code>teem</code> built, after specifying <code>Teem_DIR</code> in <code>cmake</code>.</p>
<p>Process stuck on <code>LibArchive</code>.</p>
<pre><code class="lang-auto">[ 55%] Generate version-LibArchive.txt and license-LibArchive.txt
[ 56%] Performing update step for 'LibArchive'
[ 56%] No patch step for 'LibArchive'
[ 57%] Performing configure step for 'LibArchive'
loading initial cache file /home/bohdan/Slicer-SuperBuild/LibArchive-prefix/tmp/LibArchive-cache-Debug.cmake
-- Configuring done
-- Generating done
-- Build files have been written to: /home/bohdan/Slicer-SuperBuild/LibArchive-build
[ 57%] Performing build step for 'LibArchive'
Consolidate compiler generated dependencies of target archive
[  1%] Linking C shared library libarchive.so
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__length_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): in function `slicer_zlib__tr_tally':
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1040:(.text+0x3414): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1041:(.text+0x3470): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1041:(.text+0x3494): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__length_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): in function `compress_block':
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1091:(.text+0x3728): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1099:(.text+0x3ac4): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(trees.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib__dist_code' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib/trees.c:1099:(.text+0x3ae4): dangerous relocation: unsupported relocation
/usr/bin/ld: /home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(zutil.c.o): relocation R_AARCH64_ADR_PREL_PG_HI21 against symbol `slicer_zlib_z_errmsg' which may bind externally can not be used when making a shared object; recompile with -fPIC
/home/bohdan/Slicer-SuperBuild/zlib-install/lib/libzlib.a(zutil.c.o): in function `slicer_zlib_zError':
/home/bohdan/Slicer-SuperBuild/zlib/zutil.c:136:(.text+0x74): dangerous relocation: unsupported relocation
collect2: error: ld returned 1 exit status
make[5]: *** [libarchive/CMakeFiles/archive.dir/build.make:2018: libarchive/libarchive.so.19] Error 1
make[4]: *** [CMakeFiles/Makefile2:216: libarchive/CMakeFiles/archive.dir/all] Error 2
make[3]: *** [Makefile:136: all] Error 2
make[2]: *** [CMakeFiles/LibArchive.dir/build.make:90: LibArchive-prefix/src/LibArchive-stamp/LibArchive-build] Error 2
make[1]: *** [CMakeFiles/Makefile2:409: CMakeFiles/LibArchive.dir/all] Error 2
make: *** [Makefile:101: all] Error 2
</code></pre>

---

## Post #49 by @chir.set (2024-10-06 08:12 UTC)

<aside class="quote no-group" data-username="klchtsk" data-post="48" data-topic="6459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klchtsk/48/77849_2.png" class="avatar"> klchtsk:</div>
<blockquote>
<p><code>recompile with -fPIC</code></p>
</blockquote>
</aside>
<p>This patch was helpful:</p>
<pre><code class="lang-auto">diff --git a/SuperBuild/External_zlib.cmake b/SuperBuild/External_zlib.cmake
index 5257ac65f2..13b6afeb84 100644
--- a/SuperBuild/External_zlib.cmake
+++ b/SuperBuild/External_zlib.cmake
@@ -36,7 +36,7 @@ if(NOT DEFINED ZLIB_ROOT AND NOT Slicer_USE_SYSTEM_${proj})
     "66a753054b356da85e1838a081aa94287226823e"
     QUIET
     )
-
+  set(cflags "${ep_common_c_flags} -fPIC")
   ExternalProject_Add(${proj}
     ${${proj}_EP_ARGS}
     GIT_REPOSITORY "${Slicer_${proj}_GIT_REPOSITORY}"
@@ -48,7 +48,7 @@ if(NOT DEFINED ZLIB_ROOT AND NOT Slicer_USE_SYSTEM_${proj})
       ## CXX should not be needed, but it a cmake default test
       -DCMAKE_CXX_COMPILER:FILEPATH=${CMAKE_CXX_COMPILER}
       -DCMAKE_C_COMPILER:FILEPATH=${CMAKE_C_COMPILER}
-      -DCMAKE_C_FLAGS:STRING=${ep_common_c_flags}
+      -DCMAKE_C_FLAGS:STRING=${cflags}
       -DZLIB_MANGLE_PREFIX:STRING=slicer_zlib_
       -DCMAKE_INSTALL_PREFIX:PATH=&lt;INSTALL_DIR&gt;
     DEPENDS
</code></pre>

---

## Post #50 by @klchtsk (2024-10-06 11:04 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="49" data-topic="6459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p><code>-fPIC</code></p>
</blockquote>
</aside>
<p>Wonderful!</p>
<p>I just have added <code>-fPIC</code> in <code>CMAKE_C_FLAGS</code> and <code>ADDITIONAL_C_FLAGS</code> (I have used gui).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3ef25f0a3a97e86f359d5346bf5172037744329.png" data-download-href="/uploads/short-url/pFLQ4t8uk4xH3KdvKuVDxn68SlX.png?dl=1" title="Screenshot 2024-10-06 at 12.59.11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3ef25f0a3a97e86f359d5346bf5172037744329_2_690x55.png" alt="Screenshot 2024-10-06 at 12.59.11" data-base62-sha1="pFLQ4t8uk4xH3KdvKuVDxn68SlX" width="690" height="55" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3ef25f0a3a97e86f359d5346bf5172037744329_2_690x55.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3ef25f0a3a97e86f359d5346bf5172037744329_2_1035x82.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3ef25f0a3a97e86f359d5346bf5172037744329_2_1380x110.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-06 at 12.59.11</span><span class="informations">1544×124 36.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and after <code>sudo make --debug LibArchive</code> it has successfully remade it:</p>
<pre><code class="lang-auto">[100%] Built target LibArchive
Successfully remade target file 'CMakeFiles/LibArchive.dir/all'.
Successfully remade target file 'CMakeFiles/LibArchive.dir/rule'.
Must remake target 'LibArchive'.
Successfully remade target file 'LibArchive'.
Successfully remade target file 'LibArchive'.
</code></pre>
<p>Now I’m running the whole <code>make</code>.</p>

---

## Post #51 by @klchtsk (2024-10-07 20:00 UTC)

<p>Okay,</p>
<p>I have made some progress. It has successfully built all necessary components, but while making <code>Slicer</code> it ended up in following error.</p>
<pre><code class="lang-auto">[ 41%] Building CXX object Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerSettingsInternationalizationPanel.cxx.o
    Successfully remade target file 'Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerSettingsInternationalizationPanel.cxx.o'.
     File 'Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerWebPythonProxy.cxx.o' does not exist.
    Must remake target 'Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerWebPythonProxy.cxx.o'.
[ 41%] Building CXX object Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerWebPythonProxy.cxx.o
/home/bohdan/Slicer/Base/QTGUI/qSlicerWebPythonProxy.cxx: In member function ‘QString qSlicerWebPythonProxy::evalPython(const QString&amp;, int)’:
/home/bohdan/Slicer/Base/QTGUI/qSlicerWebPythonProxy.cxx:99:3: error: ‘ctkAbstractPythonManager’ has not been declared
   99 |   ctkAbstractPythonManager::ExecuteStringMode executeStringMode{ctkAbstractPythonManager::FileInput};
      |   ^~~~~~~~~~~~~~~~~~~~~~~~
/home/bohdan/Slicer/Base/QTGUI/qSlicerWebPythonProxy.cxx:103:7: error: ‘executeStringMode’ was not declared in this scope
  103 |       executeStringMode = ctkAbstractPythonManager::EvalInput;
      |       ^~~~~~~~~~~~~~~~~
/home/bohdan/Slicer/Base/QTGUI/qSlicerWebPythonProxy.cxx:103:27: error: ‘ctkAbstractPythonManager’ has not been declared
  103 |       executeStringMode = ctkAbstractPythonManager::EvalInput;
      |                           ^~~~~~~~~~~~~~~~~~~~~~~~
/home/bohdan/Slicer/Base/QTGUI/qSlicerWebPythonProxy.cxx:106:27: error: ‘ctkAbstractPythonManager’ has not been declared
  106 |       executeStringMode = ctkAbstractPythonManager::FileInput;
      |                           ^~~~~~~~~~~~~~~~~~~~~~~~
/home/bohdan/Slicer/Base/QTGUI/qSlicerWebPythonProxy.cxx:109:27: error: ‘ctkAbstractPythonManager’ has not been declared
  109 |       executeStringMode = ctkAbstractPythonManager::SingleInput;
      |                           ^~~~~~~~~~~~~~~~~~~~~~~~
make[5]: *** [Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/build.make:1382: Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerWebPythonProxy.cxx.o] Error 1
make[4]: *** [CMakeFiles/Makefile2:6394: Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/all] Error 2
make[3]: *** [Makefile:166: all] Error 2
make[2]: *** [CMakeFiles/Slicer.dir/build.make:90: Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2
make[1]: *** [CMakeFiles/Makefile2:608: CMakeFiles/Slicer.dir/all] Error 2
make: *** [Makefile:101: all] Error 2

</code></pre>
<p>And now I’m officially stuck. The built was without Python.</p>

---

## Post #52 by @pieper (2024-10-07 20:05 UTC)

<p>If you just want to see if you can get a build, I suggest commenting out those lines that don’t compile.  You can add them back later once you know that the application runs.  That build error looks fixable but it’s not in a part of the code you are likely to need.</p>

---

## Post #53 by @klchtsk (2024-10-07 20:13 UTC)

<p>Thank you!</p>
<p>Just have disabled the <code>Slicer_BUILD_WEBENGINE_SUPPORT</code>. Re-running!</p>
<p>Bohdan</p>

---

## Post #54 by @klchtsk (2024-10-08 17:41 UTC)

<p>No luck.</p>
<p>It has successfully finished compiling:</p>
<pre><code class="lang-auto">
... (shortened)
[ 97%] Completed 'Slicer'
 File 'CMakeFiles/Slicer.dir/build' does not exist.
   File 'Slicer' does not exist.
     File 'CMakeFiles/Slicer' does not exist.
    Must remake target 'CMakeFiles/Slicer'.
    Successfully remade target file 'CMakeFiles/Slicer'.
  Must remake target 'Slicer'.
  Successfully remade target file 'Slicer'.
Must remake target 'CMakeFiles/Slicer.dir/build'.
Successfully remade target file 'CMakeFiles/Slicer.dir/build'.
[100%] Built target Slicer
 File 'all' does not exist.
Must remake target 'all'.
Successfully remade target file 'all'.
  Successfully remade target file 'all'.
Must remake target 'default_target'.
Successfully remade target file 'default_target'.
bohdan@bohdan-desktop:~/Slicer-SuperBuild$ cd Slicer-build/
bohdan@bohdan-desktop:~/Slicer-SuperBuild/Slicer-build$ ./Slicer
-bash: ./Slicer: cannot execute binary file: Exec format error
bohdan@bohdan-desktop:~/Slicer-SuperBuild/Slicer-build$ sudo ctest -j6
Test project /home/bohdan/Slicer-SuperBuild/Slicer-build

... (shortened)

        Start 472: FiducialRegistrationTest
430/481 Test #472: FiducialRegistrationTest ....................................***Failed    0.04 sec

# only few errors have a comment of missing regex:

        Start 478: slicer_nomainwindow_DisableModulesCommandLineOptionsTest
436/481 Test #478: slicer_nomainwindow_DisableModulesCommandLineOptionsTest ....***Failed  Required regular expression not found. Regex=[Number of loaded modules: 1
]  0.05 sec


... (shortened)

2% tests passed, 473 tests failed out of 481

Label Time Summary:
AddScalarVolumes                       =   0.43 sec*proc (11 tests)
CMake                                  =   0.26 sec*proc (7 tests)
CastScalarVolume                       =   0.31 sec*proc (8 tests)
CheckerBoardFilter                     =   0.04 sec*proc (1 test)
CreateDICOMSeries                      =   0.04 sec*proc (1 test)
DiffusionTensorTest                    =   0.04 sec*proc (1 test)
ExecutionModelTour                     =   0.04 sec*proc (1 test)
ExtractSkeleton                        =   0.04 sec*proc (1 test)
FiducialRegistration                   =   0.04 sec*proc (1 test)
GaussianBlurImageFilter                =   0.04 sec*proc (1 test)
GradientAnisotropicDiffusion           =   0.08 sec*proc (2 tests)
GrayscaleFillHoleImageFilter           =   0.04 sec*proc (1 test)
GrayscaleGrindPeakImageFilter          =   0.04 sec*proc (1 test)
GrayscaleModelMaker                    =   0.04 sec*proc (1 test)
HistogramMatching                      =   0.04 sec*proc (1 test)
ImageLabelCombine                      =   0.04 sec*proc (1 test)
LabelMapSmoothing                      =   0.04 sec*proc (1 test)
MRMLCore                               =   4.58 sec*proc (121 tests)
MRMLDisplayableManager                 =   0.26 sec*proc (8 tests)
MRMLLogic                              =   0.46 sec*proc (13 tests)
MaskScalarVolume                       =   0.04 sec*proc (1 test)
MedianImageFilter                      =   0.08 sec*proc (2 tests)
MergeModels                            =   0.12 sec*proc (3 tests)
ModelMaker                             =   0.28 sec*proc (7 tests)
ModelToLabelMap                        =   0.08 sec*proc (2 tests)
MultiplyScalarVolumes                  =   0.04 sec*proc (1 test)
N4ITKBiasFieldCorrection               =   0.04 sec*proc (1 test)
OrientScalarVolume                     =   0.12 sec*proc (3 tests)
PETStandardUptakeValueComputation      =   0.04 sec*proc (1 test)
ResampleDTIVolume                      =   0.26 sec*proc (7 tests)
ResampleScalarVectorDWIVolume          =   0.26 sec*proc (6 tests)
ResampleScalarVolume                   =   0.04 sec*proc (1 test)
RobustStatisticsSegmenter              =   0.05 sec*proc (1 test)
SimpleRegionGrowingSegmentation        =   0.04 sec*proc (1 test)
SlicerBaseLogic                        =   0.13 sec*proc (3 tests)
SubtractScalarVolumes                  =   0.04 sec*proc (1 test)
TestGridTransformRegistration          =   0.04 sec*proc (1 test)
ThresholdScalarVolume                  =   0.04 sec*proc (1 test)
VotingBinaryHoleFillingImageFilter     =   0.04 sec*proc (1 test)
qMRMLWidgets                           =   2.74 sec*proc (93 tests)
qSlicerAnnotationsModule               =   0.09 sec*proc (2 tests)
qSlicerApp                             =   0.09 sec*proc (2 tests)
qSlicerBaseQTApp                       =   0.08 sec*proc (2 tests)
qSlicerBaseQTCLI                       =   0.11 sec*proc (3 tests)
qSlicerBaseQTCore                      =   0.26 sec*proc (6 tests)
qSlicerBaseQTGUI                       =   0.39 sec*proc (11 tests)
qSlicerCamerasModule                   =   0.18 sec*proc (4 tests)
qSlicerColorsModule                    =   0.13 sec*proc (3 tests)
qSlicerCropVolumeModule                =   0.12 sec*proc (3 tests)
qSlicerDataModule                      =   0.13 sec*proc (3 tests)
qSlicerMarkupsModule                   =   0.87 sec*proc (20 tests)
qSlicerModelsModule                    =   0.25 sec*proc (6 tests)
qSlicerModelsModuleWidgets             =   0.09 sec*proc (2 tests)
qSlicerModulesCore                     =   0.16 sec*proc (5 tests)
qSlicerPlotsModule                     =   0.08 sec*proc (2 tests)
qSlicerPlotsModuleWidgets              =   0.05 sec*proc (1 test)
qSlicerReformatModule                  =   0.09 sec*proc (2 tests)
qSlicerSceneViewsModule                =   0.14 sec*proc (3 tests)
qSlicerSegmentationsModule             =   0.09 sec*proc (2 tests)
qSlicerSequencesModule                 =   0.27 sec*proc (6 tests)
qSlicerSequencesModuleWidgets          =   0.08 sec*proc (2 tests)
qSlicerSubjectHierarchyModule          =   0.14 sec*proc (3 tests)
qSlicerTablesModule                    =   0.13 sec*proc (3 tests)
qSlicerTablesModuleWidgets             =   0.04 sec*proc (1 test)
qSlicerTerminologiesModule             =   0.09 sec*proc (2 tests)
qSlicerTextsModule                     =   0.08 sec*proc (2 tests)
qSlicerTransformsModule                =   0.12 sec*proc (3 tests)
qSlicerTransformsModuleWidgets         =   0.09 sec*proc (2 tests)
qSlicerUnitsModule                     =   0.14 sec*proc (3 tests)
qSlicerViewControllersModule           =   0.09 sec*proc (2 tests)
qSlicerVolumeRenderingModule           =   0.51 sec*proc (11 tests)
qSlicerVolumesModule                   =   0.28 sec*proc (6 tests)
qSlicerVolumesModuleWidgets            =   0.14 sec*proc (3 tests)
qSlicerWelcomeModule                   =   0.09 sec*proc (2 tests)
vtkAddon                               =   0.22 sec*proc (5 tests)
vtkSegmentationCore                    =   0.20 sec*proc (5 tests)
vtkSlicerColorsModuleLogic             =   0.04 sec*proc (1 test)
vtkSlicerTransformsModuleLogic         =   0.12 sec*proc (3 tests)
vtkSlicerVolumeRenderingModuleLogic    =   0.09 sec*proc (2 tests)
vtkTeem                                =   0.04 sec*proc (1 test)

Total Test time (real) =   3.61 sec

The following tests FAILED:
	  8 - vtkAddonMathUtilitiesTest1 (Failed)
	  9 - vtkAddonSingletonTest1 (Failed)
	... (shortened)
	480 - slicer_nomainwindow_NoApplicationInformationOptionTest (Failed)
	481 - slicer_nomainwindow_ApplicationInformationOptionTest (Failed)
Errors while running CTest
Output from these tests are in: /home/bohdan/Slicer-SuperBuild/Slicer-build/Testing/Temporary/LastTest.log
Use "--rerun-failed --output-on-failure" to re-run the failed cases verbosely.
</code></pre>
<p>Any ideas, why it might compile but don’t run?</p>

---

## Post #55 by @pieper (2024-10-08 17:57 UTC)

<p>Does the application run at all?  Are you able to run it in a debugger?  If it won’t start can you use the launcher to create a shell with all the path settings and then run <code>ldd</code>?  If it tries to start but fails can you use <code>strace</code> to figure out where?</p>
<p>My guess is that if you just work through one representative failing test and get it working many others will also start working.</p>

---

## Post #56 by @klchtsk (2024-10-08 18:01 UTC)

<p>Execution fails.</p>
<pre><code class="lang-auto">bohdan@bohdan-desktop:~/Slicer-SuperBuild/Slicer-build$ ./Slicer
-bash: ./Slicer: cannot execute binary file: Exec format error
</code></pre>
<p>I will try with launcher as well! Thank you!</p>

---

## Post #57 by @adamrankin (2024-10-08 18:10 UTC)

<p>When I last attempted this, the CTK launcher project needs to be modified to work for ARM64</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/Slicer/AppLauncher">
  <header class="source">

      <a href="https://github.com/Slicer/AppLauncher" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/0161e078ec996c1db6a156319b017037/Slicer/AppLauncher" class="thumbnail">

  <h3><a href="https://github.com/Slicer/AppLauncher" target="_blank" rel="noopener nofollow ugc">GitHub - Slicer/AppLauncher: Simple and small program allowing to set the...</a></h3>

    <p><span class="github-repo-description">Simple and small program allowing to set the environment of any executable.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Specifically modify it to download the aarch build</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/AppLauncher/releases">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/AppLauncher/releases" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/7a1b6bb890dda296f09977899cf1596632534a317f4e780dc3cfc6d8b91a7511/Slicer/AppLauncher" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/AppLauncher/releases" target="_blank" rel="noopener nofollow ugc">Releases · Slicer/AppLauncher</a></h3>

  <p>Simple and small program allowing to set the environment of any executable. - Slicer/AppLauncher</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #58 by @chir.set (2024-10-08 18:41 UTC)

<aside class="quote no-group" data-username="klchtsk" data-post="56" data-topic="6459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klchtsk/48/77849_2.png" class="avatar"> klchtsk:</div>
<blockquote>
<p><code>-bash: ./Slicer: cannot execute binary file: Exec format error</code></p>
</blockquote>
</aside>
<p>To me, it spells mismatch between architectures, like a binary for aarch64 executed on x86_64 or the other way round.</p>
<p>It’s already surprising that you got past <em>CTKAPPLAUNCHER</em>. As I understand, the build process downloads an online pre-built binary and there’s none online for aarch64.</p>
<p>As a workaround, I built the launcher for aarch64 in <em>CTKAppLauncherLib-build</em> and copied the result in <em>CTKAPPLAUNCHER</em>. Perhaps <em>External_CTKAPPLAUNCHER.cmake</em> must be modified to point to this launcher, I don’t remember exactly how I completed this step. (Why is it not always compiled locally?)</p>
<p>Are you building on an aarch64 hardware? Virtualising? Cross-compiling using a native compiler like <em>aarch64-linux-gnu-g++</em> (failed for me)? Cross-compiling using a <em>chroot</em> in an aarch64 image (succeeded for me)?</p>

---

## Post #59 by @klchtsk (2024-10-08 19:13 UTC)

<p>I have rebuilt CTKAppLauncher with aarch64.tar.gz release:</p>
<pre><code class="lang-auto">bohdan@bohdan-desktop:~$ CTKAppLauncher --launcher-version
CTKAppLauncher launcher version 0.1.29
</code></pre>
<p>I’m building it all on <a href="https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/" rel="noopener nofollow ugc">NVIDIA Jetson Nano Orin</a>. ARM64 chip with a native aarch64-linux-gnu-g++ compiler.</p>
<p>UPD: I’m recompiling the whole project now.</p>

---

## Post #60 by @cesquerre (2025-09-03 15:21 UTC)

<p>Hi Bohdan,</p>
<p>Did you manage to run it on the Jetson Nano?</p>
<p>I’d like to install it in a Jetson AGX Orin Developer kit.</p>
<p>Regards,</p>
<p>Carlos</p>

---
