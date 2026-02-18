# Any way to edit before converting to segmentation node?

**Topic ID**: 30196
**Date**: 2023-06-23
**URL**: https://discourse.slicer.org/t/any-way-to-edit-before-converting-to-segmentation-node/30196

---

## Post #1 by @telomere (2023-06-23 14:09 UTC)

<p>I loaded my STL file as model and I tried to convert it to segmentation nodes in a data module but slicer got freezed because the my STL file is too heavy.<br>
So I want to cut unneccessary part away before converting it to segmentation nodes but don’t know how…<br>
Is there any other way to make model editable without converting to segmentation nodes?</p>
<p>Thanks for help.</p>

---

## Post #2 by @pieper (2023-06-23 14:30 UTC)

<p>You should be able to use the Dynamic Modeler for this.  It takes some practice but it’s very powerful.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dynamicmodeler.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dynamicmodeler.html</a></p>

---

## Post #3 by @lassoan (2023-06-24 14:27 UTC)

<p>You can also try to use the Uniform remeshing and Decimation tools in Surface Toolbox module to reduce the number of points in the mesh.</p>
<p>However, I’m not sure if the problem is really in the input mesh file. Even if the mesh contains millions of points, you may just need to wait a little longer to convert it to labelmap. It is more likely that you are trying to create a too high resolution labelmap out of your mesh and you run out of memory. If you open the STL file as segmentation (in “Add data” window select Description → Segmentation) then the labelmap resolution will be chosen automatically so that the conversion should be successful on an average computer.</p>

---
