---
topic_id: 35307
title: "Fiducial Registration Wizard Only Fiducials Move Not Segment"
date: 2024-04-05
url: https://discourse.slicer.org/t/35307
---

# Fiducial Registration Wizard:only fiducials move, not segmentation

**Topic ID**: 35307
**Date**: 2024-04-05
**URL**: https://discourse.slicer.org/t/fiducial-registration-wizard-only-fiducials-move-not-segmentation/35307

---

## Post #1 by @ILB (2024-04-05 09:12 UTC)

<p>Hi!<br>
Can anyone tell me why when I try to registrate a segmentation with the CT image, after establishing the markups, the only things that move after the registration is the markups themselves, but not the segmentation? I need to align the segmentation obtained in another series with the current one.<br>
Thank you!</p>

---

## Post #2 by @cpinter (2024-04-05 09:28 UTC)

<p>Have you set the output transform as parent transform to the segmentation? In the Data module you can see a Transforms column, right-click on the icon that shows the identity transform (3x3 grid aligned) and choose the transform. The icon will change to a rotated grid.</p>

---
