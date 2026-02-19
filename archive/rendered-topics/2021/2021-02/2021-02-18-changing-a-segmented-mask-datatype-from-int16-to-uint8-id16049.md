---
topic_id: 16049
title: "Changing A Segmented Mask Datatype From Int16 To Uint8"
date: 2021-02-18
url: https://discourse.slicer.org/t/16049
---

# Changing a segmented mask datatype from int16 to uint8

**Topic ID**: 16049
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/changing-a-segmented-mask-datatype-from-int16-to-uint8/16049

---

## Post #1 by @Abdulrahman (2021-02-18 01:08 UTC)

<p>Hi,<br>
I’ve exporting a segmented mask of brain in nifti format, which is int16, for CNN segmentation using Matlab, however, pixel Label Datastore only supports pixel label image files with uint8 data.<br>
Is there anyway to convert the segmented mask from int16 to uint8?</p>
<p>Thanks</p>

---

## Post #2 by @Abdulrahman (2021-02-19 00:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Can you help with that Dr?</p>

---

## Post #3 by @lassoan (2021-02-19 03:57 UTC)

<p>You can cast read the nifti file into Matlab and then cast it to int8.</p>
<p>I would not recommend to use Matlab, though. 10-20 years ago Matlab was probably the best development environment for numerical computing, but the world moved on. Nowadays you are generally much better off with using Python.</p>

---

## Post #4 by @Abdulrahman (2021-02-19 04:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks a lot</p>

---
