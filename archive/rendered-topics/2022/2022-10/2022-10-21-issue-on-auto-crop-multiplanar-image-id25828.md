# Issue on auto-crop multiplanar image

**Topic ID**: 25828
**Date**: 2022-10-21
**URL**: https://discourse.slicer.org/t/issue-on-auto-crop-multiplanar-image/25828

---

## Post #1 by @damiazlkflee (2022-10-21 12:20 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Issue: when I uploaded CT scan images, it should show full images of axial, coronal and sagittal (as attached below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a7ad2c38b73b9e994049a031734c8596c95de0f.jpeg" data-download-href="/uploads/short-url/aCStN5qWtGYM3c9BuwjDb64q1xt.jpeg?dl=1" title="3d cut 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a7ad2c38b73b9e994049a031734c8596c95de0f_2_690x325.jpeg" alt="3d cut 2" data-base62-sha1="aCStN5qWtGYM3c9BuwjDb64q1xt" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a7ad2c38b73b9e994049a031734c8596c95de0f_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a7ad2c38b73b9e994049a031734c8596c95de0f_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a7ad2c38b73b9e994049a031734c8596c95de0f.jpeg 2x" data-dominant-color="8D8C91"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d cut 2</span><span class="informations">1350×637 80.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But some images appeared cropped immediately after I uploaded the images (as attached below). May I know why this happened and how to fix this issue?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c22a0b468c7c8b57e6a39091be22625c6d8812ef.jpeg" data-download-href="/uploads/short-url/rHEHUok0vMgEfv23u1QWt9LUPjV.jpeg?dl=1" title="3d cut" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c22a0b468c7c8b57e6a39091be22625c6d8812ef_2_690x330.jpeg" alt="3d cut" data-base62-sha1="rHEHUok0vMgEfv23u1QWt9LUPjV" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c22a0b468c7c8b57e6a39091be22625c6d8812ef_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c22a0b468c7c8b57e6a39091be22625c6d8812ef_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c22a0b468c7c8b57e6a39091be22625c6d8812ef.jpeg 2x" data-dominant-color="88888E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d cut</span><span class="informations">1353×649 84.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2022-10-21 12:28 UTC)

<p>For some reason, your CT scanner assigned different acquisition numbers to groups of slices. You may be able to adjust the settings on your scanner to avoid this. Alternatively, you can force loading the entire series as one volume by clicking the “Advanced” checkbox in the DICOM browser, clicking “Examine”, then in the loadable list select the item that is not split by acquisitionNumber.</p>
<p>Please also try the current Slicer version. A lot of improvements/fixes have been implemented since Slicer-4.11, including in the DICOM browser.</p>

---
