# CT image appears to be distorted

**Topic ID**: 16519
**Date**: 2021-03-13
**URL**: https://discourse.slicer.org/t/ct-image-appears-to-be-distorted/16519

---

## Post #1 by @Tamas_Egyed (2021-03-12 19:21 UTC)

<p>My saggital and horisontal view is fully distorted and it doesn!t create a 3d image.<br>
What can be the problem<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9755741829757dadce169e4fd26d75fda5262b0.jpeg" data-download-href="/uploads/short-url/ob65PJsn4INVsh3pr6fuTgOBrzi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9755741829757dadce169e4fd26d75fda5262b0_2_690x490.jpeg" alt="image" data-base62-sha1="ob65PJsn4INVsh3pr6fuTgOBrzi" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9755741829757dadce169e4fd26d75fda5262b0_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9755741829757dadce169e4fd26d75fda5262b0_2_1035x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9755741829757dadce169e4fd26d75fda5262b0.jpeg 2x" data-dominant-color="80818B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1287×915 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-03-13 00:52 UTC)

<p>If a volume is stretched out along certain axes then it means that image spacing (voxel size) is incorrect. Is this a DICOM image coming straight from a clinical CT scanner?</p>

---
