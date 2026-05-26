---
topic_id: 47095
title: "Obscuring Bone Removal For 3D Viz Of Cardiac Cta"
date: 2026-05-20
url: https://discourse.slicer.org/t/47095
---

# Obscuring Bone Removal for 3D Viz of Cardiac CTA

**Topic ID**: 47095
**Date**: 2026-05-20
**URL**: https://discourse.slicer.org/t/obscuring-bone-removal-for-3d-viz-of-cardiac-cta/47095

---

## Post #1 by @Deep_Learning (2026-05-20 13:48 UTC)

<p>Basically trying to automatically mask the spine and ribs. Or Mask everything but the spine and ribs.</p>
<p>Thresholding is not good. Need to retain all heart calcium and blood..</p>
<p>TotalSegmentator does not completely segment the ribs.  Nothing is perfect.</p>
<p>Tried Skellytor, first results were not very good.</p>
<h2><a name="p-133906-tried-to-segment-the-lungs-and-heart-in-totalsegmentator-then-shrinkwrap-does-not-work-perfectly-1" class="anchor" href="#p-133906-tried-to-segment-the-lungs-and-heart-in-totalsegmentator-then-shrinkwrap-does-not-work-perfectly-1" aria-label="Heading link"></a>Tried to segment the lungs and heart in TotalSegmentator, then shrinkwrap.  Does not work perfectly…</h2>
<p>Is there a reliable opensource solution to mask the heart and lungs in SOTA Cardiac CTA?</p>

---

## Post #2 by @Deep_Learning (2026-05-26 11:46 UTC)

<p>There is a task in totalsegmentator called trunk_cavities which looks good for this.</p>

---
