---
topic_id: 24458
title: "Importing Label Maps With Multivolumeimporter As Segmentatio"
date: 2022-07-22
url: https://discourse.slicer.org/t/24458
---

# Importing label maps with MultiVolumeImporter as segmentations

**Topic ID**: 24458
**Date**: 2022-07-22
**URL**: https://discourse.slicer.org/t/importing-label-maps-with-multivolumeimporter-as-segmentations/24458

---

## Post #1 by @pitfall24 (2022-07-22 20:11 UTC)

<p>I have a series of nifti files which form a 4D sequence. Using MultiVolumeImporter/Explorer I was able to view the volumes perfectly. However I also have a series of corresponding segmentations in the same nifti format which I would like to be able to import as label maps so that I can view them along with their matching volumes. I was also wondering whether it would be feasible to create closed surface representations of the segmentations as well?</p>

---

## Post #2 by @lassoan (2022-07-23 05:53 UTC)

<p>MultiVolume can conveniently replay a sequence of up to two scalar volumes and plot time-density curves - but nothing more. That’s why we developed <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html">Sequences</a> module, which can replay any kind of nodes (not just volumes but segmentations, transforms, markups, etc.), any number of them (not just two), can do it synchronized (e.g., for each volume show the corresponding segmentation), can also record changes, etc.</p>
<p>You can create a sequence from segmentation nodes in Sequences module’s Edit tab as described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#creating-sequences-from-a-set-of-nodes">documentation</a>.</p>

---
