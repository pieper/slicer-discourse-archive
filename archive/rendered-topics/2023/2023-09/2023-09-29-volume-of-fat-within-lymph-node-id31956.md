---
topic_id: 31956
title: "Volume Of Fat Within Lymph Node"
date: 2023-09-29
url: https://discourse.slicer.org/t/31956
---

# Volume of fat within lymph node

**Topic ID**: 31956
**Date**: 2023-09-29
**URL**: https://discourse.slicer.org/t/volume-of-fat-within-lymph-node/31956

---

## Post #1 by @Priyanka (2023-09-29 03:29 UTC)

<p>Hello, I am new to 3D slicer and had a query. My project requires me to segment the lymph nodes and calculate the volume, which I was able to do with segment editor. Additionally, I have to calculate the volume of fat within the lymph node segmented, is that possible using 3D slicer?</p>

---

## Post #2 by @lassoan (2023-09-29 03:30 UTC)

<p>You can compute volume (and many other properties) of each segment using Segment Statistics module.</p>

---

## Post #3 by @Priyanka (2023-09-29 17:38 UTC)

<p>I need to calculate the volume of the fat within the lymph, I used thresholding to isolate the fat from the segment I extracted, but it doesnt seem to segregate the fat within the lymph node but around it.</p>

---

## Post #4 by @lassoan (2023-09-30 04:45 UTC)

<p>After you have segmented the lymph, in <code>Masking</code> section use that segment as <code>Editable area</code>. If you threshold after this then it will only affect the region within the lymps segment.</p>

---

## Post #5 by @Priyanka (2023-12-03 18:42 UTC)

<p>Hi! I tried doing this, enclosed below is the screenshot of the command I gave and the table I received I believe the fat content within the lymph node should not be zero. Could you guide me further pleas, Thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e8a714b199160c5dbe112f304f5fd964b68323f.png" data-download-href="/uploads/short-url/8VgdkkSqPf9mP3d2XBYOC1Ztj2L.png?dl=1" title="Screenshot 2023-12-03 at 1.41.11 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e8a714b199160c5dbe112f304f5fd964b68323f_2_690x103.png" alt="Screenshot 2023-12-03 at 1.41.11 PM" data-base62-sha1="8VgdkkSqPf9mP3d2XBYOC1Ztj2L" width="690" height="103" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e8a714b199160c5dbe112f304f5fd964b68323f_2_690x103.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e8a714b199160c5dbe112f304f5fd964b68323f_2_1035x154.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e8a714b199160c5dbe112f304f5fd964b68323f_2_1380x206.png 2x" data-dominant-color="EDECEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-12-03 at 1.41.11 PM</span><span class="informations">1518×228 19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3501a5099a63bc209e67d07e001078bc3bb9a70b.png" data-download-href="/uploads/short-url/7yUPr8mTFb6FkkVVsJta3RkhUq7.png?dl=1" title="Screenshot 2023-12-03 at 1.38.59 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3501a5099a63bc209e67d07e001078bc3bb9a70b_2_690x457.png" alt="Screenshot 2023-12-03 at 1.38.59 PM" data-base62-sha1="7yUPr8mTFb6FkkVVsJta3RkhUq7" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3501a5099a63bc209e67d07e001078bc3bb9a70b_2_690x457.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3501a5099a63bc209e67d07e001078bc3bb9a70b_2_1035x685.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3501a5099a63bc209e67d07e001078bc3bb9a70b.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-12-03 at 1.38.59 PM</span><span class="informations">1132×750 45.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @rbumm (2023-12-03 19:37 UTC)

<p>You can segment the lymph node in total first,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edddb728c3891449fad74c160f0b672d22b3f1fa.png" alt="image" data-base62-sha1="xWgbo6Ij3qI9FUcy6t4bj26advQ" width="220" height="321"></p>
<p>then use the fat threshold effect “in ln”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6b1122efad8bf9e6fbad98302e322f2aff2c781.jpeg" data-download-href="/uploads/short-url/wUNbQIACp3F7eJem1dQOnnxIizL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b1122efad8bf9e6fbad98302e322f2aff2c781_2_690x329.jpeg" alt="image" data-base62-sha1="wUNbQIACp3F7eJem1dQOnnxIizL" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b1122efad8bf9e6fbad98302e322f2aff2c781_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b1122efad8bf9e6fbad98302e322f2aff2c781_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6b1122efad8bf9e6fbad98302e322f2aff2c781_2_1380x658.jpeg 2x" data-dominant-color="9B9F9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1811×866 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>^</p>

---

## Post #7 by @Priyanka (2023-12-03 20:01 UTC)

<p>Hi Rudolf,</p>
<p>Thanks for getting back to me, this is exactly what I am doing, I segment the lymph node first and then threshold for fat within it but it just gives me the fat around the lymph node and not within. Just like it’s showing for you, the fat outside the lymph is recognised but not within.</p>
<p>The thresholding range i am using is -150 to -50. Let me know if I am still doing something incorrectly.</p>
<p>Thanks<br>
Priyanka</p>

---

## Post #8 by @lassoan (2023-12-03 22:17 UTC)

<p>You probably want to set <code>Modify other segments</code> to <code>Allow overlap</code>.</p>

---

## Post #9 by @Priyanka (2023-12-03 23:16 UTC)

<p>Hi Rudolf,</p>
<p>Let me know if we can do a brief zoom call or such, where I can screen share what I have done. I believe 3D slicer can help us with our project but I want to make sure, its scientifically sound.<br>
If that is not possible, let me know I can simply email my query.</p>
<p>Best,<br>
Priyanka</p>

---

## Post #10 by @rbumm (2023-12-04 13:13 UTC)

<p>If you set Masking to your “lymphnode” and Modify to “Allow overlap” then you should get your thresholded fat volume throughout the lymphnode.</p>

---
