---
topic_id: 12979
title: "Segmentation Of Maxillary Teeth From Mri"
date: 2020-08-13
url: https://discourse.slicer.org/t/12979
---

# Segmentation of Maxillary Teeth from MRI 

**Topic ID**: 12979
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/segmentation-of-maxillary-teeth-from-mri/12979

---

## Post #1 by @Maddy_Gamble (2020-08-13 16:01 UTC)

<p>Operating system: Mac<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello 3-D Slicer community,</p>
<p>I would like to use this particular software to segment maxillary teeth from an MRI scan. The problem is that teeth in an MRI have such a low signal. The program seems to be able to segment high-signal areas, but not low signal areas. The MR-Default preset is showing me the soft tissues as opposed to harder tissues. Is there a different preset I should be using? How can I segment the teeth from my MRI scan? Thank you for the feedback!</p>

---

## Post #2 by @lassoan (2020-08-13 16:12 UTC)

<p>Probably with simple direct volume rendering you won’t get too far, because air has low signal, too, and you won’t be able to simply crop it away. Instead you need to use Segment Editor module, to segment the teeth. You can try painting a few seeds and use Grow from seeds effect. More information: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">segmentation overview</a>, <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training?section=16#Segmentation">tutorials</a>. I would also recommend to update to latest Slicer Preview Release, as it has lots of improvements in segmentation modules.</p>

---
