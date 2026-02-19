---
topic_id: 17982
title: "Difficulty With Finding Cross Sectional Area Of Skeletal Mus"
date: 2021-06-07
url: https://discourse.slicer.org/t/17982
---

# difficulty with finding cross sectional area of skeletal muscle at l3 for assessing sarcopenia

**Topic ID**: 17982
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/difficulty-with-finding-cross-sectional-area-of-skeletal-muscle-at-l3-for-assessing-sarcopenia/17982

---

## Post #1 by @aman (2021-06-07 00:07 UTC)

<p>Operating system: win 64<br>
Slicer version: 4.13.0<br>
Expected behavior:<br>
Actual behavior:<br>
sir i am unable to take out the cross sectional area of dicom images i have taken<br>
the cross sectional area and volume come out to be the same after seeing in sandbox derived cross sectional area</p>
<p>i add segment , put threshold bw = -29 to 150<br>
use for masking<br>
shade out the muscle area<br>
go to quantification apply , i get the volume<br>
now with csa in quantification the are i get is same as the volume which is way outlying from the normal range of skeletal muscle cross sectional area</p>

---

## Post #2 by @lassoan (2021-06-07 00:12 UTC)

<aside class="quote no-group" data-username="aman" data-post="1" data-topic="17982">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aman/48/11164_2.png" class="avatar"> aman:</div>
<blockquote>
<p>now with csa in quantification the are i get is same as the volume which is way outlying from the normal range of skeletal muscle cross sectional area</p>
</blockquote>
</aside>
<p>If slice spacing is 1mm then cross-section surface area in mm2 will be the same as volume of a single-slice segment in mm3, so the equal volume and surface value does not indicate an error.</p>
<p>Can you attach a screenshot?</p>
<p>Do you get the same value if you draw a closed curve and enable “area” measurement? (using Markups module; using latest Slicer Preview Release)</p>

---

## Post #3 by @aman (2021-06-07 10:40 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0091d7c3b76d8a0974fc49773bfe915dbd08d9db.jpeg" data-download-href="/uploads/short-url/52sWsSeJbdYAIfhWFt26cj4vCr.jpeg?dl=1" title="slicer error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0091d7c3b76d8a0974fc49773bfe915dbd08d9db_2_690x387.jpeg" alt="slicer error" data-base62-sha1="52sWsSeJbdYAIfhWFt26cj4vCr" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0091d7c3b76d8a0974fc49773bfe915dbd08d9db_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0091d7c3b76d8a0974fc49773bfe915dbd08d9db_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0091d7c3b76d8a0974fc49773bfe915dbd08d9db.jpeg 2x" data-dominant-color="B1B1B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer error</span><span class="informations">1366×768 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4c0915af8436f6c4308c2796b75182497a355b.png" data-download-href="/uploads/short-url/fSzU4TC8pXEXa1qsmpmPfNBsbYn.png?dl=1" title="slice rerro 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4c0915af8436f6c4308c2796b75182497a355b_2_690x387.png" alt="slice rerro 2" data-base62-sha1="fSzU4TC8pXEXa1qsmpmPfNBsbYn" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4c0915af8436f6c4308c2796b75182497a355b_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4c0915af8436f6c4308c2796b75182497a355b_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4c0915af8436f6c4308c2796b75182497a355b.png 2x" data-dominant-color="B5B6B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slice rerro 2</span><span class="informations">1366×768 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-06-07 12:15 UTC)

<p>Where this image is from? Have you loaded this image directly from DICOM or u loaded it into some software and exported as jpg/png/tiff? To see if the image metadata is correct, could you take a screenshot of Volumes module (selecting this image and showing the content of Volume information section)?</p>

---

## Post #5 by @aman (2021-06-07 12:55 UTC)

<p>THIS IS DICOM IMAGE.<br>
WHERE DO I GET THE VOLUME INFORMATION SECTION?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f04364c38bfa27059c8fe47e031174072704cd01.png" data-download-href="/uploads/short-url/yhsYWQ2dwKwXyM0Kc8HVysbrg1H.png?dl=1" title="ERROR 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f04364c38bfa27059c8fe47e031174072704cd01_2_690x387.png" alt="ERROR 3" data-base62-sha1="yhsYWQ2dwKwXyM0Kc8HVysbrg1H" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f04364c38bfa27059c8fe47e031174072704cd01_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f04364c38bfa27059c8fe47e031174072704cd01_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f04364c38bfa27059c8fe47e031174072704cd01.png 2x" data-dominant-color="777676"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ERROR 3</span><span class="informations">1366×768 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-06-07 18:25 UTC)

<p>The “Volume information” section is shown in your screenshot and the values all look reasonable. Slice spacing is indeed 1mm, which means that volume and surface area in mm2 will be the same as volume in mm3.</p>
<p>The surface area on your screenshot shows 13659.8mm2 that is 136.598cm2, which looks about right. What surface area did you expect?</p>

---

## Post #7 by @aman (2021-06-08 01:00 UTC)

<p>Sir the muscle cross sectional surface area is wrong as the patient is sarcopenic by other methods but by this it is coming much  more than the normal range …</p>

---

## Post #8 by @aman (2021-06-08 11:11 UTC)

<p>also the are on radiant is almost half which is correlating with clinical data. my seniors have used this software and i too have committed for it in my research methodology so looking for urgent solution for the same…</p>

---

## Post #9 by @muratmaga (2021-06-08 11:23 UTC)

<p>In segment Cross section area there are three options (row, column, and slice). Since we always work with 3D data in Slicer, all of them will generate a result, even in a single slice. Perhaps you are not choosing the right axis.</p>
<p>If you are unsure which axis to choose, create a single circular segment with the diameter of 40mm (paint segment tool). The cross-sectional area reported for that should be about 1,256mm2.  Go through all three of them and see in which one you see the correct cross-sectional value, then repeat the same with your data.</p>

---

## Post #10 by @aman (2021-06-08 14:26 UTC)

<p>Does the software double the surface area.<br>
I mean do I need to divide it by 2 if it considers cross sectional area of both superior and inferior surface</p>

---

## Post #11 by @lassoan (2021-06-08 14:55 UTC)

<p>Surface area of the segment includes the entire surface area of the 3D object (if the object has a disk shape then it will include area of top, bottom, and side surfaces).</p>
<p>If you need the cross-section area then you can compute that using “Segment Cross-section area” module.</p>

---
