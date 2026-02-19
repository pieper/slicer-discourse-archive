---
topic_id: 2258
title: "Fine Tuning Linking Function Between Windows"
date: 2018-03-07
url: https://discourse.slicer.org/t/2258
---

# Fine-tuning linking function between windows

**Topic ID**: 2258
**Date**: 2018-03-07
**URL**: https://discourse.slicer.org/t/fine-tuning-linking-function-between-windows/2258

---

## Post #1 by @drusmanbashir (2018-03-07 14:32 UTC)

<p>Hi,<br>
Osirix has a handy function that allows you to manually set up your windows with any adjusted windowing, zoom, and position and then when you link the windows it preserves those transformations in each window. E.g., i am viewing PET and MRI done separately in two windows and set them at the same level. but when i link them the MRI disappears because its origin etc… at at different location to the PET.</p>
<p>Thanks<br>
Usman Bashir</p>

---

## Post #2 by @lassoan (2018-03-07 14:52 UTC)

<p>Have you tried to actually register them instead? You can use Fiducial registration wizard module in SlicerIGT extension to mark 3 corresponding points in each image, and apply the computed output transform to the “from” image.</p>
<p>I’m not sure if you’ve found that you can then enable hot-link between slices (long-press on link slices), which links pan, zoom, etc. between slices.</p>
<p>Let us know if you need more detailed instructions.</p>

---

## Post #3 by @drusmanbashir (2018-03-07 16:02 UTC)

<p>Ok thanks I’ll give that a try</p>

---
