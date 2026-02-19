---
topic_id: 27682
title: "Edit Segmentation Sequence"
date: 2023-02-07
url: https://discourse.slicer.org/t/27682
---

# Edit segmentation sequence

**Topic ID**: 27682
**Date**: 2023-02-07
**URL**: https://discourse.slicer.org/t/edit-segmentation-sequence/27682

---

## Post #1 by @Deep_Learning (2023-02-07 15:22 UTC)

<p>Once a segmentation sequence is created, is it possible to apply a threshold or other segmentation effects to all frames. Not frame by frame…</p>

---

## Post #2 by @lassoan (2023-02-07 17:48 UTC)

<p>Yes, but you need to write a few-line Python script for this, which iterates through the sequence. You should be able to find everything what you need in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#sequences">script repository</a>. If you cannot figure out something then feel free to ask here.</p>
<p>If users will start to ask for some segmentation sequence editing operations then we may create Segment Editor effects or modules with a GUI to implement them. However, we have been only getting a few one-off requests.</p>

---

## Post #3 by @whu (2024-12-13 06:27 UTC)

<p>Dear Iassoan, does this kind of functions has been implemented in any modules?<br>
I tried the TotalSegmentator module, it seemed support the sequence segmentations, but the installing of other packages takes too much time because of network.  Finally I can not check it.<br>
thanks.</p>

---

## Post #4 by @Deep_Learning (2024-12-27 14:05 UTC)

<p>Just a bump. Would also be nice to be able to change the color of a segment for the complete sequence.  Now only for one timepoint.  FYI, the colorize volume works great with sequences.</p>

---
