---
topic_id: 42652
title: "View Format Of 3D Slicer Coronal Axial Saggital"
date: 2025-04-22
url: https://discourse.slicer.org/t/42652
---

# View Format of 3D Slicer (Coronal, Axial, Saggital)

**Topic ID**: 42652
**Date**: 2025-04-22
**URL**: https://discourse.slicer.org/t/view-format-of-3d-slicer-coronal-axial-saggital/42652

---

## Post #1 by @aleee97 (2025-04-22 14:25 UTC)

<p>Hi Everyone</p>
<p>Is it possible, that if I load a Series of Slice in Coronal view, that 3D Slicer automatically creates the axial and saggital view ? I am asking, because when loading the date with python, I don’t find any MRI Images in the other view. I already have looked at the shape of the array (see example image, Dimension of Array: (704, 700))<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e9d285792567916f4200c2583bf153314fe2f0b.png" data-download-href="/uploads/short-url/bdrWYGqPQ6UC6cMklc4qMefR5yP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e9d285792567916f4200c2583bf153314fe2f0b.png" alt="image" data-base62-sha1="bdrWYGqPQ6UC6cMklc4qMefR5yP" width="690" height="213" data-dominant-color="252627"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">738×228 8.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If so, is there a way to download the other views? How can I agline theme afterwards to the exact coronal view?</p>
<p>Thank you and Regards</p>
<p>Alessio</p>

---

## Post #2 by @pieper (2025-04-22 15:37 UTC)

<p>Since the shape has 2 elements, this is loaded in Slicer as a single slice volume, so you should just see a line in the other two views.</p>

---

## Post #3 by @aleee97 (2025-04-22 16:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bdef6831240456b86ffcbc85f153560f64df91e.jpeg" data-download-href="/uploads/short-url/8xDRJoeBbNIGCGsMDDn1pZRuMR8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bdef6831240456b86ffcbc85f153560f64df91e_2_622x499.jpeg" alt="image" data-base62-sha1="8xDRJoeBbNIGCGsMDDn1pZRuMR8" width="622" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bdef6831240456b86ffcbc85f153560f64df91e_2_622x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bdef6831240456b86ffcbc85f153560f64df91e_2_933x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bdef6831240456b86ffcbc85f153560f64df91e_2_1244x998.jpeg 2x" data-dominant-color="43454C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1541 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I see more than two lines, so I am confused, because I don’t find any other views in the dicom.files</p>
<p>And also loaded every DICOM file with some Metadata in a pandas Dataframe to check if Image Orientation has multiple value. But it has only one unique value, see second image<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50bd22c0cfcddf3ced2662eeb0189c0a45c53705.png" data-download-href="/uploads/short-url/bwfpZ6kdy2DIOGqEZoDBaqYfcbz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50bd22c0cfcddf3ced2662eeb0189c0a45c53705_2_475x500.png" alt="image" data-base62-sha1="bwfpZ6kdy2DIOGqEZoDBaqYfcbz" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50bd22c0cfcddf3ced2662eeb0189c0a45c53705_2_475x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/50bd22c0cfcddf3ced2662eeb0189c0a45c53705_2_712x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50bd22c0cfcddf3ced2662eeb0189c0a45c53705.png 2x" data-dominant-color="2A2C2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">844×888 68.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @aleee97 (2025-04-22 20:12 UTC)

<p>I could solve it, I needed to stack on axis=0  all dicom files of that series. So I end up with ( 512, 704, 700) as a shape. By looping over and just select one of the axis I get the 3 different views [i, :, :] or [:, i, :] or [:, :, i] that I can visualise for the corresponding instance number</p>

---

## Post #5 by @lassoan (2025-04-26 12:59 UTC)

<p>Probably your MRI is determined to be more appropriate to be loaded as a time sequence rather than a 3D volume (have you noticed the Sequence Browser toolbar appearing at the top?). The logic to decide this was biased towards time sequences in some older Slicer versions. If you find that clinical MRI images coming directly from the scanner (not messed up by third-party anonymization) are loaded by default as time sequences in the latest Slicer Stable Release or latest Slicer Preview Release then let us know and we’ll investigate.</p>

---
