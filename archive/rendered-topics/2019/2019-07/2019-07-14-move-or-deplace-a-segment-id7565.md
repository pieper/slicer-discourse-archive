# Move or deplace a segment

**Topic ID**: 7565
**Date**: 2019-07-14
**URL**: https://discourse.slicer.org/t/move-or-deplace-a-segment/7565

---

## Post #1 by @Jmarcs (2019-07-14 15:31 UTC)

<p>Hello is it possible to move or deplace a segment (i use meshmixer) but with 3Dslicer?</p>

---

## Post #2 by @pieper (2019-07-14 15:43 UTC)

<p>You can use transforms: <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Transforms" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/Transforms</a></p>

---

## Post #3 by @cpinter (2019-07-14 15:54 UTC)

<p>If you want to move a single segment you need to move that segment to a separate segmentation first. You can do it in the Segmentations module (not Segment Editor) by creating new segment and move segment into new segmentation. Or you can clone the segmentation in Data module and remove the ones you don’t want to move.</p>
<p>Then use Transforms as <a class="mention" href="/u/pieper">@pieper</a> suggested.</p>

---

## Post #4 by @Jmarcs (2019-07-14 16:38 UTC)

<p>thank you so much Im orthodontist and i think 3D slicer is for Nobel price</p>

---
