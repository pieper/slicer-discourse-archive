---
topic_id: 39944
title: "Problem With Segmentation When Switching Source Volume"
date: 2024-10-30
url: https://discourse.slicer.org/t/39944
---

# Problem with segmentation when switching source volume

**Topic ID**: 39944
**Date**: 2024-10-30
**URL**: https://discourse.slicer.org/t/problem-with-segmentation-when-switching-source-volume/39944

---

## Post #1 by @maxmo (2024-10-30 19:57 UTC)

<p>Hey everyone!</p>
<p>I need to make a segmentation of a patient’s bone out of different source volumes (in this case diff. MRI planes). However, when I switch volumes, the accuracy of the manual segmentation gets very low - even if I am choosing the smallest diameter for “paint function”, I cannot perform a segmentation of the exact border of the structure, although the image itself shows quite high resolution. I can segment the structure well in one plane, but very inaccurately in another plane.</p>
<p>Also, this error shows up when switching volumes:<br>
<strong>[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1</strong></p>
<p>I would be very happy about your help!</p>

---

## Post #2 by @pieper (2024-10-30 20:55 UTC)

<p>The segmentation geometry (e.g. spacing) will be defined by the first source volume you use, so if the spacing is high in one direction you won’t be able to define fine features in that direction.  You can get around this by using the CropVolume module to make a volume with isotropic spacing and then use that to create the segmentation (or you can use the Segmentation Geometry button to convert your existing segmentation to have it use the isotropic spacing).</p>

---
