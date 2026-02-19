---
topic_id: 35458
title: "Measuring Pore Diameter Automatically"
date: 2024-04-12
url: https://discourse.slicer.org/t/35458
---

# Measuring pore diameter automatically

**Topic ID**: 35458
**Date**: 2024-04-12
**URL**: https://discourse.slicer.org/t/measuring-pore-diameter-automatically/35458

---

## Post #1 by @ahmad_alminnawi (2024-04-12 13:40 UTC)

<p>Hello,</p>
<p>I have CT scans of porous tissues and I created segmentation for my ROI. I usually have multiple pores even if the ROI is small (as in the picture) and I want to measure the diameter of these pores.<br>
I saw there was a similar thing in VMTK to calculate cross-sectional area of vessels but I am not sure it is the same as what I want since here there is no “main vessel” to get its Centerline plus I don’t want to do it by hand.</p>
<p>I was thinking something more like random point assignment in the segmentation and growing a circle in 2D (or sphere in 3D) to reach the boundary of the segment.</p>
<p>Is there a way in 3dslicer to do so? can you please provide me the code for it as I don’t use the GUI.</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e56d2f4390ccaaecef516016f6249eafae336d5.png" data-download-href="/uploads/short-url/6BVYXKGbrSKyndBwBiBg15Kmg7j.png?dl=1" title="Screenshot 2024-04-12 153158" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e56d2f4390ccaaecef516016f6249eafae336d5_2_690x389.png" alt="Screenshot 2024-04-12 153158" data-base62-sha1="6BVYXKGbrSKyndBwBiBg15Kmg7j" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e56d2f4390ccaaecef516016f6249eafae336d5_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e56d2f4390ccaaecef516016f6249eafae336d5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e56d2f4390ccaaecef516016f6249eafae336d5.png 2x" data-dominant-color="838382"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-12 153158</span><span class="informations">943×532 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
