---
topic_id: 3562
title: "After Saving The Segmentation Re Editing The Data"
date: 2018-07-23
url: https://discourse.slicer.org/t/3562
---

# After saving the segmentation re-editing the data

**Topic ID**: 3562
**Date**: 2018-07-23
**URL**: https://discourse.slicer.org/t/after-saving-the-segmentation-re-editing-the-data/3562

---

## Post #1 by @aksu (2018-07-23 13:48 UTC)

<p>Operating system:MacOS 10.13.6<br>
Slicer version:4.8.1<br>
After saving the segmentation, I couldn’t re-edit or add another segmentation to data.<br>
How could I fix that problem?<br>
Thank you</p>

---

## Post #2 by @cpinter (2018-07-23 14:11 UTC)

<p>First of all, please use a recent nightly, because a lot of development has happened since the 2017 October release of 4.8.1, including around segmentations.</p>
<p>If you save a segmentation to nrrd.seg, and load it back as a segmentation, then you should be able to edit it, as long as you have a CT/MRI/etc volume in the scene as well that you select as master in Segment Editor.</p>

---

## Post #3 by @caolong (2018-07-26 01:45 UTC)

<p>In my opinion ,you should save the file" segmentation seg.nrrd" if you use  segment editor.When you want to re-edit next time ,you can drag three files including CT or MRI nrrd file ,segmentation-label nrrd file and the segmentation seg.nrrd file to the new open slicer,then you can re-editor by segment editor.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c69f9b15a7af18be5dab786697b2a0c150020ee9.jpeg" alt="image" data-base62-sha1="sl6uz4T6VSz6XFs0XJImipsvbeN" width="534" height="172"></p>

---

## Post #4 by @lassoan (2018-07-26 03:53 UTC)

<p>If you leave the segmentation node’s master representation at the default <em>binary labelmap</em> then it is enough to save the scalar volume (CT, MRI, … .nrrd file) and segmentation node (… .seg.nrrd file).</p>

---
