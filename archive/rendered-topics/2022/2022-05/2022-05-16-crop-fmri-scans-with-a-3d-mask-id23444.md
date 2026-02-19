---
topic_id: 23444
title: "Crop Fmri Scans With A 3D Mask"
date: 2022-05-16
url: https://discourse.slicer.org/t/23444
---

# Crop fMRI scans with a 3D mask

**Topic ID**: 23444
**Date**: 2022-05-16
**URL**: https://discourse.slicer.org/t/crop-fmri-scans-with-a-3d-mask/23444

---

## Post #1 by @AdrienW (2022-05-16 15:32 UTC)

<p>Hello,</p>
<p>I’m working on python 3.9.<br>
I would like the crop the skull of fMRI scans based on a mask created based on anatomical data. The dimensions of the mask is 181 x 217 X 181. My fMRI scans are 4D time-series data with dimensions 61 X 73 X 61 X 180.<br>
First, I resampled the mask using:</p>
<p>resampled_mask = nilearn.image.resample_to_img(fmri, mask, interpolation = ‘nearest’).</p>
<p>Is this a good method to compute a mask or should I recompute a mask directly on epi images?</p>
<p>Then, I’m looking for cropping regions of my fMRI images that are outside of the mask to recreate 3D sequence of scans but I did not find any functions on nilearn to do that (nilearn.masking.apply_mask outputs a 2D matrix of features as a function of time but I would like an output of dimension x, y, z, time)</p>
<p>Thanks per advance.</p>

---

## Post #2 by @lassoan (2022-05-17 00:03 UTC)

<p>By “cropping the skull”, you mean skull stripping (set voxel values outside the brain to 0) or you want to crop the image with a box-shaped ROI (crop and resample the image)?</p>
<p>There are tools for both of these operations in Slicer that work automatically (taking into account image position, orientation, axis directions, and extents - keeping everything correctly in the same physical space). The only limitation is that currently Slicer cannot read 4D Nifti files One option would be to convert to NRRD files (Slicer supports reading 4D NRRD files), or you could split the 4D Nifti file into several 3D files. We could consider adding 4D Nifti support to Slicer if there is a strong supporting use case (e.g., a project that would use this feature extensively).</p>

---

## Post #3 by @pieper (2022-05-17 15:06 UTC)

<p>I have a draft of 4D nifti support for DWI.  The gradient directions are not correct yet, but the same approach should work for non-diffusion 4D nifti.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/compare/master...pieper:nifiio">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/compare/master...pieper:nifiio" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/63a4a35cb9b01cbbb2a8792531abb86626f7a4310fcc4bb44e2a8036d682fdcd/SlicerDMRI/SlicerDMRI" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerDMRI/SlicerDMRI/compare/master...pieper:nifiio" target="_blank" rel="noopener">Comparing SlicerDMRI:master...pieper:nifiio · SlicerDMRI/SlicerDMRI</a></h3>

  <p>Diffusion MRI analysis and visualization in 3D Slicer open source medical imaging platform. - Comparing SlicerDMRI:master...pieper:nifiio · SlicerDMRI/SlicerDMRI</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @AdrienW (2022-05-30 20:47 UTC)

<p>I found a solution using nilearn to compute mask epi for all the time series, apply them to all volumes iteratively and then concatenate all volumes into a time series. The last part is to crop 0 values and to resample all time series to the same dimensions.</p>
<pre><code class="lang-auto">import numpy as np
import nibabel as nib
import nilearn
from nilearn.image import resample_to_img as res
from nilearn.masking import compute_epi_mask
from nilearn.image import iter_img
from nilearn.image import math_img
from nilearn.image import concat_imgs
from nilearn.image import crop_img

for f in file_list:
    fmri = nib.load(f)
    mask = nilearn.masking.compute_epi_mask(fmri)
    filename = f[:-17] + "masked.nii"
    masked_list = []
    
    for img in iter_img(fmri):
        masked = math_img('img*mask', img = img, mask=mask)
        masked_list.append(masked)
        
    final = concat_imgs(masked_list)
    crop = crop_img(final)
    print(crop.shape)
    crop_resampled = res(crop, example, interpolation = 'nearest')
    print(crop_resampled.shape)  
    crop_resampled.to_filename(filename)
</code></pre>

---
