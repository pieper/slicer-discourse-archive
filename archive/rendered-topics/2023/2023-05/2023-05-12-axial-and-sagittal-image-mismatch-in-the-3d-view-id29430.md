# Axial and sagittal image mismatch in the 3D view

**Topic ID**: 29430
**Date**: 2023-05-12
**URL**: https://discourse.slicer.org/t/axial-and-sagittal-image-mismatch-in-the-3d-view/29430

---

## Post #1 by @LiliHu (2023-05-12 15:53 UTC)

<p>Slicer version: 5.2.2</p>
<p>Hello all,<br>
I would like to export coordinates of measuring points and have just noticed that the CT slice images in the 3D view do not line up correctly. Now I am afraid that I will get measurement inaccuracies. It looks to me as if one or more rows of pixels have been assigned to the axial slice image, causing an offset. I have this problem with all my DICOM data and also the sample dataset “Chest” (used here on the image). Does anyone know what this offset can be due to and how I can adjust it for all datasets? I don’t think it’s the datasets alone, at least they are displayed correctly in InVeaslius…A little tip would be great! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b99a829fbf8e5123582b51110ae8ef418a2cc462.png" data-download-href="/uploads/short-url/qtVmRlBYeQuk0eV6KSA0LWkLAY2.png?dl=1" title="3D-Slicer_Versatz" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b99a829fbf8e5123582b51110ae8ef418a2cc462_2_500x500.png" alt="3D-Slicer_Versatz" data-base62-sha1="qtVmRlBYeQuk0eV6KSA0LWkLAY2" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b99a829fbf8e5123582b51110ae8ef418a2cc462_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b99a829fbf8e5123582b51110ae8ef418a2cc462_2_750x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b99a829fbf8e5123582b51110ae8ef418a2cc462.png 2x" data-dominant-color="9A99A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D-Slicer_Versatz</span><span class="informations">840×840 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-05-12 16:03 UTC)

<p>By default, the slice image is copied to the 3D views. If the resolution of the slice view is much lower than the resolution of the 3D view (e.g., you maximized the 3D view or you zoomed out in the slice view) then up to a half-pixel offset (at the slice view’s current zoom factor) may be visible due to image interpolation. In most cases this should not be a problem, but if it is for you then you can make the interpolation in the two views independent by choosing “FOV, Spacing match Volumes” option in the slice view controllers.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cd06589c77c274e908355ce85cbc882c3790412.png" alt="image" data-base62-sha1="8FZ8qBWiNg2yIpAxOPTn1N5ma2K" width="590" height="445"></p>

---
