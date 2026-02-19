---
topic_id: 23269
title: "Linux Sliceopencv Build"
date: 2022-05-03
url: https://discourse.slicer.org/t/23269
---

# [Linux] SliceOpenCV build

**Topic ID**: 23269
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/linux-sliceopencv-build/23269

---

## Post #1 by @adamrankin (2022-05-03 21:17 UTC)

<p>I am trying to fix the SlicerOpenCV build in order to re-enable the extension, but I am experiencing some roadblocks. I am able to successfully build the extension on Ubuntu 20.04 with gcc 9.x.</p>
<p>I notice that the build machine is on gcc 7.y. This is probably the reason, right?</p>
<p>I’m trying to make sense of the build error but I don’t know if I’m missing something in the build machine log output</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=2670747" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/viewBuildError.php?buildid=2670747</a></p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> is it possible to set up a 20.04 build machine to see if it passes?</p>

---

## Post #2 by @Mik (2022-05-04 12:32 UTC)

<p>I was able to compile SlicerOpenCV with gcc-11.2 on my local machine. The main issue in my case was the correct path to OpenCV cmake files.</p>

---

## Post #3 by @adamrankin (2022-05-05 14:58 UTC)

<p>Build fixed. OpenCV install folder was distribution dependent (lib on some, lib64 on others). Explicitly setting this fixed the issue.</p>

---
