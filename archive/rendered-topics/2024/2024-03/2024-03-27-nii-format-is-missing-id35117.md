# .nii format is missing

**Topic ID**: 35117
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/nii-format-is-missing/35117

---

## Post #1 by @ReNeu (2024-03-27 04:09 UTC)

<p>Hi there,<br>
I have CT resliced volume saved as a .nii file and I drew a lesion map (segmentation) over the resliced CT volume. I saved the lesion map as a segmentation(.nrrd) file as slicer doesn’t allow me to save it as a .nii file (see attached image). How can I save the lesion map as a .nii file if I don’t get this option in file format?<br>
Thanks,<br>
Ettie<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d1edbf01284516da7609b33f73095d07af8ed00.png" data-download-href="/uploads/short-url/49BXE2hSJuCwxtuIwcwaddn8FLG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1edbf01284516da7609b33f73095d07af8ed00_2_690x272.png" alt="image" data-base62-sha1="49BXE2hSJuCwxtuIwcwaddn8FLG" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1edbf01284516da7609b33f73095d07af8ed00_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d1edbf01284516da7609b33f73095d07af8ed00.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d1edbf01284516da7609b33f73095d07af8ed00.png 2x" data-dominant-color="C0C1C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×341 72.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-03-27 13:11 UTC)

<p>You can export the segmentation to a binary labelmap volume (right click in the Data module or in Segmentations) and then save to nii.  It’s not offered by default because it can be a lossy operation (e.g. no overlap).</p>

---

## Post #3 by @ReNeu (2024-04-11 03:46 UTC)

<p>Thank you Steve, I exported the segmentation to a binary labelmap volume, but was unable to save to nii<br>
Any suggestions?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34e2f1771c8c314a09a374813fd198a04a5b0610.png" data-download-href="/uploads/short-url/7xR3ebAVEHEbBAUpwwfx4raOXJe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e2f1771c8c314a09a374813fd198a04a5b0610_2_690x240.png" alt="image" data-base62-sha1="7xR3ebAVEHEbBAUpwwfx4raOXJe" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e2f1771c8c314a09a374813fd198a04a5b0610_2_690x240.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e2f1771c8c314a09a374813fd198a04a5b0610_2_1035x360.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e2f1771c8c314a09a374813fd198a04a5b0610_2_1380x480.png 2x" data-dominant-color="D2D3D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1472×513 70.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2024-04-11 13:03 UTC)

<p>You just need to scroll down through the list.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09996e76e89971a2189b06fc7cdfc8becdb02e9a.png" alt="image" data-base62-sha1="1mV1piCoAvjNdO4ugNSiIjsRi6C" width="590" height="384"></p>

---
