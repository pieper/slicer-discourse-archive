# Recommended Segmentation Strategy from Aorta to Upper Brain Arteries

**Topic ID**: 20019
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/recommended-segmentation-strategy-from-aorta-to-upper-brain-arteries/20019

---

## Post #1 by @riro3277 (2021-10-05 12:15 UTC)

<p>I am trying to create an artery segmentation from the aorta curve to upper brain but am having great trouble filtering away skull and bones without losing upper brain arteries. I have looked at many different methods but can’t seem to get them to work. Any recommended methods?</p>

---

## Post #2 by @lassoan (2021-10-05 16:10 UTC)

<p>Contrasted vessels and bone have very similar image intensity, so simple global thresholding will not separate them. However, it should be easy to separate them using “Grow from seeds” effect as described in <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/">this segmentation recipe</a>.</p>
<p>                    <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/image-006.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/image-006.png" width="690" height="438">
          </a>

</p>

---
