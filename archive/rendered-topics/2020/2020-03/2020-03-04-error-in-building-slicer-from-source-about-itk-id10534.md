---
topic_id: 10534
title: "Error In Building Slicer From Source About Itk"
date: 2020-03-04
url: https://discourse.slicer.org/t/10534
---

# Error in building Slicer from source about ITK

**Topic ID**: 10534
**Date**: 2020-03-04
**URL**: https://discourse.slicer.org/t/error-in-building-slicer-from-source-about-itk/10534

---

## Post #1 by @Akash23 (2020-03-04 02:45 UTC)

<p>Hi, all,</p>
<p>I ran the build in my ubuntu 18, with gcc/g++ 7.4 and cmake 3.13 and qt5. But it seems to me the path for ITK git repository is not correct. Anyone ran into this issue? How should I provide correct path for ITK build?<br>
fatal: not a git repository (or any of the parent directories): .git<br>
CMake Error at /home/me/MyProjects/Slicer-SuperBuild-Debug/ITK-prefix/tmp/ITK-gitupdate.cmake:13 (message):<br>
Failed to get the hash for HEAD</p>

---

## Post #2 by @pieper (2020-03-04 14:19 UTC)

<p>Hmm, that’s an odd error, maybe a network glitch.  Probably deleting the build tree and starting from scratch will work. If this is repeatable, then try checking out ITK manually and report back with full logs.</p>

---
