# Build Slicer with custom VTK

**Topic ID**: 5552
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/build-slicer-with-custom-vtk/5552

---

## Post #1 by @drouin-simon (2019-01-29 02:53 UTC)

<p>Hi all,</p>
<p>I am developing a new feature in the VolumeRendering module which involves some changes in VTK and I’m looking for the simplest way to build Slicer in that context.</p>
<p>My first instinct was to super-build Slicer, go to the VTK directory and checkout my own branch of VTK (which is ahead of the gitlab kitware vtk by a few commits) and rebuild only VTK, then Slicer. However, it seems the CMake cache of both VTKs is not compatible. The problem could be caused by the introduction of the new module system in VTK which I believe happened between the Slicer head and the gitlab.kitware head.</p>
<p>What is the easiest way to build my own VTK to be compatible with Slicer. There are quite a lot of parameters set in SuperBuild/External_VTK.cmake. Are they all needed? Is there a shortcut that would save me some time? What are your tricks? <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @jcfr (2019-01-29 03:35 UTC)

<p>For any external  project, you can pass the options:</p>
<ul>
<li><code>Slicer_${proj}_GIT_REPOSITORY</code></li>
<li><code>Slicer_${proj}_GIT_TAG</code></li>
</ul>
<p>For VTK, you can configure Slicer passing:</p>
<ul>
<li><code>-DSlicer_VTK_GIT_REPOSITORY:STRING=https://... -DSlicer_VTK_GIT_TAG:STRING=origin/your-topic</code></li>
</ul>
<p>That said, considering VTK updated its build system in a backward incompatible way, it may not word as smoothly as you would expect …</p>

---

## Post #3 by @pieper (2019-01-29 08:04 UTC)

<p>Yes, unfortunately it may take a while to adapt Slicer to VTK’s new module system.  In the mean time it’s probably easier to maintain your patches in a fork of <a href="http://github.com/Slicer/VTK" rel="nofollow noopener">github.com/Slicer/VTK</a> (and point your superbuild there) using the parameters Jc described.</p>

---

## Post #4 by @drouin-simon (2019-01-29 13:44 UTC)

<p>Sounds good. I can backport the changes I made to VTK into a fork of the <a href="http://github.com/Slicer/VTK" rel="nofollow noopener">github.com/Slicer/VTK</a> repository to continue working.</p>
<p>But, what is the best course of action to propagate the changes forward? I’ve already submitted a merge request to VTK. Should I keep pushing them to merge it right away? Or should I try to merge the changes in <a href="http://github.com/Slicer/VTK" rel="nofollow noopener">github.com/Slicer/VTK</a> and then someone else will take care of merging this back to the official VTK?</p>

---

## Post #5 by @jcfr (2019-01-29 15:16 UTC)

<p>Ultimately you should make sure the changes are integrated in VTK proper , then we can easily backport into Slicer.</p>

---
