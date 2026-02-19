---
topic_id: 5069
title: "Slicerradiomics Contour Voxel Size"
date: 2018-12-13
url: https://discourse.slicer.org/t/5069
---

# SlicerRadiomics--contour voxel size

**Topic ID**: 5069
**Date**: 2018-12-13
**URL**: https://discourse.slicer.org/t/slicerradiomics-contour-voxel-size/5069

---

## Post #1 by @TingtingYu (2018-12-13 14:06 UTC)

<p>Hi Slicer Developer,</p>
<p>I am using SlicerRadiomics to extract features. The contour is based on CT image so the voxel size of contour matrix is the same as CT image. However, the voxel size of the Input volume (MRI image) is different from the contour matrix voxel size. So, I am wondering, during the feature calculation, will the contour will be resampled to the same voxel size of input image, and then do the feature calculation? Many thanks.</p>
<p>Best,<br>
Tingting</p>

---

## Post #2 by @fedorov (2018-12-13 15:08 UTC)

<p>You can control this in the settings, see <a href="https://pyradiomics.readthedocs.io/en/latest/customization.html#feature-extractor-level" rel="nofollow noopener">https://pyradiomics.readthedocs.io/en/latest/customization.html#feature-extractor-level</a>.</p>
<p>You should be able to set resampled voxel size in the module GUI to 0,0,0 to resample input image to the resolution of the mask. Let us know if this does not work.</p>

---

## Post #3 by @TingtingYu (2018-12-14 03:44 UTC)

<p>Hi Andrey,</p>
<p>Thank you for your reply. Actually, I want to resample contour to the resolution of input image. Could I do that easily?</p>
<p>Best,<br>
Tingting</p>

---

## Post #4 by @fedorov (2018-12-14 04:18 UTC)

<p>Yes, you can specify any resolution to use for resampling in the module interface.</p>

---

## Post #5 by @TingtingYu (2018-12-14 09:00 UTC)

<p>Hi Andrey,</p>
<p>Thank you for your quick response. I still have some confusion.</p>
<ol>
<li>
<p>In my case, contour, also named segment, is the same as mask. I generated a Labelmap Volume of segment named GTV, the voxel size is the same as CT image, which is 1.17mmx1.17mmx3mm. Then, I resampled this Labelmap Volume to a new Labelmap Volume with voxel size 0.75mmx0.75mmx1mm. However, this resampling method did not give me the right contour. Below is the screenshot, red represents the original contour, blue is the resampled contour, they have different size.</p>
</li>
<li>
<p>Thank you for sharing the link with me, I found a website from the link you shared talked about <strong>Pipeline</strong> of Radiomics, there is a function named “<strong>radiomics. imageoperations. checkMask</strong>(<em>imageNode, maskNode, <strong>kwargs</strong></em>)”, this function seems to check if the mask contains a valid ROI, which is exactly I want. So, when I choose input image and input region which is segment or mask based on CT image (they have different voxel sizes), two questions pop up. In SlicerRadiomics based on 3D slicer platform, first, will the input regions (mask) be resampled to the voxel size of input image automatically? If the answer is yes for the last question, then, will checkMask function be initialized to correct the mask if the size of resampled mask does not match the original mask automatically?</p>
</li>
</ol>
<p><strong>P.S</strong> I mention voxel size and size at the same time. To clear the confusion, voxel size is pixel spacing, size means how large it is.</p>
<p>Many thanks.</p>
<p>Best wishes,<br>
Tingting</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9cd0df12f45db21a74e717a1fdb67d07b4a5c97.jpeg" data-download-href="/uploads/short-url/qvFERVyZI8FEyCaOkylq7uHcLav.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9cd0df12f45db21a74e717a1fdb67d07b4a5c97_2_690x328.jpeg" alt="PNG" data-base62-sha1="qvFERVyZI8FEyCaOkylq7uHcLav" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9cd0df12f45db21a74e717a1fdb67d07b4a5c97_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9cd0df12f45db21a74e717a1fdb67d07b4a5c97.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9cd0df12f45db21a74e717a1fdb67d07b4a5c97.jpeg 2x" data-dominant-color="5B5A5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">837×398 68.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a href="https://pyradiomics.readthedocs.io/en/latest/radiomics.html#radiomics.imageoperations.normalizeImage" class="onebox" target="_blank" rel="noopener nofollow ugc">https://pyradiomics.readthedocs.io/en/latest/radiomics.html#radiomics.imageoperations.normalizeImage</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6406aaa8b4fb480009968c831eeea29ece7d81a.png" data-download-href="/uploads/short-url/uzmbPdCh85qxmqnkEashNb99Q6K.png?dl=1" title="Check%20Mask" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6406aaa8b4fb480009968c831eeea29ece7d81a.png" alt="Check%20Mask" data-base62-sha1="uzmbPdCh85qxmqnkEashNb99Q6K" width="598" height="500" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Check%20Mask</span><span class="informations">718×600 78.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @JoostJM (2018-12-14 14:17 UTC)

<p>As you’ve mentioned, PyRadiomics indeed checks if the geometry (i.e. spacing, size and direction) of the mask matches that of the images. By default in PyRadiomics, it throws an error if there is a mismatch.</p>
<p>By setting <code>correctMask</code> to <code>True</code>, PyRadiomics instead tries to resample the mask to the image geometry, using nearest neighbor interpolation. If correction is needed, a warning is still displayed, but extraction will not fail<br>
Only constraint here is that the bounding box of the mask has to be contained in the physical space defined by the image. If that is not the case, extraction will still fail.</p>
<p>In SlicerRadiomics, <code>correctMask</code> is already switched on  by default, as labelmaps in slicer are often represented as a cropped version of the image space (i.e. size mismatch).</p>
<p>As to you result, which functionality did you use?</p>

---

## Post #7 by @TingtingYu (2018-12-16 09:08 UTC)

<p>Hi Joost,</p>
<p>Thank you.</p>
<p>I used module named <strong>Resample Scalar Voulme</strong> to do the resampling. I tried three methods, <strong>linear, nearestNeighbor, Bspline</strong>,  and below are the results. Red represents the original mask with voxel size 1.17x1.17x3.3mm while blues are the resampled mask with voxel size 0.75x0.75x1mm. Bspline method gives the accurate boundary but some pixels inside the mask were not labeled. Will these pixels be labeled when <strong>correctMask</strong> is switched on?</p>
<p>Best,<br>
Tingting</p>
<p>linear<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f21dd8eccbd8ee76e024fda3199790ce809f483e.png" alt="linear" data-base62-sha1="yxRuIOxJzrTxpLygz3ZKp2r6TAG" width="282" height="186"><br>
Nearest Neighbor<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1f09997ebf1894c770f60b7fcabdba01baaa8dc.png" alt="nearestNei" data-base62-sha1="ywiyjrFCIu3Mnq9ekF6QUdOslRi" width="256" height="194"><br>
Bspline<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6a98083ff72f0630f7beaba0537e7e0b3541e38.png" alt="bspline" data-base62-sha1="zc4C4GcoPVAjMLyOukk5lXWKBJK" width="275" height="205"></p>

---

## Post #8 by @JoostJM (2018-12-20 07:18 UTC)

<p>Hi Tingting,</p>
<p>PyRadiomics uses nearestNeighbor to resample the mask. The interpolator that can be set in the configuration is only used for resampling the image if resampling is enabled.</p>
<p>Best,</p>
<p>Joost</p>

---

## Post #9 by @TingtingYu (2018-12-20 07:57 UTC)

<p>Hi Joost,</p>
<p>Thank you. Thank you for clearing my confusion.</p>
<p>Best wishes<br>
Tingting</p>

---
