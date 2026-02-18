# Problem about pixel value shift and orientation and origin between nifti and converted dicom series

**Topic ID**: 22103
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/problem-about-pixel-value-shift-and-orientation-and-origin-between-nifti-and-converted-dicom-series/22103

---

## Post #1 by @Liu_Lance (2022-02-22 06:29 UTC)

<p>Hello,<br>
I was trying to convert the nifti data to the dicom series. I figure out myself how to use the GUI of 3d slicer to export the loaded volume to dicom series. However, there are some problems in the output.<br>
1. the orientation is not correct. I reload the exported dicom series to 3d slicer to check. I found the “IJK to RAS direction Matrix” and the “image origin” is not the same as the volume I load from original nifti.<br>
2. the pixel values are not the same between the exported dicoms and original nifti. there seem to be a small value shift., however, the two image can stll overlap with each other.<br>
the problems are illustrated in the figures. Can anybody help ?<br>
The 00003_xxxxxxx is the original nifti volume.<br>
the unnamed_series is the exported dicom volume</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b51131c9f4bf6f6d32e4b9fa489cd5894890689.png" data-download-href="/uploads/short-url/jSs4leEYJ91Rh6LcPjcuL4RIHjj.png?dl=1" title="Screenshot from 2022-02-21 23-47-26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b51131c9f4bf6f6d32e4b9fa489cd5894890689_2_620x500.png" alt="Screenshot from 2022-02-21 23-47-26" data-base62-sha1="jSs4leEYJ91Rh6LcPjcuL4RIHjj" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b51131c9f4bf6f6d32e4b9fa489cd5894890689_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b51131c9f4bf6f6d32e4b9fa489cd5894890689.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b51131c9f4bf6f6d32e4b9fa489cd5894890689.png 2x" data-dominant-color="ECEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-02-21 23-47-26</span><span class="informations">725×584 60.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8451e90ccd88cc1c2f0637a96afac1d04a6b0449.png" data-download-href="/uploads/short-url/iSyw81UH3llnqqXxrpGU8pMNFlT.png?dl=1" title="Screenshot from 2022-02-21 23-48-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8451e90ccd88cc1c2f0637a96afac1d04a6b0449_2_543x499.png" alt="Screenshot from 2022-02-21 23-48-01" data-base62-sha1="iSyw81UH3llnqqXxrpGU8pMNFlT" width="543" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/8451e90ccd88cc1c2f0637a96afac1d04a6b0449_2_543x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8451e90ccd88cc1c2f0637a96afac1d04a6b0449.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8451e90ccd88cc1c2f0637a96afac1d04a6b0449.png 2x" data-dominant-color="EAE9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-02-21 23-48-01</span><span class="informations">725×667 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a13da7ad2a2345c50898ef9217bd2af94d581981.png" data-download-href="/uploads/short-url/n0oY0Lmli1qhq0xY3i87JiH67qp.png?dl=1" title="Screenshot from 2022-02-21 23-52-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a13da7ad2a2345c50898ef9217bd2af94d581981_2_588x500.png" alt="Screenshot from 2022-02-21 23-52-54" data-base62-sha1="n0oY0Lmli1qhq0xY3i87JiH67qp" width="588" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a13da7ad2a2345c50898ef9217bd2af94d581981_2_588x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a13da7ad2a2345c50898ef9217bd2af94d581981_2_882x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a13da7ad2a2345c50898ef9217bd2af94d581981_2_1176x1000.png 2x" data-dominant-color="929291"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-02-21 23-52-54</span><span class="informations">1291×1097 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e536877bc865c9cf540775c31ceeac877603f8bb.png" data-download-href="/uploads/short-url/wHIatVeLvcXChcH3gBo1QG2OYFd.png?dl=1" title="Screenshot from 2022-02-21 23-53-18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e536877bc865c9cf540775c31ceeac877603f8bb_2_562x500.png" alt="Screenshot from 2022-02-21 23-53-18" data-base62-sha1="wHIatVeLvcXChcH3gBo1QG2OYFd" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e536877bc865c9cf540775c31ceeac877603f8bb_2_562x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e536877bc865c9cf540775c31ceeac877603f8bb_2_843x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e536877bc865c9cf540775c31ceeac877603f8bb_2_1124x1000.png 2x" data-dominant-color="939292"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-02-21 23-53-18</span><span class="informations">1275×1133 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-02-22 06:51 UTC)

<p>Slicer guarantees that the same voxels will be at the same physical position in the saved image as the original image. However, there are many equivalent representations of the same image in the same physical space (e.g., depending on which corner of the image is chosen as the origin), and it is up to the image reader/writer classes and underlying libraries (e.g., ITK, VTK) to decide which one to choose.</p>
<p>The screenshots above show that everything is correct. For example image origin is relocated in accordance with the origin’s physical position:</p>
<pre><code>1009.5 - 1.5 * (545-1) = 193.5
</code></pre>
<p>Software applications that ignore the image geometry (image origin, spacing, axis directions) need to be improved to use the image geometry if physical position, orientation, or size matters for them. If an application just wants to get images and segmentations with matching voxels (for example, to do some simple operations that do not require awareness of the image geometry) then you can export both the master volume and segmentation. In this case the voxel coordinates will match (not just the physical position of the voxels). You can also choose to match any other volume’s geometry, if you export a segmentation using “Segmentations” module’s “Export to files” section and set the image that you want to match as “Reference volume”.</p>

---

## Post #3 by @Liu_Lance (2022-02-22 07:41 UTC)

<p>Thanks so much Andras,<br>
How about the small value shift, the pixel values (SUV) are not the same between the exported dicoms and original nifti. I think may be it is because of the datatype rounding, But I don’t have any clue how to solve this.</p>

---

## Post #4 by @lassoan (2022-02-24 06:07 UTC)

<p>Until relatively recently, DICOM images could only store integer voxel values. It is possible that the Slicer DICOM exporter does not support floating-point voxel values yet, so some rounding errors are possible. <a class="mention" href="/u/pieper">@pieper</a> have you experienced such issue with PET images?</p>

---

## Post #5 by @pieper (2022-02-24 15:47 UTC)

<p>Right, there’s no support for floating point in traditional dicom images, only in the somewhat new PM modality (parametric maps).  For pet typically people use the rescale slope / intercept tags to preserve dynamic range and that’s probably what happened here and there was some loss coming back to float.</p>
<p>It probably doesn’t apply here, but note that many dicom PET studies use a different slope/intercept on each slice, but in ITK (hence Slicer) these are all normalized across the volume to the data type and that can be a bit lossy.</p>

---
