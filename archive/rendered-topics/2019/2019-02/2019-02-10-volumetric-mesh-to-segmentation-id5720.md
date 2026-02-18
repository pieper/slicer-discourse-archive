# Volumetric mesh to Segmentation

**Topic ID**: 5720
**Date**: 2019-02-10
**URL**: https://discourse.slicer.org/t/volumetric-mesh-to-segmentation/5720

---

## Post #1 by @Hamburgerfinger (2019-02-10 16:35 UTC)

<p>Hi!  If I have a volumetric mesh, where separate regions of the mesh are defined by an associated scalar, can I import it directly into Segmentations?  (i.e. with the different scalar-defined regions as different segments).</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-02-10 18:14 UTC)

<p>There is no such feature yet. You can use a few VTK filters to do this conversion (probably 15-20 lines of Python code). Two possible approaches:</p>
<ul>
<li>get each sub-volume using threshold filter, extract surface, and then import the surface to segmentation</li>
<li>use probe filter to convert the unstructured grid to image data and import that labelmap volume to segmentation</li>
</ul>

---
