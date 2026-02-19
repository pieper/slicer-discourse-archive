---
topic_id: 36321
title: "How To Measure Volume Of White Matter Hippocampus Pituitary"
date: 2024-05-22
url: https://discourse.slicer.org/t/36321
---

# How to measure volume of white matter, hippocampus, pituitary and grey matter?

**Topic ID**: 36321
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/how-to-measure-volume-of-white-matter-hippocampus-pituitary-and-grey-matter/36321

---

## Post #1 by @GIANNIS (2024-05-22 13:15 UTC)

<p>Can I measure the volume of white matter, hippocampus, pituitary and grey matter?</p>

---

## Post #2 by @LeidyMoraV (2024-05-29 14:26 UTC)

<p>I think you can do the segmentation of the areas that you’re interested and then segment statistics module for measure the volume.</p>

---

## Post #3 by @GIANNIS (2024-05-29 16:17 UTC)

<p>How? Can you show me?</p>

---

## Post #4 by @LeidyMoraV (2024-05-29 21:47 UTC)

<p>You can use grow from seeds tool in the Segment editor module (ex: <a href="https://www.youtube.com/watch?v=S5tOn_AxrbM" rel="noopener nofollow ugc">Brain segmentation in 3D Slicer via mask scalar volume (youtube.com)</a>). And after having the final segmentation, you can calculate the volume of each segment (ex: <a href="https://www.youtube.com/watch?v=fM_rxfDTRi0" rel="noopener nofollow ugc">Segment statistics - new module in 3D Slicer - YouTube</a>)</p>

---
