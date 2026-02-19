---
topic_id: 37203
title: "3D Segmentation Eraser Tool Excessive Compute"
date: 2024-07-04
url: https://discourse.slicer.org/t/37203
---

# 3D segmentation eraser tool - excessive compute?

**Topic ID**: 37203
**Date**: 2024-07-04
**URL**: https://discourse.slicer.org/t/3d-segmentation-eraser-tool-excessive-compute/37203

---

## Post #1 by @hari_seldon (2024-07-04 22:07 UTC)

<p>Hello, I am annotating a 256x256x256 cube of voxels in 3D, through removing excess semantic mask to generate instance segmentations, and the eraser tool is crippling laggy on an amd7950X, rtx4080S, 128Gddr5, 7500mb/s nvme build. I think the software is re-drawing every voxel with every movement or something? I’m not sure what is going on, but is there a way to streamline the 3D eraser tool? There’s zero lag in Napari out of the box, which surprised me, so maybe I’m missing an optimization or setting somewhere in Slicer? Thanks so much!!</p>

---

## Post #2 by @pieper (2024-07-04 22:12 UTC)

<p>Did you try turning off 3D rendering while you edit?</p>

---

## Post #3 by @hari_seldon (2024-07-04 22:46 UTC)

<p>Well I’m editing the data in the 3D window with the eraser tool settings set to sphere brush and edit in 3D views. Does your comment still apply? If so, where is that setting? Thanks</p>

---

## Post #4 by @hari_seldon (2024-07-04 22:50 UTC)

<p>I’m in the segment editor section of Slicer when i’m annotating.</p>

---
