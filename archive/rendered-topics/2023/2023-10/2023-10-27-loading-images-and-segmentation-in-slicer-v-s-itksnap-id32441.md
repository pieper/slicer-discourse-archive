# Loading images and segmentation in Slicer v.s. ITKSNAP

**Topic ID**: 32441
**Date**: 2023-10-27
**URL**: https://discourse.slicer.org/t/loading-images-and-segmentation-in-slicer-v-s-itksnap/32441

---

## Post #1 by @Chenglin_Zhu (2023-10-27 04:39 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f07986c328c8dd48383bfe2c252a35400c036f58.jpeg" data-download-href="/uploads/short-url/yjkXE7UOgh81oUSSZUJAKMWZJXy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f07986c328c8dd48383bfe2c252a35400c036f58_2_690x286.jpeg" alt="image" data-base62-sha1="yjkXE7UOgh81oUSSZUJAKMWZJXy" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f07986c328c8dd48383bfe2c252a35400c036f58_2_690x286.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f07986c328c8dd48383bfe2c252a35400c036f58_2_1035x429.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f07986c328c8dd48383bfe2c252a35400c036f58_2_1380x572.jpeg 2x" data-dominant-color="3D3E2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1848×767 85.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi all,</p>
<p>I am wondering what is the differences between Slicer and ITKSNAP when loading images and segmentation. Here are the snapshot of dicom images and auto-segmentation based on the nifti image (using dcm2nii conversion) in Slicer (left image) and ITKSNAP (right image). There is a misalignment when I load images in ITKSNAP, I am wondering how Slicer read it correctly, so that I can avoid this misalignment issue when coding my own project. Thanks!</p>

---

## Post #2 by @pieper (2023-10-27 11:28 UTC)

<p>Looks like an RAS/LPS issue.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html</a></p>

---

## Post #3 by @jcfr (2023-10-27 14:46 UTC)

<blockquote>
<p>ITKSNAP (right image)</p>
</blockquote>
<p>To add to <a class="mention" href="/u/pieper">@pieper</a> comment, based on the image you shared, the segmentation loaded in ITKSNAP does <strong>not</strong> align with the underlying structure visible on the loaded dicom image.</p>
<blockquote>
<p>Slicer (left image)</p>
</blockquote>
<p>whereas the segmentation loaded in Slicer is properly aligned.</p>

---

## Post #4 by @lassoan (2023-10-27 21:59 UTC)

<p>I would just add that definition of image orientation in NIFTI files can be ambiguous. Therefore sometimes the same files show up differently in different software. I would recommend to use NRRD file format instead of NIFTI to avoid such issues.</p>

---
