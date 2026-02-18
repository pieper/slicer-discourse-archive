# How can we avoid removing all VTK directories when updating slicer

**Topic ID**: 1840
**Date**: 2018-01-15
**URL**: https://discourse.slicer.org/t/how-can-we-avoid-removing-all-vtk-directories-when-updating-slicer/1840

---

## Post #1 by @ihnorton (2018-01-15 02:08 UTC)

<p>(<a class="mention" href="/u/chir.set">@chir.set</a> asked the following in <a href="https://discourse.slicer.org/t/commit-69e26835e-would-burn-my-discrete-gpu/1839" class="inline-onebox">Commit 69e26835e would burn my discrete GPU!</a>)</p>
<blockquote>
<p>Secondly, I need your advice for another issue.</p>
<p>Every time I run 'git checkout ', I must remove completely VTKv9{,-build,-prefix} directories to have a successful build. Else, there are errors like :</p>
<p>make[5]: *** No rule to make target ‘/home/arc/src/Slicer-SuperBuild/VTKv9/Common/Core/vtkAngularPeriodicDataArray.h’, needed by ‘Wrapping/Python/vtkAngularPeriodicDataArrayPython.cxx’. Stop.</p>
<p>Here, it’s vtkAngularPeriodicDataArray.h, but it can be any other file in a similar complaint.</p>
<p>How can we avoid removing all VTK directories whenever we checkout a commit ? It’s quite a big download. Even if I unpack a saved VTKv9 directory from a previously failed build, its contents get cleared and pulled from git again.</p>
<p>Thank you.</p>
</blockquote>

---

## Post #2 by @ihnorton (2018-01-15 02:20 UTC)

<p>It should never be necessary to delete the VTKv9 git directory, – in the off chance the source git directory is left in a transient state by the build system, you can run a hard git reset to clean it up and avoid re-downloading that.</p>
<p>However, rebuilds are also time-consuming… The -build or -prefix directories should almost never need to be deleted. However, the error you listed could be caused by an out-of-sync superbuild after major changes, so if it happens again, try re-running cmake in the superbuild directory (one level above <code>Slicer-build</code>) – <code>cmake .</code> should do the trick at command line, or click <code>Generate</code> in the GUi.</p>

---

## Post #3 by @chir.set (2018-01-15 08:46 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="1840">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>you can run a hard git reset to clean it up and avoid re-downloading that</p>
</blockquote>
</aside>
<p>That did the trick, thanks.</p>

---
