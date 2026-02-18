# Voxel-based finite element modeling

**Topic ID**: 11223
**Date**: 2020-04-21
**URL**: https://discourse.slicer.org/t/voxel-based-finite-element-modeling/11223

---

## Post #1 by @Vasyl (2020-04-21 09:57 UTC)

<p>Hy everybody!<br>
I’m only a beginner in segmentation and meshing models and I have one precise question: how can I create voxel-based FE model.<br>
I’ve already read some articles dedicated to this topic (<a href="https://github.com/lassoan/SlicerSegmentMesher" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerSegmentMesher: Create volumetric mesh from segmentation using Cleaver2 or TetGen</a>; <a href="https://discourse.slicer.org/t/generate-a-voxel-based-mesh/2159" class="inline-onebox">Generate a voxel-based mesh</a>; Image to Finite Element Mesh: An End to End Workflow) but haven’t found some algorithm how to do it.<br>
I need to create bone-cartilage model according to its density (based on Housefield units) and to get multi-colored mesh.<br>
In older article, there is an algorithm of how to do it using IA-FEMesh extension, but in current version of 3D-Slicer this extension isn’t available. I’ve installed two extensions designed for my purpose (CleaverTetMesher and SegmentMesher). I can create only one-colored mesh using these tools, but I need multi-colored (like at picture).<br>
Can anyone explain me how to do it or give some links for tutorials.<br>
Thanks in advance!!<br>
<a href="/uploads/short-url/hTu7zjazQYHFzpAB91uM2PCWeYz.jpeg">Screenshot_2|562x361</a></p>

---

## Post #2 by @lassoan (2020-04-22 03:02 UTC)

<p>Once you have created a mesh using Segment Mesher module, you can use <code>Probe volume with model</code> module to assign Hounsfield unit to each point of the mesh. If you want to see the scalar values then choose to show it in Models module / Scalars section.</p>
<p>There was a bug with unstructured grid reading in Slicer Preview Release but I’ve pushed a fix today, so tomorrow’s version should work well.</p>

---

## Post #3 by @Vasyl (2020-04-22 08:09 UTC)

<p>Thank you so much for youк advise! It works!<br>
But I have other questions)<br>
First:<br>
do I need voxel-based FE model (it means each mesh segment corresponds to each specific voxel and the number of mesh elements is the same as a number of voxels) or I may just use fine mesh model (with scale-parameter =0.8 or 0.9) and each mesh element will get an average value of all included voxels?<br>
Second:<br>
is it possible to create a uniform mesh-model (it means that all elements have the same sizes), because in my model all the elements are different (example on a picture).<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb5019fcb64fab9f78daad3b3128cbb9f1036b0.jpeg" data-download-href="/uploads/short-url/8WJpgk5IQwOZMLe0V5AqQUYQTvO.jpeg?dl=1" title="Pelvis_mesh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eb5019fcb64fab9f78daad3b3128cbb9f1036b0_2_664x500.jpeg" alt="Pelvis_mesh" data-base62-sha1="8WJpgk5IQwOZMLe0V5AqQUYQTvO" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eb5019fcb64fab9f78daad3b3128cbb9f1036b0_2_664x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb5019fcb64fab9f78daad3b3128cbb9f1036b0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eb5019fcb64fab9f78daad3b3128cbb9f1036b0.jpeg 2x" data-dominant-color="737286"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Pelvis_mesh</span><span class="informations">894×673 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-04-22 13:38 UTC)

<p>You can configure Cleaver’s element sizing very flexibly. You can even choose to use constant element size.</p>
<p>If you don’t need a smoot surface mesh then you can create an unstructured grid from an image by using vtkThreshold filter (few lines of Python code). If you need cell data (scalars associated to a volumetric mesh element) then you can run <a href="https://vtk.org/doc/nightly/html/classvtkPointDataToCellData.html">vtkPointDataToCellData</a> on your mesh.</p>

---

## Post #5 by @Vasyl (2020-04-22 15:46 UTC)

<p>Thanks a lot for your help!!!</p>

---

## Post #6 by @Vasyl (2020-04-23 12:34 UTC)

<p>Good afternoon!<br>
I’ve tried to create one-size elements using ‘Segment Mesher’ but failed(<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d91e45b8f856a778ebae8806e03190db0fa0fca8.jpeg" data-download-href="/uploads/short-url/uYIt60M04bjJHDAXnGTxQrArrzW.jpeg?dl=1" title="Screenshot_4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d91e45b8f856a778ebae8806e03190db0fa0fca8_2_690x397.jpeg" alt="Screenshot_4" data-base62-sha1="uYIt60M04bjJHDAXnGTxQrArrzW" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d91e45b8f856a778ebae8806e03190db0fa0fca8_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d91e45b8f856a778ebae8806e03190db0fa0fca8_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d91e45b8f856a778ebae8806e03190db0fa0fca8_2_1380x794.jpeg 2x" data-dominant-color="B1B1BC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_4</span><span class="informations">1439×828 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Can you advise me, please, which criteria I should change to make elements uniform?</p>

---

## Post #7 by @lassoan (2020-04-24 00:32 UTC)

<p>I guess you have run out of memory. You may need to increase <code>--scale</code> value to make the mesh smaller or increase virtual memory size in your operating system settings.</p>
<p>If you really just want to have an unstructured grid where each voxel is an element then you can use vtkThreshold filter (but I’m not sure if this kind for mesh is suitable for FEA).</p>

---
