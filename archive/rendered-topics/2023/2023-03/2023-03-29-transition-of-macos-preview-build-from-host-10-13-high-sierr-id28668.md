# Transition of macOS Preview build from host 10.13 (High Sierra) to 13 (Ventura)

**Topic ID**: 28668
**Date**: 2023-03-29
**URL**: https://discourse.slicer.org/t/transition-of-macos-preview-build-from-host-10-13-high-sierra-to-13-ventura/28668

---

## Post #1 by @jcfr (2023-03-29 23:13 UTC)

<p>In the next few days, we will transition the Slicer preview build for application and extensions from  <code>factory-south-macos</code> (10.13 / High Sierra) to <code>computron</code> (13 / Ventura).</p>
<h3><a name="p-92832-implications-for-users-1" class="anchor" href="#p-92832-implications-for-users-1" aria-label="Heading link"></a>Implications for users</h3>
<p>Our deployment target will change from <code>10.13</code> (High Sierra) to <code>11</code> (Big Sur).</p>
<h3><a name="p-92832-implications-for-developers-2" class="anchor" href="#p-92832-implications-for-developers-2" aria-label="Heading link"></a>Implications for developers</h3>
<h4><a name="p-92832-updates-3" class="anchor" href="#p-92832-updates-3" aria-label="Heading link"></a>Updates</h4>
<p>The following pull-requests describe the changes for both <code>Slicer</code> and associated <code>DashboardScripts</code>:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/6695">https://github.com/Slicer/Slicer/pull/6695</a></li>
<li><a href="https://github.com/Slicer/DashboardScripts/pull/53">https://github.com/Slicer/DashboardScripts/pull/53</a></li>
</ul>
<h4><a name="p-92832-qt-5-4" class="anchor" href="#p-92832-qt-5-4" aria-label="Heading link"></a>Qt 5</h4>
<p>To support packaging either Slicer or Slicer-based application, at least Qt 5.15.8 (with QtWebEngine 5.15.12) is required.</p>
<p>Waiting we have more detailed instructions, see <a href="https://github.com/Slicer/DashboardScripts/pull/53#issuecomment-1384355365">here</a></p>
<h4><a name="p-92832-qt-6-5" class="anchor" href="#p-92832-qt-6-5" aria-label="Heading link"></a>Qt 6</h4>
<p>This is a required step toward supporting Qt6.</p>
<h3><a name="p-92832-next-6" class="anchor" href="#p-92832-next-6" aria-label="Heading link"></a>Next</h3>
<ul>
<li>Finalize update of <code>Build instructions / macOS / Prerequisites</code> section in the developer guide.</li>
<li>Merge pull-requests referenced above</li>
</ul>
<h3><a name="p-92832-related-posts-7" class="anchor" href="#p-92832-related-posts-7" aria-label="Heading link"></a>Related posts</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/2020-06-09-macos-packages-will-not-be-available-until-build-machine-is-updated-to-macos-10-13-6/11935" class="inline-onebox">2020.06.09: macOS packages will *not* be available until build machine is updated to macOS 10.13.6</a></li>
</ul>
<p>cc: <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---

## Post #2 by @jcfr (2023-03-31 02:21 UTC)

<p>After confirming that Slicer could be packaged and installed, the corresponding pull-requests have been merged.</p>
<p><span data-date="2023-03-31" class="discourse-local-date" data-timezone="America/New_York" data-email-preview="2023-03-31T04:00:00Z UTC">2023-03-31T04:00:00Z</span> packages for the <strong>Preview</strong> builds are expected to be completed on  <code>computron</code>.</p>
<p>Here is a summary of the environment changes:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td>hostname</td>
<td><code>factory-south-macos</code></td>
<td><code>computron</code></td>
</tr>
<tr>
<td>macOS version</td>
<td>10.13 (High Sierra)</td>
<td>13 (Ventura)</td>
</tr>
<tr>
<td>deployment target</td>
<td>10.13</td>
<td>11</td>
</tr>
<tr>
<td>Apple clang version</td>
<td>10.0</td>
<td>14.0</td>
</tr>
<tr>
<td>Qt version</td>
<td>5.15.2</td>
<td>5.15.8 (+ with qtwebengine 5.15.12-lts)</td>
</tr>
</tbody>
</table>
</div><p>Thanks to</p>
<ul>
<li>
<a class="mention" href="/u/jamesobutler">@jamesobutler</a> for the help updating the build-system &amp; documentation. <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20">
</li>
<li>
<a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, <a class="mention" href="/u/pieper">@pieper</a>  and <a class="mention" href="/u/jamesobutler">@jamesobutler</a> for the help testing the package. <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=12" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20">
</li>
</ul>
<p>Systems used for testing:</p>
<ul>
<li>2019 mac pro running macOS Ventura 13.2.1</li>
<li>Mid-2014 MacBook Pro running macOS Big Sur 11.7.1</li>
<li>Mac mini (2018)  running macOS Ventura</li>
</ul>

---

## Post #3 by @jcfr (2023-03-31 16:07 UTC)

<p>To tentatively address a non-reproducible segfault associated with <code>clang</code> compiler, the build was just restarted after installing an updated version.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td>Clang version</td>
<td>10.0</td>
<td><s>14.0.0</s> 14.0.6</td>
</tr>
</tbody>
</table>
</div><p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab85f844d839935113e16c5ba088b37cde508eea.png" data-download-href="/uploads/short-url/otmFW9XxYGkFCz9X6AewfaKTeoW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab85f844d839935113e16c5ba088b37cde508eea_2_690x27.png" alt="image" data-base62-sha1="otmFW9XxYGkFCz9X6AewfaKTeoW" width="690" height="27" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab85f844d839935113e16c5ba088b37cde508eea_2_690x27.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab85f844d839935113e16c5ba088b37cde508eea_2_1035x40.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab85f844d839935113e16c5ba088b37cde508eea_2_1380x54.png 2x" data-dominant-color="D1D7CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3640×143 57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-92919-details-1" class="anchor" href="#p-92919-details-1" aria-label="Heading link"></a>Details</h3>
<p><em>Text below copied from pull-request <a href="https://github.com/Slicer/DashboardScripts/pull/57">Slicer/DashboardScripts#/57</a> description</em></p>
<p>This updates was motivated after observing a clang <code>EXC_BAD_ACCESS</code> error that is not consistently reproducible.</p>
<p>Here are some of the observed occurrences of <code>Error while  building C++ object file</code>:</p>
<ol>
<li><code>CMakeFiles/PythonQt.dir/generated_cpp_511/com_trolltech_qt_gui/com_trolltech_qt_gui0.cpp.o</code></li>
<li><code>CMakeFiles/dcmect_tests.dir/t_roundtrip.cc.o</code></li>
<li><code>Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKBinaryMathematicalMorphology.dir/sitkBinaryDilateImageFilter.cxx.o</code></li>
<li><code>Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKCommon.dir/sitkCastImageFilter-2v.cxx.o</code></li>
<li><code>Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKConnectedComponents.dir/sitkConnectedComponentImageFilter.cxx.o</code></li>
<li><code>Code/BasicFilters/src/CMakeFiles/SimpleITK_ITKConvolution.dir/sitkFFTNormalizedCorrelationImageFilter.cxx.o</code></li>
</ol>
<p>These errors did not all happen in the same build. In the case listed above:</p>
<ul>
<li>(1) and (2) were two different clean build</li>
<li>(3), (4), (5) and (6) were reported in the same build</li>
</ul>
<h3><a name="p-92919-segfault-2" class="anchor" href="#p-92919-segfault-2" aria-label="Heading link"></a>Segfault</h3>
<p>In all cases, the message reported was similar to the copied below and attempt to re-run the associated sh script (e.g <code>com_trolltech_qt_gui0-17dcc3.sh</code>) did not lead to a segfault.</p>
<blockquote>
<pre><code class="lang-auto">clang: error: unable to execute command: Segmentation fault: 11
clang: error: clang frontend command failed due to signal (use -v to see invocation)
Apple clang version 14.0.0 (clang-1400.0.29.202)
Target: x86_64-apple-darwin22.2.0
Thread model: posix
InstalledDir: /Applications/Xcode-14.2.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
[CTest: warning matched] clang: note: diagnostic msg:
********************

PLEASE ATTACH THE FOLLOWING FILES TO THE BUG REPORT:
Preprocessed source(s) and associated run script(s) are located at:
[CTest: warning matched] clang: note: diagnostic msg: /var/folders/sh/x1zm1krn56j808c00cbtr2900000gp/T/com_trolltech_qt_gui0-17dcc3.cpp
[CTest: warning matched] clang: note: diagnostic msg: /var/folders/sh/x1zm1krn56j808c00cbtr2900000gp/T/com_trolltech_qt_gui0-17dcc3.sh
[CTest: warning matched] clang: note: diagnostic msg: Crash backtrace is located in
[CTest: warning matched] clang: note: diagnostic msg: /Users/svc-dashboard/Library/Logs/DiagnosticReports/clang_&lt;YYYY-MM-DD-HHMMSS&gt;_&lt;hostname&gt;.crash
[CTest: warning matched] clang: note: diagnostic msg: (choose the .crash file that corresponds to your crash)
[CTest: warning matched] clang: note: diagnostic msg:
********************
</code></pre>
</blockquote>
<h3><a name="p-92919-step-to-install-clang-1406-3" class="anchor" href="#p-92919-step-to-install-clang-1406-3" aria-label="Heading link"></a>Step to install clang 14.0.6</h3>
<p>Step to install the compiler were the following:</p>
<pre><code class="lang-auto">cd /D/Support
curl -#LO https://github.com/llvm/llvm-project/releases/download/llvmorg-14.0.6/clang+llvm-14.0.6-x86_64-apple-darwin.tar.xz
tar -xzvf clang+llvm-14.0.6-x86_64-apple-darwin.tar.xz
</code></pre>
<p>Installed version is</p>
<pre><code class="lang-auto">cd /D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/bin/
./clang --version
clang version 14.0.6 (https://github.com/tru/llvm-release-build 686807a176470032c208f27da2cc31b1c10777c6)
Target: x86_64-apple-darwin22.2.0
Thread model: posix
InstalledDir: /D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/bin
</code></pre>
<h3><a name="p-92919-release-notes-for-clang-140x-4" class="anchor" href="#p-92919-release-notes-for-clang-140x-4" aria-label="Heading link"></a>Release notes for clang 14.0.x</h3>
<div class="md-table">
<table>
<thead>
<tr>
<th>Date</th>
<th>Version</th>
<th>Release Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>24 Jun 2022</td>
<td>14.0.6</td>
<td><a href="https://discourse.llvm.org/t/llvm-14-0-6-release/63431">release notes</a></td>
</tr>
<tr>
<td>10 Jun 2022</td>
<td>14.0.5</td>
<td><a href="https://discourse.llvm.org/t/llvm-14-0-5-release/63118">release notes</a></td>
</tr>
<tr>
<td>24 May 2022</td>
<td>14.0.4</td>
<td><a href="https://discourse.llvm.org/t/llvm-14-0-4-release/62751">release notes</a></td>
</tr>
<tr>
<td>29 Apr 2022</td>
<td>14.0.3</td>
<td><a href="https://discourse.llvm.org/t/llvm-14-0-3-release/62133">release notes</a></td>
</tr>
<tr>
<td>26 Apr 2022</td>
<td>14.0.2</td>
<td><a href="https://discourse.llvm.org/t/llvm-14-0-2-release/62065">release notes</a></td>
</tr>
<tr>
<td>12 Apr 2022</td>
<td>14.0.1</td>
<td><a href="https://discourse.llvm.org/t/llvm-14-0-1-release/61700">release notes</a></td>
</tr>
<tr>
<td>25 Mar 2022</td>
<td>14.0.0</td>
<td><a href="https://releases.llvm.org/14.0.0/tools/clang/docs/ReleaseNotes.html">release notes</a></td>
</tr>
</tbody>
</table>
</div>

---
