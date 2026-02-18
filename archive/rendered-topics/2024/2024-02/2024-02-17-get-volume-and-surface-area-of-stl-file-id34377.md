# Get volume and surface area of STL file

**Topic ID**: 34377
**Date**: 2024-02-17
**URL**: https://discourse.slicer.org/t/get-volume-and-surface-area-of-stl-file/34377

---

## Post #1 by @Esraa_El-Mekkawy (2024-02-17 02:55 UTC)

<p>how to import an stl file and to detect its surface area and volume</p>

---

## Post #2 by @rfenioux (2024-02-19 10:49 UTC)

<p>You can fine explanations in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file" rel="noopener nofollow ugc">the documentation</a> on how to import an stl model as a segmentation.</p>
<p>Then go to the segment statistics module to compute volume / areas. Again, I invite you to read <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" rel="noopener nofollow ugc">the documentation of this module</a>.</p>

---
