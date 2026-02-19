---
topic_id: 31989
title: "Vagina Segmentation And Reconstruction From Mri Image"
date: 2023-10-01
url: https://discourse.slicer.org/t/31989
---

# Vagina segmentation and reconstruction from MRI image

**Topic ID**: 31989
**Date**: 2023-10-01
**URL**: https://discourse.slicer.org/t/vagina-segmentation-and-reconstruction-from-mri-image/31989

---

## Post #1 by @Miri_Trope (2023-10-01 23:24 UTC)

<p>Dear community,</p>
<p>I am currently in the process of segmenting the vagina from MRI images. I came across a research paper where they used OsiriX to delineate the vaginal contour (vagina_sed_1). I’m curious if Slicer, offers similar marking tools. If so, I’m interested in learning how to aggregate all those marked regions into a surface, similar to what was achieved in the paper (vagina_sed_2). Any guidance or assistance on this would be greatly appreciated.</p>
<p>Best regards,<br>
Miri</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e4d4502c03b2d0dfa1656084a5a7e8d7e6c93a6.png" data-download-href="/uploads/short-url/baGN6pUdeMln1TumdboM6sfhKDk.png?dl=1" title="vagina_seg_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e4d4502c03b2d0dfa1656084a5a7e8d7e6c93a6_2_690x258.png" alt="vagina_seg_2" data-base62-sha1="baGN6pUdeMln1TumdboM6sfhKDk" width="690" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e4d4502c03b2d0dfa1656084a5a7e8d7e6c93a6_2_690x258.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e4d4502c03b2d0dfa1656084a5a7e8d7e6c93a6_2_1035x387.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e4d4502c03b2d0dfa1656084a5a7e8d7e6c93a6.png 2x" data-dominant-color="150A0A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vagina_seg_2</span><span class="informations">1074×402 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c82a95bb85c806e23b9ecaa20232e74c4e7a4a52.png" data-download-href="/uploads/short-url/syKJn2MfShc5pTcXx7gXQUNdITE.png?dl=1" title="vagina_seg_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c82a95bb85c806e23b9ecaa20232e74c4e7a4a52_2_690x198.png" alt="vagina_seg_1" data-base62-sha1="syKJn2MfShc5pTcXx7gXQUNdITE" width="690" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c82a95bb85c806e23b9ecaa20232e74c4e7a4a52_2_690x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c82a95bb85c806e23b9ecaa20232e74c4e7a4a52_2_1035x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c82a95bb85c806e23b9ecaa20232e74c4e7a4a52.png 2x" data-dominant-color="474040"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vagina_seg_1</span><span class="informations">1090×314 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-10-01 23:25 UTC)

<p>Slicer has much more extensive and sophisticated set of image segmentation tools compared to OsiriX. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point to learn more.</p>

---

## Post #3 by @Miri_Trope (2023-10-02 06:08 UTC)

<p>Thank you for your response. To clarify further: I’m looking for a tool that can consolidate multiple “closed-curves” (marked with the Markups tool) into a single model, similar to the image I included in my initial message. A similar question regarding regions marked manually with the paint tool. Let’s say I have multiple painted circles that collectively form a tube-like structure (with gaps between the slices). How can I combine all of these segmented circles into a single model within Slicer?</p>

---

## Post #4 by @chir.set (2023-10-02 08:04 UTC)

<aside class="quote no-group" data-username="Miri_Trope" data-post="1" data-topic="31989">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miri_trope/48/67690_2.png" class="avatar"> Miri_Trope:</div>
<blockquote>
<p>aggregate all those marked regions</p>
</blockquote>
</aside>
<p>Instead of marking as in the picture, you may use the ‘Paint’ effect in the ‘Segment editor’ in a similar way, then use ‘Fill between slices’. You should get a well constructed segment, that can be further smoothed.</p>

---

## Post #5 by @JiDafeng (2023-10-06 02:38 UTC)

<p>Could you save the lines as mesh which could be imported into 3dsMax.Then UV surface could be made according the lines.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9eba2186c5f7311ab3fee2d2c9beb975bc460b5.jpeg" data-download-href="/uploads/short-url/qwJaM6mgcnqcKo3tJjHr2PtadP7.jpeg?dl=1" title="figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9eba2186c5f7311ab3fee2d2c9beb975bc460b5_2_690x341.jpeg" alt="figure1" data-base62-sha1="qwJaM6mgcnqcKo3tJjHr2PtadP7" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9eba2186c5f7311ab3fee2d2c9beb975bc460b5_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9eba2186c5f7311ab3fee2d2c9beb975bc460b5_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9eba2186c5f7311ab3fee2d2c9beb975bc460b5_2_1380x682.jpeg 2x" data-dominant-color="383838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure1</span><span class="informations">1624×804 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87faa8fadca19f771fda864b3f2e5222fd60305d.jpeg" data-download-href="/uploads/short-url/joVuHK5D76L1XNNj4DqU8RJkRsN.jpeg?dl=1" title="figure3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87faa8fadca19f771fda864b3f2e5222fd60305d_2_690x474.jpeg" alt="figure3" data-base62-sha1="joVuHK5D76L1XNNj4DqU8RJkRsN" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87faa8fadca19f771fda864b3f2e5222fd60305d_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87faa8fadca19f771fda864b3f2e5222fd60305d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87faa8fadca19f771fda864b3f2e5222fd60305d.jpeg 2x" data-dominant-color="2D2F2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure3</span><span class="informations">946×650 99.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/282f77702597462e252911013e04dbf66f7b8e84.jpeg" data-download-href="/uploads/short-url/5JuNjGkGsNCvdSqxD5TeAMzlyHa.jpeg?dl=1" title="figure5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/282f77702597462e252911013e04dbf66f7b8e84_2_690x341.jpeg" alt="figure5" data-base62-sha1="5JuNjGkGsNCvdSqxD5TeAMzlyHa" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/282f77702597462e252911013e04dbf66f7b8e84_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/282f77702597462e252911013e04dbf66f7b8e84_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/282f77702597462e252911013e04dbf66f7b8e84_2_1380x682.jpeg 2x" data-dominant-color="403D45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure5</span><span class="informations">1624×804 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Miri_Trope (2023-10-06 14:00 UTC)

<p>Thank you for your response. Could you provide more information about how you incorporated the lines into a 3D surface? What software did you use for this task? Additionally, could you suggest any open-source software that you would recommend for performing this operation?</p>

---
