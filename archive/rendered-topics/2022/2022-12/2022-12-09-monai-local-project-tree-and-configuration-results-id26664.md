---
topic_id: 26664
title: "Monai Local Project Tree And Configuration Results"
date: 2022-12-09
url: https://discourse.slicer.org/t/26664
---

# MONAI - Local Project "Tree" and Configuration - Results

**Topic ID**: 26664
**Date**: 2022-12-09
**URL**: https://discourse.slicer.org/t/monai-local-project-tree-and-configuration-results/26664

---

## Post #1 by @dalv.silvermann (2022-12-09 13:55 UTC)

<p>Dear colleagues,<br>
I have a question about the results of MONAI Label Service which I’m using on my tower-server with Asus Nvidia GeForce RTX 3080 10GiB based on Windows Server 2019 OS.</p>
<ol>
<li>We are testing two project structures:</li>
</ol>
<ul>
<li>v1 with one orig file and two labels: mandible and 1 tooth;</li>
<li>v2 with 13 additional labels but another structure.<br>
See the link <a href="https://drive.google.com/file/d/1U3XbMLDEiV5qAPA2MhjZ-IA22oiT2OxW/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">project_trees.png - Google Drive</a>
</li>
</ul>
<ol start="2">
<li>
<p>Results of v1 (not bad results)<br>
<a href="https://drive.google.com/file/d/1ikXVqvrwPcWXzyUzx17uTbvRKW20BwDD/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">res_v1_1.jpg - Google Drive</a><br>
<a href="https://drive.google.com/file/d/1NT31h5s1oduLnO8lgEj72zS2nAv0p3Ci/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">res_v1_2.jpg - Google Drive</a></p>
</li>
<li>
<p>Results of v2 (bad results)<br>
<a href="https://drive.google.com/file/d/1waahcVe673xI4mRSlIV66cVss26tonPv/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">res_v2.png - Google Drive</a></p>
</li>
<li>
<p>The questions are:<br>
4.1. What do we need to put in FINAL if we are searching to find the solution for multiple-segmentational project structure?<br>
4.2. Do we need to put a nifti file with SCALAR RANGE 0…15 (equal to labels quantity) in FINAL?<br>
4.3. Where are all of this files needs to be located? Is there any rules or manuals about to know this part of Monai workflow? Smth like: “Working with labels on the local Monai server. Guide to action”?<br>
4.4. As I’ve understood correctly, the correct abbreviation for these nifti files is labels? Is it right?<br>
4.5. Where and how to I need to correct configuration or code to tell the Monai my research structure? Because this is brand new type.<br>
4.6. What algorithm I need to use in future for reconstruction the segmentation of missing tooth?<br>
It means that I need to generate the segmentation of missed tooth by NN. And it will be locate on the proper place.<br>
4.7. How to learn NN for possibilities to create segmentations in blank places?</p>
</li>
</ol>
<p>Kind regards,<br>
Dalv Silvermann.</p>

---

## Post #2 by @diazandr3s (2022-12-12 13:37 UTC)

<p>Hi <a class="mention" href="/u/dalv.silvermann">@dalv.silvermann</a>,</p>
<p>It is great to hear you’re using MONAI Label.</p>
<p>Tooth segmentation is a nice use case -  a bit challenging though.</p>
<p>Of the tree images you’ve shared, MONAI Label supports version 1. Segmentations per volume should be in one file as a label map.</p>
<p>If you already have annotations for some of the volumes, they should be located in the folder <em>dataset/labels/final</em> with the same name as the volumes.</p>
<p>Each segment (tooth) should be consistently annotated. This means, it should have the same index/scalar in all images. If there are teeth missing, indexes/scalars representing the available teeth should still be the same in all images.</p>
<p>Here you can find a video tutorial for MONAI Label: <a href="https://www.youtube.com/watch?v=8y1OBQs2wis&amp;list=PLtoSVSQ2XzyD4lc-lAacFBzOdv5Ou-9IA" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label - Installation with PyPi, Docker, and GitHub - YouTube</a></p>
<p>Additionally, here you can find more information regarding the tree: <a href="https://youtu.be/wtiEe_jiUzg?t=3267" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label Workshop - Project Week - YouTube</a></p>
<p>BTW, I’d suggest you post these MONAI Label-related questions directly in the MONAI Label repository under the discussion section: <a href="https://github.com/Project-MONAI/MONAILabel/discussions" class="inline-onebox" rel="noopener nofollow ugc">Discussions · Project-MONAI/MONAILabel · GitHub</a><br>
You’ll get faster replies from the other MONAI Label developers as well.</p>
<p>Hope this helps,</p>
<p>Andres</p>

---
