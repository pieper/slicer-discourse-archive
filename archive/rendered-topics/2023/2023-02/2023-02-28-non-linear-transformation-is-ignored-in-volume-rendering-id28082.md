# Non-linear transformation is ignored in volume rendering

**Topic ID**: 28082
**Date**: 2023-02-28
**URL**: https://discourse.slicer.org/t/non-linear-transformation-is-ignored-in-volume-rendering/28082

---

## Post #1 by @jay1987 (2023-02-28 02:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c115bad67339dcb0f8d98e37628415bbf2d38824.jpeg" data-download-href="/uploads/short-url/ry6HSBkHgSuIXU0GCQ6Xpk6F6vO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c115bad67339dcb0f8d98e37628415bbf2d38824_2_690x427.jpeg" alt="image" data-base62-sha1="ry6HSBkHgSuIXU0GCQ6Xpk6F6vO" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c115bad67339dcb0f8d98e37628415bbf2d38824_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c115bad67339dcb0f8d98e37628415bbf2d38824_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c115bad67339dcb0f8d98e37628415bbf2d38824.jpeg 2x" data-dominant-color="565D60"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1120×694 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
the picture above shows the volume rendering and thresholding result in 3d window and 2d windows,in 2d windows the thresholding match the volume data , but in 3d window,they has a long distance,i don’t know that wrong with the dicom serial</p>

---

## Post #2 by @muratmaga (2023-02-28 02:05 UTC)

<p>Please double check that the volume rendering DICOM series is the same as the one as you have segmented. DICOMs may have contain multiple series.</p>

---

## Post #3 by @jay1987 (2023-02-28 02:09 UTC)

<p>thank you muratmaga very much<br>
i found the ct serial i read from DICOM module has a initial transform<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab771c595d7de924a038e5a1a88b795773f4e842.png" data-download-href="/uploads/short-url/osQQ8Um61mZUABglb1fZ2pKhShk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab771c595d7de924a038e5a1a88b795773f4e842.png" alt="image" data-base62-sha1="osQQ8Um61mZUABglb1fZ2pKhShk" width="690" height="59" data-dominant-color="F8F8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×63 3.37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
the problem fixed when i delete the transform node</p>

---
