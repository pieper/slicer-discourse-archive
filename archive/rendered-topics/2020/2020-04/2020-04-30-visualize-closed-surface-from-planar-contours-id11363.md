# Visualize closed surface from planar contours

**Topic ID**: 11363
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/visualize-closed-surface-from-planar-contours/11363

---

## Post #1 by @loubna (2020-04-30 13:05 UTC)

<p>Hi;</p>
<p>How can I visualize the 3D reconstructed surface from the planar contours in 3D slicer (for exemple in 3d Slicer, we can visualize the 3D surface reconstructed from the labelMap, by clicking on view 3D which execute the marching cubes (i.e flying edges) . what about planar contours?</p>
<p>I have built slicerRt and added the additional module paths, I also loaded the RTSS series in slicer and  I have now  the planar contours. but i want convert this representation to a closed surface</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-04-30 14:55 UTC)

<p>In Segmentations module, you can choose which representation you would like to use for visualization in Display / Advanced -&gt; “Representation in 3D views” and “Representation in 2D views”. You can choose “Planar contours” representation there.</p>

---

## Post #3 by @loubna (2020-04-30 15:49 UTC)

<p>Thank you very much for the response.</p>
<p>In slicer documentation “<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a>”, it montioned that is possible to convert planar contours to labelMap for per voxel analysis . however in conversion rules repository, i dont find PlanarContoursToLabelMapConversion class ?</p>

---

## Post #4 by @lassoan (2020-04-30 16:08 UTC)

<p>Conversion happens automatically, by utilizing all available rules. Planar contour to labelmap conversion happens in two steps: 1. conversion to closed surface representation 2. conversion to binary labelmap representation.</p>

---
