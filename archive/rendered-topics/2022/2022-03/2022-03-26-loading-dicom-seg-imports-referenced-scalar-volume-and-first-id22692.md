# Loading DICOM SEG imports referenced scalar volume and first slice of referenced series

**Topic ID**: 22692
**Date**: 2022-03-26
**URL**: https://discourse.slicer.org/t/loading-dicom-seg-imports-referenced-scalar-volume-and-first-slice-of-referenced-series/22692

---

## Post #1 by @jordanpn (2022-03-26 00:38 UTC)

<p>When loading DICOM SEG objects, Slicer suggests loading referenced datasets, i.e. the MR series on which segmentation was performed, which makes perfect sense. Is it expected behavior that after loading, Slicer creates two MR data objects, Image Sequence and Scalar Volume? In particular the Image Sequence object is causing some confusion as it is not visualized by default and when enabled only shows the first slice in the series. (screenshot attached)</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2fca7b315542c124b1c05d98cfe47f7e47a54c9.jpeg" data-download-href="/uploads/short-url/rOVWip4lvjTVsQYdOCc2HP8w0op.jpeg?dl=1" title="Slicer_DICOM_SEG_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2fca7b315542c124b1c05d98cfe47f7e47a54c9_2_600x500.jpeg" alt="Slicer_DICOM_SEG_1" data-base62-sha1="rOVWip4lvjTVsQYdOCc2HP8w0op" width="600" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2fca7b315542c124b1c05d98cfe47f7e47a54c9_2_600x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2fca7b315542c124b1c05d98cfe47f7e47a54c9_2_900x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2fca7b315542c124b1c05d98cfe47f7e47a54c9_2_1200x1000.jpeg 2x" data-dominant-color="44474B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_DICOM_SEG_1</span><span class="informations">1920×1600 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/536be02d99118caa149c36fc3daea75044ebeb67.jpeg" data-download-href="/uploads/short-url/bTYKFdQ7lckJwhbzwibmuU3QBAb.jpeg?dl=1" title="Slicer_DICOM_SEG_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/536be02d99118caa149c36fc3daea75044ebeb67_2_608x500.jpeg" alt="Slicer_DICOM_SEG_2" data-base62-sha1="bTYKFdQ7lckJwhbzwibmuU3QBAb" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/536be02d99118caa149c36fc3daea75044ebeb67_2_608x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/536be02d99118caa149c36fc3daea75044ebeb67_2_912x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/536be02d99118caa149c36fc3daea75044ebeb67_2_1216x1000.jpeg 2x" data-dominant-color="2C2C2C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_DICOM_SEG_2</span><span class="informations">1920×1578 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-03-26 03:47 UTC)

<p>For some reason the MRI series is recognized as an image sequence instead of a volume. Probably this issue is fixed in current Slicer versions. Let us know if you experience any issues in the latest Slicer Preview Release.</p>

---

## Post #3 by @jordanpn (2022-03-26 05:48 UTC)

<p>Thank you for the quick reply. Unfortunately, the same behavior occurs with the latest version in preview (4.13.0-2022-03-23).</p>

---

## Post #4 by @lassoan (2022-03-26 12:15 UTC)

<p>Can you share the data set?</p>

---

## Post #5 by @jordanpn (2022-03-26 23:23 UTC)

<p>Absolutely, it’s the first patient in this public dataset from TCIA: <a href="https://wiki.cancerimagingarchive.net/display/Public/QIN-PROSTATE-Repeatability" class="inline-onebox" rel="noopener nofollow ugc">QIN-PROSTATE-Repeatability - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki</a></p>
<p>I have seen this same behavior with other DICOM SEG datasets as well.</p>

---

## Post #6 by @lassoan (2022-03-27 00:13 UTC)

<p>I’ve downloaded <code>PCAMPMRI-00001</code> data set and loaded <code>series 1005</code> and indeed the referenced <code>series 5</code> was offered to be loaded both as 3D image and a 2D+t image. This is not an error, because both are completely valid interpretations of that series and these legacy DICOM information objects do not mandate any specific interpretations.</p>
<p>That said, Slicer determines a “confidence” value for each interpretation and it could make sense to offer just a single one (that with the highest confidence value), because probably that is what most users expect.</p>
<p>For now you can manually select the interpretation that you prefer, which is probably the “scalar volume” (and not “image sequence”).</p>

---

## Post #7 by @jordanpn (2022-03-27 06:07 UTC)

<p>Great, I really appreciate you investigating the issue and providing the insight. The reason I created this thread was because I initially thought something was wrong with my dataset and that I have perhaps inserted an erroneous DICOM tag. I agree that scalar volume is what most users would expect when loading a DICOM SEG object like this. Thanks again!</p>

---
