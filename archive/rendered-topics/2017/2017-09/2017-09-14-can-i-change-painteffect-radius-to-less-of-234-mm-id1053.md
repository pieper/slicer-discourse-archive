---
topic_id: 1053
title: "Can I Change Painteffect Radius To Less Of 234 Mm"
date: 2017-09-14
url: https://discourse.slicer.org/t/1053
---

# Can I change PaintEffect radius to less of .234 mm?

**Topic ID**: 1053
**Date**: 2017-09-14
**URL**: https://discourse.slicer.org/t/can-i-change-painteffect-radius-to-less-of-234-mm/1053

---

## Post #1 by @juangdiosa (2017-09-14 23:37 UTC)

<p>Hi everybody, I am new user of Slicer</p>
<p>I am trying to create 3d models of teeth with the purpose of to do some FEM analysis. I am using PaintEffect tool of editor module, but the minimum size of this tool is .234 mm. This size is big in a tooth where the axial length usually is 13 mm and the models do not capture the actual shape of the thooth. Is it possible to reduce the size? my idea is obtain models close to patient’s dental piece. I tried doing a post process using surface models but the result was not enough good for my necessities .</p>

---

## Post #2 by @lassoan (2017-09-15 00:22 UTC)

<p>What is the voxel size (spacing) of your volume? It is shown in Volumes module / info section.</p>
<p>Paintbrush size is determined based on voxel size of your volume. You can reduce the voxel size (along with cropping the volume to the necessary region of interest) by using Crop volume module.</p>

---

## Post #3 by @juangdiosa (2017-09-20 21:54 UTC)

<p>Thanks Iasson, with the Voxel size in crop model I solved my problem.</p>

---
