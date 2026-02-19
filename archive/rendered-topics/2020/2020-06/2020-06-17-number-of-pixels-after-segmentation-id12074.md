---
topic_id: 12074
title: "Number Of Pixels After Segmentation"
date: 2020-06-17
url: https://discourse.slicer.org/t/12074
---

# Number of pixels after segmentation

**Topic ID**: 12074
**Date**: 2020-06-17
**URL**: https://discourse.slicer.org/t/number-of-pixels-after-segmentation/12074

---

## Post #1 by @cotozakot (2020-06-17 16:47 UTC)

<p>Can I read the number of pixels / voxels somewhere after segmentation? Not only their volume, I mean their quantity. So far, I have been able to obtain results from the Segment Statistic module.</p>

---

## Post #2 by @lassoan (2020-06-17 17:18 UTC)

<p>What quantity would you be interested in? Number of voxels? Bounding box size in mm or voxels? Segment Statistics module should provide you all these.</p>

---

## Post #3 by @cotozakot (2020-06-17 17:39 UTC)

<p>Thank you very much for your answer! I have one more question, where<br>
can I find information on the size of the voxels?</p>

---

## Post #4 by @Andinet_Enquobahrie (2020-06-18 10:45 UTC)

<p>size of the voxel = Image spacing in X  * Image spacing in Y * Image spacing in Z direction</p>
<p>You can find image spacing information in the Volumes module</p>
<p>Or from the Segment Statistics module, you can calculate the size in mm^3 as follows</p>
<p>Volume [mm^3] / Number of voxels</p>
<p>-Andinet</p>

---
