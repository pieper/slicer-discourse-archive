# Why is it that after I import the patient's CT file (in DICOM format), the image is not displayed completely but only shows as a slit?

**Topic ID**: 42165
**Date**: 2025-03-16
**URL**: https://discourse.slicer.org/t/why-is-it-that-after-i-import-the-patients-ct-file-in-dicom-format-the-image-is-not-displayed-completely-but-only-shows-as-a-slit/42165

---

## Post #1 by @kkzmcbb (2025-03-16 02:14 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99e155b726439fd5b4cc7bd80611425c704b94e7.jpeg" data-download-href="/uploads/short-url/lXhPuTclQhcc9Bc7Gf9TlLCV5dR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99e155b726439fd5b4cc7bd80611425c704b94e7_2_609x500.jpeg" alt="image" data-base62-sha1="lXhPuTclQhcc9Bc7Gf9TlLCV5dR" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99e155b726439fd5b4cc7bd80611425c704b94e7_2_609x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99e155b726439fd5b4cc7bd80611425c704b94e7_2_913x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99e155b726439fd5b4cc7bd80611425c704b94e7.jpeg 2x" data-dominant-color="404248"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1171×960 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-03-16 02:22 UTC)

<p>This is a projection = a 2D image. It is not a 3D volume.</p>
<p>If you have hundreds of projection images like this then it is possible to reconstruct a 3D image from it, but reconstruction is a complex operation and - since you need very accurate information on the imaging geometry - usually only the manufacturer can do it.</p>
<p>You can ask the people who gave you this image to create a 3D reconstruction and send that to you, too.</p>

---
