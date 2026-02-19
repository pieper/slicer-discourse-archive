---
topic_id: 23443
title: "Build And Package Slicercat On Manylinux"
date: 2022-05-16
url: https://discourse.slicer.org/t/23443
---

# Build and package SlicerCAT on manylinux

**Topic ID**: 23443
**Date**: 2022-05-16
**URL**: https://discourse.slicer.org/t/build-and-package-slicercat-on-manylinux/23443

---

## Post #1 by @keri (2022-05-16 15:01 UTC)

<p>Hi,</p>
<p>How can I build and package SlicerCAT (C++17) so it was available on many linux distributions?<br>
For now all Linux staff I do on Ubuntu 20.04</p>

---

## Post #2 by @lassoan (2022-05-17 00:06 UTC)

<p>I don’t think you need to do anything special, just build Slicer as usual and follow the <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">installation instructions</a>. Maybe <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can give you some more details.</p>

---

## Post #3 by @keri (2022-05-17 00:40 UTC)

<p>You should be right</p>
<p>I just experienced a little problem:<br>
I compiled and packaged SlicerCAT on my Ubuntu 20.04 and tried to run it on clean Debian 11.<br>
While I can run it on clean Ubuntu 20.4 and 22.04 (I use virtual machines) I was unable to run it on Debian 11: linking error something like <code>Unable to link to libjpeg8.so</code></p>
<p>I guess some of my dependencies linked to Ubuntu’s libjpeg8.so but Debian doesn’t have it. It is just my assumption.</p>
<p>Worth to try to compile and package it on clean Debian 11 rather than on Ubuntu.</p>

---

## Post #4 by @keri (2022-05-19 20:27 UTC)

<p>Some succes</p>
<p>The goal is to build SlicerCAT for Linux for many distributions and many releases.</p>
<p>My steps:</p>
<ol>
<li>install CentOS 7</li>
<li>install <a href="https://stackoverflow.com/a/39731134/11747958" rel="noopener nofollow ugc">latest devtoolset 11</a> (more recent GCC instead of the default 4.8.5)</li>
<li>install qt (I prefer Qt installer), cmake, git</li>
<li>to avoid following errors:<br>
<strong>Could NOT find Patch (missing: Patch_EXECUTABLE) (it means GNU PATCH)</strong><br>
<strong>Failed to find “GL/gl.h” in “/usr/include/libdrm”.</strong><br>
<strong>Could NOT find LibUUID (missing: LibUUID_LIBRARY LibUUID_INCLUDE_DIR)</strong><br>
install the following packages (can be found in Slicer doc)<br>
<code>sudo yum install patch mesa-libGL-devel libuuid-devel</code>
</li>
<li>build and pack</li>
</ol>
<p>After packaging I succeded to run on fresh:<br>
<strong>Debian 10.12</strong><br>
<strong>Debian 11.3</strong><br>
<strong>Ubuntu 18.04</strong><br>
<strong>Ubuntu 20.04</strong><br>
<strong>Ubuntu 22.04</strong><br>
<strong>Fedora 34</strong></p>
<p>+install the <code>xinerama</code> <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux" rel="noopener nofollow ugc">following Slicer installation instruction</a><br>
even though <strong>Debian 10.12</strong> also needed <a href="https://forum.qt.io/topic/93247/qt-qpa-plugin-could-not-load-the-qt-platform-plugin-xcb-in-even-though-it-was-found/81#:~:text=Simple%20solution%3A-,sudo%20ln%20%2Ds%20/usr/lib/x86_64%2Dlinux%2Dgnu/libxcb%2Dutil.so%20/usr/lib/x86_64%2Dlinux%2Dgnu/libxcb%2Dutil.so.1,-All%20work%2C%20folks" rel="noopener nofollow ugc">sudo ln -s /usr/lib/x86_64-linux-gnu/libxcb-util.so /usr/lib/x86_64-linux-gnu/libxcb-util.so.1</a> to solve the error:</p>
<pre><code class="lang-auto">Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.
</code></pre>
<p>simply installing <code>sudo apt-get install --reinstall libxcb-xinerama0</code> is not enough in this case.</p>
<p>I also tried to build/package SlicerCAT on Debian 11, Ubuntu 20.04, Fedora 34 but when trying to run the packaged app I discovered that on some platform I was unable to run it.</p>

---

## Post #5 by @lassoan (2022-06-13 14:11 UTC)

<p>Thank you for sharing this. Would you mind submitting a pull request with any necessary changes/additions for the [Slicer installation instructions] (<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#installing-3d-slicer" class="inline-onebox">Getting Started — 3D Slicer documentation</a>)?</p>

---

## Post #6 by @keri (2022-06-14 00:05 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/6427" rel="noopener nofollow ugc">PR is ready</a></p>

---
