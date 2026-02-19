---
topic_id: 29231
title: "Remove Mri Background From The Threshold Selection"
date: 2023-05-01
url: https://discourse.slicer.org/t/29231
---

# Remove MRI background from the threshold selection

**Topic ID**: 29231
**Date**: 2023-05-01
**URL**: https://discourse.slicer.org/t/remove-mri-background-from-the-threshold-selection/29231

---

## Post #1 by @user_090 (2023-05-01 15:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9617b27e60eb74bc15e71d21ec82d39fced6cdf.jpeg" data-download-href="/uploads/short-url/sJuP4HXU3GQbdnqiivnb7lMDRM3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9617b27e60eb74bc15e71d21ec82d39fced6cdf_2_690x327.jpeg" alt="image" data-base62-sha1="sJuP4HXU3GQbdnqiivnb7lMDRM3" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9617b27e60eb74bc15e71d21ec82d39fced6cdf_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9617b27e60eb74bc15e71d21ec82d39fced6cdf_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9617b27e60eb74bc15e71d21ec82d39fced6cdf_2_1380x654.jpeg 2x" data-dominant-color="5C6363"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×905 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi, I did a MRI and now I’m trying to extract my skull model out of it.<br>
It seems like I’ll have to do a manual work to get the unwanted selections deleted, but what makes it hard is the fact that the skull as a similar pattern to the backgrounds one, and due to this both the bone matter and the background get selected with the threshold tool. Does anybody know if there’s an specific functionality that allows me to unselect the background area?<br>
P.S.: I already know that the CT is a better alternative to get cleaner bone images, but I didn’t do it, so I only have this alternative.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-05-01 22:05 UTC)

<p>One approach is to first <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">segment the skin surface</a>. You can then use this skin segment as mask for the thresholding (you extract low-signal areas <em>inside</em> the skin segment).</p>
<p>Note that low signal inside the skin in T1 images don’t indicate specifically bone (it can be also air, water), so you won’t get the skull with simple thresholding. Warping the CT of a similar patient may result in much better quality skull model.</p>

---
