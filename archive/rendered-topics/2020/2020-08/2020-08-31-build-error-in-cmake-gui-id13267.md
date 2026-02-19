---
topic_id: 13267
title: "Build Error In Cmake Gui"
date: 2020-08-31
url: https://discourse.slicer.org/t/13267
---

# Build - Error in CMake GUI

**Topic ID**: 13267
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/build-error-in-cmake-gui/13267

---

## Post #1 by @Valmar (2020-08-31 20:50 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43d97a216f66f7d5cd47ff67c999611b0f6e4124.png" alt="Screen Shot 2020-08-31 at 17.28.27" data-base62-sha1="9GdVQrSCDohQRjbC7hypdBFIx9y" width="572" height="147"></p>
<p>If i remove the line 70, the other errors happened.<br>
error:<br>
CMake Error at CMake/SlicerInitializeOSXVariables.cmake:70 (message):<br>
CMAKE_OSX_DEPLOYMENT_TARGET must be 10.13 or greater.<br>
Call Stack (most recent call first):<br>
CMakeLists.txt:31 (include)</p>
<p>How can i proceed here?</p>

---

## Post #2 by @jamesobutler (2020-08-31 21:34 UTC)

<p>What version of macOS are you running?<br>
What version of XCode are you using?</p>
<p>What area of Slicer development are you interested in?</p>

---

## Post #3 by @Valmar (2020-08-31 22:23 UTC)

<p>I`m using macOS Catalina 10.15.2 (19C57)<br>
Cmake:  3.18.2<br>
Xcode: Version 11.3 (11C29)</p>
<p>I just clone de Slicer and SlicerIGT github, create a new folder called Slicer-bin and Igt-bin. In the Cmake i put the “source code” = github cloned folder. In the “where to build the binaries” = -bin folders. I`m trying to build both of them to make some experiments.</p>

---

## Post #4 by @jamesobutler (2020-08-31 23:14 UTC)

<p>I would suggest not to do anything with SlicerIGT until you have a working Slicer build.</p>
<p>Have you built Slicer successfully yet?</p>

---

## Post #5 by @Valmar (2020-08-31 23:28 UTC)

<p>The present problem is in Slicer build. I did nothing with IGT yet.</p>

---

## Post #6 by @Valmar (2020-09-01 16:33 UTC)

<p>Any tips? I’m out of ideas.</p>

---

## Post #7 by @jamesobutler (2020-09-01 17:01 UTC)

<p><a class="mention" href="/u/valmar">@Valmar</a> Have you been following the macOS build instructions over at  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/macos.html</a> ?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Can you provide help for this macOS user?</p>

---

## Post #8 by @pieper (2020-09-01 19:10 UTC)

<p>Hi <a class="mention" href="/u/valmar">@Valmar</a> I start a fresh build using the cmake command line below.  This satisfies the initial checks.  After that first configuration you can use ccmake if you need to make further changes.</p>
<pre><code class="lang-auto">BUILD_TYPE=Debug
cmake \
	-DCMAKE_BUILD_TYPE:STRING=${BUILD_TYPE} \
	-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 \
	-DQt5_VERSION:STRING=5.15 \
	-DQt5_DIR:PATH=/usr/local/Cellar/qt/5.15.0/lib/cmake/Qt5 \
	/Users/pieper/slicer/latest/Slicer
</code></pre>

---

## Post #9 by @Valmar (2020-09-02 17:18 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a>! Cmake GUI isn`t working in this first step. The same problem appear again in the make step.</p>
<p>command used: make and SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk make -j20   (documentation)</p>
<p>error:<br>
CMake Error at CMake/SlicerInitializeOSXVariables.cmake:70 (message):<br>
CMAKE_OSX_DEPLOYMENT_TARGET must be 10.13 or greater.<br>
Call Stack (most recent call first):<br>
CMakeLists.txt:31 (include)</p>
<p>– Configuring incomplete, errors occurred!<br>
make: *** [cmake_check_build_system] Error 1<br>
valmarzinho@Valmarzinho Slicer-bin %</p>

---

## Post #10 by @pieper (2020-09-02 19:18 UTC)

<p>Hmm, I don’t have that error.  Are you sure you copied the cmake line that I pasted before?  It sets <code>-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15</code> so that error should not happen…</p>

---

## Post #11 by @Valmar (2020-09-02 19:28 UTC)

<p>I reinstalled cmake, xcode and qt. I deleted the cmakeCache.</p>
<p>I used the cmake command that you passed me (changing the user name) and now it worked.</p>
<p>I’m waiting for the make to end!</p>

---

## Post #12 by @pieper (2020-09-02 19:32 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji only-emoji" alt=":+1:"></p>
<p>Depending on your machine it can take a while.  Using <code>make -j N</code> where N is the number of CPU cores available can speed things along nicely.  Good luck.</p>

---
