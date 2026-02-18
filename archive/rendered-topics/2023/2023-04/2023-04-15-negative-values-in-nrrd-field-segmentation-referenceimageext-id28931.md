# Negative values in nrrd field 'Segmentation_ReferenceImageExtentOffset' 

**Topic ID**: 28931
**Date**: 2023-04-15
**URL**: https://discourse.slicer.org/t/negative-values-in-nrrd-field-segmentation-referenceimageextentoffset/28931

---

## Post #1 by @Megan (2023-04-15 16:02 UTC)

<p>When reading in a .seg.nrrd file in python using pynrrd, I get a negative value in the ‘Segmentation_ReferenceImageExtentOffset’  field (‘35 86 -1’). Are negative values relative to the end of the volume e.g. work backwards from the last pixel in that array or are they e.g. 1 voxel before the volume?</p>

---

## Post #2 by @lassoan (2023-04-15 16:10 UTC)

<p>This field stores the start extent of the segmentation binary labelmap representation. In VTK the start extent can be any integer value triplet while it is (0,0,0) in NRRD files. You can simply ignore this field because the standard NRRD fields correctly specify the image geometry in physical space.</p>

---
