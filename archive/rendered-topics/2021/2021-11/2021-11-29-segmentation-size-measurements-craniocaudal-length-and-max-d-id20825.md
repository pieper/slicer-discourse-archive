---
topic_id: 20825
title: "Segmentation Size Measurements Craniocaudal Length And Max D"
date: 2021-11-29
url: https://discourse.slicer.org/t/20825
---

# Segmentation size measurements (craniocaudal length and max diameter) to table

**Topic ID**: 20825
**Date**: 2021-11-29
**URL**: https://discourse.slicer.org/t/segmentation-size-measurements-craniocaudal-length-and-max-diameter-to-table/20825

---

## Post #1 by @rrp (2021-11-29 02:52 UTC)

<p>Operating system: Windows 11 Home<br>
Slicer version: 4.11.20200930</p>
<p>Hi,<br>
It is my first time writing in this forum.<br>
I would like to measure the craniocaudal length and max diameter (in axial plane) of a segmentation. Actually, of around 180, so not having to measure these manually would be great. I have already read the Segment Statistics module documentation, but I am still not sure if some of the values it can output there are what I am looking for. As long as I can understand, the craniocaudal length could be the same as the Oriented Bounding Box Diameter (one of its values), but in an axis oriented bounding box. And about max diameter, I have read something in another post, and it was not possible to get it automatically when it was answered.</p>
<p>Is anything of what I want to do possible?</p>
<p>Thank you very much in advance.<br>
Rafael</p>

---

## Post #2 by @pieper (2021-11-29 13:31 UTC)

<p>It would probably help if you could post a screenshot or two of the data you are trying to measure.</p>

---

## Post #3 by @rrp (2021-12-07 09:09 UTC)

<p>Thank you very much for the fast answer, and sorry for taking so long to get back to you.<br>
After reading some more articles about this topic, I don’t think anymore that these are too relevant measurements.</p>
<p>Anyway here are a pair of snapshots trying to show what I was referring to (with the properties label disabled, for better visibility).<br>
The red markup represents a measurement along the supero-inferior axis, what would be the “height” of the volume. The green markup is meant to be a measurement in a plane that is perpendicular to the previous axis, and made between the two more distant opposed points of the boundary (in a line that intersects with the supero-inferior axis that goes trough the center of mass).</p>
<p>Thank you very much for your interest and time, and feel free to leave the topic as it is, as I will be sticking to more common methods for volume comparison, such as the Dice Simmilarity Coefficient or the generalized Conformity Index.</p>
<p>Regards,<br>
Rafael</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/488ed37137ca861599f71af940cc838c96a27b4d.png" data-download-href="/uploads/short-url/alSnCL8jAwjYQriog0QM1JWHTeB.png?dl=1" title="3d layout_screenshot_01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/488ed37137ca861599f71af940cc838c96a27b4d_2_565x500.png" alt="3d layout_screenshot_01" data-base62-sha1="alSnCL8jAwjYQriog0QM1JWHTeB" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/488ed37137ca861599f71af940cc838c96a27b4d_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/488ed37137ca861599f71af940cc838c96a27b4d_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/488ed37137ca861599f71af940cc838c96a27b4d.png 2x" data-dominant-color="999B9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d layout_screenshot_01</span><span class="informations">970×858 77.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/228bc2b99db947f6b0e803d7c3f2ebb95e9c4619.png" data-download-href="/uploads/short-url/4VBFwH4Bo9IvvBHxUxkCs7auEI1.png?dl=1" title="3d layout_screenshot_02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/228bc2b99db947f6b0e803d7c3f2ebb95e9c4619_2_565x500.png" alt="3d layout_screenshot_02" data-base62-sha1="4VBFwH4Bo9IvvBHxUxkCs7auEI1" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/228bc2b99db947f6b0e803d7c3f2ebb95e9c4619_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/228bc2b99db947f6b0e803d7c3f2ebb95e9c4619_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/228bc2b99db947f6b0e803d7c3f2ebb95e9c4619.png 2x" data-dominant-color="9598A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d layout_screenshot_02</span><span class="informations">970×858 48.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-12-08 13:30 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment Statistics</a> module can compute anatomically oriented bounding box (to get craniocaudal length) and segment oriented bounding box (to get maximum diameters along the main object axes) and the module can also provide various other shape statistics. You need to enable computation of these metrics, as they are disabled by default.</p>

---

## Post #5 by @Henry_Lopes (2023-09-26 22:12 UTC)

<p>How do we enable them?</p>

---

## Post #6 by @mikebind (2023-09-26 23:41 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08b0a38278391a65434190b20493909c807b189f.png" data-download-href="/uploads/short-url/1eSgwfjCd0gc0JOjl5sgI5h4MY7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08b0a38278391a65434190b20493909c807b189f_2_690x445.png" alt="image" data-base62-sha1="1eSgwfjCd0gc0JOjl5sgI5h4MY7" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08b0a38278391a65434190b20493909c807b189f_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08b0a38278391a65434190b20493909c807b189f_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08b0a38278391a65434190b20493909c807b189f.png 2x" data-dominant-color="F2F2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1166×753 94.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In the “Advanced” section, click the “Options” button for Labelmap Statistics, and then check the boxes for the desired output (OBB=“Oriented Bounding Box”)</p>

---

## Post #7 by @Florisvaldo (2023-11-26 18:33 UTC)

<p>Hello, Mike! I am from Brazil! Thank you for the tip! But I’m having a hard time, because I can’t differentiate the numbers. I click in the OBB diameter, but I don’t now which is from de axial, coronal or saginal. Can you help me? Furthermore, this module is informing the max distante in the axial, coronol and sagital of my segmentation, right?</p>

---

## Post #9 by @Florisvaldo (2023-11-26 18:56 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbece1d3d2c243675614f8b73a802bfccc0dbc1e.png" alt="image" data-base62-sha1="zWDmujc8HSJUAQbBiB4pXIHSaho" width="160" height="80"></p>

---

## Post #10 by @Florisvaldo (2023-11-26 20:03 UTC)

<p>I think that is better say the distance in latero-lateral, anterior and posterior, cranial and caudal…</p>

---

## Post #12 by @lassoan (2023-11-27 06:59 UTC)

<p>OBB means oriented bounding box, which means it is oriented to match principal axes of the segment. These directions are not related in any way to patient anatomical directions but depend only on the shape of the segment. You can get the principal axes directions from the result table and see which anatomical directions each axis is the closest to.</p>
<p>If you just need non-oriented bounding box of the segment in the world coordinate system (with axis pointing to patient RAS directions) then you can export the segments to models and call <code>GetRASBounds()</code> method of each exported model.</p>

---

## Post #13 by @Florisvaldo (2023-11-28 23:39 UTC)

<p>Your Excellency Lasso, my English is still not satisfactory, but I wanted to thank you for your answer. My intention would be to know the dimensions of my segmentation. For example, I segmented the femur. From that, I wanted to know the length, width and height of what I did. Thank you very much!</p>

---

## Post #14 by @cpinter (2023-11-29 12:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="20825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you just need non-oriented bounding box of the segment in the world coordinate system (with axis pointing to patient RAS directions) then you can export the segments to models and call <code>GetRASBounds()</code> method of each exported model.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/florisvaldo">@Florisvaldo</a> This is your answer. If you do not understand something in concrete in this, please ask about that specifically and then we may be able to help.</p>

---
