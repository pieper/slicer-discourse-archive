# Segmentation from Landmark Registration images not aligned

**Topic ID**: 17404
**Date**: 2021-05-01
**URL**: https://discourse.slicer.org/t/segmentation-from-landmark-registration-images-not-aligned/17404

---

## Post #1 by @arif (2021-05-01 16:44 UTC)

<p>Hi;<br>
I am trying to do segmentation on fusion of 2 image sets(PET-CT and mpMRI). PET-CT is full body and MRI is pelvic. With the help of Landmark Registration module I am able to overlap the two images. I prefer mpMRI is fixed and CT is moving. As mp MRI show great anatomical detail, I need it to be the fixed one. But when I try to segment my ROI on the fusion image, the result of the segmentation in 3d is far off from where I expect it to be. Is there any suggestion on how to overlap the segmentations also.</p>
<p>Best Regards</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2600bf85cdc1fb9eb3b6ae2c4e45c99f3bcad8df.png" data-download-href="/uploads/short-url/5qbKivouWwqZGYy3gMxnkoadBr9.png?dl=1" title="Unts" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2600bf85cdc1fb9eb3b6ae2c4e45c99f3bcad8df_2_690x321.png" alt="Unts" data-base62-sha1="5qbKivouWwqZGYy3gMxnkoadBr9" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2600bf85cdc1fb9eb3b6ae2c4e45c99f3bcad8df_2_690x321.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2600bf85cdc1fb9eb3b6ae2c4e45c99f3bcad8df_2_1035x481.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2600bf85cdc1fb9eb3b6ae2c4e45c99f3bcad8df.png 2x" data-dominant-color="C5C7E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unts</span><span class="informations">1349×629 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfca57fee6353887c9e5411f71c4b8c926e29704.png" data-download-href="/uploads/short-url/vVJZI9Xm9fWbKHxDdjZc2tSSTLS.png?dl=1" title="registration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfca57fee6353887c9e5411f71c4b8c926e29704_2_690x337.png" alt="registration" data-base62-sha1="vVJZI9Xm9fWbKHxDdjZc2tSSTLS" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfca57fee6353887c9e5411f71c4b8c926e29704_2_690x337.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfca57fee6353887c9e5411f71c4b8c926e29704_2_1035x505.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfca57fee6353887c9e5411f71c4b8c926e29704.png 2x" data-dominant-color="989795"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">registration</span><span class="informations">1347×659 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-05-01 18:40 UTC)

<p>You can apply the same transform to the segmentation as you applied to the underlying image. See instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">here</a>.</p>

---
