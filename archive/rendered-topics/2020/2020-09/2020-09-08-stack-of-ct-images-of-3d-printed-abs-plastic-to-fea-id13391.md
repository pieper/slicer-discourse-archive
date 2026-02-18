# Stack of CT images of 3D printed ABS plastic to FEA

**Topic ID**: 13391
**Date**: 2020-09-08
**URL**: https://discourse.slicer.org/t/stack-of-ct-images-of-3d-printed-abs-plastic-to-fea/13391

---

## Post #1 by @aandonian (2020-09-08 13:57 UTC)

<p>Dear all,</p>
<p>I have 8 tiff files that make up slices of a section of 3D printed ABS  plastic. I would like to use the stack of images to create a volume, segment the pores in the plastic, and export for FEA in Abaqus. FEA in Abaqus will be to test the stress and strains of a porous material.</p>
<p>If there is a tutorial on this please let me know.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2020-09-08 18:59 UTC)

<p>You can create a surface mesh form the images in <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">Segment Editor module</a>. Then you can either save the surface mesh as stl/ply/obj and create the volumetric mesh in other software; or create a volumetric mesh using <a href="https://github.com/lassoan/SlicerSegmentMesher#segment-mesher-extension">Segment Mesher extension</a> and import the volumetric mesh from vtk or vtu format.</p>

---
