# individual muscle - manual segmentation

**Topic ID**: 18360
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/individual-muscle-manual-segmentation/18360

---

## Post #1 by @ryan-t (2021-06-28 01:16 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2</p>
<p>Hi,</p>
<p>I am looking to find the best way to manually segement multiple slices and multiple muscles and then export the data.</p>
<p>For example I have MRI of the thigh and I want to segment the 4 hamstring muscles to find cross sectional area (cm2) at each slice and then combined to find the volume. I was wanting to just basically find the best tool and approach to circle each hamstring on each slice, slide to the next slice, circle and continue. Then I wanted to get that data from each slice and export it to word or excel.</p>
<p>Thanks for your time.</p>

---

## Post #2 by @lassoan (2021-06-28 12:57 UTC)

<p>Muscles are typically very long and vary slowly between neighbor axial slices, therefore “Fill between slices” effect makes can make segmentation 10-20x faster compared to segmenting every slice manually.</p>
<p>You can segment the 4 hamstring muscles on 4-5 axial slices using paint or draw tool, then go to “Fill between slices” effect and generate a preview. You can then quickly browse through the slices and if anywhere you find that any of the slices the interpolated segmentation do not match accurately the underlying image then segment that slice (all 4 muscles) and the segmentation will be automatically updated based on this additional input. You can add as many additional slices as needed, then finally go to “Fill between slices” effect and click “Apply”.</p>
<p>It will take a while to learn this process, but once you are familiar with it, a complete segmentation will not take more than 5-10 minutes. You can speed up the segmentation of individual slices if you buy a Windows laptop with a pen because you can then draw the contours directly on the screen (some people can be similarly fast with using digitizer boards).</p>
<p>You can get total volume by using Segment Statistics module. If you want to plot cross-sectional area vs. position along the body inferior-superior axis then you can use “Segment cross-section area” module in Sandbox extension. If you want to plot cross-sectional area vs. centerline curve of the muscle then you can straighten the volume (extract centerline using VMTK extension and then straighten using “Curved Planar Reformat” module in Sandbox extension) and use that straightened volume as input to “Segment cross-section area” module.</p>

---
