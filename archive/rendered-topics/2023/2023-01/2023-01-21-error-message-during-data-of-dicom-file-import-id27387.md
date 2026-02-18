# Error message during data of DICOM file import 

**Topic ID**: 27387
**Date**: 2023-01-21
**URL**: https://discourse.slicer.org/t/error-message-during-data-of-dicom-file-import/27387

---

## Post #1 by @pbs543210 (2023-01-21 01:04 UTC)

<p>Hello all,</p>
<p>I am a beginner of SlicerDMRI S/W and having some difficulties with DICOM data import.</p>
<p>When I tried to import DICOM data (.dcm files) using DWIConvert option, I got an error message of below,</p>
<p>"<br>
Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
Exception creating converter<br>
itk::ExceptionObject (000000BCD0EFB3F0)<br>
Location: “unknown”<br>
File: D:\D\S\Slicer-4102-build\BRAINSTools\DWIConvert\GenericDWIConverter.cxx<br>
Line: 13<br>
Description: itk::ERROR: LoadFromDisk not relevant<br>
"<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af.jpeg" data-download-href="/uploads/short-url/kFoo3GOa2C3bZ38ObyE45v4Nohp.jpeg?dl=1" title="21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af_2_450x500.jpeg" alt="21" data-base62-sha1="kFoo3GOa2C3bZ38ObyE45v4Nohp" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af_2_450x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af_2_675x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af.jpeg 2x" data-dominant-color="F2F3F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21</span><span class="informations">785×872 99.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any help would be appreciated.</p>

---

## Post #2 by @pbs543210 (2023-01-21 01:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af.jpeg" data-download-href="/uploads/short-url/kFoo3GOa2C3bZ38ObyE45v4Nohp.jpeg?dl=1" title="21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af_2_450x500.jpeg" alt="21" data-base62-sha1="kFoo3GOa2C3bZ38ObyE45v4Nohp" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af_2_450x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af_2_675x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90d95511d2db13da8da6cde999fba7ec16bb95af.jpeg 2x" data-dominant-color="F2F3F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21</span><span class="informations">785×872 99.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @pieper (2023-01-22 19:58 UTC)

<p>Converting DWI data correctly is very tricky, and this looks like a mouse experiment so you’ll need to put in extra effort.  You can try dcm2niix, but like DWIConvert it is mostly used on human scans.  My best suggestion is to study the acquisition protocol (gradients, b-values, scan directions, etc) and manually construct a nrrd header that describes the data.</p>

---
