---
topic_id: 12839
title: "Segment Editor Functions Dont Work Past Specific Slice In Di"
date: 2020-08-03
url: https://discourse.slicer.org/t/12839
---

# Segment Editor functions don't work past specific slice in DICOM series

**Topic ID**: 12839
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/segment-editor-functions-dont-work-past-specific-slice-in-dicom-series/12839

---

## Post #1 by @Otoco (2020-08-03 22:09 UTC)

<p>Hello all,</p>
<p>I’ve been spending the last few weeks segmenting skull bones using CT skull DICOMs for research purposes. I got a fantastic solution with the help of the users of this forum last time - my current problem is a little bit simpler.</p>
<p>On this specific DICOM series, when I use the segment editor the functions stop working after a specific image in the axial series. Threshold indicates that it wants to fill in the entire series but when I run the function, it is only partially filled. Manually painting the volume at any image in the unresponsive section doesn’t work either. I have no annotations currently active and never cropped the volume to begin with. Couldn’t find a thread with an equivalent problem after searching, so posting it here.</p>
<p>Screens:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa1b52d261a0cf5384cc67b9a4c3ae8759e0ec91.jpeg" data-download-href="/uploads/short-url/ogPI2BaoZCkIVk4KqDcTOtTNrbP.jpeg?dl=1" title="Screen Shot 2020-08-03 at 6.01.12 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa1b52d261a0cf5384cc67b9a4c3ae8759e0ec91_2_475x500.jpeg" alt="Screen Shot 2020-08-03 at 6.01.12 PM" data-base62-sha1="ogPI2BaoZCkIVk4KqDcTOtTNrbP" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa1b52d261a0cf5384cc67b9a4c3ae8759e0ec91_2_475x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa1b52d261a0cf5384cc67b9a4c3ae8759e0ec91_2_712x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa1b52d261a0cf5384cc67b9a4c3ae8759e0ec91_2_950x1000.jpeg 2x" data-dominant-color="3D3C44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-03 at 6.01.12 PM</span><span class="informations">1298×1366 345 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here you can see that the threshold I did stopped at a specific axial slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d5782f995d379070c1cc2647a04053499cc5a1.jpeg" data-download-href="/uploads/short-url/c6tsKHkeXH4z9BxBrJWF2nKs8Xn.jpeg?dl=1" title="Screen Shot 2020-08-03 at 6.01.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d5782f995d379070c1cc2647a04053499cc5a1_2_475x500.jpeg" alt="Screen Shot 2020-08-03 at 6.01.51 PM" data-base62-sha1="c6tsKHkeXH4z9BxBrJWF2nKs8Xn" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d5782f995d379070c1cc2647a04053499cc5a1_2_475x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d5782f995d379070c1cc2647a04053499cc5a1_2_712x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d5782f995d379070c1cc2647a04053499cc5a1_2_950x1000.jpeg 2x" data-dominant-color="3C3A42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-03 at 6.01.51 PM</span><span class="informations">1296×1362 331 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is the preview when I am applying a threshold to my segment - you can clearly see the problematic sections are included and this is true for the entire series.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52012f4d78db5bf958287ee1a426a98c16d5144.jpeg" data-download-href="/uploads/short-url/yYtHjo1W2WoyeRUJEJBqPTsRtsg.jpeg?dl=1" title="Screen Shot 2020-08-03 at 6.02.45 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f52012f4d78db5bf958287ee1a426a98c16d5144_2_690x431.jpeg" alt="Screen Shot 2020-08-03 at 6.02.45 PM" data-base62-sha1="yYtHjo1W2WoyeRUJEJBqPTsRtsg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f52012f4d78db5bf958287ee1a426a98c16d5144_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f52012f4d78db5bf958287ee1a426a98c16d5144_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f52012f4d78db5bf958287ee1a426a98c16d5144_2_1380x862.jpeg 2x" data-dominant-color="98999B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-03 at 6.02.45 PM</span><span class="informations">2560×1600 491 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
My attempt at painting above the problematic slice - didn’t change anything.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d63985315d2decd2c4d2ff1bc1d043b7bb558fda.png" data-download-href="/uploads/short-url/uz7pKtJ99JjcLT3fnp1m3kpft0e.png?dl=1" title="Screen Shot 2020-08-03 at 6.06.06 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d63985315d2decd2c4d2ff1bc1d043b7bb558fda_2_690x469.png" alt="Screen Shot 2020-08-03 at 6.06.06 PM" data-base62-sha1="uz7pKtJ99JjcLT3fnp1m3kpft0e" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d63985315d2decd2c4d2ff1bc1d043b7bb558fda_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d63985315d2decd2c4d2ff1bc1d043b7bb558fda_2_1035x703.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d63985315d2decd2c4d2ff1bc1d043b7bb558fda.png 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-03 at 6.06.06 PM</span><span class="informations">1214×826 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Volume information if this helps - it’s a solid volumetric scan but not anything out of the ordinary.</p>
<p>Any help would be appreciated! Thank you all so much.</p>

---

## Post #2 by @lassoan (2020-08-03 22:22 UTC)

<p>You can only paint within the extent of the “binary labelmap representation”. You can specify a larger extent by selecting a different node (e.g., the volume that contains the complete skull) and use it as source geometry (see some more information <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">here</a>).</p>

---

## Post #3 by @pieper (2020-08-03 22:25 UTC)

<p>You probably have the same issue as this thread:</p>
<aside class="quote quote-modified" data-post="1" data-topic="6442">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/uneven-slice-thickness/6442">Uneven slice thickness</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Any Solution for this?? 
[image]
  </blockquote>
</aside>

<p>See this info: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Image_is_stretched_or_compressed_along_one_axis" class="inline-onebox">Documentation/Nightly/FAQ/DICOM - Slicer Wiki</a></p>

---

## Post #4 by @Otoco (2020-08-04 17:14 UTC)

<p>this was the one! the node somehow was switched to a smaller view, redefining the source geometry fixed it. Thank you so much!</p>

---
