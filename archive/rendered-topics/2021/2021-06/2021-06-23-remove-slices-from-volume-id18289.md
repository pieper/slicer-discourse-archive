---
topic_id: 18289
title: "Remove Slices From Volume"
date: 2021-06-23
url: https://discourse.slicer.org/t/18289
---

# Remove slices from volume

**Topic ID**: 18289
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/remove-slices-from-volume/18289

---

## Post #1 by @anitakh1 (2021-06-23 06:56 UTC)

<p>Dear sir. i have a volume of 587 slices (512X512) and I want to remove 200 slices of my choice by keeping dimensions same. How can I do this with 3D Slicer, please explain?</p>

---

## Post #2 by @Juicy (2021-06-23 09:56 UTC)

<p>Do you just want 200 slices cut off one end or do you want to remove random slices in the middle of the volume, or do you want to make the slice thickness higher so you have a lower resolution volume?</p>
<p>If you want to keep the overall volume dimensions the same and have less, but thicker slices you could try using the resample scalar volume module. You can type in the dimensions (x,y,z) which you want to change the volume to. It will keep the overall size of the volume the same.</p>

---
