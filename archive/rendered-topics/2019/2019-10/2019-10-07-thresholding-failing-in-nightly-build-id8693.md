# Thresholding Failing in Nightly Build

**Topic ID**: 8693
**Date**: 2019-10-07
**URL**: https://discourse.slicer.org/t/thresholding-failing-in-nightly-build/8693

---

## Post #1 by @stevenagl12 (2019-10-07 15:58 UTC)

<p>I am working on a windows 10, and have the latest nightly build from today. When I import my volume and then import a labelmap, convert it to a segmentation node, and attempt to threshold the volume, the segmentation fails (it only segments a small patch of the spine (my threshold is set at 134.63 and should be segmenting the couch and all bone). The first image is what should be thresholded, while the second is what is actually getting thresholded. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2f659579cd701c614980f2d1ef5a999880bde42.png" data-download-href="/uploads/short-url/pxaMYQIuLqEEl794Ijbdz26u8Uy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f659579cd701c614980f2d1ef5a999880bde42_2_690x373.png" alt="image" data-base62-sha1="pxaMYQIuLqEEl794Ijbdz26u8Uy" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f659579cd701c614980f2d1ef5a999880bde42_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f659579cd701c614980f2d1ef5a999880bde42_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2f659579cd701c614980f2d1ef5a999880bde42_2_1380x746.png 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2019-10-07 16:21 UTC)

<p>The extent of an existing segment will not change. What happens if you try thresholding on a newly created segment?</p>

---

## Post #3 by @stevenagl12 (2019-10-07 16:48 UTC)

<p>Just tried adding an additional segment, and the same thing happened. It’s still not thresholding past the vertebrae.</p>

---

## Post #4 by @stevenagl12 (2019-10-07 16:55 UTC)

<p>The only time it seems to work is if I create a new segmentation, threshold the DICOM, then drag and drop the segments into the new segmentation.</p>

---

## Post #5 by @lassoan (2019-10-07 16:59 UTC)

<p>As <a class="mention" href="/u/cpinter">@cpinter</a> wrote above, segment extents are not modified automatically. You can adjust extents by clicking on the segmentation geometry button (next to volume selector).</p>

---
