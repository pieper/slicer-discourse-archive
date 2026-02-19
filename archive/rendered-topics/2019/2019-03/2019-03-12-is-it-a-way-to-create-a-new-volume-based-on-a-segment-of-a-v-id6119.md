---
topic_id: 6119
title: "Is It A Way To Create A New Volume Based On A Segment Of A V"
date: 2019-03-12
url: https://discourse.slicer.org/t/6119
---

# Is it a way to create a new volume based on a segment of a volume

**Topic ID**: 6119
**Date**: 2019-03-12
**URL**: https://discourse.slicer.org/t/is-it-a-way-to-create-a-new-volume-based-on-a-segment-of-a-volume/6119

---

## Post #1 by @skagsoset (2019-03-12 17:15 UTC)

<p>Hey guy,</p>
<p>I am trying to remove the skull of the brain and in that case i want to make a new volume based on the segmentation i have created and the originale volume. Does anyone know if this is posible? I dont want to make a model of the segment.</p>
<p>Skagsoset</p>

---

## Post #2 by @muratmaga (2019-03-12 18:43 UTC)

<p>install the SegmentEditorExtraEffects extension, and use the MaskVolume to create a new volume of segmented structure only.</p>

---
