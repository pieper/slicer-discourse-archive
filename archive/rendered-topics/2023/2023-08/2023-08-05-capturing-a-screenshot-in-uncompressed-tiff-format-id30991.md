# Capturing a Screenshot in uncompressed TIFF format

**Topic ID**: 30991
**Date**: 2023-08-05
**URL**: https://discourse.slicer.org/t/capturing-a-screenshot-in-uncompressed-tiff-format/30991

---

## Post #1 by @chris_nik (2023-08-05 09:13 UTC)

<p>Hello dear Comunity,<br>
when capturing a screenshot of the multiplanar view of a CBCT volume, the only option Slicer gives me is to save it in png. format. The resolution of the saved image is inferior to the one of the CBCT in Slicer. Is it possible to save a screenshot in uncompressed TIFF format, resulting in an image with the same quality/ pixel size as the voxel size seen in Slicer’s multiplanar view?<br>
Cheers</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/012f346ee059b1482f6ece51c87ec43aeae498b3.png" data-download-href="/uploads/short-url/atC1CiSxKQ0LdTiuctTlCHNu0j.png?dl=1" title="SlicerScreenshotCapture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/012f346ee059b1482f6ece51c87ec43aeae498b3_2_690x372.png" alt="SlicerScreenshotCapture" data-base62-sha1="atC1CiSxKQ0LdTiuctTlCHNu0j" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/012f346ee059b1482f6ece51c87ec43aeae498b3_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/012f346ee059b1482f6ece51c87ec43aeae498b3_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/012f346ee059b1482f6ece51c87ec43aeae498b3_2_1380x744.png 2x" data-dominant-color="37373E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerScreenshotCapture</span><span class="informations">1919×1036 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-08-05 10:39 UTC)

<p>Screen capture module can save the <em>displayed</em> image in png without loss of quality. The displayed image may be higher or lower resolution than the original image.</p>
<p>If you want to save the original image then you can use “Export to file” feature (in right-click menu in Data module).</p>

---

## Post #3 by @chris_nik (2023-08-05 11:09 UTC)

<p>thank you, I now see that png. is also a lossless format, I compared the quality again and it is matching.</p>

---
