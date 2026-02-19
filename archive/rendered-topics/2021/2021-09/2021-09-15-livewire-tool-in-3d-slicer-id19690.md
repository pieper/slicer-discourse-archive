---
topic_id: 19690
title: "Livewire Tool In 3D Slicer"
date: 2021-09-15
url: https://discourse.slicer.org/t/19690
---

# Livewire tool in 3D slicer

**Topic ID**: 19690
**Date**: 2021-09-15
**URL**: https://discourse.slicer.org/t/livewire-tool-in-3d-slicer/19690

---

## Post #1 by @alyssan (2021-09-15 19:08 UTC)

<p>Is their something similar to say a livewire tool in 3D slicer where I can draw out where I want to segment?</p>

---

## Post #2 by @lassoan (2021-09-15 20:13 UTC)

<p>Livewire relies on visual verification of the automatic snapping of the curve. This works fine on 2D images but if you need to segment a 3D volume then you would need to segment slice by slice. We do everything to avoid slice by slice segmentation, because is very time consuming and tends to lead to poor quality results (due to large variations between slices, fatigue of the user, and time constraints).</p>
<p>Instead, in 3D Slicer we provide many segmentation tools that directly produce in 3D segmentation. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point for getting to know these tools. We can also give specific advice if you describe your segmentation task.</p>

---

## Post #3 by @lassoan (2021-09-16 03:07 UTC)

<p>I would just add that the closest to a live-wire tool in the Segment Editor is the “Level trace” effect. However, due to the above described reasons, I would recommend using 3D segmentation tools instead.</p>

---
