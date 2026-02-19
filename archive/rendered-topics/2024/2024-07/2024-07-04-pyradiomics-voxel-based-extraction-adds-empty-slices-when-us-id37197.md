---
topic_id: 37197
title: "Pyradiomics Voxel Based Extraction Adds Empty Slices When Us"
date: 2024-07-04
url: https://discourse.slicer.org/t/37197
---

# Pyradiomics voxel-based extraction adds empty slices when using rectangular mask

**Topic ID**: 37197
**Date**: 2024-07-04
**URL**: https://discourse.slicer.org/t/pyradiomics-voxel-based-extraction-adds-empty-slices-when-using-rectangular-mask/37197

---

## Post #1 by @davidpalomino6 (2024-07-04 15:21 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 4.11<br>
Expected behavior: I am trying to get the radiomic maps based on the voxel-based extraction provided by pyradiomics. In addition, I am trying to obtain the radiomics map in a rectangular region (in 3 dimensions) defined in my CT. For this, I use the pyradiomics extractor by telling it the original image, the mask (rectangular region) and the voxel-based parameter set to true. My configuration file for the extraction is as follows (leaving by default all acquisition parameters, including discretization and specifying only a resampling to isotropic voxel size [1x1x1]):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e09bb3d263d3272b1a350af5800892e0d15ff5d8.png" alt="image" data-base62-sha1="w2YxKh3d9cySfKBSKscTEevkO48" width="380" height="220"></p>
<p>The expected behavior would be to be able to obtain a radiomap resampled to [1x1x1] spacing and having the same dimensions as the rectangular segmentation mask provided to the extractor.</p>
<p>Actual behavior:<br>
When I try to visualize the volume of the radiomics map obtained in 3D Slicer on the original CT and the defined rectangular segmentation mask, I find that pyradiomics has added empty slices to the volume of the radiomics map at the margins (in red):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16b8fdca761ccd6ca23dcbf6e752a39928df1958.jpeg" data-download-href="/uploads/short-url/3f0Qu4C1N6vAKnHpCzhzJZIuR2o.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16b8fdca761ccd6ca23dcbf6e752a39928df1958_2_690x455.jpeg" alt="image" data-base62-sha1="3f0Qu4C1N6vAKnHpCzhzJZIuR2o" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16b8fdca761ccd6ca23dcbf6e752a39928df1958_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16b8fdca761ccd6ca23dcbf6e752a39928df1958_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16b8fdca761ccd6ca23dcbf6e752a39928df1958.jpeg 2x" data-dominant-color="A4A8BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1264×834 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why is this behavior? Does it have to do with the volume resampling?  The documentation for the pyradiomics resample_image function details the following information:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fcf2d96d590ba746d2e38183289d48966b559f4.png" data-download-href="/uploads/short-url/mNJNhciqsBGRVSaPVOkfDO8oigc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fcf2d96d590ba746d2e38183289d48966b559f4.png" alt="image" data-base62-sha1="mNJNhciqsBGRVSaPVOkfDO8oigc" width="633" height="500" data-dominant-color="2A2624"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">709×560 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
