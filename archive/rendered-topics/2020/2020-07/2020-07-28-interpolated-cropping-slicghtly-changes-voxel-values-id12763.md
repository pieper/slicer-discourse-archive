---
topic_id: 12763
title: "Interpolated Cropping Slicghtly Changes Voxel Values"
date: 2020-07-28
url: https://discourse.slicer.org/t/12763
---

# Interpolated cropping slicghtly changes voxel values

**Topic ID**: 12763
**Date**: 2020-07-28
**URL**: https://discourse.slicer.org/t/interpolated-cropping-slicghtly-changes-voxel-values/12763

---

## Post #1 by @manjula (2020-07-28 20:29 UTC)

<p>I am getting very minor difference in voxel values when I crop with the ROI box. I used the crop volume with Linear interpolator and isotropic spacing and default settings.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9276e5979b7953d5e75cae7dfc5cf9c98bdd01fb.jpeg" data-download-href="/uploads/short-url/kTGrEqlXI5F9YBZVnwwNef2asrh.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9276e5979b7953d5e75cae7dfc5cf9c98bdd01fb_2_690x313.jpeg" alt="1" data-base62-sha1="kTGrEqlXI5F9YBZVnwwNef2asrh" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9276e5979b7953d5e75cae7dfc5cf9c98bdd01fb_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9276e5979b7953d5e75cae7dfc5cf9c98bdd01fb_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9276e5979b7953d5e75cae7dfc5cf9c98bdd01fb_2_1380x626.jpeg 2x" data-dominant-color="534D52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1925×875 440 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I calculate the mean value in segment statistics with the Scalar volume select as the Crop volume and then with the original volume using the same segment, the mean value is slightly different.  The size remains the same.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c32792b2477c5e585e5f9a239e645d6c05d863da.jpeg" data-download-href="/uploads/short-url/rQpThbWA00nFFgmU6OmVdgJjw5I.jpeg?dl=1" title="Screenshot from 2020-07-28 22-23-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c32792b2477c5e585e5f9a239e645d6c05d863da_2_690x388.jpeg" alt="Screenshot from 2020-07-28 22-23-23" data-base62-sha1="rQpThbWA00nFFgmU6OmVdgJjw5I" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c32792b2477c5e585e5f9a239e645d6c05d863da_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c32792b2477c5e585e5f9a239e645d6c05d863da_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c32792b2477c5e585e5f9a239e645d6c05d863da_2_1380x776.jpeg 2x" data-dominant-color="C1C0BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-28 22-23-23</span><span class="informations">1920×1080 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/913f51aa2dd2cf6e5d16dd5494dbacfe1c490f12.jpeg" data-download-href="/uploads/short-url/kIUToOMdCEMJCkLCsMJYMc3X8pc.jpeg?dl=1" title="Screenshot from 2020-07-28 22-23-54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/913f51aa2dd2cf6e5d16dd5494dbacfe1c490f12_2_690x388.jpeg" alt="Screenshot from 2020-07-28 22-23-54" data-base62-sha1="kIUToOMdCEMJCkLCsMJYMc3X8pc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/913f51aa2dd2cf6e5d16dd5494dbacfe1c490f12_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/913f51aa2dd2cf6e5d16dd5494dbacfe1c490f12_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/913f51aa2dd2cf6e5d16dd5494dbacfe1c490f12_2_1380x776.jpeg 2x" data-dominant-color="C1C0BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-28 22-23-54</span><span class="informations">1920×1080 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it because of the Cropping algorithm and  is this to be expected ? or am i doing something wrong?</p>
<p>It does not affect my calculations and seems very very trivial but I am just curious why this happens.</p>

---

## Post #2 by @lassoan (2020-07-28 21:28 UTC)

<p>It is expected that if origin, spacing, or axis directions of the output volume are not exactly the same as the input volume’s then interpolated values in the output volume will not be exactly the same. However, the difference should be negligible.</p>

---
