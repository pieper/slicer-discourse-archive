---
topic_id: 43863
title: "Work The Same Data Set On Two Computers"
date: 2025-07-28
url: https://discourse.slicer.org/t/43863
---

# Work the same data set on two computers

**Topic ID**: 43863
**Date**: 2025-07-28
**URL**: https://discourse.slicer.org/t/work-the-same-data-set-on-two-computers/43863

---

## Post #1 by @JaredAmudeo (2025-07-28 04:10 UTC)

<p>Is it possible to work with the same dataset, e.g., a stack of images, on different computers? Considering both, use Grown from Seed to optimize time. For example, a microtomography of a rodent skull fossil. Is it possible to leave the tool working on the snout in PC1 and the neurocranium in PC2, and then merge the segmentations from PC2 into PC1?</p>

---

## Post #2 by @pieper (2025-07-28 07:14 UTC)

<p>You can easily open the same volume data on multiple computers (i.e. by copying the files or using a network file server) and perform segmentation on different parts of the data in parallel.  Just be sure to save the results in different files so as not to overwrite other data.  Then later you can combine the segmentations as needed.</p>

---

## Post #3 by @JaredAmudeo (2025-07-28 07:35 UTC)

<p>How can I add the segmentations from PC2 to PC1? If I segmented the entire posterior portion of the skull on PC2 and the anterior portion on PC1, how can I add each segment (each bone) from PC2 to PC1?</p>

---

## Post #4 by @SegmenterSam (2025-07-29 08:23 UTC)

<p>I think those segmentations are just saved as a file which you can drag into the folder of the final version.</p>

---

## Post #5 by @pieper (2025-07-30 16:41 UTC)

<p>yes, and if you open two seg.nrrd files you can move/copy segments to make a single composite segmentation.</p>

---

## Post #6 by @muratmaga (2025-07-30 17:39 UTC)

<aside class="quote no-group" data-username="JaredAmudeo" data-post="1" data-topic="43863">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaredamudeo/48/77474_2.png" class="avatar"> JaredAmudeo:</div>
<blockquote>
<p>Is it possible to work with the same dataset, e.g., a stack of images, on different computers? Considering both, use Grown from Seed to optimize time. For example, a microtomography of a rodent skull fossil. Is it possible to leave the tool working on the snout in PC1 and the neurocranium in PC2, and then merge the segmentations from PC2 into PC1?</p>
</blockquote>
</aside>
<p>As others alluded this doable. But the devil is in the details. Before you do this, you need to make sure you import your imagestack correctly and at the resolution you want to work with and save it as a NRRD file. You should then use this NRRD file on those two different computers. That’s because segmentation geometry is derived from the geometry of the source volume, and using the same volume will make sure that segmentation geometries are matching and correct when you copy and paste separate segments together.</p>
<p>If you independently import the data on both computers, and then start the segmentations you would be asking for trouble.</p>

---
