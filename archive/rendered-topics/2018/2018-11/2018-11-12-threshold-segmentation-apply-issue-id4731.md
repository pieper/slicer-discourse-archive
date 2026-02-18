# Threshold segmentation apply issue

**Topic ID**: 4731
**Date**: 2018-11-12
**URL**: https://discourse.slicer.org/t/threshold-segmentation-apply-issue/4731

---

## Post #1 by @EricWilson (2018-11-12 16:39 UTC)

<p>I am currently having an issue with thresholding an imported ultrasound scan. when i am setting the thresholding values, the area to be affected is shown as i would expect, like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5202d65063a3096fce5c5e8953fcd6082604970b.jpeg" alt="image" data-base62-sha1="bHvekCZmBoVrT91k0Mb0mJ1FnRN" width="396" height="470"></p>
<p>however, after the threshold operation completes, the result is very different. it will cover the entire scan instead of just the selected parts. it looks like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04b4fd562ec075127235088c54061aaa4039c748.jpeg" alt="image" data-base62-sha1="FDG3oIbPDnFPoCz10mAR31NFSE" width="392" height="472"></p>
<p>if a model is created, it will use the data from the second image.<br>
does anyone know what might be causing this, and how it can be fixed? thanks.</p>
<p>my slicer version is 4.10.0</p>

---

## Post #2 by @cpinter (2018-11-12 17:27 UTC)

<p>Threshold preview uses the rendered 2D images in the views, so it’s working a completely different way than the actual volume threshold. The result in the second screenshot seems like memory garbage. Not sure why it shows up like this.</p>
<p>Is your ultrasound image a single-component grayscale image?</p>

---

## Post #3 by @lassoan (2018-11-12 17:49 UTC)

<p>Slicer-4.10 had the problems that you show above but in recent nightly versions, Segment Editor can directly work on color images (it internally converts color images to grayscale). Please try latest nightly version of Slicer and report back.</p>

---

## Post #4 by @EricWilson (2018-11-12 18:23 UTC)

<p>It looks like you are correct. I downloaded the recent nightly build, 4.11.0 rev 27539, and ran the threshold operation again. the result is the same as the pre-application outline suggests and the model generated from it lines up with this. post threshold:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10d838177676a7dbbef03a002463d1392b47b155.png" data-download-href="/uploads/short-url/2p0SYYkzOTQLENTSqPcWP9XHlFr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d838177676a7dbbef03a002463d1392b47b155_2_404x500.png" alt="image" data-base62-sha1="2p0SYYkzOTQLENTSqPcWP9XHlFr" width="404" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10d838177676a7dbbef03a002463d1392b47b155_2_404x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10d838177676a7dbbef03a002463d1392b47b155.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10d838177676a7dbbef03a002463d1392b47b155.png 2x" data-dominant-color="2E5147"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">482×596 70.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thanks.</p>

---
