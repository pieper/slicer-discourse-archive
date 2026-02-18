# Question about DCM files orientation

**Topic ID**: 8426
**Date**: 2019-09-14
**URL**: https://discourse.slicer.org/t/question-about-dcm-files-orientation/8426

---

## Post #1 by @Mizo (2019-09-14 11:32 UTC)

<p>first it is great software, when i saw it couldn’t believe what it can do with dicom files<br>
have a simple question , i have some CT ( DCM) data when i open them inside slicer the sagittal and coronal view are not showing the correct orientation of the DCM files, as if they were flipped , while the axial view is correct<br>
i did some research and i tried reformat , and i couldn’t rotate them correctly<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54081f3a990c5f91ba036b524d0091b012245edd.jpeg" data-download-href="/uploads/short-url/bZnvxOs6eDS46BUdS8fTpX9lzNH.jpeg?dl=1" title="oriantation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54081f3a990c5f91ba036b524d0091b012245edd_2_690x460.jpeg" alt="oriantation" data-base62-sha1="bZnvxOs6eDS46BUdS8fTpX9lzNH" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54081f3a990c5f91ba036b524d0091b012245edd_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54081f3a990c5f91ba036b524d0091b012245edd_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54081f3a990c5f91ba036b524d0091b012245edd_2_1380x920.jpeg 2x" data-dominant-color="3D3D49"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">oriantation</span><span class="informations">1386×924 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Mizo (2019-09-14 11:38 UTC)

<p>found a solution that i have to open them inside the dicom browser data base first, the problem happens when i open them using add data or drag the folder inside 3d slicer</p>

---

## Post #3 by @lassoan (2019-09-14 11:47 UTC)

<p>DICOM data should be always loaded using the DICOM module by drag-and-dropping the parent folder of the data set.</p>
<p>If you use “Add data” then ITK library’s image file loader is used, which may or may not work.</p>

---
