---
topic_id: 26563
title: "About The Curvature Of The Centerline"
date: 2022-12-02
url: https://discourse.slicer.org/t/26563
---

# About The Curvature of the Centerline

**Topic ID**: 26563
**Date**: 2022-12-02
**URL**: https://discourse.slicer.org/t/about-the-curvature-of-the-centerline/26563

---

## Post #1 by @LXT (2022-12-02 23:10 UTC)

<p>Hello, I am a beginner using the VMTK module. I would like to ask how the curvature value in the exported centerline quantitative Table is calculated. Because the average and maximum values of the same centerline obtained from the measurement module are different from this value, and the difference is very large. I should choose which curvature.<br>
Thank you for your answers.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/322f0b74ef805163aed5c6d769d0f80d96ebbc80.jpeg" data-download-href="/uploads/short-url/79WFjNy8ajNS7Zx22CbCM6hQkmI.jpeg?dl=1" title="curvature" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/322f0b74ef805163aed5c6d769d0f80d96ebbc80_2_690x397.jpeg" alt="curvature" data-base62-sha1="79WFjNy8ajNS7Zx22CbCM6hQkmI" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/322f0b74ef805163aed5c6d769d0f80d96ebbc80_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/322f0b74ef805163aed5c6d769d0f80d96ebbc80_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/322f0b74ef805163aed5c6d769d0f80d96ebbc80.jpeg 2x" data-dominant-color="555665"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">curvature</span><span class="informations">1353×779 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-12-03 05:05 UTC)

<p>The curves created by the Extract Centerline module are somewhat noisy, which may result in higher mean curvature values than in the “centerline properties” table (I think there is some centerline smoothing is applied before computing the metrics). If you resample the curve then the curve measurements then you can expect to get very similar results as in the centerline properties table.</p>
<p>For example, plot the raw results of curve measurement results, by typing this into the Python console:</p>
<pre><code>plot(arrayFromMarkupsCurveData(getNode('Centerline curve (0)'), 'Curvature', world=True))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96e56c4876a16e8b13f6890a19c70160794f3d46.png" data-download-href="/uploads/short-url/lwT9JEdb7m3k14pH0aqMppA4jjw.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96e56c4876a16e8b13f6890a19c70160794f3d46_2_690x445.png" alt="image" data-base62-sha1="lwT9JEdb7m3k14pH0aqMppA4jjw" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96e56c4876a16e8b13f6890a19c70160794f3d46_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96e56c4876a16e8b13f6890a19c70160794f3d46_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96e56c4876a16e8b13f6890a19c70160794f3d46.png 2x" data-dominant-color="F4F0E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×754 53.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After clicking “Resample curve” in Markups module’s “Resample” sections, plot again:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/aca17721b8db95b3f0896418590d68858ba456ba.png" data-download-href="/uploads/short-url/oDa3TBnK0dJbHi3L3X50OkfzKps.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/aca17721b8db95b3f0896418590d68858ba456ba_2_690x472.png" alt="image" data-base62-sha1="oDa3TBnK0dJbHi3L3X50OkfzKps" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/aca17721b8db95b3f0896418590d68858ba456ba_2_690x472.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/aca17721b8db95b3f0896418590d68858ba456ba_2_1035x708.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/aca17721b8db95b3f0896418590d68858ba456ba.png 2x" data-dominant-color="F4F7EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1097×752 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
