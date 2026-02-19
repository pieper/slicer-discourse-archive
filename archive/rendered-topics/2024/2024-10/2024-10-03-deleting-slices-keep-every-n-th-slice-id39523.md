---
topic_id: 39523
title: "Deleting Slices Keep Every N Th Slice"
date: 2024-10-03
url: https://discourse.slicer.org/t/39523
---

# Deleting slices - keep every n-th slice

**Topic ID**: 39523
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/deleting-slices-keep-every-n-th-slice/39523

---

## Post #1 by @Dejf (2024-10-03 14:39 UTC)

<p>Hello, I am about to do segmentation on dataset that has more than 5000 slices. I would like to delete even slices or maybe keep every 3rd or 4th slice and get rid of the rest. Is there any way how to do this? Thank you, David</p>

---

## Post #2 by @muratmaga (2024-10-03 14:44 UTC)

<p>You cant do that once you imported the data. However if your data is in form of imagestack then you can use ImageStacks module in slicermorph extension to skip a slice or two or more…</p>

---

## Post #3 by @muratmaga (2024-10-03 15:32 UTC)

<p>Also remember that keeping every 3th or 4th slice, you will have quite anistoropic data. Depending on what you are segmenting that may not be ideal.</p>
<p>Explore the options in SlicerMorph and Slicer. If you are segmenting a specific region, import only that (use the ROI option in <code>ImageStacks</code>). Or if you need the whole thing, but want to reduce the memory consumption, consider using <code>CropVolume</code> and enter a reduction factor of 1.25. This will reduce your data volume by 2, while keeping your dataset isotropic (assuming it was originally isotropic).</p>

---
