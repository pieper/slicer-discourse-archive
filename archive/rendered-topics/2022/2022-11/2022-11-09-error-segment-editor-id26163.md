# error segment editor

**Topic ID**: 26163
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/error-segment-editor/26163

---

## Post #1 by @Sara_Jakobs (2022-11-09 15:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2e6b21454618d002926da308920f75415ee8bc.png" data-download-href="/uploads/short-url/oQSwV6DItC8Q6Ri4RaePTG9sp2I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2e6b21454618d002926da308920f75415ee8bc_2_690x388.png" alt="image" data-base62-sha1="oQSwV6DItC8Q6Ri4RaePTG9sp2I" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2e6b21454618d002926da308920f75415ee8bc_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2e6b21454618d002926da308920f75415ee8bc_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2e6b21454618d002926da308920f75415ee8bc_2_1380x776.png 2x" data-dominant-color="3C3D44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I want to edit segmentations I get this message. What should I do?</p>
<p>HELP!</p>

---

## Post #2 by @pieper (2022-11-09 18:49 UTC)

<p>Please provide some more detail about what steps you took that led to this error.  Ideally provide us with sample data to reproduce it.</p>
<p>From the screenshot it looks like you have just one slice in your source volume, so my guess is that some 3D operation couldn’t be performed on this.  Ideally the segment editor should be detecting this situation and not offering operations that will lead to this dialog being triggered.</p>

---
