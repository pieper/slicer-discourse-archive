---
topic_id: 31030
title: "Inconsistencies Between Ctk And 3D Slicer When Dealing With"
date: 2023-08-07
url: https://discourse.slicer.org/t/31030
---

# Inconsistencies between CTK and 3D Slicer when dealing with missing Patient information

**Topic ID**: 31030
**Date**: 2023-08-07
**URL**: https://discourse.slicer.org/t/inconsistencies-between-ctk-and-3d-slicer-when-dealing-with-missing-patient-information/31030

---

## Post #1 by @CertisPoette (2023-08-07 16:40 UTC)

<p>Dear All,</p>
<p>In our application, while working on managing missing patient information, we noticed inconsistencies between CTK and 3D Slicer default values.</p>
<p>The default value in 3D slicer will be:<br>
Patient name : “No name”<br>
Patient ID : "Patient- + study instance UID</p>
<p>Whereas for CTK :<br>
Patient name : empty<br>
Patient ID : study instance UID</p>
<p>The inconsistency is noticeable if you import in the DICOM database dicoms without a patient name and ID. Then if you load a volume, the name and ID in the subject hierachy tree are different from the DICOM database list of imported files.</p>
<p>Would it be possible to homogenize the patient information default values between CTK and 3D Slicer?</p>
<p>My opinion would be to modify the default value in CTK because the missing patient name generates a blank in the DICOM database list of imported files (not obvious for the user).</p>
<p>Best regards,</p>
<p>Christopher</p>

---

## Post #2 by @lassoan (2023-08-07 16:45 UTC)

<p>Slicer uses CTK, too. If you want your code to behave the same way as Slicer then you can have a look at Slicer’s source code and do exactly the same.</p>

---

## Post #3 by @CertisPoette (2023-08-10 14:04 UTC)

<p>Thank you for your reply!</p>
<p>In our application (Certis Solution), we use both CTK and Slicer 3D. Certis Solution already behaves like slicer for default values in case of missing information. The only difference noticeable is while importing files in the DICOM database and it is made through CTK which have different default values as Slicer or Certis Solution.</p>
<p>The difference is noticeable in Slicer and consequently in our application. For example, if you import DICOM with missing patient name/ID, the patient name line will be blank in the DICOM database (see screen shots taken from Slicer-5.2.2). This blank line gives the feeling that the import failed if the user does not pay attention…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33113c7ae7f5e7cda116c4f0574b985af057a6cf.png" data-download-href="/uploads/short-url/7hLhkm4mR2rTWhwb0NmGWZXqKCz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33113c7ae7f5e7cda116c4f0574b985af057a6cf_2_690x72.png" alt="image" data-base62-sha1="7hLhkm4mR2rTWhwb0NmGWZXqKCz" width="690" height="72" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33113c7ae7f5e7cda116c4f0574b985af057a6cf_2_690x72.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33113c7ae7f5e7cda116c4f0574b985af057a6cf_2_1035x108.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33113c7ae7f5e7cda116c4f0574b985af057a6cf.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1339×140 14.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a567bb44b4386a203f4fc04f7a36928b0bf922b.png" data-download-href="/uploads/short-url/aBCCzXiDYAskinzf2XTh4RGCyCv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a567bb44b4386a203f4fc04f7a36928b0bf922b_2_690x73.png" alt="image" data-base62-sha1="aBCCzXiDYAskinzf2XTh4RGCyCv" width="690" height="73" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a567bb44b4386a203f4fc04f7a36928b0bf922b_2_690x73.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a567bb44b4386a203f4fc04f7a36928b0bf922b_2_1035x109.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a567bb44b4386a203f4fc04f7a36928b0bf922b.png 2x" data-dominant-color="C4D9E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×142 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2023-08-12 16:57 UTC)

<p>The other application that uses CTK can be updated to not just use the default behavior but use the CTK DICOM classes the same way as Slicer does.</p>

---
