---
topic_id: 14349
title: "Help With Flood Filling Segmentation"
date: 2020-10-31
url: https://discourse.slicer.org/t/14349
---

# Help with flood filling segmentation

**Topic ID**: 14349
**Date**: 2020-10-31
**URL**: https://discourse.slicer.org/t/help-with-flood-filling-segmentation/14349

---

## Post #1 by @carlos.rinaldi (2020-10-31 18:14 UTC)

<p>I am new to slicer. Working on segmentation using the SegmentEditorExtraEffects on Slicer build 4.10.2 on a Mac running 10.13.6.</p>
<p>I am trying to use flood filling to create a segmentation. I create a new segment, choose Flood Filling and leave default values (Int Tol 10, Neighborhood 1) and click on a pixel in the axial slice, get the spinning wheel but nothing happens (no region is selected for the segment). I change around the values and click and sometimes it processes with nothing happening and other times it gets stuck processing.</p>
<p>What does the “neighborhood size” parameter mean? What does increasing/decreasing it do?</p>
<p>Ultimately, I am trying to create a segment for a region where the intensity is above a certain value (a tumor region), but trying to avoid another region where there is also high intensity (other organs). Perhaps I should try another tool, like watershed, but I can’t figure out how to use that one.</p>

---

## Post #2 by @lassoan (2020-11-01 20:10 UTC)

<p>Please use the latest stable release (Slicer-4.11.20200930), as it has greatly improved segmentation tools.</p>
<p>Flood filling is inherently a very fragile, unreliable operation on realistic images, and especially in 3D.</p>
<p>Grow from seeds, Watershed, and Local threshold effects all work much better. You can find detailed, step-by-step slide-based and video tutorials and segmentation recipes here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a>. For example, see this recipe: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/">https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/</a></p>
<p>If you get stuck at any point then let us know.</p>

---
