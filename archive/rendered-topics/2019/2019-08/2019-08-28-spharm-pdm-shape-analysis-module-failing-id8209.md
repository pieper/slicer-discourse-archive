# SPHARM-PDM Shape Analysis Module Failing

**Topic ID**: 8209
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/spharm-pdm-shape-analysis-module-failing/8209

---

## Post #1 by @stevenagl12 (2019-08-28 16:34 UTC)

<p>Hi, I am having some major issues getting SPHARM-PDM’s Shape Analysis Module to work. I have tried it on the newest nightly build from today, and a nightly build from 2018. When I input a folder containing mandible VTK files and an output directory, and then run with or without scaling, I am able to have the program start running, but then vtk leaks and debug errors start popping up one after another. I’ve tried this on my desktop and my laptop both of which have windows 10. Nothing seems to work.</p>

---

## Post #2 by @stevenagl12 (2019-09-05 15:33 UTC)

<p>Is there anyone who can help with this?</p>

---

## Post #3 by @muratmaga (2019-09-05 22:19 UTC)

<p>As I understand functionality in spharm-pdm is now available through SlicerSALT, a customized version of Slicer for shape analysis <a href="http://salt.slicer.org/" rel="nofollow noopener">http://salt.slicer.org/</a>. That’s probably where you want to start.</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> is that correct?</p>

---

## Post #4 by @lassoan (2019-09-06 01:06 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="1" data-topic="8209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>vtk leaks and debug errors start popping up one after another</p>
</blockquote>
</aside>
<p>These don’t necessarily indicate any problem.</p>
<p>SPHARM-PDM extension should work the same way regardless if it is downoaded from the extension manager or preinstalled by SlicerSALT.</p>

---

## Post #5 by @stevenagl12 (2019-09-11 05:49 UTC)

<p>When I go to run the program though, all it is doing is creating empty folders with nothing in them. It does not create the meshes. In addition, I have tried using both SlicerSALT and the slicer extension.</p>

---
