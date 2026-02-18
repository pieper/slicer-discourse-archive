# Export the segmentation as DICOM series

**Topic ID**: 9769
**Date**: 2020-01-10
**URL**: https://discourse.slicer.org/t/export-the-segmentation-as-dicom-series/9769

---

## Post #1 by @TongLyu (2020-01-10 02:41 UTC)

<p>Hi!<br>
I want to know if there is any way that I could cut the other parts of CT images that I want to have after segmentation and only export the part I want as DICOM series.</p>
<p>Version: 3D Slicer 4.10.2</p>

---

## Post #2 by @lassoan (2020-01-10 02:43 UTC)

<p>Would you like to export the segmentation or the CT image? What part would you like to export (crop to the smallest bounding box that contains all the segments, blank out regions that are outside all segments, …)?</p>

---

## Post #3 by @TongLyu (2020-01-10 15:36 UTC)

<p>Morning, thanks for your reply.</p>
<p>I would like to export the segmentation part as DICOM series which gets rid of the regions that are outside all segments. Besides, I still want the exported DICOM series to have the sane number of images as the series before segmentation.</p>
<p>I appreciate your help and look forward to your response.</p>
<p>On 01/9/2020 21:54，Andras Lasso via 3D Slicer Community<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> wrote：</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c436aa60568a24cbb3d23367e43ec61346819bf2.jpeg" data-download-href="/uploads/short-url/rZMHGn3tiLXYqCdPX8EFYsqhu9Q.jpeg?dl=1" title="Screen Shot 2020-01-10 at 10.33.07 AM.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c436aa60568a24cbb3d23367e43ec61346819bf2_2_690x431.jpeg" alt="Screen Shot 2020-01-10 at 10.33.07 AM.jpg" data-base62-sha1="rZMHGn3tiLXYqCdPX8EFYsqhu9Q" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c436aa60568a24cbb3d23367e43ec61346819bf2_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c436aa60568a24cbb3d23367e43ec61346819bf2_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c436aa60568a24cbb3d23367e43ec61346819bf2_2_1380x862.jpeg 2x" data-dominant-color="818387"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-01-10 at 10.33.07 AM.jpg</span><span class="informations">3360×2100 1.05 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @JanWitowski (2020-01-10 22:35 UTC)

<p>You probably would be able to do this by transforming the segmentation layer to binary labelmap in Segmentations module, and then exporting it to DICOM in Data module (by right clicking on labelmap). However this strips some meta data and some viewers might misinterpret e.g. patient orientation. Maybe <a class="mention" href="/u/lassoan">@lassoan</a> has a better idea</p>

---

## Post #5 by @lassoan (2020-01-11 19:50 UTC)

<p>It is still not clear if you want to export the segmentation (DICOM Segmentation object or RT structure set) or a modified CT image (where areas outside segments are blanked out).</p>

---
