# Wrong output volume using Model to LabelMap

**Topic ID**: 18750
**Date**: 2021-07-15
**URL**: https://discourse.slicer.org/t/wrong-output-volume-using-model-to-labelmap/18750

---

## Post #1 by @jean-marie_bonny (2021-07-15 14:16 UTC)

<p>Dear 3D slicer community<br>
I have a question relating to the Model to labelmap module. I generated a .vtp model with the RATS software. Under 3dslicer, the model looks correct and the segmentation overlaps well with the image volume input. However, it is not possible to convert the model into a nifti image with the module. All the image voxels are 0. What did I do wrong?<br>
Thanks,<br>
JMb</p>

---

## Post #2 by @lassoan (2021-07-15 14:31 UTC)

<p>The most robust way of converting model to labelmap volume is to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">import the model to segmentation</a> and then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">export the segmentation to labelmap</a>.</p>

---

## Post #3 by @jean-marie_bonny (2021-07-18 19:36 UTC)

<p>Thank you for the advise. However if import the model to segmentation goes well, the export still leads to a blank image. Can you tell me how to find a solution?</p>

---

## Post #4 by @lassoan (2021-07-19 13:44 UTC)

<p>It means that the reference volume is not at the right place. You can fill the voxels of the reference volume and display it using volume rendering to see where you placed it.</p>

---
