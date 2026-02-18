# Copy images from 3D view with the same dimensions/field-of-views

**Topic ID**: 38376
**Date**: 2024-09-14
**URL**: https://discourse.slicer.org/t/copy-images-from-3d-view-with-the-same-dimensions-field-of-views/38376

---

## Post #1 by @Deep_Learning (2024-09-14 10:59 UTC)

<p>I am trying to make a figure from several subjects.  I need to copy the image from the 3D view and then montage the images in powerpoint…  How can I display a certain field of view in the 3D view.  The problem that I have is that I copy differenet subjects with differenet zooms and FOVs and the bigger organ is actually smaller in Figure.<br>
Thanks in advance…</p>

---

## Post #2 by @lassoan (2024-09-15 02:01 UTC)

<p>You can click on the link button in the view controller bar (at the top of each view) to synchronize zoom factor between all views.</p>

---

## Post #3 by @Deep_Learning (2024-10-19 11:55 UTC)

<p>Thanks for your reply.  I believe that this sort of works.  I do not think that it works with 3D views from segmentations/volumes with different pixel sizes.</p>

---

## Post #4 by @lassoan (2024-10-22 03:10 UTC)

<p>All 2D and 3D renderings in Slicer are done in physical space, so size of all objects (volumes, segmentations, etc.) will always match the physical size of all other objects in the views, regardless of voxel size.</p>

---
