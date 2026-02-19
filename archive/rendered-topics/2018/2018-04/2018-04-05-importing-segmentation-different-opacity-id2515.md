---
topic_id: 2515
title: "Importing Segmentation Different Opacity"
date: 2018-04-05
url: https://discourse.slicer.org/t/2515
---

# Importing segmentation different opacity

**Topic ID**: 2515
**Date**: 2018-04-05
**URL**: https://discourse.slicer.org/t/importing-segmentation-different-opacity/2515

---

## Post #1 by @JanWitowski (2018-04-05 01:13 UTC)

<p>Hi, I didn’t find this describe before so I thought I’ll discuss it here. When I’m working on a segmentation with multiple layers, always when I import it into the Slicer it sets random opacities to random (it seems random) layers. So some of them have 0.20 opacity, while other layers have 1.00. I think it happens every single time on segmentation files with multiple layers (currently I have over 10 in one file). I’m working on nightly build 2018-03-25 but it happened before on stable releases as well. Cheers!</p>

---

## Post #2 by @cpinter (2018-04-05 14:59 UTC)

<p>Opacities are automatically set based on containment of one segment of another, so that when you load the segmentation, the outermost segment does not occlude the others, and all the segments are visible. You can turn this feature off in Application Settings / Segmentations.</p>

---
