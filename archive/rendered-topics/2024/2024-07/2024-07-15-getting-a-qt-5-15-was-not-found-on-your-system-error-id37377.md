# Getting a "Qt 5.15 was not found on your system" error

**Topic ID**: 37377
**Date**: 2024-07-15
**URL**: https://discourse.slicer.org/t/getting-a-qt-5-15-was-not-found-on-your-system-error/37377

---

## Post #1 by @tmondo (2024-07-15 11:34 UTC)

<p>Hello,</p>
<p>I’ve been trying to setup Slicer for local development, but I’m having trouble with Qt when going through the configuration step.</p>
<p>I’m running MacOS, and on the build instructions page(<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html" class="inline-onebox" rel="noopener nofollow ugc">macOS — 3D Slicer documentation</a>) there is a link for the Qt installer.</p>
<p>However, in the installer I wasn’t able to find Qt 5.15, even when enabling the archive filter, so I proceeded to install Qt using hombrew.</p>
<pre><code class="lang-auto">brew install qt@5
</code></pre>
<p>After installation, I tried running the configuration step, like so:</p>
<pre><code class="lang-auto">cmake \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=11.0 \
  -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DQt5_DIR:PATH=/opt/homebrew/opt/qt@5/5.15.13_1/lib/cmake/Qt5 \
  ~/Slicer
</code></pre>
<p>But I only run into this error:</p>
<pre><code class="lang-auto">CMake Error at CMake/SlicerBlockFindQtAndCheckVersion.cmake:30 (message):
  error: Qt 5.15 was not found on your system.You probably need to set the
  Qt5_DIR variable.
Call Stack (most recent call first):
  CMake/SlicerBlockFindQtAndCheckVersion.cmake:67 (__SlicerBlockFindQtAndCheckVersion_find_qt)
  CMakeLists.txt:695 (include)
</code></pre>

---

## Post #2 by @pieper (2024-07-17 15:47 UTC)

<p>I haven’t built from scratch on a mac in a while and probably the Qt5 version is updated, but usually there’s a specially named file that cmake is looking for (I thought it should be listed in the error message).  You can investigate what that file is and make sure the <code>Qt5_DIR</code> variable points to it.  You may need to read the cmake code to make sure</p>

---

## Post #3 by @tmondo (2024-07-18 08:33 UTC)

<p>Thank you for the reply!<br>
I’ll check the cmake files and see if I can figure it out.</p>

---
