---
topic_id: 28437
title: "Encoding Error For Dicom File From Chison"
date: 2023-03-18
url: https://discourse.slicer.org/t/28437
---

# Encoding Error for DICOM File from Chison

**Topic ID**: 28437
**Date**: 2023-03-18
**URL**: https://discourse.slicer.org/t/encoding-error-for-dicom-file-from-chison/28437

---

## Post #1 by @HMAH (2023-03-18 00:31 UTC)

<p>Hi everyone,</p>
<p>It’s my first time using 3D Slicer and I hit a big road block at my very first step which is importing the DICOM file to the software.  The software show me a number of faults which are:</p>
<ul>
<li>
<p>DICOM dataset contains some encoding that we never thought we would see (ISO 2022 IR 6). Using ASCII encoding.</p>
</li>
<li>
<p>Image spacing may need to be calibrated for accurate size measurements.</p>
</li>
</ul>
<p>The file is from a Chison Sonobook 9 machine.</p>
<p>I’m unable to proceed any further.  Any help is much appreciated.</p>
<p>Regards,</p>

---

## Post #2 by @pieper (2023-03-18 15:19 UTC)

<p>It could help if you paste the exact messages you get in the Slicer console.</p>
<p>Also if you post some sample data of a phantom or something (not patient identifiable data) to replicate the issue then maybe someone can check on their system.</p>

---

## Post #3 by @HMAH (2023-03-18 22:50 UTC)

<p>Hi Steve,</p>
<p>Thank you for responding.</p>
<p>I’ve taken the following screenshots as requested.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90a27a323ad480742ae265bf3b749e58ad82e3b0.png" alt="Screenshot 2023-03-19 at 9.07.43 am" data-base62-sha1="kDuRqOZUIRDBwzHgJIuqokunxTO" width="421" height="336"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448fffb996761c950cbc80c3c85587945759d423.png" data-download-href="/uploads/short-url/9MwZ1w5zwB6WAGWkYifBgxf31sv.png?dl=1" title="Screenshot 2023-03-19 at 9.11.14 am" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/448fffb996761c950cbc80c3c85587945759d423_2_690x416.png" alt="Screenshot 2023-03-19 at 9.11.14 am" data-base62-sha1="9MwZ1w5zwB6WAGWkYifBgxf31sv" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/448fffb996761c950cbc80c3c85587945759d423_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448fffb996761c950cbc80c3c85587945759d423.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448fffb996761c950cbc80c3c85587945759d423.png 2x" data-dominant-color="E0E6EE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-19 at 9.11.14 am</span><span class="informations">748×451 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e43079da2ffb85f0c9d0eac3b0cd0f38ff963ff.png" data-download-href="/uploads/short-url/mA339Gl52SdHolqoICIH2lfM00L.png?dl=1" title="Screenshot 2023-03-19 at 9.11.06 am" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e43079da2ffb85f0c9d0eac3b0cd0f38ff963ff_2_690x417.png" alt="Screenshot 2023-03-19 at 9.11.06 am" data-base62-sha1="mA339Gl52SdHolqoICIH2lfM00L" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e43079da2ffb85f0c9d0eac3b0cd0f38ff963ff_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e43079da2ffb85f0c9d0eac3b0cd0f38ff963ff.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e43079da2ffb85f0c9d0eac3b0cd0f38ff963ff.png 2x" data-dominant-color="E0E6ED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-19 at 9.11.06 am</span><span class="informations">752×455 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’d like to submit the DICOM file I’m working on to this post but because I’m unable to open it with 3DSlicer, I can’t remove the patient’s data.  Is there another software I can use to do this?</p>
<p>Thanks kindly,</p>

---

## Post #4 by @HMAH (2023-03-18 22:57 UTC)

<p>Hi Steve,</p>
<p>I have been able to delete the patient’s information from the DICOM file using Osirix.  The DICOM file is attached.</p>
<p><a href="https://www.dropbox.com/s/hrrxodm5gqzi6w4/IM-0001-0032-0001.dcm?dl=0" rel="noopener nofollow ugc">DICOM File</a></p>

---

## Post #5 by @pieper (2023-03-19 18:49 UTC)

<p>Hmm, it seems to work fine for me.  This is a rendered screen capture though (the scale on the right is burned into the image and it’s only one frame) so probably nothing meaningful to do with it in slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8a9eb0064457af44c5e20a2ca445e3d6a28016c.jpeg" data-download-href="/uploads/short-url/qlBTVQin6oXYLxfrpQUT4geTQ3W.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a9eb0064457af44c5e20a2ca445e3d6a28016c_2_690x359.jpeg" alt="image" data-base62-sha1="qlBTVQin6oXYLxfrpQUT4geTQ3W" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a9eb0064457af44c5e20a2ca445e3d6a28016c_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a9eb0064457af44c5e20a2ca445e3d6a28016c_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8a9eb0064457af44c5e20a2ca445e3d6a28016c_2_1380x718.jpeg 2x" data-dominant-color="241B17"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×999 51.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Maybe Osirix fixed the format compared to the original?</p>

---

## Post #6 by @HMAH (2023-03-20 00:32 UTC)

<p>Hi Steve,</p>
<p>Yes, it seems Osirix had fixed the format.  I can open the new file but not the original.</p>
<p>Now i’m facing with a new problem.  I thought I’ve exported a 3D Dicom file but it is in fact only an image.  I need to find a way to export the 3D file from a Chison Sonobook 9 and their manual is next to useless.</p>
<p>Your help is much appreciated.</p>

---

## Post #7 by @lassoan (2023-03-20 04:53 UTC)

<p>Most 3D ultrasound systems do not allow saving of the 3D data in standard file fornat. You can contact sales representatives or technical support people and ask for a 3D data export.</p>
<p>Alternatively, you can try to reverse engineer their proprietary file format. It should be doable if they don’t use compression.</p>

---
