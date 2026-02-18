# How to measure blood vessel thickness

**Topic ID**: 17943
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/how-to-measure-blood-vessel-thickness/17943

---

## Post #1 by @jhchoi (2021-06-04 01:54 UTC)

<p>I want to know how to measure the thickness of red blood vessels. what can i do?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3ca5a98f6ec9ea3a8601ea11065505f62f87c62.jpeg" data-download-href="/uploads/short-url/rW2EaLmgnK0LLOGQet5wkkS3kX0.jpeg?dl=1" title="2021-05-31-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3ca5a98f6ec9ea3a8601ea11065505f62f87c62_2_690x496.jpeg" alt="2021-05-31-Scene" data-base62-sha1="rW2EaLmgnK0LLOGQet5wkkS3kX0" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3ca5a98f6ec9ea3a8601ea11065505f62f87c62_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3ca5a98f6ec9ea3a8601ea11065505f62f87c62_2_1035x744.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3ca5a98f6ec9ea3a8601ea11065505f62f87c62.jpeg 2x" data-dominant-color="6B6F87"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-05-31-Scene</span><span class="informations">1286×925 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-04 05:10 UTC)

<p>You can use SlicerVMTK extension’s Extract centerline module to extract one more branches of a segmented vessel tree and get the list of diameters along the curve.</p>

---
