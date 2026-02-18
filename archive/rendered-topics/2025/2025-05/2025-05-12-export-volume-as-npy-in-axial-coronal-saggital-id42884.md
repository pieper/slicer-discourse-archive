# Export volume as .npy in Axial, Coronal, Saggital

**Topic ID**: 42884
**Date**: 2025-05-12
**URL**: https://discourse.slicer.org/t/export-volume-as-npy-in-axial-coronal-saggital/42884

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-05-12 10:13 UTC)

<p>Hi to everyone.</p>
<p>I am currently working with brain MRI DICOM files and, for further post processing pipelines, I would like to export it as npy. files. When I do that (programmatically) I found that the each volume is orient as the original acquisition (for example if the sequence was a T1 coronal, the first dimension in the npy will be the coronal…)</p>
<p>To optimize the automatization I would like to export all the volumes as Axial, Coronal, Sagittal.</p>
<p>Is this possible? How can I do it in Python?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @muratmaga (2025-05-12 15:27 UTC)

<p>Not sure how you writing the npy, but you can try reordering the dimensions prior to writing.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2025-05-13 06:55 UTC)

<p>I think the solution is use Orient Scalar Volume module, that allows me set the output orientation of of the volume and the I can export it as a npy file with <code>arrayFromVolume(volumeNode)</code></p>

---

## Post #4 by @lassoan (2025-05-13 12:49 UTC)

<p>MONAI provides well-tested tools to conveniently address common needs like this. For example, in deep learning pipelines usually there is an <a href="https://docs.monai.io/en/stable/transforms.html#orientationd">Orientationd</a> transform that can reorder or resample the voxel array to be bring all images to a canonical orientation. The transform can also compute the inverse operation to get output in the original space.</p>

---
