---
topic_id: 19611
title: "Any Way To Move Segmentations To Match The Newly Registered"
date: 2021-09-10
url: https://discourse.slicer.org/t/19611
---

# Any way to move segmentations to match the newly registered volumes?

**Topic ID**: 19611
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/any-way-to-move-segmentations-to-match-the-newly-registered-volumes/19611

---

## Post #1 by @akshay_pillai (2021-09-10 16:17 UTC)

<p>I don’t know if this is possible but if it is please let me know - I created segmentations with multiple segments using 2 volumes. But I later registered or aligned the two volumes to overlap. Now I need to move the segments and segmentation also with the volumes. Is this possible? if so how?<br>
If not then I would have to create the segmentations again for the newly aligned volumes, which is what I am trying to avoid(hence the question).</p>

---

## Post #2 by @pieper (2021-09-10 17:05 UTC)

<p>You can just apply the registration transform to the segmentation.</p>

---

## Post #3 by @akshay_pillai (2021-09-10 17:11 UTC)

<p>any link or instruction as to how I might do that?</p>

---

## Post #4 by @pieper (2021-09-10 17:13 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node</a></p>

---
