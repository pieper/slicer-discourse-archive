---
topic_id: 17482
title: "Recommended Hardware For A Very Large Ct Segmentation"
date: 2021-05-06
url: https://discourse.slicer.org/t/17482
---

#  Recommended hardware for a very large CT segmentation

**Topic ID**: 17482
**Date**: 2021-05-06
**URL**: https://discourse.slicer.org/t/recommended-hardware-for-a-very-large-ct-segmentation/17482

---

## Post #1 by @CETUS (2021-05-06 01:39 UTC)

<p>Hi, I am planning to use 3D Slicer for a research project involving segmentation of very large CT scans. A single soft tissue window can be up to 600 MB (composed of more than 1,000 individual images, each about 500 KB) due to the resolution and the size of the scanned object.</p>
<p>I intend to use thresholding and manual paint/draw functions in the segment editor module to create 3D reconstructions and generate volume measurements. As a result, I want to look for a new computer workstation that would best handle these large files in 3D Slicer. Considering the 600 MB size of these files, what size/general specification would you recommend for these hardware elements:</p>
<ol>
<li>graphics card (GPU)</li>
<li>CPU</li>
<li>RAM</li>
<li>Hard drive</li>
<li>System memory</li>
</ol>
<p>Thank you for all advice!</p>

---

## Post #2 by @hherhold (2021-05-06 01:51 UTC)

<p>Just as a benchmark, I do segmentations of microCT scans often over 1-2GB, and occasionally as large as 4-6GB. My voxel sizes range from 1-2 microns up to around 30-40 microns depending on the scan.</p>
<p>My current machine is a 2019 MacBook Pro 16" with 64GB RAM, 2.4 GHz 8-Core Intel Core i9, AMD Radeon Pro 5500M 8 GB, and 2TB SSD. I often run more than one instance of Slicer to compare scans.</p>
<p>I would consider my setup “not bad”. More RAM is always better, and if I could upgrade, I would, but this is the maximum available for this computer. SSD is very important for dealing with large files. Graphics card memory is likely important only if you’re doing a lot of volume rendering - there is not a huge benefit for just regular 3D work. I would say the critical components (in order) would be CPU, RAM, SSD, graphics card.</p>
<p>Hope this helps.</p>

---

## Post #3 by @muratmaga (2021-05-06 19:58 UTC)

<p>While they are fairly big compared to clinical data, I wouldn’t consider 600MB CT as large. Any modern laptop, with sufficient memory should be able to handle that.</p>
<p>Rule of thumb for memory consumption for segmentation is about 10X of your dataset. So if you full volume is 600MB, you will need 6-8GB of RAM to be available to Slicer during segmentation. Depending on what other programs you are running and OS, probably a computer with 32GB of RAM would suffice.</p>
<p>GPU is only used during 3D rendering, and plays no role in segmentation. Given the dataset size, even integrated GPUs in modern computers (from last couple years), probably can render them in sufficient performance.</p>

---

## Post #4 by @CETUS (2021-05-06 21:05 UTC)

<p>Hi, thank you very much for both of your responses, I will definitely keep the guidelines regarding hardware requirements mentioned in mind. Thanks as well for the correction regarding the size of these CT files, those micro CT scans of 4-6 GB mentioned certainly place the size of my scans in perspective!</p>
<p>In the event I decided to utilize volume rendering in the future for these scans and wanted an appropriate GPU, is there a general rule of thumb for graphics card size vs CT file size as with RAM?</p>

---

## Post #5 by @hherhold (2021-05-07 13:11 UTC)

<p>For volume rendering, I would say that your volume should be able to at least fit into the graphics memory of your GPU/graphics card “with some room to spare”. I’ve been able to volume render 4-6GB volumes in my 8GB GPU, but it took some tweaking, meaning I had to do some trial and error with how the volume is sent to the GPU - it can be sent all in one chunk, or in pieces, for example. For the volumes you’re talking about, as Murat mentioned, you should not have any problem with standard run-of-the-mill GPUs or even integrated GPU chipsets.</p>

---
