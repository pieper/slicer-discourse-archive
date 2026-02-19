---
topic_id: 40134
title: "Resizing Segmentation Area"
date: 2024-11-11
url: https://discourse.slicer.org/t/40134
---

# Resizing segmentation area

**Topic ID**: 40134
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/resizing-segmentation-area/40134

---

## Post #1 by @mohammad_jafari (2024-11-11 21:30 UTC)

<p>Hello everyone thanks for this great community, i recently labeled segmentations for a deep learning project via 3d slicer segment editor module ,the original size of the reference volume is 256x256x175 each slice has 256 H and 256 W .after labeling tumor structures and saving them , during training of my model i realized that the size of input images are consuming memory and i want to reduce the size of the image (i.e. from 256x256x175 to , my concern is some of high details about the labeled areas will be lost in python ,  what modules in 3d slicer can i use to achieve the best results ? thank you</p>

---

## Post #2 by @lassoan (2024-11-11 21:33 UTC)

<p>You can adjust the segmentation geometry by following <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">these instructions</a>, just specify larger spacing instead of smaller spacing.</p>
<p>Of course, if you make the resolution of the segmentation coarser then small details may be lost.</p>

---

## Post #3 by @mohammad_jafari (2024-11-12 18:26 UTC)

<p>Thank you for responding.</p>

---
