# Need help with segmentation of image stack

**Topic ID**: 16415
**Date**: 2021-03-07
**URL**: https://discourse.slicer.org/t/need-help-with-segmentation-of-image-stack/16415

---

## Post #1 by @11142 (2021-03-07 15:33 UTC)

<p>Hi, have you solved your problem now? I NEED HELP <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=9" title=":sob:" class="emoji" alt=":sob:"></p>

---

## Post #2 by @lassoan (2021-03-07 16:53 UTC)

<p>How far did you get?</p>

---

## Post #3 by @11142 (2021-03-08 01:45 UTC)

<p>I’ve read the referred segmentation guide but it seems a little bit far from my problem. My images are a series of parallel  x, y, z  cross sections, do you have any advice on building a 3D model from these slices? Or is there any code for me to probe into?</p>

---

## Post #4 by @muratmaga (2021-03-08 02:05 UTC)

<aside class="quote no-group" data-username="11142" data-post="3" data-topic="16415">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/1/e0b2c6/48.png" class="avatar"> 11142:</div>
<blockquote>
<p>do you have any advice on building a 3D model from these slices?</p>
</blockquote>
</aside>
<p>Normally the flow is to segment the region of interest either through some manual (paint/draw) or semi-automated methods (threshold, grow from seeds) with the <code>Segment Editor</code> and then use the <code>Segmentations</code> module to convert it into a 3D model.</p>
<p>If you share some screenshots of what your data looks like we can probably give more specific advise.</p>

---

## Post #5 by @11142 (2021-03-08 02:29 UTC)

<p>Here are two slices in the same direction. Outside the outline is the waves. Most of the images look similar to these two.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6866fa61ef4ea69a570b832a9287cc6c488c97ec.png" data-download-href="/uploads/short-url/eTAhKUbBzPwPBgbeeK8Pk4l71MM.png?dl=1" title="sections_z1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6866fa61ef4ea69a570b832a9287cc6c488c97ec_2_690x345.png" alt="sections_z1" data-base62-sha1="eTAhKUbBzPwPBgbeeK8Pk4l71MM" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6866fa61ef4ea69a570b832a9287cc6c488c97ec_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6866fa61ef4ea69a570b832a9287cc6c488c97ec_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6866fa61ef4ea69a570b832a9287cc6c488c97ec_2_1380x690.png 2x" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sections_z1</span><span class="informations">4000×2000 44.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8e2599ba135e7366ab27acb90881ee3d866a7d3.png" data-download-href="/uploads/short-url/o61aoNbPHlEyBmhugLn3KOiMK31.png?dl=1" title="sections_z6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8e2599ba135e7366ab27acb90881ee3d866a7d3_2_690x345.png" alt="sections_z6" data-base62-sha1="o61aoNbPHlEyBmhugLn3KOiMK31" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8e2599ba135e7366ab27acb90881ee3d866a7d3_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8e2599ba135e7366ab27acb90881ee3d866a7d3_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8e2599ba135e7366ab27acb90881ee3d866a7d3_2_1380x690.png 2x" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sections_z6</span><span class="informations">4000×2000 97.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @muratmaga (2021-03-08 04:02 UTC)

<p>And what is that you want to build 3D model out of these cross-sections, the little white bump at the bottom?</p>

---

## Post #7 by @11142 (2021-03-08 05:53 UTC)

<p>yeah, the white part</p>

---

## Post #8 by @muratmaga (2021-03-08 06:28 UTC)

<p>Because the white region is continuous with the border, I am not sure if any of the automated methods will work, but it will be real simple to do slice by slice with the draw tool and masking (set intensity range to 255-255, so it only picks up the white).</p>
<p>Alternatively, if the cross-sections always like that, perhaps you can actually segment just the solid black via simple threshold, and then use the surface cut tool to fill the indentation.</p>

---

## Post #9 by @Mehran (2021-03-08 10:33 UTC)

<p>If the image’s source are Radio Frequency, I suggest to use Hilbert(envelope) filter before segmentation. probably later a mean filter. Then it will be easier to segment the image using Slicer tools.</p>

---
