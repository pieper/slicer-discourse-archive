# Rodent skull stripping

**Topic ID**: 2677
**Date**: 2018-04-24
**URL**: https://discourse.slicer.org/t/rodent-skull-stripping/2677

---

## Post #1 by @djrowland (2018-04-24 19:39 UTC)

<p>Hello,<br>
I am interested in performing skull stripping and bias corrections for rodent data from a Bruker scanner. Since I have become comfortable with Slicer and working with DTI data in it, I was hoping that there might be some good tools in Slicer for these two additional steps. As well as a good how to guide.</p>
<p>Any suggestions would be appreciated.</p>
<p>Thanks<br>
Doug</p>

---

## Post #2 by @lassoan (2018-04-25 01:48 UTC)

<p>SwissSkullStripper extension should work well for rodent skulls. You just need to provide a pair of rodent MRI and corresponding labelmap that contains only the brain in <code>Atlas</code> section of the module. You can create a brain labelmap by manually segmenting the brain using Segment editor module and then exporting the segment to a labelmap. Let us know if it worked.</p>
<p>You can perform bias correction using “N4ITK MRI Bias correction” module.</p>

---

## Post #6 by @lassoan (2022-06-11 01:17 UTC)

<p>4 posts were split to a new topic: <a href="/t/canine-skull-stripping/23820">Canine skull stripping</a></p>

---
