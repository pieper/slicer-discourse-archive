# Converting the physical dose to biologically effective dose (BED)

**Topic ID**: 41376
**Date**: 2025-01-30
**URL**: https://discourse.slicer.org/t/converting-the-physical-dose-to-biologically-effective-dose-bed/41376

---

## Post #1 by @azam (2025-01-30 14:35 UTC)

<p>Hi everyone<br>
I have a DICOM RT dose file (It contains physical dose). I want to convert it to Biologically Effective Dose based on the below formula. That is, find the dose of each voxel (di) and put it in the formula and convert it to BED. Is it possible to convert a physical dose file to Biological dose file using 3DSlicer software?</p>
<p>(I think when the mouse is placed on the RT dose file in 3dSlicer, it shows the dose of each voxel (di) in Data probe. How can I get this dose and convert it to biologically effective dose? )<br>
Can you guide me?<br>
Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a51d6756334448ec5cffcd74df96f3396253272d.png" data-download-href="/uploads/short-url/nyFMl3VBz0JoRscdWF39DBIB8At.png?dl=1" title="BED" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a51d6756334448ec5cffcd74df96f3396253272d.png" alt="BED" data-base62-sha1="nyFMl3VBz0JoRscdWF39DBIB8At" width="375" height="79"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BED</span><span class="informations">500×106 6.63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(n , a/b are constant.)</p>

---

## Post #2 by @cpinter (2025-02-06 15:29 UTC)

<p>You can access the dose volume as numpy array as described here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates</a></p>
<p>Then you can use numpy array operations to apply the formula. It is linear so there should be no problem. Let me know if you are stuck.</p>

---
