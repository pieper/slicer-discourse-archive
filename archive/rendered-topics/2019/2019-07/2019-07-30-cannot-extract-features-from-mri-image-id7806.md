# Cannot extract features from MRI image

**Topic ID**: 7806
**Date**: 2019-07-30
**URL**: https://discourse.slicer.org/t/cannot-extract-features-from-mri-image/7806

---

## Post #1 by @TingtingYu (2019-07-30 06:01 UTC)

<p>Hi,</p>
<p>I tried to extract features from MRI volume using Radiomics module but it did not work. However, features can be extracted from CT volume. I use the same contour as input region.May I know why feature cannot be extracted from MRI volume?</p>
<p>Best,<br>
Tingting</p>

---

## Post #2 by @pieper (2019-08-01 18:29 UTC)

<p>Hi - The images might need to be <a href="https://pyradiomics.readthedocs.io/en/latest/faq.html#geometry-mismatch-between-image-and-mask" rel="nofollow noopener">resampled</a> to the same space.  If you need more help describe the steps you took to prepare the data.</p>

---

## Post #3 by @TingtingYu (2019-08-02 04:11 UTC)

<p>Hi Steve,</p>
<p>Thank you for your help. I still cannot extract the features. There are two ways I tried to extract features.</p>
<p>The first one is to extract features without any image processing (MRI image coordinate was already registered to CT coordinate), I chose MRI image as Input Image Volume, GTV as input region to extract features.</p>
<p>The second one is to extract features after image resampling. MRI image was resampled using linear interpolation to 1mm x 1mm x 1mm voxel size. Then I created the GTV binary labelmap and resampled this binary labelmap using nearestNeighbor to the same resolution, which is also 1 mm x 1 mm x 1 mm. I used the resampled MRI image as Input Image Volume, resampled GTV binary labelmap as Input Region. And features still cannot be extracted.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92dcd90b0350364bed5c9fcd873a3a9c077a0cf6.png" alt="image" data-base62-sha1="kXcSfn6VApGfIQNJ4d8Ec3f2ol0" width="409" height="267"></p>
<p>I checked the python interactor and found this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05727fdc311e06f482f62e65513122377073427a.png" data-download-href="/uploads/short-url/MbHtNtRamnbIQ6G3iiL5FEtujM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05727fdc311e06f482f62e65513122377073427a.png" alt="image" data-base62-sha1="MbHtNtRamnbIQ6G3iiL5FEtujM" width="690" height="277" data-dominant-color="F7FBF7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">993×399 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,<br>
Tingting</p>

---

## Post #4 by @pieper (2019-08-02 12:16 UTC)

<p>Hi Tingting -</p>
<p>Looks like there’s still something wrong with the coordinate systems and the label must not be in the same space with the MR.  The error message indicates that it’s trying to resample but the mask ROI is bigger than the image space.  You can doublecheck in the Volumes module and if there’s a mismatch you can <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Resampling" rel="nofollow noopener">resample</a> and use the MR as the reference (<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/BRAINSResample" rel="nofollow noopener">e.g. for BRAINSResample</a>).</p>
<p>-Steve</p>

---

## Post #5 by @TingtingYu (2019-08-05 04:23 UTC)

<p>Hi Steve,</p>
<p>Thank you for your help and quick response. I first checked the resampled MRI image and the mask ROI using Volume module. They were not in the same origin even I transformed the MRI image. Then I resampled the mask ROI in the Resample Image (Brains). Finally I set the resampled image as Input Image and resampled gtv binary labelmap as Input region, no feature was calculated.</p>
<p>Best,<br>
Tingting</p>
<p>Resampled MRI image in Volume module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/415ae180eb1092829237e44df4db8c873a2dca5b.png" data-download-href="/uploads/short-url/9k9KjhFUDwuop9cCKy6KGXf7eyf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/415ae180eb1092829237e44df4db8c873a2dca5b.png" alt="image" data-base62-sha1="9k9KjhFUDwuop9cCKy6KGXf7eyf" width="664" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×506 14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
GTV, binary labelmap in Volume module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/027d25dd541bbcc764d3117f58ec75279aa7f281.png" data-download-href="/uploads/short-url/m159qCuhh1H6cbZanyVRvlhdrr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/027d25dd541bbcc764d3117f58ec75279aa7f281.png" alt="image" data-base62-sha1="m159qCuhh1H6cbZanyVRvlhdrr" width="651" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">666×511 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Resample GTV in Resample Image (Brains)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83231182da31f667d8b48d46ae12a5c873f1da21.png" data-download-href="/uploads/short-url/iI5GiTEW97NnJ6onELjZecL5N0l.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83231182da31f667d8b48d46ae12a5c873f1da21.png" alt="image" data-base62-sha1="iI5GiTEW97NnJ6onELjZecL5N0l" width="601" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">680×565 16.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2019-08-05 16:13 UTC)

<p>Your resampling parameters look good - the output volume <code>mri-gtv-1mm</code> should end up with the same volume information (origin, spacing, directions) as <code>resample-1mm</code> - is that not happening?  Once that’s set then you should be able to extract features using those volumes.</p>

---

## Post #7 by @TingtingYu (2019-08-06 07:51 UTC)

<p>Hi Steve,</p>
<p>Thank you. I tried the nightly-built version, it worked now. Thank you!</p>
<p>Best,<br>
Tingting</p>

---
