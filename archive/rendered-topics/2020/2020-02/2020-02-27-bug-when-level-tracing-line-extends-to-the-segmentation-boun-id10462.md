---
topic_id: 10462
title: "Bug When Level Tracing Line Extends To The Segmentation Boun"
date: 2020-02-27
url: https://discourse.slicer.org/t/10462
---

# Bug when "level tracing line" extends to the segmentation boundary?

**Topic ID**: 10462
**Date**: 2020-02-27
**URL**: https://discourse.slicer.org/t/bug-when-level-tracing-line-extends-to-the-segmentation-boundary/10462

---

## Post #1 by @eyjolfur (2020-02-27 19:59 UTC)

<p>I’m segmenting a CT scan using level tracing with Slicer 4.11.0-2020-02-11.</p>
<p>When the yellow “level tracing line,” which indicates what pixels will be included once the level tracing is applied, extends to the boundary of the segmentation (which is not the boundary of the scan, due to Slicer cropping the segmentation to its minimum bounding box), something strange seems to happen.</p>
<p>In the attached screenshot, I am trying to segment the lung (or, rather, fine-tune the lung contours) using level tracing. The level tracing line has reached the segmentation boundary, and the line suddenly extends up and down along the segmentation boundary and traces the exterior of the thorax. I end up with the thorax segmented (or, as much of it that fits within the segmentation volume).</p>
<p>The desired outcome would be to have the dark area of the lung level traced, extending all the way to the segmentation boundary.</p>
<p>Anyway, in this case I can get past this relatively easily, but wanted to flag as a potential bug. I’ve included a screenshot of the application before and after applying the level tracing (my mouse pointer is not showing up on the “before” screenshot, but it’s not positioned at the boundary of the segmentation but closer to the center of the image).</p>
<p>Before applying level tracing:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45c793d7a00c8ac750a509a4470b6df608e23db1.jpeg" data-download-href="/uploads/short-url/9XixneoGMhCue6zRw6dADRDel0Z.jpeg?dl=1" title="LevelTracing-Boundary" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c793d7a00c8ac750a509a4470b6df608e23db1_2_480x500.jpeg" alt="LevelTracing-Boundary" data-base62-sha1="9XixneoGMhCue6zRw6dADRDel0Z" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c793d7a00c8ac750a509a4470b6df608e23db1_2_480x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c793d7a00c8ac750a509a4470b6df608e23db1_2_720x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/45c793d7a00c8ac750a509a4470b6df608e23db1_2_960x1000.jpeg 2x" data-dominant-color="646463"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LevelTracing-Boundary</span><span class="informations">1345×1401 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After applying level tracing:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97870dc50771102414228222999105c676cc210d.jpeg" data-download-href="/uploads/short-url/lCtrREX4Yg3xpvIULJ2FCgOel8p.jpeg?dl=1" title="LevelTracing-Boundary-After" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97870dc50771102414228222999105c676cc210d_2_485x500.jpeg" alt="LevelTracing-Boundary-After" data-base62-sha1="lCtrREX4Yg3xpvIULJ2FCgOel8p" width="485" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97870dc50771102414228222999105c676cc210d_2_485x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97870dc50771102414228222999105c676cc210d_2_727x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97870dc50771102414228222999105c676cc210d_2_970x1000.jpeg 2x" data-dominant-color="6C6C6C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LevelTracing-Boundary-After</span><span class="informations">1282×1321 290 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-02-27 20:03 UTC)

<p>Probably your segmentation extents are smaller than the currently selected master volume extents. You can adjust your segmentation by clicking the “specify geometry” button next to the master volume selector (see screenshots <a href="https://discourse.slicer.org/t/smooth-object-volume-statistics/3596">here</a>).</p>

---

## Post #3 by @eyjolfur (2020-02-28 12:51 UTC)

<p>Thanks for the reply.</p>
<p>Yes, that is indeed the case. But I was wondering, should this be the expected behavior? I would assume that the level tracing should just extend to the boundary of the segmentation, but not break down completely as happens in this example.</p>

---

## Post #4 by @lassoan (2020-02-28 15:55 UTC)

<p>For me, the previewed and the final filling looks the same. If you can reproduce a different behavior with publicly shareable data then save the scene as .mrb file, upload it somewhere and post the link here.</p>
<p>In general, I would not recommend to use slice-based segmentation tools because segmentation takes too long. What would you like to segment, on what imaging modalities, for what purpose? Have you tried using “Grow from seeds” effect?</p>

---

## Post #5 by @eyjolfur (2020-02-28 16:55 UTC)

<p>Yes, the preview and the final filling look the same, but I’m not trying to segment out the boundary of the thorax, I’m trying to segment out the lung. And that works fine when the level tracing line doesn’t extend to the boundary of the segmentation volume. However, when it extends to the boundary, the level tracing fails and produces something completely different to what I wanted.</p>
<p>To better illustrate this, we can look at the level tracing result on a superior slice, where the lung does not extend to the boundary of the segmentation volume. In this case, the yellow level tracing line only outlines the lung (in any case, the darker parts of the lung):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f564c2ac5eebef3fb24ece0691795cf35fdcad02.jpeg" data-download-href="/uploads/short-url/z0QRe7DQOyR4hnWK3b9aF1YfwgW.jpeg?dl=1" title="LevelTracing-SuperiorSlice" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f564c2ac5eebef3fb24ece0691795cf35fdcad02_2_587x500.jpeg" alt="LevelTracing-SuperiorSlice" data-base62-sha1="z0QRe7DQOyR4hnWK3b9aF1YfwgW" width="587" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f564c2ac5eebef3fb24ece0691795cf35fdcad02_2_587x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f564c2ac5eebef3fb24ece0691795cf35fdcad02_2_880x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f564c2ac5eebef3fb24ece0691795cf35fdcad02_2_1174x1000.jpeg 2x" data-dominant-color="878786"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LevelTracing-SuperiorSlice</span><span class="informations">1345×1144 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>On a more inferior slice, the lung extends to the boundary of the segmentation, and that’s where this behavior is observed, in which the level tracing breaks down and the yellow line jumps to the boundary of the segmentation volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/524a6998a29c0073f7def162c4c3e730347771d6.jpeg" data-download-href="/uploads/short-url/bJYzZN9ujMOPoTcsPsZt30thaOa.jpeg?dl=1" title="LevelTracing-ExtendingToTheBoundary" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/524a6998a29c0073f7def162c4c3e730347771d6_2_558x500.jpeg" alt="LevelTracing-ExtendingToTheBoundary" data-base62-sha1="bJYzZN9ujMOPoTcsPsZt30thaOa" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/524a6998a29c0073f7def162c4c3e730347771d6_2_558x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/524a6998a29c0073f7def162c4c3e730347771d6_2_837x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/524a6998a29c0073f7def162c4c3e730347771d6_2_1116x1000.jpeg 2x" data-dominant-color="A0A0A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LevelTracing-ExtendingToTheBoundary</span><span class="informations">1159×1037 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m just bringing this up to see if this is the expected behavior. Shouldn’t the yellow line just follow the level that one is trying to trace to the boundary of the segmentation volume? What I’m observing is that it fails completely in cases where the level tracing extends to the boundary of the segmentation volume.</p>
<p>Thanks for the suggestion, but the seed-growing will not work for these cases, as the lungs contain diffuse fibrosis. I am developing a deep learning model, and this is just the part where I am manually correcting segmentations to be used as ground-truth.</p>

---
