# MultivolumeExplorer for 4D NIFTI image

**Topic ID**: 37856
**Date**: 2024-08-13
**URL**: https://discourse.slicer.org/t/multivolumeexplorer-for-4d-nifti-image/37856

---

## Post #1 by @Aylin (2024-08-13 14:02 UTC)

<p>Hello,<br>
I am trying to open Multivolume data (T2*) using 3D Slicer. My 4D volume was .nii, and the slicer could not recognize it as 4D volume, so I transferred it to multiple 3D volumes and then uploaded it using the multvolumeImporter tool. However, I still can’t do any further processing steps, like visualizing the intensity time plot, what is the possible reason for that, and what can be alternative ways to make the slicer recognize 4D volumes?</p>

---

## Post #2 by @lassoan (2024-08-15 13:44 UTC)

<p>We have struggled so much with problems due to NIFTI file format’s poor design and inconsistent implementations that we generally try to avoid it. 4D NIFTI file format is also very limited in what axis metadata can be stored in it, thereby limiting the use cases. Therefore, we have not implemented support for 4D NIFTI files in Slicer.</p>
<p>You can read 4D volume sequences from NRRD file format instead. We are adding 5D volume sequence support for NRRD files soon and 3D/4D/5D NGFF file format support is probably coming in the future (it is a more complex file format, but allows better handling of very large files). Adding 4D NIFTI support in the future is a possibility, too, but I’m not aware of any plans.</p>

---
