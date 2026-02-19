---
topic_id: 1693
title: "Are Vs2015 Builds More Verbose"
date: 2017-12-20
url: https://discourse.slicer.org/t/1693
---

# Are VS2015 builds more verbose?

**Topic ID**: 1693
**Date**: 2017-12-20
**URL**: https://discourse.slicer.org/t/are-vs2015-builds-more-verbose/1693

---

## Post #1 by @ihnorton (2017-12-20 21:40 UTC)

<p>This is admittedly very anecdotal, but I’m curious if the Visual Studio 2015 (+Qt5, CMake 3.9.4) builds are known to be somewhat slower and much chattier than VS2013. For one example, while doing a build of the Slicer target within the superbuild solution (“Slicer” specifically, not of superbuild ALL), I get many lines like below for various other superbuild targets/sub-targets:</p>
<pre><code class="lang-auto">InitializeBuildStatus:
34&gt;    Creating "x64\Debug\ITKTransform-all\ITKTransform-all.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
34&gt;  CustomBuild:
34&gt;    All outputs are up-to-date.
34&gt;  FinalizeBuildStatus:
34&gt;    Deleting file "x64\Debug\ITKTransform-all\ITKTransform-all.tlog\unsuccessfulbuild".
34&gt;    Touching "x64\Debug\ITKTransform-all\ITKTransform-all.tlog\ITKTransform-all.lastbuildstate".
</code></pre>
<p>This whole thing appears to be effectively a no-op, but we end up with multiple shell-outs to cmake.exe and file i/o operations each time (similar message shows up at least 400 times in the build I’m currently updating, with no ITK compilation actually done).</p>

---

## Post #2 by @dzenanz (2017-12-20 22:16 UTC)

<p>I started an almost clean build of Slicer yesterday (VS2015, Qt5, CMake 3.10.1) in release mode, and it didn’t finish overnight. I had testing enabled (how foolish of me), but I kept ITK, VTK, CTK and DCMTK source, prefix and build directories from previous builds. I ended up cancelling the build, and opening the inner-build’s <code>Slicer.sln</code> and building that (so the rest of build would be parallelized).</p>

---
