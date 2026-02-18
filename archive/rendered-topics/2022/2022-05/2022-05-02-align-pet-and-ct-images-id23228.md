# Align PET and CT images

**Topic ID**: 23228
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/align-pet-and-ct-images/23228

---

## Post #1 by @Liu_Lance (2022-05-02 07:26 UTC)

<p>Hi<br>
I feel very curious about how the two images PET (img_suv) and CT (imgCT) align together in the 3d slicer. they are from the same object. but the nifti affines are different as shown in the following figures. in the right four-up views. the two image are perfectly aligned. However, when I use nibabel package to load the two scans and try to rescale the CT to match the size (H and W) of the PET and overlay them into two channel for my data tensor. the ratio of the objects changes. the object from PET is much slimmer than that from CT. Could you help. I hope I have clearly state the problem, Thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0289a38aede254919535213d7f8e8da81db39c9.jpeg" data-download-href="/uploads/short-url/p8n1ytGYOkfyuXv3M42XuMhoFMR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0289a38aede254919535213d7f8e8da81db39c9_2_690x365.jpeg" alt="image" data-base62-sha1="p8n1ytGYOkfyuXv3M42XuMhoFMR" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0289a38aede254919535213d7f8e8da81db39c9_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0289a38aede254919535213d7f8e8da81db39c9_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0289a38aede254919535213d7f8e8da81db39c9_2_1380x730.jpeg 2x" data-dominant-color="9D9F9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1016 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcf6a09fe7040c9b10f428d332dd1460bb42823e.jpeg" data-download-href="/uploads/short-url/A5OIBoEneKyP79AYmaFOSEZ1PBQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcf6a09fe7040c9b10f428d332dd1460bb42823e_2_690x364.jpeg" alt="image" data-base62-sha1="A5OIBoEneKyP79AYmaFOSEZ1PBQ" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcf6a09fe7040c9b10f428d332dd1460bb42823e_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcf6a09fe7040c9b10f428d332dd1460bb42823e_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fcf6a09fe7040c9b10f428d332dd1460bb42823e_2_1380x728.jpeg 2x" data-dominant-color="9D9F9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1015 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
