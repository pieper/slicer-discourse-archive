---
topic_id: 7907
title: "Trouble Segmenting The Tongue After Fixing Threshold"
date: 2019-08-07
url: https://discourse.slicer.org/t/7907
---

# Trouble segmenting the Tongue, after fixing threshold

**Topic ID**: 7907
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/trouble-segmenting-the-tongue-after-fixing-threshold/7907

---

## Post #1 by @Raid (2019-08-07 02:40 UTC)

<p>Operating system: Windows 10 Enterprise<br>
Slicer version: 4.10.2<br>
Data type: NRRD</p>
<p>Hello, I’m working on a human fetal head stained with <strong>Phosphotungstic acid</strong> (PTA) to be able to visualize soft tissue.</p>
<p>I’ve used the scissors tool to erase all unwanted surroundings of the tongue, yet after fixing the threshold it still includes most of the mandible and muscles around it as they all share the same intensity range even after trying to increase or decrease the contrast.</p>
<p>Screenshot 1:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ed3a62960be07444e9268b91979c0b82407d1e4.jpeg" data-download-href="/uploads/short-url/6Gfq1flWqtzCyke6ngROXDMEfBi.jpeg?dl=1" title="screen%20shot%201%20for%20forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ed3a62960be07444e9268b91979c0b82407d1e4_2_690x493.jpeg" alt="screen%20shot%201%20for%20forum" data-base62-sha1="6Gfq1flWqtzCyke6ngROXDMEfBi" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ed3a62960be07444e9268b91979c0b82407d1e4_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ed3a62960be07444e9268b91979c0b82407d1e4_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ed3a62960be07444e9268b91979c0b82407d1e4.jpeg 2x" data-dominant-color="444C4F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen%20shot%201%20for%20forum</span><span class="informations">1289×921 322 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After trying to refine the boundaries of the tongue as much as possible still, the root of the tongue slices aren’t as clear as the dorsum (superior border)</p>
<p>Screenshot 2:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe2271f5746ee1059a40c122b2a7d40ec0d660ad.jpeg" data-download-href="/uploads/short-url/Agb4HIWOLtNpBKS1VD3dBdnAkEZ.jpeg?dl=1" title="screenshot%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe2271f5746ee1059a40c122b2a7d40ec0d660ad_2_690x483.jpeg" alt="screenshot%202" data-base62-sha1="Agb4HIWOLtNpBKS1VD3dBdnAkEZ" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe2271f5746ee1059a40c122b2a7d40ec0d660ad_2_690x483.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe2271f5746ee1059a40c122b2a7d40ec0d660ad_2_1035x724.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe2271f5746ee1059a40c122b2a7d40ec0d660ad.jpeg 2x" data-dominant-color="9096BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot%202</span><span class="informations">1288×902 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’ve also tried the “Grow from seeds” tool but this is the result I get after many attempts<br>
with and without changing the Window/Level in the Volumes module.</p>
<p>Screenshot 3<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8295c875fc99cbc14a122e06049cd4afb34ea5af.jpeg" data-download-href="/uploads/short-url/iDcYKAXjDl0cuk1wVhGnO3fLYf5.jpeg?dl=1" title="sc3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8295c875fc99cbc14a122e06049cd4afb34ea5af_2_689x412.jpeg" alt="sc3" data-base62-sha1="iDcYKAXjDl0cuk1wVhGnO3fLYf5" width="689" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8295c875fc99cbc14a122e06049cd4afb34ea5af_2_689x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8295c875fc99cbc14a122e06049cd4afb34ea5af_2_1033x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8295c875fc99cbc14a122e06049cd4afb34ea5af.jpeg 2x" data-dominant-color="867DC6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sc3</span><span class="informations">1290×772 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In my opinion, the main problem is finding the correct threshold that is confined to the area selected, even though one of the windows/levels show excellent differentiation between the tongue and its surroundings as shown below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be2fdaf069e6f5210746bd0d9e416fd9afab613e.jpeg" data-download-href="/uploads/short-url/r8tfqaPoZBiFYBrUIfd2OZrZodg.jpeg?dl=1" title="40%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be2fdaf069e6f5210746bd0d9e416fd9afab613e_2_690x431.jpeg" alt="40%20PM" data-base62-sha1="r8tfqaPoZBiFYBrUIfd2OZrZodg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be2fdaf069e6f5210746bd0d9e416fd9afab613e_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be2fdaf069e6f5210746bd0d9e416fd9afab613e_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be2fdaf069e6f5210746bd0d9e416fd9afab613e_2_1380x862.jpeg 2x" data-dominant-color="4B667B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">40%20PM</span><span class="informations">2880×1800 860 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would still get the same results (a lot of noise/unwanted slices around the segmented area)</p>
<p>Help is needed to overcome these issues…</p>
<p>Many thanks,</p>
<p>Raid</p>

---

## Post #2 by @lassoan (2019-08-07 03:34 UTC)

<p>Overall intensity of the tongue is somewhat different from surroundings, but it is very noisy. It may make segmentation easier if you apply some noise filter on the input image (simple Gaussian smoothing or one of the Anisotropic diffusion filters may work).</p>
<p>Try “Grow from seeds” method again on the noise-filtered image, using Slicer-4.10.2 or later, maybe using masking (see tutorial <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/" rel="nofollow noopener">here</a>). Use “Smoothing” effect after you clicked “Apply” in Grow from seeds.</p>
<p>If you find boundaries of “Grow from seeds” too noisy (even after smoothing) then you can try to use Watershed effect (provided by SegmentEditorExtraEffects extension), with the same seeds as “Grow from seeds”. It has a spatial smoothness constraint.</p>

---

## Post #3 by @Raid (2019-08-13 21:30 UTC)

<p>Thank you so much for your help.</p>
<p>I’ve added the noise filter and re-segmented using Grow from seeds (Watershed effect didn’t give a better result). There was some improvement then, I tried to apply the (median smoothening) but the software just freezes and doesn’t respond even after trying to increase the factor to the max.<br>
I cropped the volume again and increased the spacing (x3) on the account of resolution, just for the sake of median smoothening but still it’s not working as in the screenshots:</p>
<p><a href="/uploads/short-url/iRibxixhHzyeeujHjRwNN9NSexV.jpeg">smoothening%20not%20responding%2013%20Aug|690x388</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8dd8b2a0f2fb11a6ba84845dc58a6ceae4eafaaf.png" data-download-href="/uploads/short-url/kePAXDPzpEBBwHxiZ4R1Sbs0eWb.png?dl=1" title="smoothening%20not%20responding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dd8b2a0f2fb11a6ba84845dc58a6ceae4eafaaf_2_690x388.png" alt="smoothening%20not%20responding" data-base62-sha1="kePAXDPzpEBBwHxiZ4R1Sbs0eWb" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dd8b2a0f2fb11a6ba84845dc58a6ceae4eafaaf_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dd8b2a0f2fb11a6ba84845dc58a6ceae4eafaaf_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8dd8b2a0f2fb11a6ba84845dc58a6ceae4eafaaf_2_1380x776.png 2x" data-dominant-color="D1D5DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">smoothening%20not%20responding</span><span class="informations">1920×1080 456 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Although (Joint smoothening) works and removes all the noise but the segment loses all the surface morphology as in the screenshot.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff56ecf64af342fd510f1b5e151ae308006d23f0.jpeg" data-download-href="/uploads/short-url/AqPZwiOsZRtdFpv1gN27RXQXuzS.jpeg?dl=1" title="joint%20smoothening%20lost%20morphology" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff56ecf64af342fd510f1b5e151ae308006d23f0_2_690x388.jpeg" alt="joint%20smoothening%20lost%20morphology" data-base62-sha1="AqPZwiOsZRtdFpv1gN27RXQXuzS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff56ecf64af342fd510f1b5e151ae308006d23f0_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff56ecf64af342fd510f1b5e151ae308006d23f0_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff56ecf64af342fd510f1b5e151ae308006d23f0_2_1380x776.jpeg 2x" data-dominant-color="B598B2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">joint%20smoothening%20lost%20morphology</span><span class="informations">1920×1080 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Regards,<br>
Raid</p>

---

## Post #4 by @lassoan (2019-08-14 03:58 UTC)

<aside class="quote no-group" data-username="Raid" data-post="3" data-topic="7907">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dc4da7/48.png" class="avatar"> Raid:</div>
<blockquote>
<p>Watershed effect didn’t give a better result</p>
</blockquote>
</aside>
<p>Did you try a wide range of values for “Object scale”? Could you post a couple of pictures of what you got with different object scales?</p>
<aside class="quote no-group" data-username="Raid" data-post="3" data-topic="7907">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dc4da7/48.png" class="avatar"> Raid:</div>
<blockquote>
<p>There was some improvement then, I tried to apply the (median smoothening) but the software just freezes and doesn’t respond even after trying to increase the factor to the max.</p>
</blockquote>
</aside>
<p>If kernel size is more than 10-15 then you can expect very high computation time (for the 61x61x125 kernel size you would probably need several hours to compute). If you need too large kernel then it means that your image has unnecessarily fine resolution and you can resample it in <code>Crop volume</code> module to have much larger voxels. Larger voxels will make all computations much faster and the resulting segments smoother.</p>
<aside class="quote no-group" data-username="Raid" data-post="3" data-topic="7907">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dc4da7/48.png" class="avatar"> Raid:</div>
<blockquote>
<p>Although (Joint smoothening) works and removes all the noise but the segment loses all the surface morphology as in the screenshot.</p>
</blockquote>
</aside>
<p>The image looks pretty good to me. You can reduce smoothing factor if you need to preserve more details.</p>

---
