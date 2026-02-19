---
topic_id: 26750
title: "Scaling Radiographs"
date: 2022-12-15
url: https://discourse.slicer.org/t/26750
---

# Scaling radiographs

**Topic ID**: 26750
**Date**: 2022-12-15
**URL**: https://discourse.slicer.org/t/scaling-radiographs/26750

---

## Post #1 by @anromero (2022-12-15 16:36 UTC)

<p>I am working with radiographs of patient heads with a known scale of 5.7143 pixels/mm and 1.2 magnification. Once I upload the image to 3D Slicer, I am having trouble figuring out how to input this information so that we can take accurate measurements of the bones. Right now when I use the line tool to measure the ~2mm markers, it says that the markers are 8.635mm. How do I scale these images?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6a358568ae57dc48eab61eded196e8fef74c317.jpeg" data-download-href="/uploads/short-url/zbRqdK4KDn4wTcIvz4vEKyoYRTh.jpeg?dl=1" title="Screenshot 2022-12-15 at 10.28.34 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6a358568ae57dc48eab61eded196e8fef74c317_2_690x485.jpeg" alt="Screenshot 2022-12-15 at 10.28.34 AM" data-base62-sha1="zbRqdK4KDn4wTcIvz4vEKyoYRTh" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6a358568ae57dc48eab61eded196e8fef74c317_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6a358568ae57dc48eab61eded196e8fef74c317_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6a358568ae57dc48eab61eded196e8fef74c317_2_1380x970.jpeg 2x" data-dominant-color="888787"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-12-15 at 10.28.34 AM</span><span class="informations">1920×1350 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-12-15 17:46 UTC)

<p>It sounds like you just need to type in 5.7143 for the first two fields of the Image Spacing of the (one slice) volume.  I’m not sure what you mean by 1.2 magnification, but probably that’s already included in the spacing so you don’t need to include it.  Generally speaking, measuring off projection X-rays without a calibration ruler in the image is likely to have inaccuracies so use caution.</p>

---

## Post #4 by @lassoan (2022-12-15 20:59 UTC)

<p>5.7143 pixels/mm “scale” is somewhat misleading, as it is not the pixel size but the inverse of that. So, you need to type the inverse (0.175 mm) into the image spacing field.</p>
<p>The magnification (M = SID / SOD) may or may not be included in the pixels/mm value that you got. If it is not included then you need to divide the spacing by the magnification value before you type it in the spacing field: 0.175mm * 1.2 = 0.1458 mm.</p>
<p>Of course distance measurement in projection images, such as X-rays is just approximate, as the size depends on the magnification factor (ratio of the source-to-object and source-to-detector distance), which varies across the imaged anatomy.</p>
<p>Adding an object of known size (such as a radioopaqe sphere) near the object of interest and measuring its size in the image as <a class="mention" href="/u/pieper">@pieper</a> suggested is always a good idea when you establish a new workflow or introduce new hardware or software.</p>

---
