# Lock a specific plane for rotating or translating only

**Topic ID**: 37327
**Date**: 2024-07-11
**URL**: https://discourse.slicer.org/t/lock-a-specific-plane-for-rotating-or-translating-only/37327

---

## Post #1 by @Miguel_Nobre_Menezes (2024-07-11 15:56 UTC)

<p>I’m currently building a module for CT analysis. I’ve managed to do quite a bit and am in the process of refining it. I already created planes, rotated and centered them, added custom measurements and plotted a way to get the 3D view to rotate perpendicularly to the plane to get the correct C-arm views.</p>
<p>I would now like to lock a specific plane from rotating or translating. Specifically, I need to stop the sagital and coronal planes from rotating, and the axial plane from translating. How can this be done with python for the module?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf51908d54ff650fe0f1d1835f3d8e935b54e605.jpeg" data-download-href="/uploads/short-url/ritWNmKUK3L6ORzQ9EDASKrj9gF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf51908d54ff650fe0f1d1835f3d8e935b54e605_2_690x477.jpeg" alt="image" data-base62-sha1="ritWNmKUK3L6ORzQ9EDASKrj9gF" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf51908d54ff650fe0f1d1835f3d8e935b54e605_2_690x477.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf51908d54ff650fe0f1d1835f3d8e935b54e605_2_1035x715.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf51908d54ff650fe0f1d1835f3d8e935b54e605_2_1380x954.jpeg 2x" data-dominant-color="605F59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1329 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-07-13 20:21 UTC)

<p>You can customize what actions and mouse&amp;keyboard gestures are available for each view as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#disable-certain-user-interactions-in-slice-views">examples in the script repository</a>.</p>

---
