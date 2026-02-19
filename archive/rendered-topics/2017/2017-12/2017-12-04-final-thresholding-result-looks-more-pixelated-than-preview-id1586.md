---
topic_id: 1586
title: "Final Thresholding Result Looks More Pixelated Than Preview"
date: 2017-12-04
url: https://discourse.slicer.org/t/1586
---

# Final thresholding result looks more pixelated than preview

**Topic ID**: 1586
**Date**: 2017-12-04
**URL**: https://discourse.slicer.org/t/final-thresholding-result-looks-more-pixelated-than-preview/1586

---

## Post #1 by @timeanddoctor (2017-12-04 13:20 UTC)

<p>Operating system: win 7<br>
Slicer version:12-2<br>
Expected behavior:<br>
Actual behavior:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f352d673d85280277d314e0c88c834629a7f4a7.jpeg" data-download-href="/uploads/short-url/dAfi57eAc3V24BpzlAlo29AT5f9.jpg?dl=1" title="2017-12-04_211038" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5f352d673d85280277d314e0c88c834629a7f4a7_2_690x375.jpg" alt="2017-12-04_211038" data-base62-sha1="dAfi57eAc3V24BpzlAlo29AT5f9" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5f352d673d85280277d314e0c88c834629a7f4a7_2_690x375.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5f352d673d85280277d314e0c88c834629a7f4a7_2_1035x562.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f352d673d85280277d314e0c88c834629a7f4a7.jpeg 2x" data-dominant-color="A6A7A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2017-12-04_211038</span><span class="informations">1341×729 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9dc4cbee31de47d4b634539ccc037d05b434002.jpeg" data-download-href="/uploads/short-url/sNJXCGWw7jWgMmYaTM1Pa6DsAzE.jpg?dl=1" title="2017-12-04_211052" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c9dc4cbee31de47d4b634539ccc037d05b434002_2_690x378.jpg" alt="2017-12-04_211052" data-base62-sha1="sNJXCGWw7jWgMmYaTM1Pa6DsAzE" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c9dc4cbee31de47d4b634539ccc037d05b434002_2_690x378.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c9dc4cbee31de47d4b634539ccc037d05b434002_2_1035x567.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9dc4cbee31de47d4b634539ccc037d05b434002.jpeg 2x" data-dominant-color="A7A8AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2017-12-04_211052</span><span class="informations">1355×744 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @timeanddoctor (2017-12-04 13:25 UTC)

<p>The picture looks rough and serrated after Apply…why?</p>

---

## Post #3 by @pieper (2017-12-04 13:36 UTC)

<p>Segmentation happens at pixel resolution but the preview is shown at screen resolution.  If you need higher resolution you could upsample the master volume first.  But smoothing is applied when you build models, so typically working at the native resolution of the scan is the best place to start.</p>

---

## Post #4 by @timeanddoctor (2017-12-10 13:42 UTC)

<p>Thank you Steve Pieper for your replay.<br>
However, I had the same resolution in MIMICS software(below pictures).<br>
I couldnot understand “upsample the master volume first”, what should I do  in 3d-slicer to get the same result between final thresholding and preview.<br>
Thanks.</p>

---

## Post #5 by @timeanddoctor (2017-12-10 13:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d52d61d7cc9f8d0f891eab94d7791ccd0ca28c3f.jpeg" data-download-href="/uploads/short-url/upQVN4050pzIaIGozi1WytVHpjF.jpg?dl=1" title="2017-12-10_213643" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d52d61d7cc9f8d0f891eab94d7791ccd0ca28c3f_2_680x500.jpg" alt="2017-12-10_213643" data-base62-sha1="upQVN4050pzIaIGozi1WytVHpjF" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d52d61d7cc9f8d0f891eab94d7791ccd0ca28c3f_2_680x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d52d61d7cc9f8d0f891eab94d7791ccd0ca28c3f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d52d61d7cc9f8d0f891eab94d7791ccd0ca28c3f.jpeg 2x" data-dominant-color="747B7C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2017-12-10_213643</span><span class="informations">1002×736 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/693d236bf8b4b127897366d2653a526d3a58f414.jpeg" data-download-href="/uploads/short-url/f0Z7BP2gFnTww1IUjPFwFnH4Giw.jpg?dl=1" title="2017-12-10_213656" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/693d236bf8b4b127897366d2653a526d3a58f414_2_645x500.jpg" alt="2017-12-10_213656" data-base62-sha1="f0Z7BP2gFnTww1IUjPFwFnH4Giw" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/693d236bf8b4b127897366d2653a526d3a58f414_2_645x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/693d236bf8b4b127897366d2653a526d3a58f414_2_967x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/693d236bf8b4b127897366d2653a526d3a58f414.jpeg 2x" data-dominant-color="60686B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2017-12-10_213656</span><span class="informations">992×768 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2017-12-10 14:56 UTC)

<p>To be able to represent smaller details, do as Steve suggested, increase the input volume resolution using Crop Volume module’s interpolation option. I would also recommend to set isotropic voxel size.</p>
<p>If you just need smoother model, then you may try Smoothing effect after thresholding and tune mesh generation smoothing (click small “down arrow” on the 3D button).</p>

---
