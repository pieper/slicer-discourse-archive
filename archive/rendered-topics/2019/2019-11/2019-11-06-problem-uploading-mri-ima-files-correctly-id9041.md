# Problem uploading MRI (IMA files) correctly 

**Topic ID**: 9041
**Date**: 2019-11-06
**URL**: https://discourse.slicer.org/t/problem-uploading-mri-ima-files-correctly/9041

---

## Post #1 by @Jonathan (2019-11-06 12:07 UTC)

<p>Operating system: WINDOWS 10<br>
Slicer version: 4.10.1<br>
Actual behavior: partial volume of the geometry is presented. (all planes are sliced)</p>
<p>printsceen is attached.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ad46f6545895dfa6cb607780a66a0c35cbf7b7c.png" alt="Sagittal_plane" data-base62-sha1="66Tc1wyKnKG2aKkOEWkdSiwkHMg" width="661" height="480"></p>

---

## Post #2 by @lassoan (2019-11-06 13:37 UTC)

<p>Use DICOM module to import and load DICOM files. DICOM module is greatly improved in recent Slicer Preview Release, so I would recommend to try that.</p>
<p>You might be able to use “Add data” dialog to load certain DICOM files. For that, check “Show Options” and uncheck “SingleFile” before clicking Apply. However, this will not likely to work correctly for cine images (time sequences).</p>

---

## Post #3 by @pieper (2019-11-06 13:40 UTC)

<p>Also it looks like your images were acquired obliquely, so you may want to rotate the view to volume plane.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8866b27a216e349f4e652ef21c6cc734b7c85b1.png" data-download-href="/uploads/short-url/qknQohS1Hj0WWsHiM6alu2ResDL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8866b27a216e349f4e652ef21c6cc734b7c85b1_2_690x217.png" alt="image" data-base62-sha1="qknQohS1Hj0WWsHiM6alu2ResDL" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8866b27a216e349f4e652ef21c6cc734b7c85b1_2_690x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8866b27a216e349f4e652ef21c6cc734b7c85b1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8866b27a216e349f4e652ef21c6cc734b7c85b1.png 2x" data-dominant-color="E1D5D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">792×250 46.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Jonathan (2019-11-10 08:23 UTC)

<p>I have tried to upload the files via the DICOM module and also by using the "Add data"option without success. The rotation tip was useful.</p>

---

## Post #5 by @lassoan (2019-11-10 12:42 UTC)

<p>Use the DICOM module and follow tips in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">DICOM FAQ</a>. If you still have issues then tell us what you do, what you expect to happen, and what happens instead (what messages are displayed, what is displayed in the viewers). Or upload a phantom or anonymized dataset somewhere and post the link.</p>

---
