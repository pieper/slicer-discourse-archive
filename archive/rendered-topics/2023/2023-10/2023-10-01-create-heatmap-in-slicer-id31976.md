# Create "heatmap" in slicer

**Topic ID**: 31976
**Date**: 2023-10-01
**URL**: https://discourse.slicer.org/t/create-heatmap-in-slicer/31976

---

## Post #1 by @umair04 (2023-10-01 04:29 UTC)

<p>Hi,<br>
Does anyone know how to create a “heatmap” on slicer? I am trying to overlay 5 different segmentations below and make areas where overlap occurs darker and highlight the areas where most overlap occurs.</p>
<p>Thanks</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/093ae962c54f93f5306b9fe3fadef72f053b73ab.png" alt="image" data-base62-sha1="1jEvVeS4Y3ERFcdZsBdO2diR4hB" width="684" height="428"></p>

---

## Post #2 by @manjula (2023-10-01 06:03 UTC)

<p>I think what you looking  for is the Model to Model distance extension and shape population viewer.</p>

---

## Post #3 by @umair04 (2023-10-13 21:59 UTC)

<p>I tried using the extension but was unable to figure out how to do it. Do you know what specific steps I need to follow to create the heat map?</p>

---

## Post #4 by @lassoan (2023-10-15 21:50 UTC)

<p>If segments are this much misaligned then closest point distance (computed by ModelToModelDistance extension) is not meaningful, because closest point on the other surface is not the correponding point. Therefore, I would suggest to try to align the structures and voaualize the transform using Transforms module (or export the computed transform into a displacement field magnitude volume and then use “Probe volume with model” to color the model by the displacement).</p>

---
