# Import DICOM multiple AcquisitionNumber instead of one series

**Topic ID**: 30554
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/import-dicom-multiple-acquisitionnumber-instead-of-one-series/30554

---

## Post #1 by @lvdw (2023-07-12 14:55 UTC)

<p>Operating system: MacOS<br>
Slicer version: 5,2,2<br>
Expected behavior: One continuous series<br>
Actual behavior: 10 series of 4 slices each</p>
<p>Unlike post <a href="https://discourse.slicer.org/t/problems-during-dicom-import/9060" class="inline-onebox">Problems during Dicom import</a> the ImageOrientationPatient is the same.</p>
<p>Problem looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/630c33620cd97a1fa2797ecd9f06696ee178870f.png" data-download-href="/uploads/short-url/e8dpo3RHp9n1KQZTkQQY6D1VPCD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/630c33620cd97a1fa2797ecd9f06696ee178870f_2_690x374.png" alt="image" data-base62-sha1="e8dpo3RHp9n1KQZTkQQY6D1VPCD" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/630c33620cd97a1fa2797ecd9f06696ee178870f_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/630c33620cd97a1fa2797ecd9f06696ee178870f_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/630c33620cd97a1fa2797ecd9f06696ee178870f_2_1380x748.png 2x" data-dominant-color="262729"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×1038 74.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So when I load them this happens:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61185bcdbb26792539baca82e3abe605c70f18c1.png" data-download-href="/uploads/short-url/dQWvapY1JEKPWmWGuIW1rLHG3VD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61185bcdbb26792539baca82e3abe605c70f18c1_2_690x374.png" alt="image" data-base62-sha1="dQWvapY1JEKPWmWGuIW1rLHG3VD" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61185bcdbb26792539baca82e3abe605c70f18c1_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61185bcdbb26792539baca82e3abe605c70f18c1_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61185bcdbb26792539baca82e3abe605c70f18c1_2_1380x748.png 2x" data-dominant-color="191918"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×1038 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Files were acquired elsewhere, pseudonymized, zipped and transferred using BOX<br>
I never encountered this problem with my locally acquired datasets, but the problem is persistent with this transferred dataset.</p>
<p>If I import them in another DICOM viewer (Horos in my case), there is no problem loading them as one series.<br>
Of course it could be a transfer problem, but is there a way to make them usable again in 3D slicer for lesion segmentation?</p>

---

## Post #2 by @lassoan (2023-07-12 15:00 UTC)

<p>Maybe this image was sequential (scan-move-scan) acquisition from decades ago? By default each image acquisitions is reconstructed into a separate volume, but you can probably choose load it as one volume if you enable “Advanced” option in the DICOM browser.</p>

---

## Post #3 by @lvdw (2023-07-12 15:08 UTC)

<p>Thank you, this worked:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a695b2c947d41e8d4225148ce4525362549b7a6.png" data-download-href="/uploads/short-url/jKrC9IeB9GB0OmLxTa5RuQJvEQm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a695b2c947d41e8d4225148ce4525362549b7a6.png" alt="image" data-base62-sha1="jKrC9IeB9GB0OmLxTa5RuQJvEQm" width="690" height="18" data-dominant-color="555555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1361×37 5.32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
If I only load the last one it works fine.</p>
<p>It’s a scan from 2011.</p>

---
