---
topic_id: 16643
title: "Nvidia Aiaa Default Server Error When Running Auto Segmentat"
date: 2021-03-19
url: https://discourse.slicer.org/t/16643
---

# NVIDIA AIAA default server error when running auto-segmentation

**Topic ID**: 16643
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/nvidia-aiaa-default-server-error-when-running-auto-segmentation/16643

---

## Post #1 by @icerchou (2021-03-19 15:26 UTC)

<p>I’m new to using 3d-slicer and want to do fully-automatic segmentation of liver and tumor on CT.<br>
When I followed the steps in <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin" rel="noopener nofollow ugc">Tutorials and examples</a>, there’s a slicer error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40828c967c2c23259247a42dd5ffecacc5673467.png" alt="image" data-base62-sha1="9cGg1mgS5kc0nVox4ROlS49lPSv" width="502" height="226"><br>
It seems something wrong with the server, so what can I do ?<br>
I have tried other versions of 3d-slicer but it still goes wrong.</p>

---

## Post #2 by @lassoan (2021-03-26 02:47 UTC)

<p>Unfortunately, the liver model and the default server is not compatible with the latest NVidia AIAA client version (see error report <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/76">here</a>).</p>
<p>You can segment from boundary points (that is faster and more robust anyway) or set up your own server as described in the link provided in <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#setup">setup instructions</a>.</p>

---

## Post #3 by @icerchou (2021-03-26 05:39 UTC)

<p>Thanks for your help. So is it possible to use the old version of 3d-slicer/Nvidia AIAA to do the auto-segement? And could you please tell me the specific version of it? I’d like to try for it.</p>

---

## Post #4 by @icerchou (2021-03-26 06:08 UTC)

<p>“segment from boundary points” you mean the follwing function of Nvidian AIAA?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5162b35c722714e4edeafd63016c865914c6ad6b.png" alt="image" data-base62-sha1="bBY8H2CrDImKtaNAV9clYWlg2dJ" width="655" height="101"><br>
But it using default server as well, isn’t it? Or you mean another function in 3d-slicer? Please be more specific. Too many thx!</p>

---
