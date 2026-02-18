# RFC: Branch clipper module

**Topic ID**: 27234
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/rfc-branch-clipper-module/27234

---

## Post #1 by @chir.set (2023-01-13 20:18 UTC)

<p><span class="mention">@coredevs</span> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I hereby draw your attention to ‘<a href="https://github.com/chir-set/ToolX/tree/master/BranchClipper" rel="noopener nofollow ugc">Branch clipper</a>’ module newly written in C++.</p>
<p>It splits a bifurcated vascular segmentation using its centerline model as produced by ‘Extract centerline’ module.</p>
<p>I believe that its logical home is the SlicerVMTK extension. The single problem is that VMTK is compiled in SlicerVMTK targeting Python development only, and is not C++ friendly. I <em>suppose</em> that VMTK there could be built for development in both languages, but I could not find a nice way to do that for C++. So ‘Branch clipper’ builds against an independent VMTK build. As such, it can’t be integrated in SlicerVMTK.</p>
<p>‘Branch clipper’ can also be rewritten in Python. I’m ready to do that, being left with an uneasy feeling of “VMTK in SlicerVMTK is good for Python, bad for C++ !”. It would of course take time.</p>
<p>I wish to know :</p>
<ul>
<li>Would ‘Branch clipper’ module be welcome in SlicerVMTK?</li>
<li>Is there any chance that VMTK in SlicerVMTK may become friendly for C++ development, even on some remote day?</li>
<li>Would splitting SlicerVMTK into SlicerVMTKLibs and SlicerVMTK be a thinkable option? SlicerVMTKLibs would here provide VMTK libraries only, fit for both Python and C++, while SlicerVMTK would be another extension interacting with SlicerVMTKLibs. (Just a question; and I don’t have sufficient cmake skills to do that.)</li>
</ul>
<p>Thank your for any comments.</p>
<p>Regards.</p>

---

## Post #2 by @pieper (2023-01-13 21:07 UTC)

<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a> that looks really useful and would be great to include.</p>
<p>I think the idea of extensions in C++ being linked to other C++ extensions is a hard problem in general but not unsolvable.  Setting up SlicerVMTK has always been one of the more complex extensions since it has both VTK and ITK classes.</p>
<p>Would it make sense to contribute your features to VMTK upstream?  That might simplify the build process.</p>

---

## Post #3 by @chir.set (2023-01-13 21:55 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="27234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Would it make sense to contribute your features to VMTK upstream?</p>
</blockquote>
</aside>
<p>VMTK already provides vmtkbranchclipper.py, which is the basis for the proposed module. It’s designed for PypeS (which is quite foreign to me). The purpose of ‘Branch clipper’ is to do same in Slicer. It’s doubtful that VMTK devs would create a dependency on Slicer.</p>

---

## Post #4 by @pieper (2023-01-13 22:10 UTC)

<p>I see, thanks for the info.  No, of course we don’t want a circular dependency with VMTK depending on SlicerVMTK or Slicer.  What I meant to say is can’t you add your code to SlicerVMTK.</p>

---

## Post #5 by @lassoan (2023-01-14 03:00 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="27234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I think the idea of extensions in C++ being linked to other C++ extensions is a hard problem in general but not unsolvable</p>
</blockquote>
</aside>
<p>There are several extensions that has C++ modules that uses on C++ modules (module logics, MRML classes, etc) of another extension. When you first do this it is probably not trivial, but I don’t think there is anything very special about it - it all works very similarly as using any other external project in CMake (you specify <code>&lt;external_package&gt;_DIR</code> as CMake variable and use <code>find_package()</code> in the CMakeLists.txt file of the project to get targets, include files, etc. from the external project).</p>
<p>See for example [PathReconstruction extension(<a href="https://github.com/SlicerIGT/SlicerPathReconstruction" class="inline-onebox">GitHub - SlicerIGT/SlicerPathReconstruction: This is an extension for 3D Slicer. The module allows creation of catheter models from electromagnetic spatial tracking.</a>) using <a href="https://github.com/SlicerIGT/SlicerIGT">SlicerIGT extension</a> using SlicerIGSIO extension modules - all in C++.</p>
<p>If you get stuck at any point then post the error message and we will help with figuring out the solution.</p>
<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="27234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>VMTK already provides vmtkbranchclipper.py, which is the basis for the proposed module. It’s designed for PypeS (which is quite foreign to me)</p>
</blockquote>
</aside>
<p>“PypeS” is just a set of helper functions to make it easier to implement command-line scripts in Python. Those people who learn how to use it like it. However, I don’t like it because it makes the code more opaque, non-standard, unfamiliar - or as you put it “foreign”. It is foreign to everyone but the few VMTK developers who originally developed it and those few people who actually learned how to use it. I just refuse to learn how to use them because that would mean I would need to use shell scripting to use VMTK, and I much prefer Python scripting.</p>
<p>I just use these PypeS scripts as examples by copying the contents of their <code>Execute</code> method, use the <code>__init__</code> method as documentation.</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="27234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>What I meant to say is can’t you add your code to SlicerVMTK.</p>
</blockquote>
</aside>
<p>I agree, that would be the appropriate place. The same was as we did for vessel enhancement and centerline extraction modules.</p>

---

## Post #6 by @chir.set (2023-01-14 10:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="27234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The same was as we did for vessel enhancement and centerline extraction modules.</p>
</blockquote>
</aside>
<p>These are Python projects, vtkvmtk libraries are searched for and used at runtime only, at least that’s what I understand.</p>
<p>Consider these steps :</p>
<ul>
<li>Try 1 ::</li>
<li>add BranchClipper directory to a SlicerVMTK source tree, and the corresponding add_subdirectory() instruction in CMakeLists.txt</li>
<li>configure setting Slicer_DIR only<br>
-build result is</li>
</ul>
<pre><code class="lang-auto">/home/arc/src/SlicerExtension-VMTK/BranchClipper/Logic/vtkSlicerBranchClipperLogic.cxx:32:10: fatal error: 'vtkvmtkPolyDataCenterlineGroupsClipper.h' file not found
#include &lt;vtkvmtkPolyDataCenterlineGroupsClipper.h&gt;
</code></pre>
<ul>
<li>Try2 ::</li>
<li>add BranchClipper directory to a SlicerVMTK source tree, and the corresponding add_subdirectory() instruction in CMakeLists.txt</li>
<li>add find_package(VMTK) in the CMakeLists.txt of BranchClipper</li>
<li>configure setting Slicer_DIR, and VMTK_DIR to a non existing VMTK-build directory that has not yet been created because VMTK is not built yet; the result is</li>
</ul>
<pre><code class="lang-auto">CMake Error at SuperBuild/External_VMTK.cmake:18 (message):
  VMTK_DIR [/home/user/tmp/Slicer/VMTKBranchClipper/VMTK-build] variable is
  defined but corresponds to nonexistent directory
Call Stack (most recent call first):
  /home/arc/src/Slicer/CMake/ExternalProjectDependency.cmake:844 (include)
  /home/arc/src/Slicer/CMake/ExternalProjectDependency.cmake:918 (ExternalProject_Include_Dependencies)
  SuperBuild.cmake:35 (ExternalProject_Include_Dependencies)
  CMakeLists.txt:35 (include)
</code></pre>
<p>How can we point to a non-built external project, and get its include directories, link directories and link libraries ?</p>

---

## Post #7 by @chir.set (2023-01-14 20:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="27234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you get stuck at any point then post the error message and we will help with figuring out the solution.</p>
</blockquote>
</aside>
<p>I could include BranchClipper, in fact the extension containing it, inside SlicerVMTK and get a successful build, in this <a href="https://github.com/chir-set/SlicerExtension-VMTK/tree/WithToolX_Experimental" rel="noopener nofollow ugc">branch</a>. It’s certainly not optimal.</p>
<p>There are 2 clear problems I could not resolve :</p>
<ol>
<li>packaging ignores BranchClipper</li>
<li>in a clean build, the first try will fail in BranchClipper while VMTK is being built.</li>
</ol>
<p>I’ll explore further the links you provided.</p>

---

## Post #8 by @lassoan (2023-01-14 21:24 UTC)

<p>Please send a pull request and I’ll fix it up.</p>

---

## Post #9 by @chir.set (2023-01-14 21:32 UTC)

<p>Here is the <a href="https://github.com/vmtk/SlicerExtension-VMTK/pull/71" rel="noopener nofollow ugc">PR</a>. Thanks.</p>

---

## Post #10 by @chir.set (2023-01-14 21:53 UTC)

<p>I just pushed a <a href="https://github.com/chir-set/SlicerExtension-VMTK/commit/0978d69f9e0202435f537699d509f365fab0551b" rel="noopener nofollow ugc">commit</a> that simplifies things and results in a fully packaged archive.</p>

---

## Post #11 by @chir.set (2023-01-14 22:04 UTC)

<p>Big deception. The module loads, and crashes on clicking the ‘Apply’ button. Running in lldb did not help.</p>
<pre><code class="lang-auto">Switch to module:  "BranchClipper"
Process 35038 exited with status = 127 (0x0000007f) 
(lldb) bt
error: invalid thread
</code></pre>

---

## Post #12 by @lassoan (2023-01-15 05:36 UTC)

<p>I’ve made a few small fixes and merged to the VMTK extension. Let us know how it works.</p>

---

## Post #13 by @chir.set (2023-01-15 10:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="27234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Let us know how it works.</p>
</blockquote>
</aside>
<p>It works perfectly well, thanks.</p>
<p>I think this <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/71eccd4837179457068cacbefc97ff310d660492/SuperBuild.cmake#L67" rel="noopener nofollow ugc">line</a> has done the magic of using VMTK_DIR downstream, very clean CMakeLists.txt files with this fix.</p>

---

## Post #14 by @gpu (2024-06-03 08:21 UTC)

<p>is there article or code to introduce the algorithm of the ‘branch clipper’?<br>
Thanks!<br>
It seems hard to clip 1 single branch while not clip the neighbor branches as the whole artery vascular is 1 big mesh with many levels of branches.</p>

---
