---
topic_id: 46516
title: "Areas Where I Cant Draw In Ct Scans"
date: 2026-03-20
url: https://discourse.slicer.org/t/46516
---

# areas where I can't draw in ct scans

**Topic ID**: 46516
**Date**: 2026-03-20
**URL**: https://discourse.slicer.org/t/areas-where-i-cant-draw-in-ct-scans/46516

---

## Post #1 by @RDLmomo (2026-03-20 14:34 UTC)

<p>Hi Forum, just wanna ask you if you have any suggestions. Sometimes in specific areas of the CTs in the segmentation, I can’t draw on them, I tried many times to change setting but it’ s like I cannot write them, do you have any suggestion?</p>
<p>Bests, thanks in advance</p>

---

## Post #2 by @mikebind (2026-03-20 15:41 UTC)

<p>Two possibilities come to mind.  One is that you have masking settings activated such that those areas are not editable.  Read over this page to understand how they work: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#masking-options" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a> .  The other possibility is that your segmentation geometry does not include all of your CT image.  Your segmentation geometry is the grid of voxels that you are painting on for all of your segments.  By default this grid is set by the first image volume you use when creating the first segment; if this image volume was not your CT and did not fully cover your CT, there will be regions of your CT which you cannot paint on (those regions which are outside the segmentation geometry)  This can be fixed by adjusting the segmentation geometry using the “specify geometry” button next to the “Source volume” selector (see further up on the reference page here <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a> ) .  If neither of those fixes your issue, report back and we can troubleshoot some more.</p>

---
