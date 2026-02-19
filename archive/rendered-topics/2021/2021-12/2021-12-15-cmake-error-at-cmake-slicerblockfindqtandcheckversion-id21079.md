---
topic_id: 21079
title: "Cmake Error At Cmake Slicerblockfindqtandcheckversion"
date: 2021-12-15
url: https://discourse.slicer.org/t/21079
---

# CMake Error at CMake/SlicerBlockFindQtAndCheckVersion

**Topic ID**: 21079
**Date**: 2021-12-15
**URL**: https://discourse.slicer.org/t/cmake-error-at-cmake-slicerblockfindqtandcheckversion/21079

---

## Post #1 by @Fabiola (2021-12-15 17:10 UTC)

<p>Hello,<br>
I am trying to build Slicer on Ubuntu 20.04 (with NVIDIA GK 107M GeForce GT 750 graphics card). Fighting with an OpenGL cmake error which I can’t win a few days now, can someone help me please with ideas, direction potential solution even if you solved similar issue, please?</p>
<p>Configuring VTK<br>
Slicer_VTK_RENDERING_BACKEND is OpenGL2<br>
Slicer_VTK_SMP_IMPLEMENTATION_TYPE is Sequential<br>
Slicer_VTK_VERSION_MAJOR is 9<br>
CMake Error at CMake/SlicerBlockFindQtAndCheckVersion.cmake:44 (message):<br>
error: Missing Qt module named “Core”<br>
Call Stack (most recent call first):<br>
CMake/SlicerBlockFindQtAndCheckVersion.cmake:67 (__SlicerBlockFindQtAndCheckVersion_find_qt)<br>
CMakeLists.txt:644 (include)</p>
<p>Thank you in advance for any lead.</p>

---

## Post #2 by @RafaelPalomar (2021-12-15 21:25 UTC)

<p>Hello,</p>
<p>it looks to me that your error has to do with Qt and not with OpenGL. Have you tried to install all the dependencies listed in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html?highlight=linux#ubuntu-20-04-focal-fossa" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html?highlight=linux#ubuntu-20-04-focal-fossa</a>?</p>
<pre><code class="lang-auto">sudo apt update &amp;&amp; sudo apt install git subversion build-essential cmake cmake-curses-gui cmake-qt-gui \
  qt5-default qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev qtwebengine5-dev qtscript5-dev \
  qtbase5-private-dev libqt5x11extras5-dev libxt-dev
</code></pre>

---

## Post #3 by @Fabiola (2021-12-16 13:05 UTC)

<p>Hi Rafael, thank you so much for your reply.<br>
Yes, I run the dependencies above. Meanwhile I realized that I copy pasted the wrong error message.</p>
<p>After a several rounds of nvidia driver and Qt5 reinstallation, I think I reinstall my Ubuntu.<br>
Thank you for the help.</p>

---
