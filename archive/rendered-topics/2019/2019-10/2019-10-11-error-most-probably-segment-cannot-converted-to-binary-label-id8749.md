# error most probably segment cannot converted to binary label map 3d

**Topic ID**: 8749
**Date**: 2019-10-11
**URL**: https://discourse.slicer.org/t/error-most-probably-segment-cannot-converted-to-binary-label-map-3d/8749

---

## Post #1 by @Pinar_Uskaner_Hepsag (2019-10-11 18:52 UTC)

<p>I want to save my annotations as a binary volume in common medical imaging formats (e.g. nifti). After I annotated tumor areas in breast MRIs, I tried to export binary label map. But it gives error : Failed to export segments to labelmap. I want to get a binary mask of each slice which are annotated. How can I do that? Why I cannot export to binary labelmap?</p>

---

## Post #2 by @lassoan (2019-10-11 18:54 UTC)

<p>Could you please attach the application log (menu: Help / Report a bug).</p>

---

## Post #3 by @Pinar_Uskaner_Hepsag (2019-10-17 11:34 UTC)

<p>Thanks! It is solved. I think I saved binary masks in .nrrd file format. I am very new in using 3D Slicer so I have another question. I have brain MRi images. I have segmented those slices and save them in nrrd file format. How can I visualize those original slices and their  binary masks. How can I see each slice and its mask? Is there a python code for this? Because I need to use each original slice and its binary mask for automatic segmentation. I will train a U-Net model using those slices and binary masks.</p>

---
