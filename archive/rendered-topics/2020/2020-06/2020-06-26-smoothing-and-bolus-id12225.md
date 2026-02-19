---
topic_id: 12225
title: "Smoothing And Bolus"
date: 2020-06-26
url: https://discourse.slicer.org/t/12225
---

# Smoothing and bolus

**Topic ID**: 12225
**Date**: 2020-06-26
**URL**: https://discourse.slicer.org/t/smoothing-and-bolus/12225

---

## Post #1 by @BORIPHAT (2020-06-26 07:45 UTC)

<p>Hello,<br>
I’m a beginner for using 3D slicer. I would like to smooth the surface. I use the segment editor Median smoothing method, kernel size 10 mm but It’s still rough and what’s the module to create 3D bolus object. Could you please advise me. Thank you in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/106e31645aa272ddbb7bdd73e124fad4fdac6a70.jpeg" data-download-href="/uploads/short-url/2llJ3QsLOVybG8uEW7EY7uXGX8Q.jpeg?dl=1" title="Breast2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/106e31645aa272ddbb7bdd73e124fad4fdac6a70_2_666x500.jpeg" alt="Breast2" data-base62-sha1="2llJ3QsLOVybG8uEW7EY7uXGX8Q" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/106e31645aa272ddbb7bdd73e124fad4fdac6a70_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/106e31645aa272ddbb7bdd73e124fad4fdac6a70.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/106e31645aa272ddbb7bdd73e124fad4fdac6a70.jpeg 2x" data-dominant-color="7C8084"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Breast2</span><span class="informations">912×684 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-06-26 15:57 UTC)

<p>The surface that you show looks smooth. Can you post an image that shows the end result that you would like to have (copy-paste from somewhere else, hand-drawn sketch, or photoshopping an image would all work well)?</p>
<p>Would you like to create a segment that matches the skin surface and has a certain thickness? If yes, then segment the body surface and then use “Hollow” effect to create a shell that uses the current segment as inside surface, and finally crop it using Scissors effect.</p>

---

## Post #3 by @BORIPHAT (2020-06-27 04:22 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4fb483e8b9b5bf6655faac11be4df7847dc128.jpeg" data-download-href="/uploads/short-url/fSHLx9Gl837ZGOacLIc7WspittK.jpeg?dl=1" title="breast4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f4fb483e8b9b5bf6655faac11be4df7847dc128_2_690x342.jpeg" alt="breast4" data-base62-sha1="fSHLx9Gl837ZGOacLIc7WspittK" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f4fb483e8b9b5bf6655faac11be4df7847dc128_2_690x342.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f4fb483e8b9b5bf6655faac11be4df7847dc128_2_1035x513.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6f4fb483e8b9b5bf6655faac11be4df7847dc128_2_1380x684.jpeg 2x" data-dominant-color="717470"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">breast4</span><span class="informations">1739×863 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9edab1732f96d80bd11ad3bcd94acc18c2d35f5e.jpeg" data-download-href="/uploads/short-url/mFhZgVgnr0vvuziE0qxo3a7lRhA.jpeg?dl=1" title="breast5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9edab1732f96d80bd11ad3bcd94acc18c2d35f5e_2_690x365.jpeg" alt="breast5" data-base62-sha1="mFhZgVgnr0vvuziE0qxo3a7lRhA" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9edab1732f96d80bd11ad3bcd94acc18c2d35f5e_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9edab1732f96d80bd11ad3bcd94acc18c2d35f5e_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9edab1732f96d80bd11ad3bcd94acc18c2d35f5e.jpeg 2x" data-dominant-color="7A7D7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">breast5</span><span class="informations">1322×701 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Dear Dr. Andras Lasso</p>
<p>Hello,<br>
I would like to create many boluses by vary thicknesses of each piece. I use the hollow effect to follow your suggestion but It creates all outside and inside phantom and it is quite rough.   And how to separate the segment between phantom and bolus. Thank you very much for your kind support.</p>

---

## Post #4 by @lassoan (2020-06-27 06:17 UTC)

<aside class="quote no-group" data-username="BORIPHAT" data-post="3" data-topic="12225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> BORIPHAT:</div>
<blockquote>
<p>I use the hollow effect to follow your suggestion but It creates all outside and inside phantom</p>
</blockquote>
</aside>
<p>You can cut the grown shell using Scissors effect and then keep selected parts using Islands effect.</p>
<aside class="quote no-group" data-username="BORIPHAT" data-post="3" data-topic="12225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> BORIPHAT:</div>
<blockquote>
<p>and it is quite rough</p>
</blockquote>
</aside>
<p>It is most likely because your input volume has anisotropic resolution. You can use Crop volume module to crop the image to the region of interest and resample it to have isotropic resolution.</p>

---

## Post #5 by @BORIPHAT (2020-06-29 08:31 UTC)

<p>Dear Dr.Andras Lasso</p>
<p>Thank you very much for your suggestion but I have a problem with the next step. I would like to cut to the circle shape for every piece of bolus at the same size. I try to use scissors and overwrite all segments but it cuts only one segmentation. Could you please advise me.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3dc72111400cdf09075568801851d360086aec6.jpeg" data-download-href="/uploads/short-url/wvKGFEd4tm4RvMGcaT5a6LedOsu.jpeg?dl=1" title="B3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3dc72111400cdf09075568801851d360086aec6_2_690x361.jpeg" alt="B3" data-base62-sha1="wvKGFEd4tm4RvMGcaT5a6LedOsu" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3dc72111400cdf09075568801851d360086aec6_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e3dc72111400cdf09075568801851d360086aec6_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3dc72111400cdf09075568801851d360086aec6.jpeg 2x" data-dominant-color="A3A5A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">B3</span><span class="informations">1322×692 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2020-06-30 18:09 UTC)

<p>You can cut all segments at once using this trick: create a new segment and use Scissors effect in “Fill outside” mode.</p>
<p>Why does it work: Since outside the marked region Scissors effect fills the entire segmentation with that other segment, it means all other segments in that region are erased. You can delete the new segment after you finished with the cutting.</p>
<p>You can choose to overwrite specific segments by “Overwrite visible” masking option (and hiding segments that you don’t want to modify).</p>

---

## Post #7 by @BORIPHAT (2020-07-01 09:07 UTC)

<p>Thank you very much for your suggestion.</p>

---
