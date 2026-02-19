---
topic_id: 45481
title: "Is There An Existing Trame Slicer Docker Image"
date: 2025-12-13
url: https://discourse.slicer.org/t/45481
---

# Is there an existing trame-slicer docker image?

**Topic ID**: 45481
**Date**: 2025-12-13
**URL**: https://discourse.slicer.org/t/is-there-an-existing-trame-slicer-docker-image/45481

---

## Post #1 by @rlhisey (2025-12-13 20:52 UTC)

<p>Hi, I’m looking for a way to create a basic Slicer application on the web using trame-slicer. Ideally, I think I’d like to run it in a docker container to make it somewhat portable. Is there an existing, recommended docker image that I could base my application on? I know there is a trame image but I believe that trame-slicer requires the slicer  python interpreter. Sorry I’m fairly new to all of this</p>

---

## Post #2 by @Thibault_Pelletier (2025-12-14 09:18 UTC)

<p>Hi <a class="mention" href="/u/rlhisey">@rlhisey</a>,</p>
<p>There is no official trame-slicer docker image yet, but there is an open <a href="https://github.com/KitwareMedical/trame-slicer/pull/23" rel="noopener nofollow ugc">draft PR</a> open on the subject to have a minimal dockerfile recipe to get people started on the deployment.</p>
<p>The docker image doesn’t rely on the Slicer environment but on the VTK MRML wheel which corresponds to the core 3D Slicer classes and compiled for Python 3.10 on Windows and Linux x64.</p>
<p>These wheels are compatible with deployment for cloud / k8s and desktop apps using PyInstaller / Tauri.</p>
<p>What kind of application are you looking to build?</p>
<p>Best,<br>
Thibault</p>

---

## Post #3 by @rlhisey (2025-12-14 19:49 UTC)

<p>Thanks! Right now I’m just doing some investigation to see if it’s possible to run some basic Slicer functionality through a web interface mostly for my own learning. I’ll start with the docker file you’ve mentioned.</p>

---

## Post #4 by @rlhisey (2025-12-17 02:41 UTC)

<p>I took a look at the dockerfile PR mentioned above and running the medical_viewer example throws `ImportError: cannot import name ‘vtkMRMLLayerDMObjectEventObserverScripted’ from ‘slicer’ (/usr/local/lib/python3.10/site-packages/slicer/<strong>init</strong>.py)` I know the PR is still in draft so I may need to do some additional debugging, just wondering if there is something obvious I’m missing.</p>

---

## Post #5 by @Thibault_Pelletier (2025-12-19 07:07 UTC)

<p>Hi <a class="mention" href="/u/rlhisey">@rlhisey</a>,</p>
<p>This problem is likely due to an outdated vtk-mrml wheel being installed. Make sure you’re using the latest in the Docker image which <a href="https://github.com/KitwareMedical/trame-slicer/releases/download/v1.4.0/vtk_mrml-9.4.0-cp310-cp310-manylinux_2_35_x86_64.whl" rel="noopener nofollow ugc">should be this one.</a></p>

---
