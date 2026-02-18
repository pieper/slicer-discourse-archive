# Importing PLY file with color scale associated to a numerical "user scalar"

**Topic ID**: 37543
**Date**: 2024-07-24
**URL**: https://discourse.slicer.org/t/importing-ply-file-with-color-scale-associated-to-a-numerical-user-scalar/37543

---

## Post #1 by @JiB (2024-07-24 12:33 UTC)

<p>Operating system: Windows 10 Enterprise<br>
Slicer version: 5.6.2<br>
Expected behavior: Display Colors Corresponding to Facet User Defined Values<br>
Actual behavior: No Color</p>
<p>Hi to the 3D Slicer community.</p>
<p>This post is in relation with <a href="https://discourse.slicer.org/t/importing-ply-with-color/5500">Importing PLY with Color</a></p>
<p>I have been struggling quite a lot trying to import a PLY file containing a model with a numerical (float32) “user scalar” (called “myscalar”) associated with each model’s facet into 3D Slicer.</p>
<p>The model is nicely displaying but I am trying without success to apply a color table corresponding to this scalar value.<br>
I even feel like my user scalar is not considered at all by 3D slicer.</p>
<p>What I managed to do is to correctly display colors for a given RGB triplet associated to each facet in the PLY file but, then, I find complicated to link back this color to my user scalar that I would like to be shown in the color  legend.</p>
<p>Here is the header of my PLY file :</p>
<p><em>ply</em><br>
<em>format ascii 1.0</em><br>
<em>element vertex 1576</em><br>
<em>property float32 x</em><br>
<em>property float32 y</em><br>
<em>property float32 z</em><br>
<em>element face 394</em><br>
<em>property list uint8 int32 vertex_indices</em><br>
<em>property float32 <strong>myscalar</strong></em><br>
<em>end_header</em></p>
<p>Would anybody on this forum be so kind to help me displaying my model with a color scale corresponding to my user scalar variation through the model facet ?</p>

---
