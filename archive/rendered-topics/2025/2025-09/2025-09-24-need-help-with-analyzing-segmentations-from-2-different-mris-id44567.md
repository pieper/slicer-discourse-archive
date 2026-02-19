---
topic_id: 44567
title: "Need Help With Analyzing Segmentations From 2 Different Mris"
date: 2025-09-24
url: https://discourse.slicer.org/t/44567
---

# Need help with analyzing segmentations from 2 different MRIs :( 

**Topic ID**: 44567
**Date**: 2025-09-24
**URL**: https://discourse.slicer.org/t/need-help-with-analyzing-segmentations-from-2-different-mris/44567

---

## Post #1 by @Mc_Konni (2025-09-24 02:16 UTC)

<p>Hi Guys,</p>
<p>i am completely new to 3D Slicer, i have tried to solve the following issue for a couple of days and im honestly about to give up. Heres my issue:</p>
<p>Im conducting research with ULF MR Imaging and have segmentated lesions in those using itk Snap. Now im trying to compare those segmentations with segmentations made from HighField MRIs, but i dont know how <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=14" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"> . If anyone got any ideas, please let me know!</p>
<p>Best regards<br>
Konni</p>

---

## Post #2 by @cpinter (2025-09-24 11:05 UTC)

<p>First of all, I suggest that you use Slicer for segmentation. It has more advanced segmentation tools than ITKSnap.</p>
<p>Second, what kind of comparison are you looking for? If quantitative, Dice and Hausdorff metrics are available in the SlicerRT extension (SegmentComparison module). Let us know otherwise.</p>

---
