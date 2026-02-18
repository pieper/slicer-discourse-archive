# MRI image quality

**Topic ID**: 24330
**Date**: 2022-07-15
**URL**: https://discourse.slicer.org/t/mri-image-quality/24330

---

## Post #1 by @akil.prabhakar (2022-07-15 13:51 UTC)

<p>Why only the axial images of the mri are clear and the saggital and coronal images are of poor quality. how can i improve these image qualities</p>

---

## Post #2 by @akil.prabhakar (2022-07-15 13:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/684a46211612390df0df312c9433fc404dc83e3a.jpeg" data-download-href="/uploads/short-url/eSAMRvHBltoWykZ2ZOu6lBXIQem.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/684a46211612390df0df312c9433fc404dc83e3a_2_690x460.jpeg" alt="image" data-base62-sha1="eSAMRvHBltoWykZ2ZOu6lBXIQem" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/684a46211612390df0df312c9433fc404dc83e3a_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/684a46211612390df0df312c9433fc404dc83e3a_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/684a46211612390df0df312c9433fc404dc83e3a_2_1380x920.jpeg 2x" data-dominant-color="716F6E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2736×1824 458 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3e5eb495efab8c9a9d16c22c493cdf4b78249f8.png" data-download-href="/uploads/short-url/yNCCJk3V0aTPtD9n9sq9MtGwltu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3e5eb495efab8c9a9d16c22c493cdf4b78249f8_2_690x460.png" alt="image" data-base62-sha1="yNCCJk3V0aTPtD9n9sq9MtGwltu" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3e5eb495efab8c9a9d16c22c493cdf4b78249f8_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3e5eb495efab8c9a9d16c22c493cdf4b78249f8_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f3e5eb495efab8c9a9d16c22c493cdf4b78249f8_2_1380x920.png 2x" data-dominant-color="6B6A6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2736×1824 561 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @akil.prabhakar (2022-07-15 14:31 UTC)

<p>sorry guys, i just found that we have to load the DICOM files and not the folders to have the full series of MRI. Moreover, one series has only one section (either the sag, cor or axial) as a good quality image and the others are blurred.</p>

---

## Post #4 by @kopachini (2022-07-18 16:59 UTC)

<p>If you want to have “nice” pictures, you have to have isovoxel sequences in the MR study… different vendors probably name it differently, but look for space, spc, or iso in names if you have a Siemens MR machine.<br>
Other sequences are non isovoxel, meaning they will have good xy spatial resolution but will have bad z resolution - depending the scanning plane (cor, sag or axial), i.e. because most of the sequences use thick slices</p>

---

## Post #5 by @mohamad_saidi (2024-06-19 17:23 UTC)

<p>hello sir, im having similar issues but i didnt understand what you meant with loading the files not the folders. can you please explain a bit more?</p>

---
