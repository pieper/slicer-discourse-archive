# Qt Path - Configuration for Building Slicer

**Topic ID**: 9171
**Date**: 2019-11-15
**URL**: https://discourse.slicer.org/t/qt-path-configuration-for-building-slicer/9171

---

## Post #1 by @marie (2019-11-15 19:35 UTC)

<p>Hi there!</p>
<p>I would like to build Slicer on Ubuntu 19.10. I installed Qt5 via:<br>
$ sudo apt install qt5-default</p>
<p>Now I am struggling with the following command (see Documentation):<br>
cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:PATH=/path/to/Qt5.11.0/5.11.0/gcc_64/lib/cmake/Qt5 …/Slicer</p>
<p>Documentation:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Common_Prerequisites" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Common_Prerequisites</a></p>
<p>How should I replace <em>/path/to/QtSDK</em> ?? I just can’t find such a path.</p>
<p>Thanks for helping!</p>
<ul>
<li>marie</li>
</ul>

---

## Post #2 by @marie (2019-11-15 20:15 UTC)

<p>I just solved it myself. Thank you anyway!</p>

---

## Post #3 by @lassoan (2019-11-15 20:32 UTC)

<p>It seems that the build instructions were not clear enough. Could you tell us how to change them to make them easier to follow?</p>

---

## Post #4 by @marie (2019-11-15 21:46 UTC)

<p>Of course. In the documentation it says:</p>
<blockquote>
<p>Qt 5.11: <strong>tested and recommended</strong></p>
<ul>
<li>To build Slicer: install Qt using the distribution package manager.</li>
<li>To package and redistribute Slicer: download and execute <a href="https://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run" rel="noopener nofollow ugc">qt-unified-linux-x64-online.run</a>, install Qt, make sure to select qtscript and qtwebengine components.</li>
</ul>
</blockquote>
<p>I thought only the first option was suitable for building 3DSlicer. It turned out, that the second solution works fine! After execution and installing version <strong>5.11.0</strong> (not 5.12), everything worked as expected. Versions older than 5.12 are available on the left (see archive tab in the installation window). I didn’t choose all components but qtscript and qtwebengine as recommended. Some options can occupy much space!</p>
<p>I don’t know whether it works with apt installation though.</p>

---
