---
topic_id: 40719
title: "New Module Remote Vista3D Server For Ct Segmentation"
date: 2024-12-16
url: https://discourse.slicer.org/t/40719
---

# New Module: Remote VISTA3D server for CT segmentation

**Topic ID**: 40719
**Date**: 2024-12-16
**URL**: https://discourse.slicer.org/t/new-module-remote-vista3d-server-for-ct-segmentation/40719

---

## Post #1 by @aylward (2024-12-16 19:37 UTC)

<p><strong>Goal</strong><br>
Provide access to MONAI-based foundation models to users running 3D Slicer on low-end (e.g., no GPU) machines by launching those AI methods on freely available (albeit limited total usage) high-end servers.</p>
<p><strong>Overview</strong><br>
I am proposing to offer a set of Slicer Extensions that will allow Slicer users to call AI methods built using MONAI and running on NVIDIA servers.</p>
<p>Access to the servers requires registration which is free, to get an API key with which 1,000 or more images can be processed for free.  Research users can also register as developers (also for free) to get unlimited local access.</p>
<p>The first Extension will allow Slicer users (with a free API key) to process images using the <strong>MONAI VISTA-3D segmentation (remote)</strong> running on NVIDIA servers.  Via this Extension, Slicer users will be able to perform large / fast CT image AI segmentations on low-end (e.g., no GPU) machines.</p>
<p><strong>TLDR</strong>:<br>
Try the VISTA-3D module running on NVIDIA’s GPU Cloud: <a href="https://build.nvidia.com/nvidia/vista-3d" class="inline-onebox" rel="noopener nofollow ugc">vista-3d Model by NVIDIA | NVIDIA NIM</a></p>
<p>I am proposing to make that service callable using a simple Slicer extension, to enable remote VISTA-3D processing of data from within 3D Slicer.</p>
<p><strong>Details</strong><br>
NVIDIA is defined NIMs (NVIDIA Inference Microservices) as optimized containers for portable, scalable AI.  These are nominally offered on NV AI Enterprise / GPU Cloud servers as callable methods.  Anyone can register for free and get 1,000 to 5,000 free credits (depending on email domain used for registration, with 1 credit used for each image processed).  Additionally, anyone can register for free to become an NVIDIA Developer, and then they can download NIMs for free for research purposes - enabling unlimited data processing, albeit using local GPU resources.  NIMs can also run on AWS and Azure servers.</p>
<p>NVIDIA AI Enterprise / GPU-Cloud servers use high-end GPUs (e.g., H100s) so via NIMS running on these servers it is possible to evaluate very large AI models and very large images very rapidly.</p>
<p>Initially I propose to developed a "<strong>MONAI VISTA-3D segmentation (remote)</strong> Extension.  For details on VISTA-3D, see the online demo:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://build.nvidia.com/nvidia/vista-3d">
  <header class="source">
      <img src="https://build.nvidia.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://build.nvidia.com/nvidia/vista-3d" target="_blank" rel="noopener nofollow ugc">NVIDIA NIM</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/392;"><img src="https://assets.ngc.nvidia.com/products/api-catalog/images/vista-3d.jpg" class="thumbnail" width="690" height="392"></div>

<h3><a href="https://build.nvidia.com/nvidia/vista-3d" target="_blank" rel="noopener nofollow ugc">vista-3d Model by NVIDIA | NVIDIA NIM</a></h3>

  <p>VISTA-3D is a specialized interactive foundation model for segmenting and anotating human anatomies.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><strong>Required Inputs</strong></p>
<ul>
<li>Image currently loaded in Slicer that the user wants to process.</li>
<li>NVIDIA GPU Cloud API Key (available with free registration)</li>
</ul>
<p><strong>Output</strong></p>
<ul>
<li>Segmentation results as a labelmap using same categories as TotalSegmentator</li>
</ul>
<p><strong>Optional Inputs</strong></p>
<ul>
<li>Seeds indicating object and not-object locations for arbitrary object segmentation</li>
<li>List of specific anatomic structures to be segmented (of 120+ supported)</li>
</ul>

---

## Post #2 by @pieper (2024-12-16 20:41 UTC)

<p>Sounds great <a class="mention" href="/u/aylward">@aylward</a> - any chance you or others might want to work on this as part of <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/">Project Week</a>?</p>

---

## Post #3 by @aylward (2024-12-17 14:37 UTC)

<p>Definitely!   I will attend today’s Project Week meeting, and attend Project Week (probably virtually).</p>
<p>Open to suggestions and help as always!</p>

---
