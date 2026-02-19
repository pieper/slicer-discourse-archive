---
topic_id: 4876
title: "Difference Between Two Or More Models"
date: 2018-11-26
url: https://discourse.slicer.org/t/4876
---

# Difference between two or more models

**Topic ID**: 4876
**Date**: 2018-11-26
**URL**: https://discourse.slicer.org/t/difference-between-two-or-more-models/4876

---

## Post #1 by @Gonzalo_Rojas_Costa (2018-11-26 20:19 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.0<br>
Expected behavior: How can I get a new 3D model showing the difference between both models?<br>
Actual behavior: I have two 3D models of MS lesions of the same patient.</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @cpinter (2018-11-26 21:05 UTC)

<p>What would you like the new model to contain? Would you like to subtract one from the other?</p>
<p>Did you use Segment Editor to get the “models” of the lesions or you loaded them from file? If the latter, then what kind of file?</p>

---

## Post #3 by @Gonzalo_Rojas_Costa (2018-11-27 03:37 UTC)

<p>Hi:</p>
<p>I want that the new model shows the difference between each model… Yes… I want to substract one from the other…</p>
<p>I segment the MS lesions using another software, and then I used that segmentation file (label) to generate the model using Model Maker 3D slicer module.</p>
<p>Sincerely</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #4 by @cpinter (2018-11-27 17:02 UTC)

<ol>
<li>Please use Slicer 4.10</li>
<li>Instead of Model Maker, please use the Segmentations module to import the labelmap to a segmentation node, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations#How_to" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations#How_to</a>
</li>
<li>Go to Segment Editor module</li>
<li>Use Logical operators effect to do the subtraction</li>
</ol>
<p>My 2 cents is that in addition to getting the volume difference, you would probably benefit from calculating the Hausdorff distance between the two segments. You can do it in Segment Comparison module, which is in the SlicerRT extension.</p>

---
