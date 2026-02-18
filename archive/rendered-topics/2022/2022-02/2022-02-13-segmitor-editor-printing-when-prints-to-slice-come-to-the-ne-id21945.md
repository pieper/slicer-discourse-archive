# Segmitor editor  printing when prints to slice come to the next slice so distribute the segmentation 

**Topic ID**: 21945
**Date**: 2022-02-13
**URL**: https://discourse.slicer.org/t/segmitor-editor-printing-when-prints-to-slice-come-to-the-next-slice-so-distribute-the-segmentation/21945

---

## Post #1 by @mohkhan (2022-02-13 03:21 UTC)

<p>Segmitor editor  printing when prints to slice come to the next slice so distribute the segmentation</p>

---

## Post #2 by @lassoan (2022-02-13 13:49 UTC)

<p>Could you provide more details, perhaps attach a screenshot to explain what you mean?</p>

---

## Post #3 by @mohkhan (2022-02-13 21:01 UTC)

<p>When I print in slice it become larger and when I go to next slice the work i did in the first slice coped the same so it will inculde others area and in 3D in will be like bloke without not the usual shape when do segmentation</p>

---

## Post #4 by @mohkhan (2022-02-13 21:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d74f5f8337e9d03a3ee8abe1ea0765f84e5ba2f8.jpeg" data-download-href="/uploads/short-url/uIII9M3XUwCdECdV2O9UL8TJxYA.jpeg?dl=1" title="٢٠٢٢٠٢١٤_٠٠٢٢٠٩" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d74f5f8337e9d03a3ee8abe1ea0765f84e5ba2f8_2_375x500.jpeg" alt="٢٠٢٢٠٢١٤_٠٠٢٢٠٩" data-base62-sha1="uIII9M3XUwCdECdV2O9UL8TJxYA" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d74f5f8337e9d03a3ee8abe1ea0765f84e5ba2f8_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d74f5f8337e9d03a3ee8abe1ea0765f84e5ba2f8_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d74f5f8337e9d03a3ee8abe1ea0765f84e5ba2f8_2_750x1000.jpeg 2x" data-dominant-color="707370"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">٢٠٢٢٠٢١٤_٠٠٢٢٠٩</span><span class="informations">1920×2560 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48d0b3b18221e724b964620e67012f86b4aedb27.jpeg" data-download-href="/uploads/short-url/ao9wdGxdMu02jX6tyu6TcEds7DF.jpeg?dl=1" title="٢٠٢٢٠٢١٤_٠٠٢٢٣٢" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48d0b3b18221e724b964620e67012f86b4aedb27_2_375x500.jpeg" alt="٢٠٢٢٠٢١٤_٠٠٢٢٣٢" data-base62-sha1="ao9wdGxdMu02jX6tyu6TcEds7DF" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48d0b3b18221e724b964620e67012f86b4aedb27_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48d0b3b18221e724b964620e67012f86b4aedb27_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48d0b3b18221e724b964620e67012f86b4aedb27_2_750x1000.jpeg 2x" data-dominant-color="6F7371"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">٢٠٢٢٠٢١٤_٠٠٢٢٣٢</span><span class="informations">1920×2560 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-02-14 00:42 UTC)

<p>Most likely you switched master volume after you created the segmentation. Therefore, the voxel grid of the segmentation differs from the voxel grid of the current master volume. Following <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">these instructions</a> will probably result in the behavior you expect.</p>

---
