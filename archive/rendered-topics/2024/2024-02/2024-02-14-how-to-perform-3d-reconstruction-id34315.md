---
topic_id: 34315
title: "How To Perform 3D Reconstruction"
date: 2024-02-14
url: https://discourse.slicer.org/t/34315
---

# How to perform 3d reconstruction

**Topic ID**: 34315
**Date**: 2024-02-14
**URL**: https://discourse.slicer.org/t/how-to-perform-3d-reconstruction/34315

---

## Post #1 by @labixin (2024-02-14 07:49 UTC)

<p>Hello everyone,</p>
<p>As shown in figure 1, there is a breast CT with breast contour (labelled by blue outline), and high density markers (labelled by red dots). Now I want to perform 3d reconstruction.</p>
<p>Specifically:</p>
<ol>
<li>Create an ellipsoid within breast contour which has known length in three dimensions (such as 4.5×4.0×1.0).</li>
<li>Let the ellipsoid translate or rotate, and finally pass through these red dots. That is, make these red dots eventually on the inner surface of the ellipsoid.</li>
</ol>
<p>I would like to know if there is any module or extension suitable for achieving this. And if there is any suggestion on self-built algorithm.</p>
<p>Thanks a lot. Your help is highly appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87fb036269c1ce90ac415eb9b9e645c427a0dad1.jpeg" data-download-href="/uploads/short-url/joWfC87m8YlpxG6ProW9AnOBA6R.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87fb036269c1ce90ac415eb9b9e645c427a0dad1_2_437x375.jpeg" alt="Screenshot" data-base62-sha1="joWfC87m8YlpxG6ProW9AnOBA6R" width="437" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87fb036269c1ce90ac415eb9b9e645c427a0dad1_2_437x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87fb036269c1ce90ac415eb9b9e645c427a0dad1_2_655x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87fb036269c1ce90ac415eb9b9e645c427a0dad1_2_874x750.jpeg 2x" data-dominant-color="3D3E3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1170×1002 88.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Figure 1</p>
<p>Best regards,</p>
<p>Crayon</p>

---
