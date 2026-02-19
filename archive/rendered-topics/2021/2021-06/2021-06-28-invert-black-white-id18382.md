---
topic_id: 18382
title: "Invert Black White"
date: 2021-06-28
url: https://discourse.slicer.org/t/18382
---

# Invert black/white

**Topic ID**: 18382
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/invert-black-white/18382

---

## Post #1 by @johanna (2021-06-28 19:31 UTC)

<p>Hello!<br>
Sorry if this question has been asked before - I wasn’t able to find anything. How can I invert black and white for MRI? I found this:</p>
<p>The simplest is probably to invert your image by using SimpleFilters module: Filter = ShiftScaleImageFilter, Scale = -1.</p>
<p>I tried it and it worked for the Sample Data, but unfortunately not with my own DICOM files.<br>
Thank you for your help!</p>

---

## Post #2 by @pieper (2021-06-28 19:35 UTC)

<p>If it’s just for display, you can just pick InvertedGrey in the Volumes Module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a9656574a06e25b152b87922415ae12401be2a.jpeg" data-download-href="/uploads/short-url/kMAa5bYgpdndbSDghsRH5HDQH1g.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a9656574a06e25b152b87922415ae12401be2a_2_690x444.jpeg" alt="image" data-base62-sha1="kMAa5bYgpdndbSDghsRH5HDQH1g" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a9656574a06e25b152b87922415ae12401be2a_2_690x444.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91a9656574a06e25b152b87922415ae12401be2a_2_1035x666.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a9656574a06e25b152b87922415ae12401be2a.jpeg 2x" data-dominant-color="BDBDBC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1103×711 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @johanna (2021-06-28 19:47 UTC)

<p>Thank you for your quick answer! I found it, but somehow I cannot apply it.<br>
Maybe to explain why: The idea was to make teeth and surrounding bone structure look more like a CT image. I started using 3D Slicer a week ago, so maybe the answer is very easy but right now I’m not able to find my mistake.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2315663f20de0f9b05bbc3bca824d164422925fe.jpeg" data-download-href="/uploads/short-url/50myGBsE7aoqMZag7IfkUuouvYG.jpeg?dl=1" title="Bildschirmfoto 2021-06-28 um 21.41.41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2315663f20de0f9b05bbc3bca824d164422925fe_2_587x500.jpeg" alt="Bildschirmfoto 2021-06-28 um 21.41.41" data-base62-sha1="50myGBsE7aoqMZag7IfkUuouvYG" width="587" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2315663f20de0f9b05bbc3bca824d164422925fe_2_587x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2315663f20de0f9b05bbc3bca824d164422925fe_2_880x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2315663f20de0f9b05bbc3bca824d164422925fe_2_1174x1000.jpeg 2x" data-dominant-color="363534"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2021-06-28 um 21.41.41</span><span class="informations">1786×1520 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @cpinter (2021-06-28 19:50 UTC)

<p>It seems you loaded your adtaset one volume per slice, in which case you probably changed the color table of the wrong image. You need to load the volume using the DICOM browser so that it’s a real 3D image.</p>

---

## Post #5 by @johanna (2021-06-28 19:54 UTC)

<p>Yes! Thank you so much!</p>

---

## Post #6 by @pieper (2021-06-28 20:13 UTC)

<p>You need to be sure you have selected the volume that you want to change in the using the Active Volume selector.</p>
<p>To display it needs to match what’s shown in the slice view.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41c3fbb24f0d74dd7a74b7afee62b5fbe2aee82b.png" alt="image" data-base62-sha1="9nMVvNiOF2CzY3lQxsz3Y8ij6Bl" width="176" height="48"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbd0d567e6be5303bf2083ad140b0cdbd4be0647.png" alt="image" data-base62-sha1="t52lJaKGFTGvCDR91kl2wioC34P" width="505" height="52"></p>

---

## Post #7 by @johanna (2021-06-28 20:15 UTC)

<p>Yes, perfect! Thank you for helping me.</p>

---
