---
topic_id: 18824
title: "Export Dicom As Tif 16Bit Problems"
date: 2021-07-20
url: https://discourse.slicer.org/t/18824
---

# Export DICOM as tif 16bit problems

**Topic ID**: 18824
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/export-dicom-as-tif-16bit-problems/18824

---

## Post #1 by @ibl3d (2021-07-20 19:16 UTC)

<p>Hello everyone, I wanted to comment on a couple of problems<br>
How can I export a serie of DICOM files to a serie of individual 16b tif files.<br>
When I try it I get a multi-image TIFF with broken levels.</p>
<p>When I try to export in any other type of image file I get error</p>
<p>on the other hand, when I import a series of tiff 16b files and<br>
export it as Dicom, I also get errors in the levels when I open it in another Dicom reader<br>
Thanks in advance and excuse my english<br>
IBL</p>

---

## Post #2 by @ibl3d (2021-07-20 20:37 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/268bcf9ae988ddc34b00c22e7cb1889380e7225c.jpeg" data-download-href="/uploads/short-url/5uZGCDQp9WRUKMvYiWu9ji0qdFa.jpeg?dl=1" title="Slice_01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/268bcf9ae988ddc34b00c22e7cb1889380e7225c_2_245x500.jpeg" alt="Slice_01" data-base62-sha1="5uZGCDQp9WRUKMvYiWu9ji0qdFa" width="245" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/268bcf9ae988ddc34b00c22e7cb1889380e7225c_2_245x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/268bcf9ae988ddc34b00c22e7cb1889380e7225c_2_367x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/268bcf9ae988ddc34b00c22e7cb1889380e7225c_2_490x1000.jpeg 2x" data-dominant-color="292A2C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slice_01</span><span class="informations">664×1354 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77736b345883c061d7c397afaf5df18a107ae208.jpeg" data-download-href="/uploads/short-url/h2I6md5o3yt5Ysq8voBsyf2x1KE.jpeg?dl=1" title="Slice_02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77736b345883c061d7c397afaf5df18a107ae208_2_500x500.jpeg" alt="Slice_02" data-base62-sha1="h2I6md5o3yt5Ysq8voBsyf2x1KE" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77736b345883c061d7c397afaf5df18a107ae208_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77736b345883c061d7c397afaf5df18a107ae208.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77736b345883c061d7c397afaf5df18a107ae208.jpeg 2x" data-dominant-color="BDBDBD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slice_02</span><span class="informations">512×512 81.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @ibl3d (2021-07-20 20:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41e0f5a655dce87d6a3d6e301f4aea5a137ac7c6.jpeg" data-download-href="/uploads/short-url/9oN0zuDfSY8IeLVihFcSIU73z7M.jpeg?dl=1" title="Slice_03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e0f5a655dce87d6a3d6e301f4aea5a137ac7c6_2_690x387.jpeg" alt="Slice_03" data-base62-sha1="9oN0zuDfSY8IeLVihFcSIU73z7M" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e0f5a655dce87d6a3d6e301f4aea5a137ac7c6_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e0f5a655dce87d6a3d6e301f4aea5a137ac7c6_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/41e0f5a655dce87d6a3d6e301f4aea5a137ac7c6_2_1380x774.jpeg 2x" data-dominant-color="373841"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slice_03</span><span class="informations">2557×1437 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2021-07-20 21:15 UTC)

<p>It might be that your data is not compatible with tiff.  It looks like a datatype wrap-around issue or simillar.  I tried saving and reloading the MRHead sample data and although the orientation information was not preserved the images looked fine.  You could start by looking at what’s different in the Volume Information between that data and yours.</p>
<p>By the way, tiff is not a good format for saving volumetric data (not only because the orientation is lost, but also because only supports limited data types) so Slicer’s implementation may not be the best.  If you must use tiff maybe better to find a dedicated tool that people use a lot to work with tiff, like ImageMagick or FIJI.</p>

---

## Post #5 by @lassoan (2021-07-20 21:56 UTC)

<p>For many years many groups have been desperately trying to make TIFF work for biomedical imaging, but it has become obvious that it is just a too complicated and too limited format.</p>
<p>It has never been usable for 3D images because it does not have standard fields for storing slice spacing or axis directions.</p>
<p>TIFF has been used for microscopy imaging, but due to failure of bigtiff and other reasons even the microscopy people are moving away from it now and developing OME-Zarr instead.</p>
<p>For 3D images, I would recommend to use NRRD format. It is extremely simple yet sufficient for most applications, and has readers/writers in all environments.</p>

---

## Post #6 by @ibl3d (2021-07-20 22:10 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="18824">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It might be that your data is not compatible with tiff. It looks like a datatype wrap-around issue or simillar. I tried saving and reloading the MRHead sample data and although the orientation information was not preserved the images looked fine. You could start by looking at what’s different in the Volume Information between that data and yours.</p>
<p>By the way, tiff is not a good format for saving volumetric data (not only because the orientation is lost, but also because only supports limited data types) so Slicer’s implementation may not be the best. If you must use tiff maybe better to find a dedicated tool that people use a lot to work with tiff, like ImageMagick or FIJI</p>
</blockquote>
</aside>
<p>Thank you very much for your answer, I will study it</p>

---

## Post #7 by @ibl3d (2021-07-20 22:11 UTC)

<p>Thanks a lot Andrass</p>

---
