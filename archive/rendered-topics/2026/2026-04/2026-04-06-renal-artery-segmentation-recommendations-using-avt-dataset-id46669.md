---
topic_id: 46669
title: "Renal Artery Segmentation Recommendations Using Avt Dataset"
date: 2026-04-06
url: https://discourse.slicer.org/t/46669
---

# Renal Artery Segmentation: Recommendations using AVT Dataset

**Topic ID**: 46669
**Date**: 2026-04-06
**URL**: https://discourse.slicer.org/t/renal-artery-segmentation-recommendations-using-avt-dataset/46669

---

## Post #1 by @kryspiechicken (2026-04-06 12:21 UTC)

<p>Hey everyone!</p>
<p>I’m just starting with Slicer3D, any recommendations for renal artery segmentations? Currently working on a BME project of comparison of endovascular paths (radial versus femoral) access to renal arteries, just until the ostium.</p>
<p>I’m having some trouble in extracting centerlines from segmentations. The dataset being used is <a href="https://figshare.com/articles/dataset/Aortic_Vessel_Tree_AVT_CTA_Datasets_and_Segmentations/14806362" rel="noopener nofollow ugc">Aortic Vessel Tree</a>, specifically the KiTS collection (K1, K4, K5, K6, K7) as the ones I identified with left or right renal artery in their segmentation, may be wrong tho. Anatomy being considered proximal subclavian (as radial in), proximal common illiac (as femoral in) and left and/or right renal artery.</p>
<p>How can I extract centerlines from these segmentations or can I add additional segmentations to it or would you recommend other dataset for this approach?</p>
<p>I’m open for any suggestions</p>

---

## Post #2 by @lassoan (2026-04-06 12:22 UTC)

<p>You can extract vessel centerline very quickly and robustly using VMTK extension.</p>

---
