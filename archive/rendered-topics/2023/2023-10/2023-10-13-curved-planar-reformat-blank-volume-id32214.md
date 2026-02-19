---
topic_id: 32214
title: "Curved Planar Reformat Blank Volume"
date: 2023-10-13
url: https://discourse.slicer.org/t/32214
---

# Curved Planar Reformat Blank Volume

**Topic ID**: 32214
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/curved-planar-reformat-blank-volume/32214

---

## Post #1 by @chris_nik (2023-10-13 16:24 UTC)

<p>Dear community,<br>
I am running Slicer 5.4.0 on Windows 11. I am trying to create a panoramic image from a Micro-CT ISQ volume (Voxel size 0.036mm) using the Curved Planar Reformat module. My Input volume is a hardened Micro-CT volume (as there is a transform on it). My Input curve is a spline with 4 points. Curve and Slice resolution I set to 0.036mm (equaling the volume’s voxel size). Slice size is 40mm. As output I choose only the straightened volume.<br>
The result I get is a volume with all black voxels. Does somebody have a suggestion what I might be doing wrong or if there is a voxel size limit of the module? (I tested it with a CT Volume, voxel size 0.15mm, and it worked fine)</p>

---

## Post #2 by @lassoan (2023-10-13 18:46 UTC)

<p>Please try it on one of the sample data sets in Slicer, with a 5-10cm curve and all default options. If it works well then you can check step-by-step what is the difference between your scene and this default scene.</p>

---

## Post #3 by @chris_nik (2023-10-14 09:13 UTC)

<p>It worked Professor Lasso! I got inspired from the sample volume and did following adjustments: 1.Crop the transformed volume instead of hardening it 2.Draw the curve so that it stays within the borders of the volume. I am not sure which of both solved the problem but with the above settings it works now. Thank you very much Prof. Lasso, also for creating this wonderful module (I was very happy when I discovered it in the threads).</p>

---
