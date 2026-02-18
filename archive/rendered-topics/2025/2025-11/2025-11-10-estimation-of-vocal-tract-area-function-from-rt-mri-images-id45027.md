# Estimation of vocal tract area function from rt MRI images

**Topic ID**: 45027
**Date**: 2025-11-10
**URL**: https://discourse.slicer.org/t/estimation-of-vocal-tract-area-function-from-rt-mri-images/45027

---

## Post #1 by @cbbader (2025-11-10 18:56 UTC)

<p>I’m a phonetician with lots of 2D and 3D rt MRI images of the vocal tract.  Any tips on how to extract the vocal tract area function from these images?</p>

---

## Post #2 by @ebrahim (2025-11-11 05:26 UTC)

<p>Some starting points for segmentation in 3D Slicer:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox" rel="noopener nofollow ugc">Image Segmentation — 3D Slicer documentation</a>
<ul>
<li>If cross-sectional area is what you mean then: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html#how-to-get-cross-sectional-area-of-a-segment-along-a-certain-axis" class="inline-onebox" rel="noopener nofollow ugc">Segment statistics — 3D Slicer documentation</a></li>
</ul>
</li>
<li><a href="https://lassoan.github.io/SlicerSegmentationRecipes/" class="inline-onebox" rel="noopener nofollow ugc">Segmentation recipes for 3D Slicer | 3D Slicer segmentation recipes</a></li>
</ul>
<p>Can you show an example of what it looks like in a few slices, indicating what kind of structure/metrics you want to extract?</p>

---
