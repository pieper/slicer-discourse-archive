# Using 3D Slicer for Soil Scans Containing Insects

**Topic ID**: 22944
**Date**: 2022-04-13
**URL**: https://discourse.slicer.org/t/using-3d-slicer-for-soil-scans-containing-insects/22944

---

## Post #1 by @Laricobius (2022-04-13 17:55 UTC)

<p>Operating system: iMac, Monterey 12.0.1<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: Viewing insects in scanned soil tubes<br>
Actual behavior: I am unable to use the ROI preset features to identify my insect in the scan. I have watched tutorials of people doing exactly what I want to do with identifying lung masses etc., however I cannot seem to figure out how to do it with insects in soil.</p>
<p>Any suggestions?</p>

---

## Post #2 by @lassoan (2022-04-13 18:37 UTC)

<p>Can you attach a few screenshots that shows how the insect looks in slice views?</p>
<p>Due to density of soil, it may be hard to visualize the smaller, less dense insects inside. A solution can be to blank out the soil regions in the scan (you can do it using <code>Mask volume</code> effect in <code>Segment Editor</code> module).</p>

---

## Post #3 by @hherhold (2022-04-13 19:03 UTC)

<p>If the samples were scanned on a micro-CT scanner (not a medical scanner), the presets for visualizing bone, liver, etc will be useless as they are calibrated for specific dosages and tissues. Most zoological scans are not so standardized, and require determining proper transfer curves, thresholds, and so on manually.</p>

---

## Post #4 by @Laricobius (2022-04-14 15:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c46239b7fe91c8db637c379b4e6543ba757a6465.jpeg" data-download-href="/uploads/short-url/s1i1Wi8GlsnjwFpB2aOSivqkX7D.jpeg?dl=1" title="Screen Shot 2022-04-14 at 10.53.16 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c46239b7fe91c8db637c379b4e6543ba757a6465_2_550x500.jpeg" alt="Screen Shot 2022-04-14 at 10.53.16 AM" data-base62-sha1="s1i1Wi8GlsnjwFpB2aOSivqkX7D" width="550" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c46239b7fe91c8db637c379b4e6543ba757a6465_2_550x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c46239b7fe91c8db637c379b4e6543ba757a6465_2_825x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c46239b7fe91c8db637c379b4e6543ba757a6465_2_1100x1000.jpeg 2x" data-dominant-color="434343"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-04-14 at 10.53.16 AM</span><span class="informations">1460×1326 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb5d2d1251b016177ce0db21cc9342b6a7f8706b.jpeg" data-download-href="/uploads/short-url/zRFtnz1zJupZFxOziLCueCzuhWr.jpeg?dl=1" title="Screen Shot 2022-04-14 at 10.54.42 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb5d2d1251b016177ce0db21cc9342b6a7f8706b_2_690x421.jpeg" alt="Screen Shot 2022-04-14 at 10.54.42 AM" data-base62-sha1="zRFtnz1zJupZFxOziLCueCzuhWr" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb5d2d1251b016177ce0db21cc9342b6a7f8706b_2_690x421.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb5d2d1251b016177ce0db21cc9342b6a7f8706b_2_1035x631.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb5d2d1251b016177ce0db21cc9342b6a7f8706b_2_1380x842.jpeg 2x" data-dominant-color="545353"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-04-14 at 10.54.42 AM</span><span class="informations">1880×1148 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32be04e6dac27f5df216f073b6e37f7d5434d760.jpeg" data-download-href="/uploads/short-url/7eSZeB3LXUbvcedqHzWigop6FP2.jpeg?dl=1" title="Screen Shot 2022-04-14 at 11.09.59 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32be04e6dac27f5df216f073b6e37f7d5434d760_2_643x500.jpeg" alt="Screen Shot 2022-04-14 at 11.09.59 AM" data-base62-sha1="7eSZeB3LXUbvcedqHzWigop6FP2" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32be04e6dac27f5df216f073b6e37f7d5434d760_2_643x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32be04e6dac27f5df216f073b6e37f7d5434d760_2_964x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32be04e6dac27f5df216f073b6e37f7d5434d760_2_1286x1000.jpeg 2x" data-dominant-color="50726E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-04-14 at 11.09.59 AM</span><span class="informations">1920×1493 339 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here are several screenshots. Yes, I have found that those presets are useless. Are there guidelines for manually indicating my thresholds etc.?</p>

---

## Post #5 by @hherhold (2022-04-14 17:14 UTC)

<p>Generally, what I do is determine the voxel values for the area in question using the Data Probe in Segment Editor. If I can use thresholding combined with painting or scissors to extract what I’m looking for. Often, I will also use fill between slices combined with masking the volume to pull out a sub-volume for further processing.</p>
<p>What’s the insect in question? It’s hard to tell from this scan - is it a beetle or fly larva? What’s your voxel size and how big is the insect?</p>

---

## Post #6 by @lassoan (2022-04-14 18:13 UTC)

<p>Could you also tell the end goal of your analysis? Would you like to count, measuring size &amp; shape, visualize distribution within the soil sample, …? Do you have a plan for how to find the insects in the sample volume?</p>

---
