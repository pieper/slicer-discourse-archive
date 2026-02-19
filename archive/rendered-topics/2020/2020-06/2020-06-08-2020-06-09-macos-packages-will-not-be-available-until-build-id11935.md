---
topic_id: 11935
title: "2020 06 09 Macos Packages Will Not Be Available Until Build"
date: 2020-06-08
url: https://discourse.slicer.org/t/11935
---

# 2020.06.09: macOS packages will *not* be available until build machine is updated to macOS 10.13.6

**Topic ID**: 11935
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/2020-06-09-macos-packages-will-not-be-available-until-build-machine-is-updated-to-macos-10-13-6/11935

---

## Post #1 by @jcfr (2020-06-08 22:41 UTC)

<p>Tomorrow, we plan to initiate the update the build machine responsible to build:</p>
<ul>
<li>Slicer macOS application installer distributed on <a href="https://download.slicer.org">https://download.slicer.org</a></li>
<li>corresponding Slicer extensions</li>
</ul>
<h2><a name="p-41285-implications-for-users-1" class="anchor" href="#p-41285-implications-for-users-1" aria-label="Heading link"></a>Implications for users</h2>
<ul>
<li>Preview Slicer package and extensions may not be available for one or two days</li>
</ul>
<h2><a name="p-41285-implications-for-developers-2" class="anchor" href="#p-41285-implications-for-developers-2" aria-label="Heading link"></a>Implications for developers</h2>
<p>This should allow us to update the minimum deployment target to 10.13 and build against the latest version of Qt5. See <a href="https://github.com/Slicer/Slicer/pull/4940" class="inline-onebox">COMP: Update minimum required CMAKE_OSX_DEPLOYMENT_TARGET to 10.13 by jamesobutler · Pull Request #4940 · Slicer/Slicer · GitHub</a></p>
<p>cc: <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fbf3c22e3fbb515b190c6e543a89b6ba01a6e3d.png" data-download-href="/uploads/short-url/bntrdLte5jsQXcM4onpwZYTPLsx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fbf3c22e3fbb515b190c6e543a89b6ba01a6e3d_2_660x500.png" alt="image" data-base62-sha1="bntrdLte5jsQXcM4onpwZYTPLsx" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4fbf3c22e3fbb515b190c6e543a89b6ba01a6e3d_2_660x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fbf3c22e3fbb515b190c6e543a89b6ba01a6e3d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fbf3c22e3fbb515b190c6e543a89b6ba01a6e3d.png 2x" data-dominant-color="E2DDDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×578 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2020-06-09 23:43 UTC)

<p>Update: The upgrade process has been initiated. Thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---

## Post #3 by @jcfr (2020-06-10 00:57 UTC)

<p>The upgrade has been completed of both the firmware and the operating system have been completed <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=12" title=":tada:" class="emoji" alt=":tada:" loading="lazy" width="20" height="20">  (see below)</p>
<p>Next steps:</p>
<ul>
<li>Update XCode</li>
<li>Update Qt5 installation</li>
<li>Integrate <a href="https://github.com/Slicer/Slicer/pull/4940" class="inline-onebox">COMP: Update minimum required CMAKE_OSX_DEPLOYMENT_TARGET to 10.13 by jamesobutler · Pull Request #4940 · Slicer/Slicer · GitHub</a> and <a href="https://github.com/Slicer/DashboardScripts/pull/27" class="inline-onebox">factory-south-macos: Update nightly builds to use Qt 5.15.0 by jamesobutler · Pull Request #27 · Slicer/DashboardScripts · GitHub</a></li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae27df49efdf1da5382cfe83d3f51491b033e316.png" alt="image" data-base62-sha1="oQEvlUo5xXcL38SINrjmqgefS1o" width="551" height="225"></p>

---

## Post #4 by @jamesobutler (2020-06-10 01:26 UTC)

<p>It would also be good if you can update <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#Software" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory#Software</a></p>

---

## Post #5 by @jcfr (2020-06-12 16:28 UTC)

<p>I re-initiated the XCode update on the <code>factory-south-macos</code> build machine.</p>
<p>Once this is done I will start the Qt build using <a href="https://github.com/jcfr/qt-easy-build/tree/5.15.0">5.15.0</a> branch doing the following:</p>
<pre><code class="lang-auto">$ ./Build-qt.sh -s macosx10.14 -d 10.13 -j 4

[...]

This script will build Qt for Darwin system

QT_VERSION      : 5.15.0
OPENSSL_VERSION : 1.1.1d

[...]

Script options (macOS):

 -a OSX architectures ............................ x86_64
 -d OSX deployment target ........................ 10.13
 -s OSX sysroot .................................. macosx10.14

</code></pre>

---

## Post #6 by @jcfr (2020-06-12 16:41 UTC)

<p>It looks like the XCode update is incompatible <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd02e4728a4567851504c39f4afaef3482d5a52.png" data-download-href="/uploads/short-url/oEM9jeZJctsriYZqGDXDVcQ6hvY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd02e4728a4567851504c39f4afaef3482d5a52_2_690x97.png" alt="image" data-base62-sha1="oEM9jeZJctsriYZqGDXDVcQ6hvY" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/acd02e4728a4567851504c39f4afaef3482d5a52_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd02e4728a4567851504c39f4afaef3482d5a52.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd02e4728a4567851504c39f4afaef3482d5a52.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">824×117 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jcfr (2020-06-12 17:02 UTC)

<p>Now downloading XCode 10.1 from <a href="https://developer.apple.com/download/more/">https://developer.apple.com/download/more/</a></p>
<p>That seems to be the latest version supporting 10.13.6 (see <a href="https://developer.apple.com/documentation/xcode_release_notes/xcode_10_1_release_notes">here</a>)</p>
<p>Indeed, version 10.2 and beyond requires  macOS 10.14.3 or later  (see <a href="https://developer.apple.com/documentation/xcode_release_notes/xcode_10_2_release_notes">here</a>)</p>
<p>For the record, the version currently installed is:</p>
<pre><code class="lang-auto">/usr/bin/xcodebuild -version
Xcode 8.2.1
Build version 8C1002
</code></pre>

---

## Post #8 by @jcfr (2020-06-12 17:57 UTC)

<p>After downloading the file <code>Xcode_10.1.xip</code> it will be available in <code>~/Downloads</code>, then here are the steps:</p>
<ul>
<li>double-click on it from finder, it extracts to <code>Xcode.app</code></li>
<li><code>sudo mv /Application/Xcode.app /Applications/Xcode-8.2.1.app</code></li>
<li><code>sudo mv ~/Downloads/Xcode.app /Applications/</code></li>
</ul>
<p>Nest step is to download and install the command line tool:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69f6c618d10746d2e4f82f1c09a28f61fdbbe92d.png" alt="image" data-base62-sha1="f7oQnDLSqBQPflL08SjXuFMMthX" width="636" height="150"></p>
<p>Once the file is downloaded, double-click on the <code>.dmg</code> file, and then double click again on the <code>.pkg</code> file and following instructions.</p>
<p>After starting Xcode, you will be prompted with additional installation instructions.</p>
<p>XCode 10.1 is now installed:</p>
<pre><code class="lang-auto">$ /usr/bin/xcodebuild -version
Xcode 10.1
Build version 10B61

$ gcc --version 
Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
Apple LLVM version 10.0.0 (clang-1000.11.45.5)
Target: x86_64-apple-darwin17.7.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a22a8af39a3fc90d73a0321df47c669a377fd28.png" alt="image" data-base62-sha1="60KjefVl68TX5pDOjTxX0WczIU0" width="473" height="221"></p>

---

## Post #9 by @jcfr (2020-06-12 19:28 UTC)

<p>Qt5 build is moving along. I edited the instruction posted <a href="https://discourse.slicer.org/t/2020-06-09-macos-packages-will-not-be-available-until-build-machine-is-updated-to-macos-10-13-6/11935/5">above</a>. <code>macosx10.14</code> had to be specified as the SDK root (instead of <code>macosx10.13</code>)</p>

---

## Post #10 by @jcfr (2020-06-12 20:03 UTC)

<p>The corresponding dashboard script have also been updated.</p>
<p><strong>Note:</strong> Build of Slicer ‘Stable’ release extensions has been disabled on macOS</p>
<p>Assuming the Qt5 build completes, we should expect tonight Slicer preview build to complete without issues.</p>

---

## Post #11 by @jcfr (2020-06-15 18:30 UTC)

<p>It turns out that Qt has been built in the wrong directory which caused the regular build to fail.</p>
<p>Qt is now being rebuilt following these instructions:</p>
<pre><code class="lang-auto">cd /Volumes/Dashboards/Support
./qt-easy-build/Build-qt.sh -s macosx10.14 -d 10.13 -j 4
</code></pre>
<p>This will ensure the Qt will be available in the expected directory <code>/Volumes/Dashboards/Support/qt-everywhere-build-5.15.0</code></p>

---

## Post #12 by @jamesobutler (2020-06-15 19:44 UTC)

<p>I haven’t tried myself, but as of 5.14.0 Qt is relocatable. See <a href="https://www.qt.io/blog/qt-is-relocatable" rel="nofollow noopener">https://www.qt.io/blog/qt-is-relocatable</a></p>

---

## Post #13 by @jcfr (2020-06-15 20:34 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="12" data-topic="11935">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I haven’t tried myself, but as of 5.14.0 Qt is relocatable</p>
</blockquote>
</aside>
<p>Good to know. It turns out I deleted the previous directory and restarted the build.</p>

---

## Post #14 by @jcfr (2020-06-18 13:05 UTC)

<p>Updates:</p>
<ul>
<li>Qt 5.15 has been built on the factory</li>
<li>Slicer build failed with <code>malformed mach-o: load commands size</code> error.
<ul>
<li>A first attempt to address the problem was implemented in <a href="https://github.com/Slicer/DashboardScripts/commit/26a343d5670b97aac7b7d004f95041c6f6692231">Slicer/DashboardScripts@26a343</a> by changing the basename from <code>Slicer</code> to <code>S</code>.</li>
<li>With that change to number of failed tests went from  <code>77</code> to <code>44</code>
</li>
</ul>
</li>
</ul>
<p>Next steps:</p>
<ul>
<li>Update to use <code>P</code> instead of <code>Preview</code> and <code>S</code> instead of <code>Stable</code> to address remaining failures.</li>
</ul>
<p>Related posts:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/macos-sierra-10-12-6-dynamic-linker-errors/2339" class="inline-onebox">MacOS Sierra (10.12.6) dynamic linker errors</a></li>
<li><a href="https://discourse.slicer.org/t/building-on-mac-10-14-mojave/4554/30" class="inline-onebox">Building on Mac 10.14 Mojave</a></li>
</ul>

---

## Post #15 by @jcfr (2020-06-18 14:08 UTC)

<p>Updates:</p>
<ul>
<li>Dashboard script have been updated to use <code>P</code> instead of <code>Preview</code> and <code>S</code> instead of <code>Stable</code>. See <a href="https://github.com/Slicer/DashboardScripts/commit/e234e0154ae5becba26259148cb251ff605e69cb">Slicer/DashboardScripts@e234e01</a>
</li>
<li>Directory <code>/Volumes/Dashboards/Preview</code> has been deleted</li>
<li>Previous <code>macOS</code> entry has been deleted from <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">http://slicer.cdash.org/index.php?project=SlicerPreview</a>
</li>
<li>macOS build has been manually restarted</li>
</ul>

---

## Post #16 by @jcfr (2020-06-18 22:40 UTC)

<p>Updates:</p>
<ul>
<li>Reducing the path addressed some more issues there are remaining <code>malformed mach-o: load commands size</code> errors</li>
</ul>
<p>Next steps:</p>
<ul>
<li>Evaluate these options:
<ul>
<li>(1) Further reduce the path length  by renaming the volume from <code>/Volumes/Dashboards</code> to <code>/Volumes/D</code>
</li>
<li>(2) Look into adapting the <code>ld</code> wrapper developed to address similar issue in NixOS:
<ul>
<li>
<a href="https://github.com/NixOS/nixpkgs/pull/27536">https://github.com/NixOS/nixpkgs/pull/27536</a> and <a href="https://github.com/NixOS/nixpkgs/issues/22810">https://github.com/NixOS/nixpkgs/issues/22810</a>
</li>
<li><a href="https://github.com/NixOS/nixpkgs/blob/master/pkgs/build-support/bintools-wrapper/macos-sierra-reexport-hack.bash">https://github.com/NixOS/nixpkgs/blob/master/pkgs/build-support/bintools-wrapper/macos-sierra-reexport-hack.bash</a></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>I will probably go with option (1), this means we will have to rebuild Qt5, update cronjobs, …</p>
<p>We should look into (2) if we still have these issues after transitioning to the latest VTK, in this case we will have less libraries (no more <code>*PythonD.dylib</code>)</p>

---

## Post #17 by @jcfr (2020-06-19 00:26 UTC)

<p>Updates:</p>
<ul>
<li>Volume has been renamed from <code>Dashboards</code> to <code>D</code>
</li>
<li>Cronjobs updated</li>
<li>Misc python virtual env recreated</li>
<li>Dashboard scripts updated (see <a href="https://github.com/Slicer/DashboardScripts/commit/2e56a8b97b681b0e8d3a596b92f9de7cfb3194ae">Slicer/DashboardScripts@2e56a8b</a>)</li>
<li>Qt5 build in progress</li>
</ul>
<p><img src="https://emoji.discourse-cdn.com/twitter/crossed_fingers.png?v=9" title=":crossed_fingers:" class="emoji" alt=":crossed_fingers:"> If the timing is right, and we forgot nothing … tomorrow build should look better !</p>

---

## Post #18 by @jcfr (2020-06-20 02:48 UTC)

<p>Updates:</p>
<ul>
<li>There are no more <code>malformed mach-o: load commands size</code> error <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">
</li>
<li>Remaining errors are related to OpenSSL issues, these will be addressed in <a href="https://github.com/Slicer/Slicer/pull/4992">https://github.com/Slicer/Slicer/pull/4992</a>
</li>
</ul>

---
