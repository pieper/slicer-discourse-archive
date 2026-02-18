# How to fill inside the holes

**Topic ID**: 3169
**Date**: 2018-06-13
**URL**: https://discourse.slicer.org/t/how-to-fill-inside-the-holes/3169

---

## Post #1 by @Fang (2018-06-13 15:00 UTC)

<p>Hi,</p>
<p>I would like to ask how to fill inside the holes<br>
I have tried on ’ Smoothing ’ &gt; ’ Closing ’ but it just fills in the small holes and if I using a larger number of a kernel, it does not fill in the area that I desired.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24557197c5483ece46151c11b1fbd3ac2b1989a6.jpeg" data-download-href="/uploads/short-url/5bqfzRPErikrlGUdtMPfUTkGSpM.JPG?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24557197c5483ece46151c11b1fbd3ac2b1989a6_2_443x500.JPG" alt="Capture" data-base62-sha1="5bqfzRPErikrlGUdtMPfUTkGSpM" width="443" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24557197c5483ece46151c11b1fbd3ac2b1989a6_2_443x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24557197c5483ece46151c11b1fbd3ac2b1989a6_2_664x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24557197c5483ece46151c11b1fbd3ac2b1989a6_2_886x1000.JPG 2x" data-dominant-color="B1B0C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">918×1034 54.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As the figure above, I desire to fill inside in the middle area.</p>
<p>Thank you for your helping,<br>
Best regards.</p>

---

## Post #2 by @lassoan (2018-06-13 18:01 UTC)

<p>It seems that the resolution of the segmentation is too low (voxel spacing is too high), relative to thickness of the structure that you would like to segment.</p>
<p>One solution is to supersample the input volume before starting segmentation, using Crop volume module (enable isotropic spacing; and set spacing scale to 0.5 or maybe 0.3).</p>

---

## Post #3 by @Fang (2018-06-24 15:01 UTC)

<p>I already follow your suggestion but it does not change anything.</p>

---

## Post #4 by @lassoan (2018-06-24 15:37 UTC)

<p>You need to supersample the input volume <strong>before</strong> starting segmentation. If you have already started segmentation and have some segments, this will have no effect. We’ll add a new feature in 1-2 weeks that will allow you to easily resample an existing segmentation.</p>

---

## Post #5 by @Fang (2018-06-24 16:23 UTC)

<p>I already enable isotropic spacing and set spacing scale to 0.5 and 0.3 from Crop volume module before I do any segmentation but it does not effect. I will waiting for the new feature in order to work on this.</p>

---

## Post #6 by @cpinter (2018-06-24 18:12 UTC)

<aside class="quote no-group" data-username="Fang" data-post="5" data-topic="3169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/96bed5/48.png" class="avatar"> Fang:</div>
<blockquote>
<p>but it does not effect</p>
</blockquote>
</aside>
<p>What do you mean? Please describe otherwise we cannot help. What <a class="mention" href="/u/lassoan">@lassoan</a> is suggesting works. Make sure you select the resampled image for the new segmentation before you add any segments.</p>

---

## Post #7 by @Fang (2018-06-24 18:22 UTC)

<p>I not sure that I misunderstood in some step or not.<br>
So, the steps that I do are performed as a figure below this in sequence.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a76bc8f1b74a89654efb0aeb284cc6d3738d2688.jpeg" data-download-href="/uploads/short-url/nT4Fh49WtB6gjQb24LssQ4U2EwU.JPG?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a76bc8f1b74a89654efb0aeb284cc6d3738d2688_2_690x163.JPG" alt="1" data-base62-sha1="nT4Fh49WtB6gjQb24LssQ4U2EwU" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a76bc8f1b74a89654efb0aeb284cc6d3738d2688_2_690x163.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a76bc8f1b74a89654efb0aeb284cc6d3738d2688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a76bc8f1b74a89654efb0aeb284cc6d3738d2688.jpeg 2x" data-dominant-color="FAFAFA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1011×239 12.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae5fb6855c34f5fac98063edc77dd08c0ac7d9dd.jpeg" data-download-href="/uploads/short-url/oSA8VmH6lxZ9Kt744aa6IjK3lJX.JPG?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae5fb6855c34f5fac98063edc77dd08c0ac7d9dd_2_690x240.JPG" alt="2" data-base62-sha1="oSA8VmH6lxZ9Kt744aa6IjK3lJX" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae5fb6855c34f5fac98063edc77dd08c0ac7d9dd_2_690x240.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae5fb6855c34f5fac98063edc77dd08c0ac7d9dd_2_1035x360.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae5fb6855c34f5fac98063edc77dd08c0ac7d9dd.jpeg 2x" data-dominant-color="F8F8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1313×458 42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c28c58b73e89b391ba4e8c4f92eff847c6bc451d.jpeg" data-download-href="/uploads/short-url/rL3jRrE2rUTJZxUBEdlhHzDQxg9.JPG?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c28c58b73e89b391ba4e8c4f92eff847c6bc451d_2_492x500.JPG" alt="3" data-base62-sha1="rL3jRrE2rUTJZxUBEdlhHzDQxg9" width="492" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c28c58b73e89b391ba4e8c4f92eff847c6bc451d_2_492x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c28c58b73e89b391ba4e8c4f92eff847c6bc451d_2_738x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c28c58b73e89b391ba4e8c4f92eff847c6bc451d_2_984x1000.JPG 2x" data-dominant-color="F6F6F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1337×1356 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea0e4035fae387375f23bcc476c8ad46732d5de.jpeg" data-download-href="/uploads/short-url/klKvsMGpu3OIosCR0Tt1v4xeMfs.JPG?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ea0e4035fae387375f23bcc476c8ad46732d5de_2_690x417.JPG" alt="4" data-base62-sha1="klKvsMGpu3OIosCR0Tt1v4xeMfs" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ea0e4035fae387375f23bcc476c8ad46732d5de_2_690x417.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ea0e4035fae387375f23bcc476c8ad46732d5de_2_1035x625.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea0e4035fae387375f23bcc476c8ad46732d5de.jpeg 2x" data-dominant-color="EDF2F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1339×811 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f8f84c71ffc6a656d92b9250380a6c55362c51.jpeg" data-download-href="/uploads/short-url/5yLyGzHg12DsgwCNmIoIcspH0DD.JPG?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26f8f84c71ffc6a656d92b9250380a6c55362c51_2_344x500.JPG" alt="5" data-base62-sha1="5yLyGzHg12DsgwCNmIoIcspH0DD" width="344" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26f8f84c71ffc6a656d92b9250380a6c55362c51_2_344x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26f8f84c71ffc6a656d92b9250380a6c55362c51_2_516x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f8f84c71ffc6a656d92b9250380a6c55362c51.jpeg 2x" data-dominant-color="B6ABA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">605×877 37.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @cpinter (2018-06-24 19:05 UTC)

<p>If you resample an existing segmentation, it won’t contain a finer resolution segmentation afterwards, just a different sampling of the same segmentation. You need to segment the anatomical image that you use for segmenting the tooth. That’s what you need to supersample if you want to achieve higher accuracy segmentation.</p>

---
