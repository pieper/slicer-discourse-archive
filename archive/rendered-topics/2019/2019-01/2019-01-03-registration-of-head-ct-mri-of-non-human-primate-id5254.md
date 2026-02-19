---
topic_id: 5254
title: "Registration Of Head Ct Mri Of Non Human Primate"
date: 2019-01-03
url: https://discourse.slicer.org/t/5254
---

# Registration of Head CT & MRI of Non-human Primate

**Topic ID**: 5254
**Date**: 2019-01-03
**URL**: https://discourse.slicer.org/t/registration-of-head-ct-mri-of-non-human-primate/5254

---

## Post #1 by @Bori (2019-01-03 03:37 UTC)

<p><strong>Operating system:</strong> OS X El Capitan<br>
<strong>Slicer version:</strong> 4.10.0 r27501<br>
<strong>Overall Goal:</strong> Obtaining the best possible registration of head CT and MRI from non-human primate subject to be used in image-guided surgery for electrode implantation.<br>
<strong>Problem:</strong> Registration of head CT and MRI using several modules of 3D Slicer gives suboptimal accuracy. In hope of receiving advice and help to improve the resulting registration.</p>
<p>Hi all,<br>
I am relatively new to the 3D Slicer program and currently undergoing the registration of head CT and MRI from a non-human primate subject in the lab. The resulting registration will be used in an image-guided surgery session where the landmarks (screws form implant) present on the skull and appearing on the CT will be used to co-register the scans with the subject, allowing implantation of recording electrode in the desired target area indicated in the MRI images. As a result we would like to have the highest possible registration accuracy between the CT (landmarks) and MRI (where target is indicated) as this will increase our chance of hitting the target.</p>
<p>This is a bit of an extension of this question in this thread: <a href="https://discourse.slicer.org/t/head-ct-mri-fusion-registration/1333" class="inline-onebox">Head CT MRI fusion/registration</a></p>
<p>I have currently used the following modules in 3D slicer (Important to indicate that I am only using a <strong>Rigid (6DOF) registration</strong> as I would not like to distort or change either of the images.):</p>
<ul>
<li>Expert Automated Registration</li>
<li>General Registration (BRAINS)</li>
<li>General Registration (Elastix) - I have used this on Windows platform.</li>
<li>Fiducial Registration (used alone and in conjunction with modules indicated above).</li>
</ul>
<p>So far I have:<br>
<em>Step 1</em> Fiducial registration module was used to register the two images by using markups module to indicate anatomical landmarks for registration. This did not have the desired accuracy.</p>
<p><em>Step 2</em> Used the automated registration modules above, out of which General Registration (BRAINS) gave me the highest accuracy with the initial registration using the transform from step 1 (fiducial registration module).</p>
<p>Below is a coronal cut of the registration. As it is apparent the subcortical areas do not have a good registration.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/913626edb37bf2d9e83d5bab623d0f448d9333aa.jpeg" data-download-href="/uploads/short-url/kIBfImYoqEf1kiSwAxGmYax3DhU.jpeg?dl=1" title="CT-MRI-Coregistration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/913626edb37bf2d9e83d5bab623d0f448d9333aa_2_690x489.jpeg" alt="CT-MRI-Coregistration" data-base62-sha1="kIBfImYoqEf1kiSwAxGmYax3DhU" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/913626edb37bf2d9e83d5bab623d0f448d9333aa_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/913626edb37bf2d9e83d5bab623d0f448d9333aa_2_1035x733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/913626edb37bf2d9e83d5bab623d0f448d9333aa_2_1380x978.jpeg 2x" data-dominant-color="3A3A39"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CT-MRI-Coregistration</span><span class="informations">1439×1021 334 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am including a <a href="https://drive.google.com/open?id=1scLAwhFpF46SrvLN-njC7RSNQLTZpwJ6" rel="noopener nofollow ugc">google-drive link</a> to the images used for registration:<br>
Mick_154um_20180308-cropped.nii.gz (CT in native CT space)<br>
Radiological_sub-mick_inv-2_run-01_MP2RAGE.nii.gz (MRI in native MRI space).</p>
<p>I also have tried taking out “artifacts” in the CT from the implant which might make the registration more difficult (e.g. cropping out headpost on top of the head) and have gotten the same results.</p>
<p>Any help if greatly appreciated and thank you for reading this!<br>
Bori</p>

---

## Post #2 by @lassoan (2019-01-03 05:40 UTC)

<aside class="quote no-group" data-username="Bori" data-post="1" data-topic="5254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/a88e57/48.png" class="avatar"> Bori:</div>
<blockquote>
<p>Fiducial registration module was used to register the two images by using markups module to indicate anatomical landmarks for registration. This did not have the desired accuracy.</p>
</blockquote>
</aside>
<p>Registration is as accurate as your ability to mark corresponding landmarks. Why were you not able to reach the desired accuracy? What is the desired accuracy?<br>
Try Fiducial Registration Wizard (in SlicerIGT extension) for improved user interface compared to plain Fiducial Registration module. You might also try Landmark Registration module.</p>
<p>You may also segment structures that you would like to align and use Segment Registration extension. Or export segments to models and use Model registration (in SlicerIGT extension).</p>
<p>The registered images look quite nicely aligned. Difference of bone surface position seems to be submillimeter</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97a8ce0fb5f5b34eaf30e9d48c6de881c3e7e231.jpeg" data-download-href="/uploads/short-url/lDDLb04szMifR3nuPJJXNjRg145.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97a8ce0fb5f5b34eaf30e9d48c6de881c3e7e231_2_690x464.jpeg" alt="image" data-base62-sha1="lDDLb04szMifR3nuPJJXNjRg145" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97a8ce0fb5f5b34eaf30e9d48c6de881c3e7e231_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97a8ce0fb5f5b34eaf30e9d48c6de881c3e7e231_2_1035x696.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97a8ce0fb5f5b34eaf30e9d48c6de881c3e7e231_2_1380x928.jpeg 2x" data-dominant-color="54524F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1757×1183 556 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What would be an acceptable position error? In the image there does not seem to be any obvious rigid translation or rotation error at the bone surface. Are you sure that the MRI spatial distortion is a magnitude lower than the desired position error?</p>

---
