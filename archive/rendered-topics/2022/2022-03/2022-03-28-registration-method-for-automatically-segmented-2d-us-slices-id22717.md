---
topic_id: 22717
title: "Registration Method For Automatically Segmented 2D Us Slices"
date: 2022-03-28
url: https://discourse.slicer.org/t/22717
---

# Registration method for automatically segmented 2D US slices

**Topic ID**: 22717
**Date**: 2022-03-28
**URL**: https://discourse.slicer.org/t/registration-method-for-automatically-segmented-2d-us-slices/22717

---

## Post #1 by @Marijn_H (2022-03-28 10:42 UTC)

<p>I am trying to automatically register tracked US images to a CT scan (with 3D model). I already developed a way to automatically segment bone from US images in real-time. The segmented binary image can be loaded in slicer as scalar volume or labelmap, which looks like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3eda0d1088fabfb7c0a7d3620b269abbdec8a24.png" alt="image" data-base62-sha1="pFIAa2QFBh9U8TtVxVtB22e3YYA" width="484" height="418"></p>
<p>Now, I am trying to find a way to register these segmentations to the CT scan, but I am a bit struggling which method is most efficient. I tried exporting each 2D segmentation to a 3D volume, but then you end up with a lot of different segments in the slicer scene. I also tried the volume reconstruction module, but this results in a 3D segmentation with a thickness of multiple millimeters, while I only want the bone surface. I was also thinking: maybe it is possible to convert each 2D US segmentation to a 3D point cloud? Then the point cloud can be registered to the CT bone model with the fiducials-model registration module.</p>
<p>Which method do you think is most efficient? Or do you have other suggestions?</p>

---
