---
topic_id: 31624
title: "Sublobar Pulmonary Reconstruction"
date: 2023-09-08
url: https://discourse.slicer.org/t/31624
---

# Sublobar pulmonary reconstruction

**Topic ID**: 31624
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/sublobar-pulmonary-reconstruction/31624

---

## Post #1 by @JawnyP (2023-09-08 21:32 UTC)

<p>Hi, I‘m quiet new to 3D Slicer and am looking for a way to create 3D reconstructions of pulmonary segments to be used in preoperative planing for sublobar resections.</p>
<p>Can anyone here help get closer to this goal?</p>
<p>Sincerely.</p>

---

## Post #2 by @rbumm (2023-09-09 12:34 UTC)

<p>You can try the Lung CT Analyzer extension and use their segmenter to achieve lobar segmentation and airway segmentation. There is also an airways segmentation tool in the Chest imaging platform. In the sublobar detail region, there is really not much available in Slicer and you would be more than welcome to provide lung segments for training AI tools like lungmask, TotalSegmentator, or MonaiLabel.</p>

---

## Post #3 by @JawnyP (2024-05-06 16:33 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Thanks for your quick reply.<br>
It’s taken some time for me to take the first steps here. As you mentioned there is still additional labled data needed to enhance existing tools to sublobar details.<br>
In an other thread I’v read, that you an some colleagues are training a MONAI Auto3DSeg model. Is there a way i can support your work?</p>

---
