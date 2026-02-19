---
topic_id: 24082
title: "Segmentation Of Thin Vessels"
date: 2022-06-27
url: https://discourse.slicer.org/t/24082
---

# Segmentation of thin vessels

**Topic ID**: 24082
**Date**: 2022-06-27
**URL**: https://discourse.slicer.org/t/segmentation-of-thin-vessels/24082

---

## Post #1 by @sannpeterson (2022-06-27 18:38 UTC)

<p>Thank you for the suggestion. Can you give me tips for smaller vessels? Some arteries are very thin and hypoplastic. More automated methods tend to miss these types of vessels.</p>

---

## Post #2 by @lassoan (2022-06-27 19:16 UTC)

<p>You can use Grow from seeds effect for smaller vessels, too, you just need to paint more seeds: with your initial seeds some vessel segments will be missed, so you paint a few more, which will result in some noise to be detected as vessels, so you need to paint scribbles there with the “non-vessel” segment, and do this iteratively until you get all the vessels you need, without noise.</p>
<p>If the vessels are very small then you can simplify segmentation by doing subtraction. See <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/">this segmentation recipe</a>.</p>

---
