# Total segmentation resolution

**Topic ID**: 33571
**Date**: 2023-12-30
**URL**: https://discourse.slicer.org/t/total-segmentation-resolution/33571

---

## Post #1 by @Caterina (2023-12-30 15:28 UTC)

<p>Dear support,<br>
I’m interesting to improve resolution of segmentation from dice image (CT) and by using TotalSegmentation Module.<br>
Dicom images are from hight resolution CT (1 mm from slices) but segmentation appears jagged. Suggestions?<br>
Thanks</p>

---

## Post #2 by @lassoan (2024-01-01 17:32 UTC)

<p>For most clinical use cases, the 1mm segmentation resolution is actually sufficient. In whole-body imaging, you rarely need to conduct details that are smaller than 1mm.</p>
<p>Of course, there are special cases where it would be nice to have higher resolution (e.g., quantify stenosis in small vessels or segment very thin structures). In these cases, you probably acquire images with specialized protocol and would need to train models that operate on these special images.</p>
<p>What do you need to segment? What is the goal of the segmentation (volumetric measurement, visualization, surgical planning, 3D printed surgical guide generation,…)? What is the accuracy requirement?</p>

---

## Post #3 by @Caterina (2024-01-02 11:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you very much for reply.<br>
I need to segment several anatomical regions for volumetric measurement and visualization.<br>
My question was whether, with a dicom resolution of 1 mm, it is normal to result in segmentation (via Total Segmentation) with segmented contours or whether this can be attributed to some segmentation process parameter.</p>

---

## Post #4 by @lassoan (2024-01-02 16:18 UTC)

<aside class="quote no-group" data-username="Caterina" data-post="3" data-topic="33571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>I need to segment several anatomical regions for volumetric measurement and visualization.</p>
</blockquote>
</aside>
<p>The 1.5mm internal resolution of the TotalSegmentator model should be sufficient for both these purposes.</p>
<p>You can use “Colorize volume” module to <a href="https://discourse.slicer.org/t/vtk-multivolume-cinematic-volume-rendering/31981/53">combine all the original details of the input CT image with the colors provided by the segmentation</a>.</p>

---

## Post #5 by @Caterina (2024-01-04 12:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Can I have more information about “the 1.5mm internal resolution of the TotalSegmentator model?”</p>

---

## Post #6 by @lassoan (2024-02-26 21:39 UTC)

<p>Internally, your input volume is resampled to 1.5mm resolution, the segmentation is created at this resolution, and then the result is resampled to the original input volume resolution.</p>

---
