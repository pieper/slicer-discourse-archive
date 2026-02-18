# DICOM export from Slicer

**Topic ID**: 36337
**Date**: 2024-05-23
**URL**: https://discourse.slicer.org/t/dicom-export-from-slicer/36337

---

## Post #1 by @khajta (2024-05-23 03:04 UTC)

<p>Dear experts,</p>
<p>I use 3D Slicer for registering SPECT images at different time points. However, the exported DICOM files of all series show different voxel sizes between Python code (which shows the voxel size as 1.95313, 1.95313, 1) and DICOM viewer tools such as Slicer, MicroDICOM, and ImageJ (which show the voxel size as 1.95313, 1.95313, 1.95313). However, when I use this code and DICOM viewer tool with original DICOM images, they show the voxel dimensions as 1.95313, 1.95313, 1.95313."</p>
<p>My python code to extract pixel dimension is</p>
<blockquote>
<blockquote>
<p>img.SetSpacing(dicom_images.GetSpacing())<br>
print(img.GetSpacing())</p>
</blockquote>
</blockquote>
<p>Best regards,<br>
Khajonsak</p>

---

## Post #2 by @lassoan (2024-05-23 03:18 UTC)

<p>Spacing between slices is determined from “Image Position Patient” values.</p>

---

## Post #3 by @khajta (2024-05-23 03:24 UTC)

<p>Thank you for your response.</p>
<p>I want to clarify my understanding that the thickness should be get from dicom header of export file right?</p>
<p>Morover, which kind of export should be exported for SPECT, scalar volume or RT? What is the difference between both?</p>
<p>Best regard.</p>

---

## Post #4 by @lassoan (2024-05-23 03:27 UTC)

<aside class="quote no-group" data-username="khajta" data-post="3" data-topic="36337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/khajta/48/76581_2.png" class="avatar"> khajta:</div>
<blockquote>
<p>I want to clarify my understanding that the thickness should be get from dicom header of export file right?</p>
</blockquote>
</aside>
<p>Slice thickness value is irrelevant. It must not be used for determining the image geometry (origin, spacing, axis directions).</p>
<aside class="quote no-group" data-username="khajta" data-post="3" data-topic="36337">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/khajta/48/76581_2.png" class="avatar"> khajta:</div>
<blockquote>
<p>Morover, which kind of export should be exported for SPECT, scalar volume or RT?</p>
</blockquote>
</aside>
<p>I don’t know what you mean by “RT”.</p>

---

## Post #5 by @khajta (2024-05-23 03:31 UTC)

<p>RT is the second one of DICOM export option.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73c0bcc3437d56dda0a25402aa6fa03f33cc9947.png" data-download-href="/uploads/short-url/gvZQvMQWloeAlQqMuohEMckebEr.png?dl=1" title="Screenshot 2567-05-23 at 12.29.40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73c0bcc3437d56dda0a25402aa6fa03f33cc9947_2_527x500.png" alt="Screenshot 2567-05-23 at 12.29.40" data-base62-sha1="gvZQvMQWloeAlQqMuohEMckebEr" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73c0bcc3437d56dda0a25402aa6fa03f33cc9947_2_527x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73c0bcc3437d56dda0a25402aa6fa03f33cc9947_2_790x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73c0bcc3437d56dda0a25402aa6fa03f33cc9947_2_1054x1000.png 2x" data-dominant-color="EBECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2567-05-23 at 12.29.40</span><span class="informations">1312×1244 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-05-23 12:33 UTC)

<p>I see, OK. RT is for radiationntherapy export (export of segmentation as RT structure set, transform as spatial registration object, and associated images). It is not relevant for SPECT.</p>
<p>Note that the exported SPECT image may need some additional fields - check the generated files if they contain all required fields described in the DICOM standard for this information object type; or use <a href="https://www.dclunie.com/dicom3tools/dciodvfy.html">David Clunie’s DICOM verifier</a>.</p>

---

## Post #7 by @khajta (2024-05-24 04:01 UTC)

<p>Thank you for your kind suggestion.</p>
<p>I have one more error that I tried to export the SPECT as scalar volume, but it has error as attached images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c29fa5786628065b22d74dbf33e1ce29af565851.jpeg" data-download-href="/uploads/short-url/rLIFxBQoU6OGA1U1ULu5yUb0lSV.jpeg?dl=1" title="Screenshot 2567-05-24 at 12.57.54" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c29fa5786628065b22d74dbf33e1ce29af565851_2_524x500.jpeg" alt="Screenshot 2567-05-24 at 12.57.54" data-base62-sha1="rLIFxBQoU6OGA1U1ULu5yUb0lSV" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c29fa5786628065b22d74dbf33e1ce29af565851_2_524x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c29fa5786628065b22d74dbf33e1ce29af565851_2_786x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c29fa5786628065b22d74dbf33e1ce29af565851_2_1048x1000.jpeg 2x" data-dominant-color="EBEAE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2567-05-24 at 12.57.54</span><span class="informations">1544×1472 332 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e655273443639534ef786fd57796af604d76488.png" data-download-href="/uploads/short-url/4kTp9jMsznLmryOkmT7DvA5bn60.png?dl=1" title="Screenshot 2567-05-24 at 13.01.03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e655273443639534ef786fd57796af604d76488_2_690x376.png" alt="Screenshot 2567-05-24 at 13.01.03" data-base62-sha1="4kTp9jMsznLmryOkmT7DvA5bn60" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e655273443639534ef786fd57796af604d76488_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e655273443639534ef786fd57796af604d76488_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e655273443639534ef786fd57796af604d76488_2_1380x752.png 2x" data-dominant-color="E9EDF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2567-05-24 at 13.01.03</span><span class="informations">3032×1654 609 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07c97e8fc27495fbf75d32e7d4d25546257ef623.png" data-download-href="/uploads/short-url/16T2Bv23jTBJlR3MMwPDjUpwqEX.png?dl=1" title="Screenshot 2567-05-24 at 13.00.56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07c97e8fc27495fbf75d32e7d4d25546257ef623_2_690x376.png" alt="Screenshot 2567-05-24 at 13.00.56" data-base62-sha1="16T2Bv23jTBJlR3MMwPDjUpwqEX" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07c97e8fc27495fbf75d32e7d4d25546257ef623_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07c97e8fc27495fbf75d32e7d4d25546257ef623_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07c97e8fc27495fbf75d32e7d4d25546257ef623_2_1380x752.png 2x" data-dominant-color="E2E7EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2567-05-24 at 13.00.56</span><span class="informations">3032×1654 751 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2024-05-24 10:56 UTC)

<p>I don’t see any error message that tells why export failed. Could you please provide the full application log as text (menu: help / report a bug, so not delete any lines from it, but if there are any details you dont want to ahare then replace them by <code>*****</code>).</p>
<p>You could also try first with <code>Export to folder</code> option disabled.</p>

---
