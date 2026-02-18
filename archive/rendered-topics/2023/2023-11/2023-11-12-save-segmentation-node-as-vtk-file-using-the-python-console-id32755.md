# Save Segmentation Node as VTK file using the Python Console

**Topic ID**: 32755
**Date**: 2023-11-12
**URL**: https://discourse.slicer.org/t/save-segmentation-node-as-vtk-file-using-the-python-console/32755

---

## Post #1 by @jhernandezr (2023-11-12 12:21 UTC)

<p>Hi there!<br>
Me and my team are trying to develop a code where we export automatically as vtk segmentatino nodes, however we are not able to do so.<br>
To be specific, we have a label node with the same structure as the segmentation node, in case it is easier to export as vtk the label node instead of the segmentation node.<br>
Inside the Segmentation node, we have a hierarchy called ‘jake’ corresponding to the only segmentation that is in blue.<br>
We would highly appreciate your help if you were able to save the segmentation as vtk. Thank you all in advance!</p>

---

## Post #2 by @lassoan (2023-11-13 02:36 UTC)

<p>Last time we checked .vtk file format could not store image orientation, which prevented it to be used for the medical image computing. Therefore, I don’t think anyone plans to enable saving or exporting of segmentations into .vtk file format.</p>
<p>If you have absolutely no other choice than to use .vtk format then you can export the segmentation to a labelmap volume and save that as .vtk.</p>

---
