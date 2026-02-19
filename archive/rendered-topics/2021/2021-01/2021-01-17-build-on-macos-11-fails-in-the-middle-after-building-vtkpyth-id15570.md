---
topic_id: 15570
title: "Build On Macos 11 Fails In The Middle After Building Vtkpyth"
date: 2021-01-17
url: https://discourse.slicer.org/t/15570
---

# Build on macOS 11 fails in the middle (after building vtkpython)

**Topic ID**: 15570
**Date**: 2021-01-17
**URL**: https://discourse.slicer.org/t/build-on-macos-11-fails-in-the-middle-after-building-vtkpython/15570

---

## Post #1 by @pll_llq (2021-01-17 20:41 UTC)

<p>Hi! I’m having trouble trying to build Slicer on macOS 11 (Intel)</p>
<ul>
<li>Source code from git (master branch)</li>
<li>Qt 5.15.0</li>
<li>cmake version 3.19.3</li>
<li>Apple clang version 12.0.0 (clang-1200.0.32.28)</li>
</ul>
<p>I configure the build with this command:</p>
<pre><code class="lang-auto">cmake \
    -DCMAKE_OSX_DEPLOYMENT_TARGET=11 \
    -DCMAKE_BUILD_TYPE:STRING=Debug \
    -DQt5_DIR:PATH=/Users/p2p/Qt/5.15.0/clang_64/lib/cmake/Qt5 \
    ../Slicer
</code></pre>
<p>The build continues for somewhat 30 minutes to stop with a message that’s not that informative to me</p>
<pre><code class="lang-auto"> [100%] Linking CXX shared library ../../lib/libvtkViewsInfovisPython36D-8.2.dylib
 [100%] Built target vtkViewsInfovisPythonD
 Scanning dependencies of target vtkViewsInfovisPython
 [100%] Building CXX object Wrapping/Python/CMakeFiles/vtkViewsInfovisPython.dir/vtkViewsInfovisPythonInit.cxx.o
 [100%] Linking CXX shared module ../../lib/python3.6/site-packages/vtkmodules/vtkViewsInfovisPython.so
 [100%] Built target vtkViewsInfovisPython
 Scanning dependencies of target vtk_python_package
 [100%] Built target vtk_python_package
 Scanning dependencies of target vtkpython
 [100%] Building CXX object Wrapping/Python/CMakeFiles/vtkpython.dir/vtkPythonAppInit.cxx.o
 [100%] Linking CXX executable ../../bin/vtkpython
 [100%] Built target vtkpython
 [ 81%] No install step for 'VTK'
 [ 81%] Creating '/Users/p2p/GitClones/CMI/Slicer-SuperBuild/python-install/lib/python3.6/site-packages/vtk-8.2.0-py3.6.egg-info' directory
 [ 81%] Completed 'VTK'
 [ 81%] Built target VTK
 make: *** [all] Error 2
</code></pre>
<p>The CMakeFiles/CMakeError.log has the following lines</p>
<pre><code class="lang-auto">Compiling the C compiler identification source file "CMakeCCompilerId.c" failed.
Compiler: /Applications/DevelopmentTools/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang
Build flags:
Id flags:
The output was:
1
ld: library not found for -lSystem
clang: error: linker command failed with exit code 1 (use -v to see invocation)

Compiling the CXX compiler identification source file "CMakeCXXCompilerId.cpp" failed.
Compiler: /Applications/DevelopmentTools/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++
Build flags:
Id flags:
The output was:
1
ld: library not found for -lc++
clang: error: linker command failed with exit code 1 (use -v to see invocation)
</code></pre>
<p>Am I missing something in the configuration? Are there any mac-heads here who can advice how to debug this?</p>

---

## Post #2 by @pll_llq (2021-01-18 16:26 UTC)

<p>If this might help suggesting a debug path, the last modified error log file in the superbuild folder is <code>./VTK-build/CMakeFiles/CMakeError.log</code> and it ends with the following error message:</p>
<pre><code class="lang-auto">
int main(int argc, char** argv)
{
  (void)argv;
#ifndef _stat
  return ((int*)(&amp;_stat))[argc];
#else
  (void)argc;
  return 0;
#endif
}
Checking for DIR in sys/ndir.h failed to compile with the following output:
Change Dir: /tmp/sb/VTK-build/ThirdParty/libxml2/vtklibxml2/CMakeFiles/CMakeTmp

Run Build Command(s):/usr/bin/make cmTC_99e16/fast &amp;&amp; /Applications/DevelopmentTools/Xcode.app/Contents/Developer/usr/bin/make  -f CMakeFiles/cmTC_99e16.dir/build.make CMakeFiles/cmTC_99e16.dir/build
Building C object CMakeFiles/cmTC_99e16.dir/platformTestsC.c.o
/Applications/DevelopmentTools/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -DTEST_HAVE_SYS_NDIR_H  -w -w  -isysroot /Applications/DevelopmentTools/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.1.sdk -mmacosx-version-min=11 -o CMakeFiles/cmTC_99e16.dir/platformTestsC.c.o -c /tmp/sb/VTK/ThirdParty/libxml2/vtklibxml2/platformTestsC.c
/tmp/sb/VTK/ThirdParty/libxml2/vtklibxml2/platformTestsC.c:82:10: fatal error: 'sys/ndir.h' file not found
#include &lt;sys/ndir.h&gt;
         ^~~~~~~~~~~~
1 error generated.
make[4]: *** [CMakeFiles/cmTC_99e16.dir/platformTestsC.c.o] Error 1
make[3]: *** [cmTC_99e16/fast] Error 2
</code></pre>

---

## Post #3 by @pieper (2021-01-18 18:27 UTC)

<p>I don’t get these errors on my mac builds.  I’ll bet your problem is using <code>/tmp</code> as the build tree, since files may get deleted from there as it fills.  On mac I now use <code>/opt/s</code> to keep the path short.</p>

---

## Post #4 by @pll_llq (2021-01-18 18:40 UTC)

<p>Thanks, will try that. I was looking through error logs that are left after the build and noticed several odd things:</p>
<ul>
<li>The python-numpy error log says that the hash of the downloaded package doesn’t match the hash that’s in the repo</li>
</ul>
<pre><code class="lang-auto">ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE. If you have updated the package versions, please update the hashes. Otherwise, examine the package contents carefully; someone may have tampered with them.
    numpy==1.19.2 from https://files.pythonhosted.org/packages/bf/e8/15aea783ea72e2d4e51e3ec365e8dc4a1a32c9e5eb3a6d695b0d58e67cdd/numpy-1.19.2.zip#sha256=0d310730e1e793527065ad7dde736197b705d0e4c9999775f212b03c44a8484c (from -r /tmp/sb/python-numpy-requirements.txt (line 8)):
        Expected sha256 967c92435f0b3ba37a4257c48b8715b76741410467e2bdb1097e8391fccfae15
        Expected     or b594f76771bc7fc8a044c5ba303427ee67c17a09b36e1fa32bde82f5c419d17a
        Expected     or 3733640466733441295b0d6d3dcbf8e1ffa7e897d4d82903169529fd3386919a
        Expected     or 7c6646314291d8f5ea900a7ea9c4261f834b5b62159ba2abe3836f4fa6705526
        Expected     or 7118f0a9f2f617f921ec7d278d981244ba83c85eea197be7c5a4f84af80a9c3c
             Got        0d310730e1e793527065ad7dde736197b705d0e4c9999775f212b03c44a8484c
</code></pre>
<p>After I manually add the hash of the package that I get I ran into a different error saying that pip is looking for a <code>MACOSX_DEPLOYMENT_TARGET</code> that should be a string, not an int. I got your message when I just started the build specifying both the hash and <code>-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=11.1</code> but before I continue my experiments I’ll try to move to <code>/opt/</code>.</p>

---

## Post #5 by @jamesobutler (2021-01-18 20:01 UTC)

<p>The numpy install issue is probably because Slicer is currently using pip 20.2.4 and in the <a href="https://pip.pypa.io/en/stable/news/#id15" rel="noopener nofollow ugc">pip 20.3 release notes</a> it includes “Add support for MacOS Big Sur compatibility tags.”  This might be solved by just updating the pip version.</p>

---

## Post #6 by @pll_llq (2021-01-18 21:54 UTC)

<p>I see python package hash issues with numpy, scipy and pillow that comes with python-dicom.<br>
If I try to specify the package hashes that I get, I end up with scipy not being able to install because of</p>
<pre><code class="lang-auto">numpy.distutils.system_info.NotFoundError: No lapack/blas resources found. Note: Accelerate is no longer supported.
</code></pre>
<p>I’ll try to update the version of pip along with some other stuff that it advised in the scipy’s github issue (like installing openblas from brew), but I’m not sure this is the reason for my build to fail.</p>
<p>Just to check, <a class="mention" href="/u/pieper">@pieper</a> is the Slicer source code also required to be in a folder with a short path, or only the build dir? If it is this might be my problem.</p>

---

## Post #7 by @pieper (2021-01-18 21:59 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="6" data-topic="15570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>Just to check, <a class="mention" href="/u/pieper">@pieper</a> is the Slicer source code also required to be in a folder with a short path, or only the build dir? If it is this might be my problem.</p>
</blockquote>
</aside>
<p>No, just the build tree.  And typically on mac the long path is only a problem at runtime (on windows it can be a compile time issue).</p>

---

## Post #8 by @pll_llq (2021-01-18 22:01 UTC)

<p>I am about to give up=)<br>
What CMAKE_OSX_DEPLOYMENT_TARGET do you use in your builds?</p>
<p>Also can anyone advice some secret command I can type into the black hole of the terminal to see what exactly caused the make error?=)</p>

---

## Post #9 by @jamesobutler (2021-01-18 23:35 UTC)

<p>I issued <a href="https://github.com/Slicer/Slicer/pull/5393" class="inline-onebox" rel="noopener nofollow ugc">COMP: Update python pip to latest by jamesobutler · Pull Request #5393 · Slicer/Slicer · GitHub</a> to attempt to address that pip install issue when using macOS Big Sur.</p>

---

## Post #10 by @jcfr (2021-01-19 00:15 UTC)

<p>Thanks everyone for taking the time to investigate <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"> and thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> for submitting a pull request,  it has been integrated <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=9" title=":rocket:" class="emoji" alt=":rocket:"></p>

---

## Post #11 by @pieper (2021-01-19 00:35 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="8" data-topic="15570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>I am about to give up=)</p>
</blockquote>
</aside>
<p>Don’t give up!</p>
<aside class="quote no-group" data-username="pll_llq" data-post="8" data-topic="15570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>What CMAKE_OSX_DEPLOYMENT_TARGET do you use in your builds?</p>
</blockquote>
</aside>
<p>I use this command:</p>
<pre><code class="lang-auto">BUILD_TYPE=Debug

cmake \
	-DCMAKE_BUILD_TYPE:STRING=${BUILD_TYPE} \
	-DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 \
	-DQt5_VERSION:STRING=5.15 \
	-DQt5_DIR:PATH=/usr/local/Cellar/qt/5.15.0/lib/cmake/Qt5 \
	/Users/pieper/slicer/latest/Slicer
</code></pre>
<p>I can’t recall if I’ve build from scratch on mac since updating the OS.  If you are still having trouble tomorrow I’ll try a fresh build.</p>
<aside class="quote no-group" data-username="pll_llq" data-post="8" data-topic="15570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>Also can anyone advice some secret command I can type into the black hole of the terminal to see what exactly caused the make error?=)</p>
</blockquote>
</aside>
<p>Not exactly a secret, but I often do something like:</p>
<pre><code class="lang-auto">make -j10 -k; make 2&gt;&amp;1 | tee /tmp/build.log
</code></pre>
<p>Just let this run and the -k will build everything it can on the first round, then the second make will stop at the real error.  The <code>2&gt;&amp;1</code> sends errors to stdout and <code>tee</code> saves a file you can search through but also shows progress in the terminal.</p>

---

## Post #12 by @pll_llq (2021-01-19 21:28 UTC)

<p>Hey <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20"></p>
<p>Just to follow up on this one. First of all, thanks everyone for looking into this and thank you <a class="mention" href="/u/jamesobutler">@jamesobutler</a> for the PR. The upgrade of pip version did solve the issue I had yesterday.</p>
<p>Here’s a small log of my endeavours.</p>
<p>As discussed on the Weekly Hangout the core of the problems might have been that I’ve specified <code>CMAKE_OSX_DEPLOYMENT_TARGET=11.1</code> while everyone specifies 10.15 or earlier. Not that this is a problem, but this could have popped up later while creating the build for Apple Silicon.</p>
<p>Despite that I’ve succeeded with the build there are a couple things that seem strange.</p>
<p>After my first attempt to build with the latest version of pip I ended up with logs full of errors saying that OpenBLAS could not be found and the app didn’t launch. I understand that OpenBLAS is not a requirement for Slicer, though it’s needed for scipy. So I’ve installed openblas from homebrew and the build went smooth without a single error.<br>
But the Slicer app still didn’t launch. Only a distorted splashscreen and the app freezes after that.</p>
<p>So I decided to run the tests.<br>
When I launched the tests the widgets started popping up as expected so it seemed that Slicer is working. And only after I ran the tests launching the application would produce a distorted splashscreen followed by the UI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1ae98e20ce1e288f6fb3f544d6d1d3ae9985807.jpeg" data-download-href="/uploads/short-url/tUVRzAL6KXjGcZKY5mWBLFgqKRF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1ae98e20ce1e288f6fb3f544d6d1d3ae9985807_2_690x402.jpeg" alt="image" data-base62-sha1="tUVRzAL6KXjGcZKY5mWBLFgqKRF" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1ae98e20ce1e288f6fb3f544d6d1d3ae9985807_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1ae98e20ce1e288f6fb3f544d6d1d3ae9985807_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1ae98e20ce1e288f6fb3f544d6d1d3ae9985807_2_1380x804.jpeg 2x" data-dominant-color="3E4040"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2824×1648 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Functionally Slicer is working as expected.</p>
<p>Regarding the distorted splashscreen, I think this has something to do with an HDPI display settings (like the <code>AA_UseHighDpiPixmaps</code> attribute is missing somewhere).</p>
<p>P.S. Some tests failed</p>
<pre><code class="lang-auto">Total Test time (real) = 3712.16 sec

The following tests FAILED:
    184 - qMRMLLayoutManagerTest4 (Failed)
    373 - py_MarkupsCurveMeasurementsTest (Failed)
    407 - py_nomainwindow_SegmentationsModuleTest2 (Failed)
    524 - ModelMakerGenerateAllOneLabelTest (Failed)
    647 - py_WebEngine (Failed)
    651 - py_SlicerRestoreSceneViewCrashIssue3445 (Failed)
</code></pre>

---

## Post #13 by @lassoan (2021-01-19 22:16 UTC)

<p>When you start Slicer, you see two splash images: one rendered immediately by the launcher, then some time later a second one rendered by the Slicer application. Which splash images are scaled incorrectly: the first, the second, or both?</p>

---

## Post #14 by @pll_llq (2021-01-19 22:18 UTC)

<p>I only see one. It’s rendered immediately, then it goes away and in a couple of seconds I see the UI.</p>

---

## Post #15 by @pieper (2021-01-19 22:35 UTC)

<p>Did you run Slicer.app from within a package?  On the mac that will only have one splash screen because there is no launcher for that case.</p>

---

## Post #16 by @jamesobutler (2021-01-19 23:09 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="12" data-topic="15570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>After my first attempt to build with the latest version of pip I ended up with logs full of errors saying that OpenBLAS could not be found and the app didn’t launch. I understand that OpenBLAS is not a requirement for Slicer, though it’s needed for scipy. So I’ve installed openblas from homebrew and the build went smooth without a single error.</p>
</blockquote>
</aside>
<p>I would’ve probably cleared out any “python-scipy*” directories or project files. Possibly just cleared out all the “python-*” type directories to rebuild the python stuff.</p>
<p>What could be happening is that the original build did not find a Scipy wheel that fit the os platform, and therefore download the Scipy source which might require OpenBLAS as a build requirement. Then even with pip upgraded it might’ve attempted to still build from source which is why I suggest the clearing out of directories.  This would make sure that it does not try to build Scipy from source and picks an appropriate wheel.</p>

---

## Post #17 by @pll_llq (2021-01-20 05:43 UTC)

<p>No, I didn’t package the app</p>

---
