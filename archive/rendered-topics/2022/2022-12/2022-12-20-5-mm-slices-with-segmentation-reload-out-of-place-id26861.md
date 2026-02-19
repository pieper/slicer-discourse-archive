---
topic_id: 26861
title: "5 Mm Slices With Segmentation Reload Out Of Place"
date: 2022-12-20
url: https://discourse.slicer.org/t/26861
---

# 5 mm slices with segmentation reload out of place

**Topic ID**: 26861
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/5-mm-slices-with-segmentation-reload-out-of-place/26861

---

## Post #1 by @bcahill24 (2022-12-20 22:07 UTC)

<p>Hello! I have been working in 3D slicer a lot lately, but don’t know much of the technical aspect of things so maybe this has been answered before. I will create segmentations on a scan with thicker slices, save it, and when reopened during a new session the segmentations will be slightly off. Sometimes if I toggle to another scan and segmentation and go back later it will be back in the correct position. I’m in slicer version 4.11.0-2020-04-30 r29028 / 1956d89, working with CT dicom data. Has this happened to anyone else and any advice on how to fix it?</p>

---

## Post #2 by @mau_igna_06 (2022-12-20 22:29 UTC)

<p>Please test if you find this issue on <a href="https://download.slicer.org/" rel="noopener nofollow ugc">latest preview release</a></p>

---

## Post #3 by @lassoan (2022-12-21 00:05 UTC)

<p>Definitely upgrade to the latest Slicer version, as even though this is most likely not a software issue, we have made many fixes and improvements since April 2020.</p>
<p>Most likely the difference you see between the segmentation and the input image is just because images are smoothly interpolated between slices, while segmentations are binary images, which are not interpolated (they are “blocky”). If the slice spacing is large and you use Shift+MouseMove to navigate then you will see this difference.</p>
<p>You can choose to simply ignore the difference, because these differences are less than the size of a voxel, so your image just does not contain more accurate 3D information than the voxel size.</p>
<p>If you want to avoid seeing slightly misaligned contours then I would recommend to resample the input volume using Crop volume module to have isotropic spacing, and then segment it. See some more instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---
