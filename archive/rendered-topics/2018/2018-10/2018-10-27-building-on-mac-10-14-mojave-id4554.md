---
topic_id: 4554
title: "Building On Mac 10 14 Mojave"
date: 2018-10-27
url: https://discourse.slicer.org/t/4554
---

# Building on Mac 10.14 Mojave

**Topic ID**: 4554
**Date**: 2018-10-27
**URL**: https://discourse.slicer.org/t/building-on-mac-10-14-mojave/4554

---

## Post #1 by @hjmjohnson (2018-10-27 10:12 UTC)

<p>After running into:</p>
<pre><code class="lang-auto">./cryptlib.h:62:11: fatal error: 'stdlib.h' file not found
# include &lt;stdlib.h&gt;
          ^~~~~~~~~~
1 error generated.
</code></pre>
<p>I found:  <a href="https://github.com/frida/frida/issues/338#issuecomment-426777849" rel="nofollow noopener">https://github.com/frida/frida/issues/338#issuecomment-426777849</a></p>
<p>For anyone discovering this later on who may not be familiar with the command line, here’s how to install the  <code>macOS_SDK_headers_for_macOS_10.14.pkg</code>  package as explained in <a href="https://github.com/yicongli" rel="nofollow noopener">@yicongli</a>’s <a href="https://github.com/frida/frida/issues/338#issuecomment-424595668" rel="nofollow noopener">response above</a>:</p>
<p>In  <code>Terminal.app</code>  or any shell app like  <code>iTerm</code> :</p>
<pre><code class="lang-auto">cd /Library/Developer/CommandLineTools/Packages/
open macOS_SDK_headers_for_macOS_10.14.pkg
</code></pre>

---

## Post #2 by @pieper (2018-10-28 01:30 UTC)

<p>Also on macOS Mojave on a new mac, I had the same issue, but <code>macOS_SDK_headers_for_macOS_10.14.pkg</code> wasn’t there.  I got it by downloading and running <a href="https://download.developer.apple.com/Developer_Tools/Command_Line_Tools_macOS_10.14_for_Xcode_10/Command_Line_Tools_macOS_10.14_for_Xcode_10.dmg">this</a> from the developer site.  Running <code>xcode-select --install</code> might also have worked.</p>
<p>Then I had to <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27525">fix some tests</a> but then the compile completed.</p>
<p>Slicer runs, but it’s not usable.  This is with Qt 5.11.2 on a macbook pro retina, with the resolution set as “best for display”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4245403ef4d37e5916d4103949d78ecde36b8042.jpeg" data-download-href="/uploads/short-url/9sfSIw1D3peHCYRhEGaKe5o2PSi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4245403ef4d37e5916d4103949d78ecde36b8042_2_690x443.jpeg" alt="image" data-base62-sha1="9sfSIw1D3peHCYRhEGaKe5o2PSi" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4245403ef4d37e5916d4103949d78ecde36b8042_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4245403ef4d37e5916d4103949d78ecde36b8042_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4245403ef4d37e5916d4103949d78ecde36b8042_2_1380x886.jpeg 2x" data-dominant-color="DA8C97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1852×1190 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2018-10-28 16:01 UTC)

<p>This issue of VTK renderer filling up only half of view was a common issue with older VTK versions on MacOS. Interestingly, this issue was recently reported on Surface Pro tablets on Windows and now you see this on MacOS, too.</p>
<p>Maybe it has to do something with switching to native widget as base class? <a class="mention" href="/u/jcfr">@jcfr</a> do you have idea how to address this?</p>

---

## Post #4 by @pieper (2018-10-28 16:23 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="4554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This issue of VTK renderer filling up only half of view was a common issue with older VTK versions on MacOS. Interestingly, this issue was recently reported on Surface Pro tablets on Windows and now you see this on MacOS, too.</p>
</blockquote>
</aside>
<p>Yes, but interestingly it isn’t just the VTK windows - the other QWidgets are also messed up.  For example in the SampleData module clicking on the MRHead result in loading the DTI example so the display vs event handling geometry is messed up.</p>
<p>BTW the Nightly build works fine on the same machine, so it’s something about the newer Qt and/or the Xcode or OSX deployment target settings.</p>

---

## Post #5 by @lassoan (2018-10-28 16:37 UTC)

<p>I see. It may be a different issue then. On Windows, it often takes some time for Qt with catch up with operating system and compiler changes. I guess it could be similar on MacOS, too, and so you can either go back to a bit older toolchain or wait for a new Qt version. Probably many people have reported this issue, so there may be a patch or beta version available already.</p>

---

## Post #6 by @pieper (2018-10-29 02:38 UTC)

<p>Yes, I’m sure it’ll be sorted out.  Just need to look at what might be leading to the differences or wait for bugs to be fixed upstream.</p>
<p>I tried recompiling with CMAKE_OSX_DEPLOYMENT_TARGET set to 10.`14 but no difference.</p>

---

## Post #7 by @che85 (2018-12-06 15:24 UTC)

<p>Is there anything new on this? I also ran into the same issues on MacOS Mojave where the SliceViews only occupy a small space of what it’s supposed to be.</p>
<p>Or is there maybe a workaround?</p>

---

## Post #8 by @lassoan (2018-12-06 15:42 UTC)

<p>First <a href="http://blog.qt.io/blog/2018/11/08/qt-macos-10-14-mojave/" rel="nofollow noopener">Qt had to add support for MacOS Mojave</a>, which should be OK now. Various error reported in other dependencies, such as <a href="http://cmake.3232098.n2.nabble.com/Odd-Behavior-in-macOS-Mojave-td7598637.html" rel="nofollow noopener">CMake</a> and <a href="http://vtk.1045678.n5.nabble.com/QVTKRenderWindowInteractor-bug-in-Mac-OS-tt5749012.html" rel="nofollow noopener">VTK</a>. If those are fixed, too, then remaining potential Slicer-specific issues must be addressed. Eventually (in a few weeks or months) things will be sorted out, but if you don’t have time to help out with reporting and investigating issues then it may be simpler to wait it out and use earlier build environment for a while.</p>

---

## Post #9 by @pieper (2018-12-06 19:08 UTC)

<p>FWIW, I installed the homebrew Qt5 environment and rebuilt on the Mojave mac laptop and the rendering issues went away.</p>

---

## Post #10 by @jcfr (2018-12-06 19:44 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="4554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>homebrew Qt5 environment and rebuilt on the Mojave mac laptop and the rendering issues went away.</p>
</blockquote>
</aside>
<p>Interesting, the recipe use to create the corresponding Qt5 package seems to be quite normal, see <a href="https://github.com/Homebrew/homebrew-core/blob/master/Formula/qt.rb">https://github.com/Homebrew/homebrew-core/blob/master/Formula/qt.rb</a></p>
<p>As a side note, when building on macOS, the variable Qt5_DIR and CMAKE_OSX_DEPLOYMENT_TARGET must be specified when doing a clean configuration.</p>

---

## Post #11 by @lassoan (2018-12-07 00:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="4554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>installed the homebrew Qt5 environment</p>
</blockquote>
</aside>
<p>Which Qt version did you use?</p>

---

## Post #12 by @pieper (2018-12-07 13:34 UTC)

<p>Both home brew and the Qt download were 5.11 (both 5.11.2 I believe).</p>

---

## Post #13 by @che85 (2018-12-07 14:30 UTC)

<p>I used 5.10 and it didn’t work. Will try with brew and 5.11 again.</p>

---

## Post #14 by @che85 (2018-12-26 22:40 UTC)

<p>I built Slicer with Qt 5.11.2 (downloaded and installed from Qt) and set <code>CMAKE_OSX_DEPLOYMENT_TARGET=10.14</code></p>
<p>Sadly, it’s not working that way either for me.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6ba267485f5e2947a51d7de2e7af32c0477fb4ba.jpeg" data-download-href="/uploads/short-url/fmb2iGVD26zjT0exRHfBnwFM3GO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ba267485f5e2947a51d7de2e7af32c0477fb4ba_2_690x410.jpeg" alt="image" data-base62-sha1="fmb2iGVD26zjT0exRHfBnwFM3GO" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ba267485f5e2947a51d7de2e7af32c0477fb4ba_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ba267485f5e2947a51d7de2e7af32c0477fb4ba_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6ba267485f5e2947a51d7de2e7af32c0477fb4ba_2_1380x820.jpeg 2x" data-dominant-color="D55C62"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4064×2418 751 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>While starting I get the following warning.</p>
<pre><code class="lang-auto">Warning: In /Users/herzc/sources/cpp/Slicer/Libs/MRML/DisplayableManager/vtkMRMLThreeDReformatDisplayableManager.cxx, line 99
vtkMRMLThreeDReformatDisplayableManager (0x7faeea1000e0): Widget outline mode not available
</code></pre>
<p>Some more details on my environment:</p>
<pre><code class="lang-auto">XCode Version 10.1 (10B61)
Apple LLVM version 10.0.0 (clang-1000.11.45.5)
Target: x86_64-apple-darwin18.2.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
</code></pre>

---

## Post #15 by @lassoan (2018-12-27 04:52 UTC)

<aside class="quote no-group" data-username="che85" data-post="14" data-topic="4554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/che85/48/636_2.png" class="avatar"> che85:</div>
<blockquote>
<p>vtkMRMLThreeDReformatDisplayableManager (0x7faeea1000e0): Widget outline mode not available</p>
</blockquote>
</aside>
<p>This error is logged when you use VTK7 or older. We have switched to VTK8 long time ago and just keep VTK7 compatibility to allow building with Qt4 + legacy OpenGL rendering backend.</p>
<p>Can you double-check your VTK version by executing <code>print(vtk.vtkVersion().GetVTKVersion())</code>?</p>
<p>If you don’t get VTK version <code>8.2.0</code> then double-check your build scripts to make sure you don’t force Slicer to use VTK 7.</p>

---

## Post #16 by @che85 (2018-12-27 15:15 UTC)

<p>You are right! It’s using VTK version 7.1.0</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fd580ab3650d2c883534c459d845256fcb13288.png" data-download-href="/uploads/short-url/2g4AxflxcQ3Z93GNgfeFsFUlUXC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd580ab3650d2c883534c459d845256fcb13288_2_690x191.png" alt="image" data-base62-sha1="2g4AxflxcQ3Z93GNgfeFsFUlUXC" width="690" height="191" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd580ab3650d2c883534c459d845256fcb13288_2_690x191.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd580ab3650d2c883534c459d845256fcb13288_2_1035x286.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fd580ab3650d2c883534c459d845256fcb13288.png 2x" data-dominant-color="F0A8AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1254×348 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For some reason CMake did not set Slicer_VTK_VERSION_MAJOR to “8” after I set Qt5_DIR.</p>
<p>If I set Slicer_VTK_VERSION_MAJOR to “8” before setting CMAKE_OSX_DEPLOYMENT_TARGET it configures correctly (also asking for Qt version &gt; 5.6).</p>
<p>Will do a fresh build now again.</p>

---

## Post #17 by @lassoan (2018-12-27 16:31 UTC)

<p>You need to set Qt5_DIR before configuring your project as described in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Unix-like" rel="nofollow noopener">build instructions</a>. We’ll disable Qt4/Vtk7 build in the master right after releasing 4.10.1 (within days), which will prevent this error.</p>

---

## Post #18 by @che85 (2018-12-27 16:52 UTC)

<p>Ok that’s good to know for the next time! Thanks a lot.</p>
<p>It worked!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a808d7f0e25ef7e692c51cbcbe559cc03e46c9c7.jpeg" data-download-href="/uploads/short-url/nYva3s0mEDCMqnH0iGPxOtOsljV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a808d7f0e25ef7e692c51cbcbe559cc03e46c9c7_2_690x409.jpeg" alt="image" data-base62-sha1="nYva3s0mEDCMqnH0iGPxOtOsljV" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a808d7f0e25ef7e692c51cbcbe559cc03e46c9c7_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a808d7f0e25ef7e692c51cbcbe559cc03e46c9c7_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a808d7f0e25ef7e692c51cbcbe559cc03e46c9c7_2_1380x818.jpeg 2x" data-dominant-color="7E7D84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4064×2412 593 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @drouin-simon (2019-01-28 19:59 UTC)

<p>FYI: <code>xcode-select --install</code> doesn’t install the headers. You have to install <code>macOS_SDK_headers_for_macOS_10.14.pkg</code> to get the headers. This should be added to the build instructions for Slicer. Where is that now? <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">This page</a> seems pretty out of date now.</p>

---

## Post #20 by @drouin-simon (2019-01-28 20:51 UTC)

<p><a class="mention" href="/u/che85">@che85</a>: did you also change the version of Qt you were using? Changing vtk version alone cannot fix the huge buttons problem? I’ve had the huge button problem with two other applications I’m working on, one of them not even using vtk. I think it is a problem with the management of retina (hi-dpi) vs. non-retina displays.</p>
<p>I use only Qt binaries from <a href="http://www.qt.io" rel="nofollow noopener">www.qt.io</a> and get the huge button problem on Mojave if I use any version above 5.9.* which was the last LTS version before 5.12. Maybe the 5.12.1 binary fixes the problem but I haven’t tried. The fact that <a class="mention" href="/u/pieper">@pieper</a> had success with Qt &gt; 5.9 suggests that there is something in the build process rather than in the version of Qt itself that causes the problem. Perhaps the deployment target? Binaries from <a href="http://qt.io" rel="nofollow noopener">qt.io</a> have a minimum osx version of 10.10. Building Qt for 10.14 might fix the problem. Does anybody have better insights into this problem so that we can come up with clear build instructions?</p>

---

## Post #21 by @drouin-simon (2019-04-18 20:49 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/che85">@che85</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, does one of you have write access to the Slicer build instruction page <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">here</a>? It would be nice to add a comment on the need to install the header package (<code>macOS_SDK_headers_for_macOS_10.14.pkg</code>) to build Slicer. <code>xcode-select --install</code> alone still doesn’t install the headers.</p>

---

## Post #22 by @jcfr (2019-04-18 21:45 UTC)

<p>Thanks for the reminder.</p>
<p>Here it is: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Mac_OSX_10.14_.28Mojave.29" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Mac_OSX_10.14_.28Mojave.29</a></p>
<p>If you create a wiki account, I will make sure it is approved and you should be able to improve further.</p>

---

## Post #23 by @pieper (2019-04-18 21:58 UTC)

<p>I ran into this the other day and <a href="https://issues.slicer.org/view.php?id=4681" rel="nofollow noopener">filed an issue</a> with a workaround to specify the SDK version.  It turns out <a href="https://developer.apple.com/documentation/xcode_release_notes/xcode_10_release_notes#3035623" rel="nofollow noopener">Apple deprecated /usr/include</a>.  I updated the wiki with what I think it the preferred solution for now.</p>

---

## Post #24 by @jcfr (2019-04-18 22:20 UTC)

<p>Thanks Steve. I will submit a PR to update the build system, it should be quite straightforward.</p>

---

## Post #25 by @bpaniagua (2019-06-09 13:28 UTC)

<p>Hi,</p>
<p>Has anybody tried to install gfortran in MacOS 10.14? I was able to build Slicer no problem thanks to this thread, but now I cant build <a href="http://salt.slicer.org" rel="nofollow noopener">SALT</a> in my new Macbook pro since Xcode 10 has no gfortran. <a href="https://github.com/NIRALUser/SPHARM-PDM" rel="nofollow noopener">SPHARM</a> still depends on this compiler.</p>
<p>This <a href="https://solarianprogrammer.com/2017/05/21/compiling-gcc-macos/" rel="nofollow noopener">tutorial</a> explains in great detail how to install gcc9 (includes gfortran), but I wanted to check in first with you guys in case somebody has tried other ones successfully…</p>
<p>Thanks!<br>
Bea</p>

---

## Post #26 by @hjmjohnson (2019-06-09 14:50 UTC)

<p>I have not used gfortran in a long time.</p>
<p>I’d recommend using homebrew.  “brew install gcc”</p>
<p>If you meant “gfortran” specifically:</p>
<p>GNU Fortran is part of the GCC formula:</p>
<p>brew install gcc</p>
<p>Hans</p>

---

## Post #27 by @bpaniagua (2019-06-10 13:35 UTC)

<p>Thanks <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a><br>
Is gcc part of XCode or it got deprecated, favoring clang instead?</p>

---

## Post #28 by @hjmjohnson (2019-06-10 13:49 UTC)

<p>Xcode is only Clang by default (and has been for many years now).</p>
<p>Gcc is not distributed with MacOSX directly.  You need to install it using homebrew (or other approaches).</p>

---

## Post #29 by @bpaniagua (2019-06-10 14:53 UTC)

<p>Gotcha. Also, it worked like a charm.<br>
Thanks!</p>

---

## Post #30 by @priya.vada4 (2019-08-19 18:18 UTC)

<p>Hi</p>
<p>I seem to be running into a problem building Slicer on Mojave. Slicer builds without any errors but when I try to run it, I get the following error:</p>
<pre><code>dyld: malformed mach-o: load commands size (34376) &gt; 32768

2019-08-19 14:11:49.981 Slicer[92126:1188397] *** WARNING: Method userSpaceScaleFactor in class NSView is deprecated on 10.7 and later. It should not be used in new applications. Use convertRectToBacking: instead.

error: [/Users/Priya/Project/Slicer-latest/Slicer-Superbuild-Debug/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer] exit abnormally - Report the problem.
</code></pre>
<p>Is there any log file created to investigate the problem? Details of build as follows:</p>
<p>Qt version: Tried 5.11 and 5.13 - same problem exists<br>
Mac OS: 10.14.6</p>
<p>Priya</p>

---

## Post #31 by @lassoan (2019-08-19 19:21 UTC)

<p>There is a limit on total number and length of paths in a build project (reasons and limits vary on different operating systems and compilers). To avoid such issues we use short path for source and build directories.</p>

---

## Post #32 by @Samuel_Gerber (2020-05-19 12:46 UTC)

<p>Which version of QT should be used?</p>
<p>In the instructions there appear three:<br>
For building Slicer: download and execute <a href="https://download.qt.io/official_releases/online_installers/qt-unified-mac-x64-online.dmg" rel="nofollow noopener">qt-unified-mac-x64-online.dmg</a>, install Qt 5.10</p>
<ul>
<li>Install Qt 5.11.2 using <a href="http://download.qt.io/official_releases/online_installers/qt-unified-mac-x64-online.dmg" rel="nofollow noopener">Qt Online Installer for macOS</a>
</li>
<li>Build qt from homebrew<br>
brew install qt ccmake -DCMAKE_OSX_DEPLOYMENT_TARGET=10.14 -DQt5_DIR=/usr/local//Cellar/qt/5.13.2/lib/cmake/Qt5 ~/slicer/latest/Slicer</li>
</ul>

---

## Post #33 by @jamesobutler (2020-05-19 13:32 UTC)

<p>You can find out if a specific version is working by getting the version of Qt used in the current Slicer nightly for macOS.  Open Slicer and in the python interactor run</p>
<pre><code class="lang-python">qt.qVersion()
</code></pre>
<p>This is currently version 5.10.0 on macOS.  Then generally anything on the same line of 5.10.x is likely to work while anything newer than 5.10 is something experimental and you will have to try on your own.</p>

---

## Post #34 by @pieper (2020-05-19 13:44 UTC)

<p>I use 5.14.1 from homebrew on my mac builds and it’s fine.</p>

---
