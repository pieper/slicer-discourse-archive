---
topic_id: 38515
title: "Matching Volumes"
date: 2024-09-24
url: https://discourse.slicer.org/t/38515
---

# Matching volumes

**Topic ID**: 38515
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/matching-volumes/38515

---

## Post #1 by @Olivier (2024-09-24 12:07 UTC)

<p>Hello,</p>
<p>Context:<br>
I have volumes from the same muscle collected with 3D ultrasound and the IGT link extension, at 2 different time points.<br>
Aim:<br>
After volume reconstruction, I would like to match the volume orientation and relative position to segment matching slices.<br>
Question:<br>
I managed to align the volumes with fiducial registration. Is there an extension that would allow browsing through slices of both volumes and do the segmentation? (I get to do this with the “Compare Volume” extension but not to segment independently)</p>

---

## Post #2 by @cpinter (2024-09-30 09:14 UTC)

<p>Do I understand correctly that you want to have one segmentation for the two volumes? If so, it is quite unusual, especially that you say they are from two different time points. I suggest doing the segmentation for both of them, and that will give you a basis for comparison.</p>

---

## Post #3 by @Olivier (2024-09-30 10:05 UTC)

<p>Thanks for the answer!</p>
<p>I do want to segment each volume separately.<br>
I can do that already but if I am only interested in comparing a cross-section of each volume, it is not accurate because of the slight differences in volume orientation. I solved this by registrering the volumes and now I am looking for a way to browse and segment volume slices simultaneously in the segment editor (eg in side-by-side windows of their axial views).</p>

---

## Post #4 by @cpinter (2024-09-30 11:09 UTC)

<p>There are comparative layouts in Slicer. You can select one and set up display so that in one group you show one volume and the corresponding segmentation, and in the other group the other volume/segmentation pair.</p>
<p>You’ll need this option in the Segmentations module so that only one segmentation is visible in each group:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13cb6e3923dc7f4ec496501fee3f1f59e1e7edff.png" data-download-href="/uploads/short-url/2P6V26nKkRJv6xuprZLfzDjxaKH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13cb6e3923dc7f4ec496501fee3f1f59e1e7edff_2_354x500.png" alt="image" data-base62-sha1="2P6V26nKkRJv6xuprZLfzDjxaKH" width="354" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13cb6e3923dc7f4ec496501fee3f1f59e1e7edff_2_354x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13cb6e3923dc7f4ec496501fee3f1f59e1e7edff_2_531x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13cb6e3923dc7f4ec496501fee3f1f59e1e7edff.png 2x" data-dominant-color="F1F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">541×763 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the “Four over four” layout set up like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecd913ece092be940fecf05c2d00d0b8656d24f5.jpeg" data-download-href="/uploads/short-url/xNfLKpBKzYyVNoyOPnyPgc9XELX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd913ece092be940fecf05c2d00d0b8656d24f5_2_690x434.jpeg" alt="image" data-base62-sha1="xNfLKpBKzYyVNoyOPnyPgc9XELX" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd913ece092be940fecf05c2d00d0b8656d24f5_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd913ece092be940fecf05c2d00d0b8656d24f5_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecd913ece092be940fecf05c2d00d0b8656d24f5_2_1380x868.jpeg 2x" data-dominant-color="959797"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1210 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The only thing you don’t get is simultaneous scrolling, because the navigation (shift+mouse move or slice intersections with interaction) works only within groups. A solution could be adding a fiducial that serves as the common 3D cursor, and you can navigate it in one group, then click on it in the 3D of the other group, making the slice views in the other group jump to the same position.</p>
<p>This is probably just one of the many solutions, but it seems viable to me.</p>

---

## Post #5 by @Olivier (2024-10-03 04:20 UTC)

<p>Thank you again for your help. Yes, I am using a similar approach (although I didn’t think of using a fiducial in the process). This will do. Synchronised scrolling between groups would be a nice feature addition though.</p>

---

## Post #6 by @cpinter (2024-10-03 08:42 UTC)

<p>Maybe adding another option here for linking all view groups as well wouldn’t overcomplicate things (Slicer is already too complex).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b503aad160b8a92eb7c70c004a49e6bc76ca3189.png" alt="image" data-base62-sha1="pPkhjiuG78nyF7ha7JlyQfwyhWF" width="158" height="95"></p>
<p>Or improving the CompareVolumes module…</p>

---

## Post #7 by @Olivier (2024-10-03 09:29 UTC)

<p>I agree, this would be a better approach.</p>

---
