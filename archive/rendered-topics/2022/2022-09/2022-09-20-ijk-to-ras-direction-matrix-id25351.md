---
topic_id: 25351
title: "Ijk To Ras Direction Matrix"
date: 2022-09-20
url: https://discourse.slicer.org/t/25351
---

# IJK to RAS direction Matrix

**Topic ID**: 25351
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/ijk-to-ras-direction-matrix/25351

---

## Post #1 by @jegberink (2022-09-20 09:02 UTC)

<p>Hello everyone,</p>
<p>Quick questions:<br>
I have a CT scan. In its volume information is the IJK to RAS direction matrix.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a790ff0012fc79cae3cc1770c41bd3641d7e8984.png" data-download-href="/uploads/short-url/nUmocbd3yE8xPGdP1l9XFjCbebW.png?dl=1" title="ijktoras" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a790ff0012fc79cae3cc1770c41bd3641d7e8984_2_637x500.png" alt="ijktoras" data-base62-sha1="nUmocbd3yE8xPGdP1l9XFjCbebW" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a790ff0012fc79cae3cc1770c41bd3641d7e8984_2_637x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a790ff0012fc79cae3cc1770c41bd3641d7e8984_2_955x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a790ff0012fc79cae3cc1770c41bd3641d7e8984.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ijktoras</span><span class="informations">971×762 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any measurements i do in the coronal, sagittal or axial views would now be in the RAS system correct?</p>
<p>And any models i make from segmentations in this volume would by default be in RAS since these arent voxel based?</p>
<p>And the RAS coordinates (or the position of the patient when compared to the world and IJK system) have been set when the initial scan was made, correct?</p>
<p>Thank you kindly in advance.</p>

---

## Post #2 by @cpinter (2022-09-20 13:45 UTC)

<p>All assumptions are correct. By the way World and RAS are considered the same in Slicer.</p>

---

## Post #3 by @jegberink (2022-09-20 13:49 UTC)

<p>Thank you, I’m glad I’m starting to understand it.</p>

---
