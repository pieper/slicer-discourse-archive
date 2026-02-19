---
topic_id: 29621
title: "Measuring Two Specific Points On The Both Stl Models"
date: 2023-05-24
url: https://discourse.slicer.org/t/29621
---

# Measuring two specific points on the both STL models

**Topic ID**: 29621
**Date**: 2023-05-24
**URL**: https://discourse.slicer.org/t/measuring-two-specific-points-on-the-both-stl-models/29621

---

## Post #1 by @wael_telha (2023-05-24 06:04 UTC)

<p>I need a help Regarding measuring two specific points on the both STL models : the aim of the work is to measure the accuracy between virtual planning and actual surgery output. i ahve tried some steps and i need you to confirm if thecorrect or not</p>
<p>I started with a model registration between the pre-operative planning and post-operative model (stl)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8a032da61a6f947a8f47056bd24263240ed256b.jpeg" data-download-href="/uploads/short-url/uUmmaJl7vKQN2G54Xv7eJZsT2Qz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a032da61a6f947a8f47056bd24263240ed256b_2_690x388.jpeg" alt="image" data-base62-sha1="uUmmaJl7vKQN2G54Xv7eJZsT2Qz" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a032da61a6f947a8f47056bd24263240ed256b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a032da61a6f947a8f47056bd24263240ed256b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d8a032da61a6f947a8f47056bd24263240ed256b_2_1380x776.jpeg 2x" data-dominant-color="BCCDD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>
<p>following the registration of the two models I used pick’n Point I choose the reference point ( edge of tooth) in the post-operative model T2  (REFERENCE MODEL) I made a point on the reference model at the area of interest to measure the distance between the same points between the two models and  BEFORE running  I chose the propagate the non- corresponding mesh.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/556e673e918aa3238cb9da2c8763cc03418534a6.jpeg" data-download-href="/uploads/short-url/cbL7CFOVcOfvBDIQKOnnCsaw26a.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556e673e918aa3238cb9da2c8763cc03418534a6_2_690x388.jpeg" alt="image" data-base62-sha1="cbL7CFOVcOfvBDIQKOnnCsaw26a" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556e673e918aa3238cb9da2c8763cc03418534a6_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556e673e918aa3238cb9da2c8763cc03418534a6_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556e673e918aa3238cb9da2c8763cc03418534a6_2_1380x776.jpeg 2x" data-dominant-color="B7D6E0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>then through Model to Model Distance : the source model is the post-operative Model and the target model is the pre-operative model and the calculation was done<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9122bbc74572a7f7b38e1fc0f5721fba9c52d842.jpeg" data-download-href="/uploads/short-url/kHVEglXFMhdxg1G4TQQd1AaYjJg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9122bbc74572a7f7b38e1fc0f5721fba9c52d842_2_690x388.jpeg" alt="image" data-base62-sha1="kHVEglXFMhdxg1G4TQQd1AaYjJg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9122bbc74572a7f7b38e1fc0f5721fba9c52d842_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9122bbc74572a7f7b38e1fc0f5721fba9c52d842_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9122bbc74572a7f7b38e1fc0f5721fba9c52d842_2_1380x776.jpeg 2x" data-dominant-color="C5BFC9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>the fourth and last step was to get the measured value through Mesh Statistics I chose the absolute value and X AXIS, Y, AND Z AXIS<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/063211280ba9802c02f90a4f9e0cc06e7db68c34.jpeg" data-download-href="/uploads/short-url/SO8eUMjeoCW2v6AuEEa9dOcI4I.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/063211280ba9802c02f90a4f9e0cc06e7db68c34_2_690x388.jpeg" alt="image" data-base62-sha1="SO8eUMjeoCW2v6AuEEa9dOcI4I" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/063211280ba9802c02f90a4f9e0cc06e7db68c34_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/063211280ba9802c02f90a4f9e0cc06e7db68c34_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/063211280ba9802c02f90a4f9e0cc06e7db68c34_2_1380x776.jpeg 2x" data-dominant-color="C6BFC8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
</ol>

---
