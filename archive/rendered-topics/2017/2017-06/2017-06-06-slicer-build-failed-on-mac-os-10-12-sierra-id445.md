---
topic_id: 445
title: "Slicer Build Failed On Mac Os 10 12 Sierra"
date: 2017-06-06
url: https://discourse.slicer.org/t/445
---

# Slicer build failed on Mac OS 10.12 Sierra

**Topic ID**: 445
**Date**: 2017-06-06
**URL**: https://discourse.slicer.org/t/slicer-build-failed-on-mac-os-10-12-sierra/445

---

## Post #1 by @mschumaker (2017-06-06 15:37 UTC)

<p>I’m having difficulty building Slicer on Sierra.<br>
Operating system: OSX 10.12.5<br>
Slicer: Newest nightly (Jun 6 2017)<br>
Qt: cartr/qt4/qt<br>
CMake: 3.8.0<br>
Xcode: 8.3.2<br>
I’ve tried CMAKE_BUILD_TYPE set to Debug and Release, CMAKE_OSX_DEPLOYMENT_TARGET set to 10.12 and 10.9. CMAKE_C_COMPILER is set to /usr/bin/clang and CMAKE_CXX_COMPILER is set to /usr/bin/clang++. QT_QMAKE_EXECUTABLE is set to /usr/local/bin/qmake, which has a symbolic link to qmake in the Cellar directory.</p>
<p>The build fails on the “python” target. Error output is:</p>
<p>PhaseScriptExecution CMake\ Rules /Users/michaelschumaker/Packages/Slicer-SuperBuild-Debug/Slicer.build/Debug/python.build/Script-30496EF0E9A74020BE818B09.sh<br>
cd /Users/michaelschumaker/Packages/Slicer<br>
/bin/sh -c /Users/michaelschumaker/Packages/Slicer-SuperBuild-Debug/Slicer.build/Debug/python.build/Script-30496EF0E9A74020BE818B09.sh</p>
<p>make: *** No rule to make target <code>/Users/michaelschumaker/Packages/Slicer-SuperBuild-Debug/python-source-prefix/src/python-source-stamp/Release/python-source-done', needed by</code>/Users/michaelschumaker/Packages/Slicer-SuperBuild-Debug/python-prefix/src/python-stamp/Release/python-configure’.  Stop.<br>
Command /bin/sh failed with exit code 2</p>
<p>What’s interesting is that, even when I set it to the Debug build type, the directories of python-source-done and python-configure in the error are still “Release”. Is there a mistake in the configuration script?</p>

---

## Post #2 by @mschumaker (2017-06-12 14:47 UTC)

<p>I’m just moving this to the top. Can anyone suggest a solution?</p>

---

## Post #3 by @lassoan (2017-06-12 14:52 UTC)

<p>I don’t use a Mac, but on Windows Python is always built in Release mode (regardless of the application is built in debug or release).</p>
<p>Have you tried to build/get Qt as described on Slicer build instructions page?</p>

---

## Post #4 by @mschumaker (2017-06-12 15:11 UTC)

<p>Ok, thanks, I won’t worry about the build mode for the Python job. I was trying to identify any reason it might be the job that’s failing to build.<br>
I installed cartr/qt4/qt before compiling Slicer. I had previously installed Qt5.8, though.</p>

---

## Post #5 by @ihnorton (2017-06-12 15:14 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="1" data-topic="445">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>What’s interesting is that, even when I set it to the Debug build type, the directories of python-source-done and python-configure in the error are still “Release”. Is there a mistake in the configuration script?</p>
</blockquote>
</aside>
<p>No, Slicer <a href="https://github.com/Slicer/Slicer/blob/a27c91d2adbd390b7524f1c41aa1d4d3e4fc3e4e/SuperBuild/External_python.cmake#L104-L111">always builds python in Release</a> (IIRC because of symbol export variations when built in debug).</p>
<p>For what it’s worth, I did a successful clean build of all python dependencies (<code>rm python-*</code> in the superbuild folder) in a Release build on Sierra within the past two weeks, and my folders look like this:</p>
<pre><code class="lang-auto">:r4nj inorton$ ls python-source-prefix/src/python-source-stamp/
download-python-source.cmake	python-source-configure		python-source-install		python-source-update
extract-python-source.cmake	python-source-done		python-source-mkdir		python-source-urlinfo.txt
python-source-build		python-source-download		python-source-patch		verify-python-source.cmake
</code></pre>

---

## Post #6 by @lassoan (2018-06-25 12:20 UTC)

<p>A post was split to a new topic: <a href="/t/slicer-build-error-on-macosx-in-dcmtk/3277">Slicer build error on MacOSX in DCMTK</a></p>

---
