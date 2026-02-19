---
topic_id: 2689
title: "Fragmental Bone"
date: 2018-04-25
url: https://discourse.slicer.org/t/2689
---

# fragmental bone

**Topic ID**: 2689
**Date**: 2018-04-25
**URL**: https://discourse.slicer.org/t/fragmental-bone/2689

---

## Post #1 by @Patrycja_Grygny (2018-04-25 17:31 UTC)

<p>Operating system: MacOS<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
Hi,<br>
I have a cremation material which is located in the Popiel during the Pomeranian culture period. Itry to crop a fragments and do 3D. The program doesn’t see a single bones. Ceramics ashtray treats as bones. In small fragments he doesn’t read at all.<br>
How can I deal with it? Anyone have an idea?<br>
Please help.</p>

---

## Post #2 by @lassoan (2018-04-25 18:54 UTC)

<p>Probably you need to segment out bone fragments and separate from other dense materials using Segment editor. Start with simple Thresholding effect then clean up using Scissors, Smoothing, etc.</p>
<p>If bone fragments are visible just occluded by more dense materials then you can remove those irrelevant outer regions using Mask volume effect and after that you might be able to create 3D visualization without further segmentation - using volume rendering.</p>
<p>If you can share an image we can give more specific advice.</p>

---
