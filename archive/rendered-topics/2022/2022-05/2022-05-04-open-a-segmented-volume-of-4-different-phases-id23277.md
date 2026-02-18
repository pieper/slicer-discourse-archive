# Open a segmented volume of 4 different phases

**Topic ID**: 23277
**Date**: 2022-05-04
**URL**: https://discourse.slicer.org/t/open-a-segmented-volume-of-4-different-phases/23277

---

## Post #1 by @lolamartinalonso (2022-05-04 11:09 UTC)

<p>Hi, I have a segmented volume with 4 different phases. Each phase has a different value from 0 to 4 in the histogram.</p>
<p>When I try to upload the volume (saved as .mrrda) it appears in black and white only. When in ImageJ has 4 different colour. (See the image attached)</p>
<p>The thing is that I want to tenderize the segmented volume in 3D Slicer, giving each phase a different color.</p>
<p>Do I have to apply a threshold to the segmented volume?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77aced375edf00525fd1ee3c937953a75c766d0d.jpeg" data-download-href="/uploads/short-url/h4HjnwtFudaxAF6986qtkwbtlH7.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77aced375edf00525fd1ee3c937953a75c766d0d_2_469x500.jpeg" alt="Capture" data-base62-sha1="h4HjnwtFudaxAF6986qtkwbtlH7" width="469" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77aced375edf00525fd1ee3c937953a75c766d0d_2_469x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77aced375edf00525fd1ee3c937953a75c766d0d_2_703x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77aced375edf00525fd1ee3c937953a75c766d0d.jpeg 2x" data-dominant-color="D06FCC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">863×919 91.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-05-04 11:58 UTC)

<p>When you load in Slicer, try picking Segmentation instead of the default Volume.</p>

---
