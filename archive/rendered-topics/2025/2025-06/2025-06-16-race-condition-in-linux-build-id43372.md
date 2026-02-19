---
topic_id: 43372
title: "Race Condition In Linux Build"
date: 2025-06-16
url: https://discourse.slicer.org/t/43372
---

# Race condition in linux build

**Topic ID**: 43372
**Date**: 2025-06-16
**URL**: https://discourse.slicer.org/t/race-condition-in-linux-build/43372

---

## Post #1 by @pieper (2025-06-16 19:18 UTC)

<p>Building fresh with yesterday’s git checkout on a Ubuntu 24.04 machine I got the following repeatably with <code>make -j8</code>.  However when I tried to narrow it down with plain <code>make</code> the build succeeded and the program runs fine.  I’m guessing this is some kind of race condition because the Transforms module depends on Markups?</p>
<p>Does it happen on for others?  My mac builds from a few days ago are fine (using June 2 checkout so with python3.12).</p>
<pre><code class="lang-auto">...
[ 24%] Built target vtkSlicerAnnotationsModuleMRMLHierarchy
[ 24%] For vtkSlicerTransformsModuleLogic - updating vtkSlicerTransformsModuleLogicHierarchy.txt
[ 24%] Generating Python wrapper sources for vtkMRMLSceneViewNode
vtkWrapHierarchy: couldn't open file /media/share/tms-work/slicer/Slicer-superbuild/Slicer-build/vtkSlicerMarkupsModuleMRMLHierarchy.txt
make[5]: *** [Modules/Loadable/Transforms/Logic/CMakeFiles/vtkSlicerTransformsModuleLogicHierarchy.dir/build.make:77: Modules/Loadable/Transforms/Logic/vtkSlicerTransformsModuleLogicHierarchy.stamp.txt] Error 1
make[4]: *** [CMakeFiles/Makefile2:8746: Modules/Loadable/Transforms/Logic/CMakeFiles/vtkSlicerTransformsModuleLogicHierarchy.dir/all] Error 2
make[4]: *** Waiting for unfinished jobs....
[ 24%] Generating Python wrapper sources for vtkMRMLSceneViewStorageNode
[ 24%] Generating Python wrapper sources for vtkMRMLScriptedModuleNode
...
</code></pre>

---

## Post #2 by @RafaelPalomar (2025-06-16 19:55 UTC)

<p>Hello <a class="mention" href="/u/pieper">@pieper</a>. I’ve never experienced anything like this. Have you tried Ninja? I can give a try in Ubuntu 25.04 tomorrow.</p>

---

## Post #3 by @pieper (2025-06-16 20:00 UTC)

<p>Thanks for checking.  No, I haven’t tried ninja for this.</p>
<p>Looks like the preview build failed last night with some github glitch.  I’m able to download the file that it says it couldn’t.  So maybe tomorrow we’ll see what the dashboard shows.  I believe it uses <code>make</code>.</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=3830826">https://slicer.cdash.org/viewBuildError.php?buildid=3830826</a></p>

---

## Post #4 by @jcfr (2025-06-16 20:07 UTC)

<p>I am wondering if this is a side effect of:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/8464">PR-8464</a>: <code>COMP: Move vtkSlicerCLIModuleLogic from Base/QTCLI to Base/Logic</code></li>
<li><a href="https://github.com/Slicer/Slicer/pull/8475">PR-8475</a>: <code>COMP: Fix macOS build removing obsolete VTK wrapping of qSlicerBaseQTCLI</code></li>
</ul>
<hr>
<p>The Linux (‘metroplex’) factory uses ninja<sup class="footnote-ref"><a href="#footnote-126035-1" id="footnote-ref-126035-1">[1]</a></sup>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd1c9ee6c59022f5662801a45f03d5e316590beb.png" data-download-href="/uploads/short-url/qYXyOpkvjRkEAOl22zo95sShjmP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd1c9ee6c59022f5662801a45f03d5e316590beb_2_517x161.png" alt="image" data-base62-sha1="qYXyOpkvjRkEAOl22zo95sShjmP" width="517" height="161" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd1c9ee6c59022f5662801a45f03d5e316590beb_2_517x161.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd1c9ee6c59022f5662801a45f03d5e316590beb_2_775x241.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd1c9ee6c59022f5662801a45f03d5e316590beb_2_1034x322.png 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1678×523 42.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-126035-1" class="footnote-item"><p><a href="https://github.com/Slicer/DashboardScripts/blob/091a5e2b6571b34b412de6e92baa6927199dda9d/metroplex-slicer_preview_nightly.cmake#L20">https://github.com/Slicer/DashboardScripts/blob/091a5e2b6571b34b412de6e92baa6927199dda9d/metroplex-slicer_preview_nightly.cmake#L20</a> <a href="#footnote-ref-126035-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #5 by @pieper (2025-06-16 20:27 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>.  Yes, it could be related to moving the logic code, but the error message looks like it comes from the wrapping, so I’m not sure.</p>
<p>If everything works with ninja maybe we should make it the default and update the documentation suggesting not to use make.  I know some people like to say that if it’s not tested it’s probably broken, so having our instructions match our testing might simplify our lives.</p>
<p>I’m trying a ninja build now to see what happens.</p>

---

## Post #6 by @chir.set (2025-06-16 20:30 UTC)

<p>I did a clean build today on Arch Linux with <code>make -j24</code> and it completed in a single step.</p>

---

## Post #7 by @jcfr (2025-06-16 20:36 UTC)

<p>Transitioning to  <code>Ninja</code>  as our default  CMake generator  on Linux would require more work as <code>Unix Makefiles</code> is currently used as the default<sup class="footnote-ref"><a href="#footnote-126040-1" id="footnote-ref-126040-1">[1]</a></sup> one for building all extensions.</p>
<p>The fact <code>Ninja</code> is used was done out of convenience to easily <em>split</em><sup class="footnote-ref"><a href="#footnote-126040-2" id="footnote-ref-126040-2">[2]</a></sup> the build-system to allow support continuous integration without having to rebuild everything.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-126040-1" class="footnote-item"><p><a href="https://github.com/Slicer/DashboardScripts/blob/091a5e2b6571b34b412de6e92baa6927199dda9d/metroplex-slicerextensions_preview_nightly.cmake#L18">https://github.com/Slicer/DashboardScripts/blob/091a5e2b6571b34b412de6e92baa6927199dda9d/metroplex-slicerextensions_preview_nightly.cmake#L18</a> <a href="#footnote-ref-126040-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-126040-2" class="footnote-item"><p><a href="https://github.com/Slicer/SlicerDocker/blob/a66255f354cace3511a1a1c5047c398f2f605233/slicer-base/Dockerfile#L30-L33">https://github.com/Slicer/SlicerDocker/blob/a66255f354cace3511a1a1c5047c398f2f605233/slicer-base/Dockerfile#L30-L33</a> <a href="#footnote-ref-126040-2" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #8 by @pieper (2025-06-16 22:29 UTC)

<p>My build with ninja worked with no problem, of course so do some <code>make</code> builds, so it’s hard to know for sure.  I guess we’ll just need to keep our eye open for it.</p>

---
