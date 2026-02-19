---
topic_id: 6883
title: "Graphcutsegment Extension"
date: 2019-05-22
url: https://discourse.slicer.org/t/6883
---

# GraphCutSegment extension

**Topic ID**: 6883
**Date**: 2019-05-22
**URL**: https://discourse.slicer.org/t/graphcutsegment-extension/6883

---

## Post #1 by @Thomas (2019-05-22 12:36 UTC)

<p>My Extension Manager (version 4.10.0) can’t find GraphCutSegment extension. How can I fix it and install this extension? Thank you for advices.</p>

---

## Post #2 by @lassoan (2019-05-22 12:47 UTC)

<p>It is built into the Segment Editor module (“Grow from seeds effect”). Always use latest stable version (currently 4.10.1).</p>

---

## Post #3 by @Thomas (2019-05-22 13:09 UTC)

<p>I thought Grow from seeds effect is based on Grow cut algorithm.</p>

---

## Post #4 by @lassoan (2019-05-22 17:50 UTC)

<p>The methods are formulated differently but in practice they produce similar results. If there is good contrast difference between structures then any method can separate them automatically. If there is no contrast difference in some regions then it is not possible to automatically separate, and you need to explicitly label segments in those regions. Very small errors or leaks may be addressed by regularization (enforcing smoothness).</p>
<p>Grow from seeds effect has the huge advantage over all other implementations that it is quick to initialize and subsequent incremental updates are immediate. Its limitation is that it does not provide any regularization. If you need to control boundary smoothness then you may use Watershed effect (provided by SegmentEditorExtraEffects extension).</p>
<p>You could probably dig up additional methods, but Grow from seeds and Watershed effects mostly cover all the general semi-automatic interactive segmentation use cases. To do significantly better, you would probably need to incorporate application-specific prior knowledge (classic shape models, neural networks, etc.).</p>
<p>What would you like to segment on what kind of images?</p>

---

## Post #5 by @Thomas (2019-05-22 20:53 UTC)

<p>Thank you for the clearing. I would like to segment abdominal adipose from MR images, so I’m just testing which approach would be the best.</p>

---
