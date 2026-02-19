---
topic_id: 2325
title: "Latest Build Vtkv9 Step Requires Git Lfs"
date: 2018-03-15
url: https://discourse.slicer.org/t/2325
---

# Latest build - VTKv9 step requires git-lfs

**Topic ID**: 2325
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/latest-build-vtkv9-step-requires-git-lfs/2325

---

## Post #1 by @hherhold (2018-03-15 14:11 UTC)

<p>It looks like the changes for VTKv9 require git-lfs to be installed (from HomeBrew on mac, at least).</p>
<p>I can update the build docs to note this if this is a permanent change? Let me know.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @jcfr (2018-03-15 15:04 UTC)

<p>Hi Hollister,</p>
<p>I will look into removing this dependency. Or see if it can be optional.</p>
<p>Jc</p>

---

## Post #3 by @che85 (2018-04-04 20:18 UTC)

<p>Hi guys,</p>
<p>I am getting the following error while building Slicer on MacOS even though I installed git-lfs from brew.</p>
<pre><code>HEAD is now at 0f8cf0373d... Merge topic 'clipping_plane_uniform'
Submodule 'VTK-m' (https://gitlab.kitware.com/vtk/vtk-m.git) registered for path 'ThirdParty/vtkm/vtk-m'
Cloning into '/Users/christian/sources/cpp/Slicer/cmake-build-debug/VTKv9/ThirdParty/vtkm/vtk-m'...
git-lfs filter-process: git-lfs: command not found
fatal: The remote end hung up unexpectedly
Unable to checkout '6a908cc9da6076a42d41b9397ad71f56a1f69a70' in submodule path 'ThirdParty/vtkm/vtk-m'
CMake Error at VTKv9-prefix/tmp/VTKv9-gitclone.cmake:93 (message):
Failed to update submodules in:
'/Users/christian/sources/cpp/Slicer/cmake-build-debug/VTKv9'
</code></pre>
<p>Any thoughts?</p>

---

## Post #4 by @lassoan (2018-04-06 00:33 UTC)

<p>Can you clone the VTK git repository manually?</p>

---
