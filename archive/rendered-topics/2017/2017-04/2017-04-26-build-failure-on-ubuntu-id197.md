---
topic_id: 197
title: "Build Failure On Ubuntu"
date: 2017-04-26
url: https://discourse.slicer.org/t/197
---

# Build failure on Ubuntu

**Topic ID**: 197
**Date**: 2017-04-26
**URL**: https://discourse.slicer.org/t/build-failure-on-ubuntu/197

---

## Post #1 by @Lorensen (2017-04-26 14:59 UTC)

<p>Just did and update and tried to rebuild Slicer. I get the error:</p>
<p>loading initial cache file /home/lorensen/ProjectsGIT/Slicer-Superbuild/zlib-prefix/tmp/zlib-cache-Release.cmake<br>
CMake Error at CMakeLists.txt:3 (PROJECT):<br>
Generator</p>
<pre><code>Unix Makefiles
</code></pre>
<p>does not support toolset specification, but toolset</p>
<pre><code>USES_TERMINAL_DOWNLOAD
</code></pre>
<p>was specified.</p>
<p>– Configuring incomplete, errors occurred!<br>
See also “/home/lorensen/ProjectsGIT/Slicer-Superbuild/zlib-build/CMakeFiles/CMakeOutput.log”.</p>

---

## Post #2 by @pieper (2017-04-26 15:31 UTC)

<p>I did a fresh build on ubuntu with make -j20 and got an error that had scrolled off.  When I did a second build it completed with no error.  I’ll try another fresh build into a log file and see if it’s the same issue you reported.</p>

---

## Post #3 by @Lorensen (2017-04-26 15:56 UTC)

<p>Clean build, same error.</p>

---

## Post #4 by @Lorensen (2017-04-26 16:03 UTC)

<p>got bisect says it was this commit that broke the build:<br>
[7cafe8c8bc9be7128ffd3179a734a98850539af9] ENH: Update ExternalProjectDependency based on commontk/Artichoke@5ee3d50</p>

---

## Post #5 by @Lorensen (2017-04-26 16:05 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> looks like your commit:</p>
<p>commit 7cafe8c8bc9be7128ffd3179a734a98850539af9<br>
Author: jcfr <a href="mailto:jcfr@3bd1e089-480b-0410-8dfb-8563597acbee">jcfr@3bd1e089-480b-0410-8dfb-8563597acbee</a><br>
Date:   Fri Apr 14 22:24:36 2017 +0000</p>
<pre><code>ENH: Update ExternalProjectDependency based on commontk/Artichoke@5ee3d50

This commit improves the support for Ninja generator by ensuring the
option USES_TERMINAL_* options are set to give Ninja access to the
terminal when the CMake version supports it.

See https://cmake.org/cmake/help/v3.4/module/ExternalProject.html

Also Update CTK to integrate a similar update:

$ git shortlog 19fc678..b8587e5 --no-merges
Jean-Christophe Fillion-Robin (2):
      Update ExternalProjectDependency based on commontk/Artichoke@5ee3d50
      ENH: ExternalProjecDependency: Re-apply commontk/CTK@6cc426b

git-svn-id: http://svn.slicer.org/Slicer4/trunk@25929 3bd1e089-480b-0410-8df</code></pre>

---

## Post #6 by @Lorensen (2017-04-26 16:09 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
Interesting, I’m using cmake version 3.3.2 and the test to use the new USES_TERMINAL_* says:<br>
if(CMAKE_VERSION VERSION_GREATER “3.3”)<br>
# USES_TERMINAL_* options were introduced in CMake 3.4</p>
<p>Looks like the test is wrong.</p>

---

## Post #7 by @pieper (2017-04-26 16:14 UTC)

<p>Another clean build completed without error.  Probably a race condition.</p>
<p>IMy cmake is 3.5.1 so I didn’t see the TERMINAL issue.</p>

---

## Post #8 by @Lorensen (2017-04-26 16:15 UTC)

<p>In Slicer/CMake/ExternalProjectDependency.cmake</p>
<p>Test should be:<br>
if(CMAKE_VERSION VERSION_GREATER “3.3.2”)<br>
NOT<br>
if(CMAKE_VERSION VERSION_GREATER “3.3”)</p>

---

## Post #9 by @Lorensen (2017-04-26 17:03 UTC)

<p>The same error exists in CTK. I will update my cmake, but I think this error should be fixed.</p>
<p>Bill</p>

---

## Post #10 by @jcfr (2017-04-26 17:27 UTC)

<p>Thanks for the note. I will update the CMake modules now.</p>

---

## Post #11 by @jcfr (2017-04-26 17:33 UTC)

<p><a href="https://github.com/commontk/Artichoke/pull/18" class="onebox" target="_blank">https://github.com/commontk/Artichoke/pull/18</a></p>

---

## Post #12 by @jcfr (2017-04-26 17:34 UTC)

<p>As soon CI returns green, I will update CTK and Slicer.</p>
<p>Change integrated in Slicer in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=25978">r25978</a></p>

---
