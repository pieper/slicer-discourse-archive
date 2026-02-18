# Segments to label maps number

**Topic ID**: 19753
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/segments-to-label-maps-number/19753

---

## Post #1 by @muratmaga (2021-09-20 03:39 UTC)

<p>I am a little bit confused about how labelmap indices are determined after the segmentation-&gt;Label map conversions. I was under the impression that it was the order of the segments. Am I mistaken? Because in the screenshot below for both converted volumes the skull segment  is the first in the segmentation, but it got index number of 1 in the one labelmap and the 2 in the other.</p>
<p>I am using the right-click convert visible Segments to labelmaps option in the data module. Is there another way to make sure label indices match the order.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a9367a5d169c0a5b3a0e18b6ddf73b5b59f6763.jpeg" data-download-href="/uploads/short-url/jLTHFK776Gk67UZ4hU3Lr6ArAJ5.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a9367a5d169c0a5b3a0e18b6ddf73b5b59f6763_2_450x500.jpeg" alt="image" data-base62-sha1="jLTHFK776Gk67UZ4hU3Lr6ArAJ5" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a9367a5d169c0a5b3a0e18b6ddf73b5b59f6763_2_450x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a9367a5d169c0a5b3a0e18b6ddf73b5b59f6763.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a9367a5d169c0a5b3a0e18b6ddf73b5b59f6763.jpeg 2x" data-dominant-color="818181"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">567×630 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-09-21 22:20 UTC)

<p>Due to strong demand, we implemented preservation of label values during labelmap-&gt;segmentation-&gt;labelmap roundtrip. This is achieved by matching segment names to color names in the color table.</p>
<p>If you don’t want to use this color mapping then disable “Use color table values” in Segmentations / Export / Advanced.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88a000b98ae67377a6ee908496b234a0a29a5af0.png" data-download-href="/uploads/short-url/juDJUlJNZmSe6tjFE00mt3FgRlm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a000b98ae67377a6ee908496b234a0a29a5af0_2_353x500.png" alt="image" data-base62-sha1="juDJUlJNZmSe6tjFE00mt3FgRlm" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a000b98ae67377a6ee908496b234a0a29a5af0_2_353x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a000b98ae67377a6ee908496b234a0a29a5af0_2_529x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a000b98ae67377a6ee908496b234a0a29a5af0_2_706x1000.png 2x" data-dominant-color="3A3A39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×1130 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
