---
topic_id: 43066
title: "Nninteractive Slicer Server Does Not Start"
date: 2025-05-23
url: https://discourse.slicer.org/t/43066
---

# Nninteractive_slicer_server Does not start

**Topic ID**: 43066
**Date**: 2025-05-23
**URL**: https://discourse.slicer.org/t/nninteractive-slicer-server-does-not-start/43066

---

## Post #1 by @eNable_Polska (2025-05-23 16:56 UTC)

<p>I had been using nninteractive_slicer_server for segmentation for some time and everything worked fine. Unfortunately, since a few days the server stopped working.<br>
I am running ArchLinux, all packages and drivers are up to date.<br>
So far I have been running the server according to the instructions from <a href="https://github.com/coendevente/SlicerNNInteractive/tree/main?tab=readme-ov-file" class="inline-onebox" rel="noopener nofollow ugc">GitHub - coendevente/SlicerNNInteractive: A 3D Slicer extension for efficient segmentation with nnInteractive.</a><br>
Installing the server using the docker tool<br>
Currently after typing the command “docker run --gpus all --rm -it -p 1527:1527 coendevente/nninteractive-slicer-server:latest” the prompt goes to a new line and nothing happens, the server does not start, there are no error messages.<br>
I tried to fix this by deleting active images (docker rmi “ID_image”), restarting the system and reinstalling the server according to the instructions from github, but unfortunately with no result.<br>
I tried compiling the server from source. the process went without error messages, the server image showed up in docker resources (docker image ls) unfortunately, the server prepared in this way still does not work.<br>
Can you help to solve this problem? The tool is very helpful for segmentation, I mainly work with pediatric images which are difficult and laborious to segment, especially newborns and very young children. The nninteractice tool is very helpful in such cases.</p>
<p>Translated with <a href="http://DeepL.com" rel="noopener nofollow ugc">DeepL.com</a> (free version)</p>

---

## Post #2 by @pieper (2025-05-23 18:55 UTC)

<p>You should probably file an issue at the github site and include all the details: <a href="https://github.com/coendevente/SlicerNNInteractive/issues">https://github.com/coendevente/SlicerNNInteractive/issues</a></p>

---

## Post #3 by @eNable_Polska (2025-05-31 14:55 UTC)

<p>I found a solution to the problem. For reasons unknown to me, sometimes docker doesn’t work properly in linux, if when you try to start the server nothing happens, there are no messages, you have to “forcefully” restart docker and everything starts working properly.</p>

---
