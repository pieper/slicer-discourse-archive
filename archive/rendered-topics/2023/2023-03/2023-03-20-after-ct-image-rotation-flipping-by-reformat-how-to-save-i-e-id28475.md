# After CT image rotation & flipping by [Reformat], how to save? I export reformatted DICOM, but get no change at all

**Topic ID**: 28475
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/after-ct-image-rotation-flipping-by-reformat-how-to-save-i-export-reformatted-dicom-but-get-no-change-at-all/28475

---

## Post #1 by @Teddy (2023-03-20 13:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ea93649d74adde1b7212740d4aca959739260d1.jpeg" data-download-href="/uploads/short-url/mDzYtQwDPxpRDOfoVfnq8RCFt7P.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ea93649d74adde1b7212740d4aca959739260d1_2_690x385.jpeg" alt="image" data-base62-sha1="mDzYtQwDPxpRDOfoVfnq8RCFt7P" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ea93649d74adde1b7212740d4aca959739260d1_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ea93649d74adde1b7212740d4aca959739260d1_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ea93649d74adde1b7212740d4aca959739260d1_2_1380x770.jpeg 2x" data-dominant-color="42424E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1387×775 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7764fe294c77b17b73d18383fa30f3404ad87aae.jpeg" data-download-href="/uploads/short-url/h2dc5Xan3OX4c0jQOKnSYj6vqtU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7764fe294c77b17b73d18383fa30f3404ad87aae_2_690x307.jpeg" alt="image" data-base62-sha1="h2dc5Xan3OX4c0jQOKnSYj6vqtU" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7764fe294c77b17b73d18383fa30f3404ad87aae_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7764fe294c77b17b73d18383fa30f3404ad87aae_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7764fe294c77b17b73d18383fa30f3404ad87aae_2_1380x614.jpeg 2x" data-dominant-color="7A7A82"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1950×868 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-21 01:41 UTC)

<p>By rotating a view, you don’t make any changes to the image. Instead, you can leave your views as is (don’t use <code>Reformat</code> module) and apply a transform to the volume. You can then resample the module using one of the resampling modules or using <code>Crop volume</code> module.</p>

---
