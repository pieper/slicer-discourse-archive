# Interactive lung lobe segmentation fails with NIFTI volume

**Topic ID**: 24052
**Date**: 2022-06-26
**URL**: https://discourse.slicer.org/t/interactive-lung-lobe-segmentation-fails-with-nifti-volume/24052

---

## Post #1 by @rbumm (2022-06-26 13:27 UTC)

<p>Hi,</p>
<p>I am trying to generate lung lobe labels for a MONAI Label segmentation with the “Interactive Lobe Segmentation”.</p>
<p>With a COV-19 lung CT demo dataset (as well as with the Slicers “CTChest” demo)  I get:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/461e2fc415d6dbac133196e7e2f7d22fdb188333.jpeg" data-download-href="/uploads/short-url/a0i62nwlI6yI2NSD1QFZvaD4uTp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/461e2fc415d6dbac133196e7e2f7d22fdb188333_2_405x500.jpeg" alt="image" data-base62-sha1="a0i62nwlI6yI2NSD1QFZvaD4uTp" width="405" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/461e2fc415d6dbac133196e7e2f7d22fdb188333_2_405x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/461e2fc415d6dbac133196e7e2f7d22fdb188333_2_607x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/461e2fc415d6dbac133196e7e2f7d22fdb188333.jpeg 2x" data-dominant-color="404441"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">632×779 92.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>… which is reasonable.</p>
<p>When I load data from MONAI Labels “Task06Lung” dataset (which obviously is a NIFTI volume) the interactive lobe segmentation is not correct:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14b4a3d8aebec9311d6d31e14e401f11f84ac126.jpeg" data-download-href="/uploads/short-url/2XazgLv0ZNQkuUSpYdEoQ448EFo.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14b4a3d8aebec9311d6d31e14e401f11f84ac126_2_405x500.jpeg" alt="image" data-base62-sha1="2XazgLv0ZNQkuUSpYdEoQ448EFo" width="405" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14b4a3d8aebec9311d6d31e14e401f11f84ac126_2_405x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14b4a3d8aebec9311d6d31e14e401f11f84ac126_2_607x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14b4a3d8aebec9311d6d31e14e401f11f84ac126.jpeg 2x" data-dominant-color="3B4247"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">628×775 96.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The file name: lung_001.nii.gz</p>
<p>Do I need to convert the volume?</p>
<p>PS: The “Lung CT Segmenter” works well in both cases.</p>

---

## Post #2 by @rbumm (2022-06-26 13:36 UTC)

<p>“Volume” for “DemoChestCT” (lobe segmentation working) shows:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a06b2b93c6c5cca2dd216732b689968ae4fe68e0.png" alt="image" data-base62-sha1="mT80oFmmkjby11DtrjuPKtuonx6" width="652" height="412"></p>
<p>Volume for lung_001.nii.gz (lobe segmentation not working) shows:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1481d54fa15c185b43ca4cee69e2433b5f083ada.png" alt="image" data-base62-sha1="2VpInKBr4DxYC9VYReS3OZ4pT4K" width="635" height="419"></p>
<p>Two things I tried and that had no effect:</p>
<ul>
<li>Export the NIFTI Volume as DICOM dataset, then reload the DICOM</li>
<li>Load the NIFT volume and “Cast scalar volume” to integer</li>
</ul>

---

## Post #3 by @lassoan (2022-06-26 20:13 UTC)

<p>This lung_001.nii.gz image seems to be quite unusual, i.e., messed up.</p>
<ol>
<li>
<p>Float scalar type does not make sense for clinical CTs, so change that to <code>short</code>. Do not choose <code>Int</code>, as that would be 32 bits per voxel, which would be unusual, too.</p>
</li>
<li>
<p>The IJK coordinate system is a left-handed coordinate system (determinant of the IJK to RAS direction matrix is negative, so the transformation turns the volume inside out). You can fix this by resampling the volume using Crop volume module with the default settings (you don’t need to crop away any part of the volume, you just take advantage of that <code>Interpolated cropping</code> enables resampling and the module always uses right-handed coordinate system for IJK).</p>
</li>
<li>
<p>Nifti is for brain imaging. For general imaging purposes, use nrrd instead. Nifti has many issues, for example it is very easy to mess up the image orientation (as it is stored in Nifti in a complex, redundant way and interpretation of non-trivial cases is inconsistent between different applications).</p>
</li>
</ol>

---

## Post #4 by @rbumm (2022-06-26 20:45 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a><br>
Did as advised:</p>
<ul>
<li>changed (with “Cast Scalar Volume” module) the scalar type to short</li>
<li>resampled the volume. There is still the circled “1” in the Matrix which is “-1” in all working cases …</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1ffbf8d087116765b8c74a47bdc02d4c5a65e588.png" alt="image" data-base62-sha1="4yWEeAUJpnQ80kDiE5jKKigKxC0" width="638" height="417"></p>
<p>Unfortunately still no lobes detected:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ae298c0901a3b85862653354155253267bd1b4a.jpeg" alt="image" data-base62-sha1="jODn4iTcNBO7wctNe4zPI5UUkm6" width="605" height="376"></p>

---

## Post #5 by @rbumm (2022-06-26 21:03 UTC)

<p>Link to a folder containing the initial file is here:<br>
<a href="https://drive.google.com/drive/folders/1-5MlZWz9wbqLsHuaQq81-4HUWwCnJxPs?usp=sharing" class="onebox" target="_blank" rel="noopener">https://drive.google.com/drive/folders/1-5MlZWz9wbqLsHuaQq81-4HUWwCnJxPs?usp=sharing</a></p>

---
