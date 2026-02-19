---
topic_id: 2936
title: "Slicer Three Dimension Widget Layout Not Correct On Mac"
date: 2018-05-26
url: https://discourse.slicer.org/t/2936
---

# Slicer three dimension widget layout not correct on Mac

**Topic ID**: 2936
**Date**: 2018-05-26
**URL**: https://discourse.slicer.org/t/slicer-three-dimension-widget-layout-not-correct-on-mac/2936

---

## Post #1 by @priya.vada4 (2018-05-26 23:39 UTC)

<p>Hi</p>
<p>I built the latest version of Slicer 4.9 (4.9.0-2018-05-25 rde9b19d) using Qt 5.10 executable file on a Mac. The three D widgets don’t look correct. I have attached a screenshot with this post. Could someone please help resolve the problem.</p>
<p>Thanks<br>
Priya</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3574b81ca767f4d4b382b2c244c91d12d17633e5.png" data-download-href="/uploads/short-url/7CTnhXjPCX9Tmb8wV9zZf5Gls3z.png?dl=1" title="ThreeD" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3574b81ca767f4d4b382b2c244c91d12d17633e5_2_658x500.png" alt="ThreeD" data-base62-sha1="7CTnhXjPCX9Tmb8wV9zZf5Gls3z" width="658" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3574b81ca767f4d4b382b2c244c91d12d17633e5_2_658x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3574b81ca767f4d4b382b2c244c91d12d17633e5_2_987x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3574b81ca767f4d4b382b2c244c91d12d17633e5_2_1316x1000.png 2x" data-dominant-color="2A2B3C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ThreeD</span><span class="informations">1940×1474 78.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-05-27 00:05 UTC)

<p>Does the official nightly release that you download works well?<br>
Have you built Slicer using VTK9?</p>

---

## Post #3 by @priya.vada4 (2018-05-28 03:03 UTC)

<p>Thanks Andras. That is exactly what I am trying. Can you let me know the git tag for downloading and building VTK 9 with Slicer? I was getting errors downloading VTK 9 with the git tag mentioned in Cmake files.</p>
<p>Thanks<br>
Priya</p>

---

## Post #4 by @lassoan (2018-05-28 05:31 UTC)

<p>Slicer downloads and builds the correct VTK version automatically. Did you try to build Slicer with some other pre-built VTK version?</p>

---

## Post #5 by @priya.vada4 (2018-05-28 13:04 UTC)

<p>Hi Andras</p>
<p>When I try to choose VTK version 9 in CMake and then build Slicer, I get the following error. I suspect that the git tag is incorrect for VTK 9.</p>
<p>Error is as follows:</p>
<p>You are in ‘detached HEAD’ state. You can look around, make experimental<br>
changes and commit them, and you can discard any commits you make in this<br>
state without impacting any branches by performing another checkout.</p>
<p>If you want to create a new branch to retain commits you create, you may<br>
do so (now or later) by using -b with the checkout command again. Example:</p>
<p>git checkout -b </p>
<p>HEAD is now at 10e8cdc30e… Merge topic ‘give_up_on_eigin’<br>
Submodule ‘VTK-m’ (<a href="https://gitlab.kitware.com/vtk/vtk-m.git" rel="nofollow noopener">https://gitlab.kitware.com/vtk/vtk-m.git</a>) registered for path ‘ThirdParty/vtkm/vtk-m’<br>
Cloning into ‘/Users/Priya/Project/Slicer-latest/Slicer-Superbuild-Debug-QT/VTKv9/ThirdParty/vtkm/vtk-m’…<br>
git-lfs filter-process: git-lfs: command not found<br>
fatal: The remote end hung up unexpectedly<br>
Unable to checkout ‘6a908cc9da6076a42d41b9397ad71f56a1f69a70’ in submodule path ‘ThirdParty/vtkm/vtk-m’<br>
CMake Error at VTKv9-prefix/tmp/VTKv9-gitclone.cmake:93 (message):<br>
Failed to update submodules in:<br>
‘/Users/Priya/Project/Slicer-latest/Slicer-Superbuild-Debug-QT/VTKv9’</p>
<p>make[2]: *** [VTKv9-prefix/src/VTKv9-stamp/VTKv9-download] Error 1<br>
make[1]: *** [CMakeFiles/VTKv9.dir/all] Error 2<br>
make[1]: *** Waiting for unfinished jobs…</p>
<p>Thanks<br>
Priya</p>

---

## Post #6 by @lassoan (2018-05-28 13:26 UTC)

<p>It seems that you need to install git-lfs.</p>

---

## Post #7 by @priya.vada4 (2018-05-28 20:44 UTC)

<p>Thanks Andras. That fixed the problem. Also, with VTK 9, I don’t have the problem with the threeD widgets anymore.</p>
<p>Thanks for your help.</p>
<p>Priya</p>

---
