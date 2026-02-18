# reslicing nifti(.nii) file

**Topic ID**: 1662
**Date**: 2017-12-14
**URL**: https://discourse.slicer.org/t/reslicing-nifti-nii-file/1662

---

## Post #1 by @NaglisR (2017-12-14 20:00 UTC)

<p>Hey everyone,</p>
<p>I am working with nii files (head MRI scans) that i 1)open and save in 3D Slicer as nii.gz 2)Load the nii.gz file with python  and take a certain number of slices from the 3D numpy array (for example the 10 slices from the axial view). 3)Then I construct a nii image to save using the saved original nii affine transformation data. However after saving it isn’t properly displayed if I load the resliced nii file into Slicer. The whole code basically looks like this:</p>
<pre><code class="lang-auto">image = nib.load(file_name_MRI)
original_image_affine = image.affine
image = image.get_data()
resliced = image[:,60:70,:]
resliced_nii_image = nib.Nifti1Image(resliced, original_img_affine)
nib.save(resliced_nii_image, path_to_save_destination)
</code></pre>
<p>So my question is how can I save the resliced nii image (what affine data should I use when saving) in the way that it is correctly/ displayed in 3D Slicer?<br>
Thanks in advance!</p>

---

## Post #2 by @ihnorton (2017-12-14 20:17 UTC)

<p>Could you please post a full example of the issue using e.g. the MRhead dataset, or one of the [NIfTI test datasets](<a href="https://nifti.nimh.nih.gov/nifti-1/data">https://nifti.nimh.nih.gov/nifti-1/data</a>.</p>

---
