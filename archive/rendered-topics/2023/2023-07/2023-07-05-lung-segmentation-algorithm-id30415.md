# Lung Segmentation Algorithm

**Topic ID**: 30415
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/lung-segmentation-algorithm/30415

---

## Post #1 by @Nima_Yousefi (2023-07-05 18:20 UTC)

<p>Hi,</p>
<p>I’m using 3D Slicer for Lung segmentation and I’ve done that using LungCtSegmenter.</p>
<p>Can you tell me what algorithm is used for this task in slicer?</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a><br>
<a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Best Regards.</p>

---

## Post #2 by @rbumm (2023-07-06 05:36 UTC)

<p>We are placing 13 markups (3 right coronal, 3 left coronal, 3 right sagittal, 3 left sagittal, and one in the trachea.<br>
Then the grow-from-seeds effect of the segment editor is used with a special lung threshold.</p>
<p>Alternatively, you can create the segmentation touch-free with lungmask AI or TotalSegmenter AI, or even MONAILabel.</p>
<p>See <a href="https://www.researchsquare.com/article/rs-3027617/v5">some more descriptions here</a>.</p>

---
