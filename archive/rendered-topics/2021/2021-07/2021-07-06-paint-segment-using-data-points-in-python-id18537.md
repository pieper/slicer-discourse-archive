# Paint Segment Using Data Points in Python

**Topic ID**: 18537
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/paint-segment-using-data-points-in-python/18537

---

## Post #1 by @tpereira (2021-07-06 17:31 UTC)

<p>Hi, so I have a series of (x,y,z) data points. I want to create a segmentation that will use paint to set the location and paint a sphere with a diameter of 3 at that location using code. I would be adding this to an existing segmentation of the spine. The circle location does not have to be super exact so I could round to the nearest existing pixel in the image. Would appreciate any guidance I am very new at this. Thank you!</p>

---

## Post #2 by @lassoan (2021-07-09 05:17 UTC)

<p>You can create spheres and import them into the segmentation. See complete example <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b#file-segmentgrowcutsimple-py-L10-L34">here</a>. You can find many more examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>

---
