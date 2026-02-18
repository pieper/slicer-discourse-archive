# Loading multiple MRI series (T1, T2, FLAIR, ...) under one subject

**Topic ID**: 29096
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/loading-multiple-mri-series-t1-t2-flair-under-one-subject/29096

---

## Post #1 by @laurentletg (2023-04-24 21:05 UTC)

<p>Hello,</p>
<p>I am currently working on the BraTS dataset with different MRI sequences (T1, T2, FLAIR, T1CE) saved as separate *.nii.gz files. I am trying to write a script that can load all sequences under a subject so that the segmentation can be seen in all sequences. It is also possible that there is a better way to do this.</p>
<p>I found how to load a single sequence using</p>
<blockquote>
<p>slicer.util.loadVolume(path_to_single_file)</p>
</blockquote>
<p>But I’d like to create a parent subject that contains all segmentations (programmatically).</p>
<p>Thanks a lot for your help!</p>

---

## Post #2 by @lassoan (2023-04-26 22:13 UTC)

<p>Slicer does not support reading 3D+t NIFTI files. You could convert them to 4D NRRD files (read using nibabel and write using pynrrd Python packages). However, since the BraTS image files contain unrelated 3D volumes (they are not a volume sequence but independent acquisitions with very different properties), it is probably more appropriate to save them as separate 3D images.</p>

---
