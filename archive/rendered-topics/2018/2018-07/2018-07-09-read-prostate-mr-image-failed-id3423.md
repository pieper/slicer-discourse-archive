---
topic_id: 3423
title: "Read Prostate Mr Image Failed"
date: 2018-07-09
url: https://discourse.slicer.org/t/3423
---

# Read Prostate MR image failed

**Topic ID**: 3423
**Date**: 2018-07-09
**URL**: https://discourse.slicer.org/t/read-prostate-mr-image-failed/3423

---

## Post #1 by @zgk110 (2018-07-09 12:30 UTC)

<p>Operating system:Windows 64 bit<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4edd81d321755af049fe9246d5ddc5662af55aa0.jpeg" data-download-href="/uploads/short-url/bfFOOgoUviJX6Z8dvQgqh8mY7MA.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4edd81d321755af049fe9246d5ddc5662af55aa0_2_690x364.jpg" alt="image" data-base62-sha1="bfFOOgoUviJX6Z8dvQgqh8mY7MA" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4edd81d321755af049fe9246d5ddc5662af55aa0_2_690x364.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4edd81d321755af049fe9246d5ddc5662af55aa0_2_1035x546.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4edd81d321755af049fe9246d5ddc5662af55aa0_2_1380x728.jpg 2x" data-dominant-color="393939"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1762×930 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b34d205c06fa2878d4e8b9d14512afec51608a56.jpeg" data-download-href="/uploads/short-url/pAaI0lUgk7NaiSFZSukEKXjUOx0.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34d205c06fa2878d4e8b9d14512afec51608a56_2_690x444.jpg" alt="image" data-base62-sha1="pAaI0lUgk7NaiSFZSukEKXjUOx0" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34d205c06fa2878d4e8b9d14512afec51608a56_2_690x444.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34d205c06fa2878d4e8b9d14512afec51608a56_2_1035x666.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b34d205c06fa2878d4e8b9d14512afec51608a56_2_1380x888.jpg 2x" data-dominant-color="1C1C1B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1389×894 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hello,  i am trying to read a prostate image by 3D slicer, however, when i open it, it seems some of the images is not complete and the rotation looks like being mistake, so i wonder if there are some solutions for that.<br>
Thanks a lot.</p>

---

## Post #2 by @lassoan (2018-07-10 02:53 UTC)

<p>This looks perfect. MRI images are often acquired with orientation that is not aligned with anatomical axes.</p>
<p>If you prefer, you can adjust slice views from the default (anatomical) orientation to image acquisition axes orientation: open slice view controller, click double-arrow to show more options, click views link, and click <em>Rotate to volume</em> button.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b6815359e7127db64baa7f52eb47e2b95e434bb.png" data-download-href="/uploads/short-url/d2CrFwKJtMBbTlDgwC3LJR9paf9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b6815359e7127db64baa7f52eb47e2b95e434bb_2_690x413.png" alt="image" data-base62-sha1="d2CrFwKJtMBbTlDgwC3LJR9paf9" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b6815359e7127db64baa7f52eb47e2b95e434bb_2_690x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b6815359e7127db64baa7f52eb47e2b95e434bb_2_1035x619.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b6815359e7127db64baa7f52eb47e2b95e434bb.png 2x" data-dominant-color="DBD6D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1222×732 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @zgk110 (2018-07-10 05:58 UTC)

<p>Really appreciate for your help.<br>
Well, the MR image display seems work well, however, I also want to annotate the ROI region and get the center coordinates of the region and export them for future research (deep learning analysis et.). I have tried this module, and the exported coordinates(red rectangle, voxel coordinate) is just as below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38e9c7e8748a9031a4bbe811984e321eddcf0090.png" data-download-href="/uploads/short-url/87tBUXRIsYTveHtGah2gpa8XByo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38e9c7e8748a9031a4bbe811984e321eddcf0090.png" alt="image" data-base62-sha1="87tBUXRIsYTveHtGah2gpa8XByo" width="606" height="500" data-dominant-color="F6F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">736×607 15.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I use the SimpleItk (python)  to convert the voxel coordinate to world coordinate, the code is just as :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/962e44c3bc7f77b4df020139a2a71376ef44f547.png" alt="image" data-base62-sha1="lqyKxlyvyT1iyKCVUAgJB0Zn0a3" width="590" height="150"><br>
The world coordinate by using SimpleItk is (88,-35,31), but in fact the true world coordinate is :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84134f9ea69f3ebe9dc25a191948ac8ad39c522f.png" alt="image" data-base62-sha1="iQooMFknLZU92OZEgspXui7BYpF" width="226" height="34"></p>
<p>So i am confused where i am wrong, or some other ways to directly export the right world coordinates ?<br>
Thanks a lot.</p>

---

## Post #4 by @lassoan (2018-07-10 06:24 UTC)

<p>The code snippet above ignores image orientation and therefore the computed physical coordinates are incorrect. The world_xyz computation formula looks suspicious, too (you cannot subtract physical coordinates origin_xyz from voxel coordinates center_xyz). You either need to fix the formula (it would be something like origin_xyz + voxel_ijk * spacing * direction) or use <code>TransformIndexToPhysicalPoint</code> method (or one of its variants).</p>
<p>Also note that Slicer uses RAS as world coordinates, while ITK uses LPS (so you may need to multiply physical coordinates by diag(-1, -1, 1, 1) matrix), and if you access arrays in numpy then you may also need to deal with Fortran/C index order.</p>

---

## Post #5 by @zgk110 (2018-07-10 09:03 UTC)

<p>Thanks a lot for your help.</p>
<p>Anyway, what is the meaning of the operation ’ rotate to volume plane’, I have many other MR images to handle, and I want to process these image previously by a script.<br>
I wonder if there are some script function in SimpleITK to do this operation in bulk.</p>

---

## Post #6 by @lassoan (2018-07-10 14:38 UTC)

<aside class="quote no-group" data-username="zgk110" data-post="5" data-topic="3423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ed8c4c/48.png" class="avatar"> zgk110:</div>
<blockquote>
<p>what is the meaning of the operation ’ rotate to volume plane</p>
</blockquote>
</aside>
<p>Reorient slice views to match direction of image axes.</p>
<aside class="quote no-group" data-username="zgk110" data-post="5" data-topic="3423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ed8c4c/48.png" class="avatar"> zgk110:</div>
<blockquote>
<p>I wonder if there are some script function in SimpleITK to do this operation in bulk.</p>
</blockquote>
</aside>
<p>All operations that you can do on the GUI are available from Python - some of them use MRML library, some use module logic, and some may be accessible using SimpleITK. We can give more specific advice if you tell what operations you plan to do.</p>

---

## Post #7 by @zgk110 (2018-09-15 11:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="3423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We can give more specific advice if you tell what operations you plan to do.</p>
</blockquote>
</aside>
<p>Hello, is there any example codes of ‘rotate MRI images to volume plane’ operation by python, can you show me some examples, thank you.</p>

---

## Post #8 by @lassoan (2018-09-15 23:00 UTC)

<aside class="quote no-group" data-username="zgk110" data-post="7" data-topic="3423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/ed8c4c/48.png" class="avatar"> zgk110:</div>
<blockquote>
<p>is there any example codes of ‘rotate MRI images to volume plane’ operation by python</p>
</blockquote>
</aside>
<p>See this code snippet in the script repository:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_slice_views_to_volume_plane" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_slice_views_to_volume_plane</a></p>

---

## Post #9 by @zgk110 (2018-09-22 16:55 UTC)

<p>Hi , How to save the transformed  (‘rotate to volume plane’ )  volume in GUI?<br>
I have tried the "rename the current volume’’ and then save it, however when i open it again it seems that the transformed volume not changed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a3ab9aa80ddf0c22a0af22ba398d7abdf04d791.png" data-download-href="/uploads/short-url/1suALrXy1NoFGUlJTC62cvO6HjX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a3ab9aa80ddf0c22a0af22ba398d7abdf04d791_2_690x207.png" alt="image" data-base62-sha1="1suALrXy1NoFGUlJTC62cvO6HjX" width="690" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a3ab9aa80ddf0c22a0af22ba398d7abdf04d791_2_690x207.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a3ab9aa80ddf0c22a0af22ba398d7abdf04d791_2_1035x310.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a3ab9aa80ddf0c22a0af22ba398d7abdf04d791_2_1380x414.png 2x" data-dominant-color="373534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1434×431 53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Meanwhile, i also want to save the plane by python, the code is as below in .slicerrc.py , and i want to know how can i get the transformed volume and save it through python.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c48d774bfd4f765c505f26093912b2c90a67259a.png" data-download-href="/uploads/short-url/s2MFLMR0t2FpRCvJZDSb7bWiycW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c48d774bfd4f765c505f26093912b2c90a67259a_2_690x145.png" alt="image" data-base62-sha1="s2MFLMR0t2FpRCvJZDSb7bWiycW" width="690" height="145" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c48d774bfd4f765c505f26093912b2c90a67259a_2_690x145.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c48d774bfd4f765c505f26093912b2c90a67259a_2_1035x217.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c48d774bfd4f765c505f26093912b2c90a67259a_2_1380x290.png 2x" data-dominant-color="34302A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1601×338 29.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2018-09-23 12:54 UTC)

<p>“Rotate to volume plane” rotates slice view plane to match orientation of volume axes. The volume is not transformed. Why would you like to rotate the volume?</p>

---
