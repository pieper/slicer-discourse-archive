# Volume Rendering CPU VS GPU

**Topic ID**: 15922
**Date**: 2021-02-09
**URL**: https://discourse.slicer.org/t/volume-rendering-cpu-vs-gpu/15922

---

## Post #1 by @Raj_Kumar_Ranabhat (2021-02-09 20:59 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 2020-03-06<br>
Expected behavior: better rendering<br>
Actual behavior: Unknown</p>
<p>In our spine simulation project, due to issue on speed of burring. We are trying to switch from surface rendering to volume rendering for the visualization of the label map model. A volume rendering performance in the laptop Intel-5 without GPU is shown in figure (a). Quality was selected as maximum and interpolation as linear. The same rendered volume was saved as mrb file and loaded into the Intel - I9 computer with GPU GTX 1600 super. (some experiments were also done by directly performing volume rendering of the label map model). Figure (b)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a2c63d3202a919463dafd39050d91d14392cde4.jpeg" data-download-href="/uploads/short-url/cRI4Nkogia8FbfueypU9uG0a41C.jpeg?dl=1" title="volum_rend_VR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a2c63d3202a919463dafd39050d91d14392cde4_2_690x402.jpeg" alt="volum_rend_VR" data-base62-sha1="cRI4Nkogia8FbfueypU9uG0a41C" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a2c63d3202a919463dafd39050d91d14392cde4_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a2c63d3202a919463dafd39050d91d14392cde4_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a2c63d3202a919463dafd39050d91d14392cde4_2_1380x804.jpeg 2x" data-dominant-color="BFBFCA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volum_rend_VR</span><span class="informations">1601×933 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95d72a0b2fc5225755295c95d6105a4ca2400b64.jpeg" data-download-href="/uploads/short-url/lny851MG0BTne9wWUBq7eoT0gba.jpeg?dl=1" title="Volume_rendering_Laptop" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95d72a0b2fc5225755295c95d6105a4ca2400b64_2_690x392.jpeg" alt="Volume_rendering_Laptop" data-base62-sha1="lny851MG0BTne9wWUBq7eoT0gba" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95d72a0b2fc5225755295c95d6105a4ca2400b64_2_690x392.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95d72a0b2fc5225755295c95d6105a4ca2400b64_2_1035x588.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95d72a0b2fc5225755295c95d6105a4ca2400b64_2_1380x784.jpeg 2x" data-dominant-color="CBC9D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Volume_rendering_Laptop</span><span class="informations">1583×901 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>According to our expectation,  the quality and smoothness of rendered volume should be superior in the GPU based computer. But based on the experiments, the quality and smoothness of rendered volume in CPU based computer without GPU looks superior. Is there any explanations or suggestions, what might be the actual reason? How can I improve volume rendering properties, beside the properties mentioned in volume rendering module ?</p>
<p>It would be a great helpful for our project.</p>
<p>Thank You !!</p>
<p>Raj Kumar Ranabhat</p>

---

## Post #2 by @lassoan (2021-02-09 21:14 UTC)

<p>CPU volume rendering can change the order of interpolation and mapping, which can result in slightly higher quality images with CPU volume rendering. However, you can drastically improve rendering quality by blurring the edge of the volume (e.g., rescale the exported labelmap to range 0-255 using Simple Filters module RescaleIntensityImageFilter and apply slight Gaussian blur image filter).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12c9bdf27e502c6d69ded6c9346d51f0dde404ab.jpeg" data-download-href="/uploads/short-url/2GcP81UmcCO8Okc3B5cEqOLpR5V.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/12c9bdf27e502c6d69ded6c9346d51f0dde404ab_2_690x358.jpeg" alt="image" data-base62-sha1="2GcP81UmcCO8Okc3B5cEqOLpR5V" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/12c9bdf27e502c6d69ded6c9346d51f0dde404ab_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/12c9bdf27e502c6d69ded6c9346d51f0dde404ab_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12c9bdf27e502c6d69ded6c9346d51f0dde404ab.jpeg 2x" data-dominant-color="84878F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1080×561 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Left: volume rendering of labelmap volume.<br>
Right: volume rendering of the same labelmap volume after rescaling and blurring</p>
<p>You simulate burring, by subtracting a precomputed volume (with soft edges) from the volume-rendered image.</p>

---
