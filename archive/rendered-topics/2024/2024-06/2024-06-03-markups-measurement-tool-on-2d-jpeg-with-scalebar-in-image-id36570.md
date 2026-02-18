# Markups Measurement Tool on 2D [jpeg] with scalebar in image

**Topic ID**: 36570
**Date**: 2024-06-03
**URL**: https://discourse.slicer.org/t/markups-measurement-tool-on-2d-jpeg-with-scalebar-in-image/36570

---

## Post #1 by @skillingsworth (2024-06-03 12:58 UTC)

<p>Operating system: Intel(R) Core™ i7-8650U CPU @ 1.90GHz   2.11 GHz Windows 11<br>
Slicer version: 5.6.2<br>
Expected behavior: …<br>
Actual behavior: …</p>
<p>Interested in using 3D Slicer for 2D  (jpeg) images. I took all of my images with a scalebar in the photo as seen here, and wondered how I get the markups measuring tool to register the proper scale. See the image here for reference-<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8fe30f298c9e67a22242e822d6ef05ed06eab02.jpeg" data-download-href="/uploads/short-url/qowsjyyrfvfb44OMSKtSIEFv9Ci.jpeg?dl=1" title="img" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8fe30f298c9e67a22242e822d6ef05ed06eab02.jpeg" alt="img" data-base62-sha1="qowsjyyrfvfb44OMSKtSIEFv9Ci" width="532" height="500" data-dominant-color="C9C2BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">img</span><span class="informations">588×552 37.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you, Stephanie</p>

---

## Post #2 by @muratmaga (2024-06-03 15:36 UTC)

<p>First check the spacing of the JPG image you loaded in the Slicer (volumes module). If it is not 1x1x1, set 1x1x1.</p>
<p>Then measure a known distance on the ruler, e.g., from 3 to 10cm (the bigger a distance you measure, the smaller your calibration error will be) using the line tool. Then divide this distance (in mm) to the measurement you obtained by the Line tool (e.g., 1400, so 70/1400 = 0.05 mm/px.</p>
<p>This is the true spacing of your volume after the calibration. If you go back and type in this as your volume spacing, then you should be able to obtain measurements that are correct (you can validate by remeasuring the ruler).</p>
<p>Or you can simply keep the ruler measurement external in a file, and then do the math later.</p>
<p>Regardless though, if you want correct calibration, and your ruler is slanted like this in a picture, you should first put it under a transformation to make the ruler straight to obtain an accurate distance.</p>

---

## Post #3 by @skillingsworth (2024-06-03 15:40 UTC)

<p>Thank you. I’ll give these steps a try.</p>

---

## Post #5 by @muratmaga (2024-06-03 15:50 UTC)

<p>I made a decimal error in the previous screenshot (and corrected my cm to mm conversion. not enough coffee).  Here is the updated screenshot.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eb280dd3cc82138392d524aa31ee64d9f143840.jpeg" data-download-href="/uploads/short-url/kmmf2fW7NKZGvGG67n2jfSPaaUE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb280dd3cc82138392d524aa31ee64d9f143840_2_419x500.jpeg" alt="image" data-base62-sha1="kmmf2fW7NKZGvGG67n2jfSPaaUE" width="419" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb280dd3cc82138392d524aa31ee64d9f143840_2_419x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb280dd3cc82138392d524aa31ee64d9f143840_2_628x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8eb280dd3cc82138392d524aa31ee64d9f143840_2_838x1000.jpeg 2x" data-dominant-color="C4B7AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×2289 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
