# Apply deconvolution filter on the image to correct blurring

**Topic ID**: 5091
**Date**: 2018-12-16
**URL**: https://discourse.slicer.org/t/apply-deconvolution-filter-on-the-image-to-correct-blurring/5091

---

## Post #1 by @shahrokh (2018-12-16 06:36 UTC)

<p>Hello Dear Developers and Users</p>
<p>I have images acquired from a radiation field using Electronic Portal Imaging Device (EPID) in radiotherapy.<br>
Due to scattered beams in EPID, there was a blurring effect. As expected on the edges, the image quality is reduced.<br>
It seems that deconvolution filters should be used to improve image quality.<br>
For it, I have calculated the EPID response to a pencil beam through the GATE Monte Carlo code. In other words, I have determined the EPID response to a pencil beam (PSF system).<br>
The following images are related to the image acquired with the EPID and the logarithm of the EPID response to a pencil beam.</p>
<p>Specifications of EPID image:<br>
Image Dimensions: 1024 1024 1<br>
Image spacing: 0.25mm 0.25mm 1.00mm<br>
Scalar Type: double<br>
Scalar Range: 530 to 304446<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b4cbf851b75d2400460c5cf03327aa3de954a8b.png" data-download-href="/uploads/short-url/hAL9YKieXfMMBczPeY93IaLIT7J.png?dl=1" title="EPID" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b4cbf851b75d2400460c5cf03327aa3de954a8b_2_500x500.png" alt="EPID" data-base62-sha1="hAL9YKieXfMMBczPeY93IaLIT7J" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b4cbf851b75d2400460c5cf03327aa3de954a8b_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b4cbf851b75d2400460c5cf03327aa3de954a8b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b4cbf851b75d2400460c5cf03327aa3de954a8b.png 2x" data-dominant-color="6F6F6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">EPID</span><span class="informations">650×649 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Specification of scatter kernel:<br>
Image Dimensions: 250 250 1<br>
Image spacing: 0.40mm 0.40mm 1.00mm<br>
Scalar Type: double<br>
Scalar Range: -27 to 0<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6998fdf8f1d20e71525560c2c5638ccafdedec5.jpeg" data-download-href="/uploads/short-url/zbwsH2inICn0v5enzbhCNI4ijBj.jpeg?dl=1" title="scatterKernel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6998fdf8f1d20e71525560c2c5638ccafdedec5_2_499x499.jpeg" alt="scatterKernel" data-base62-sha1="zbwsH2inICn0v5enzbhCNI4ijBj" width="499" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6998fdf8f1d20e71525560c2c5638ccafdedec5_2_499x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6998fdf8f1d20e71525560c2c5638ccafdedec5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6998fdf8f1d20e71525560c2c5638ccafdedec5.jpeg 2x" data-dominant-color="434343"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scatterKernel</span><span class="informations">573×574 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve noticed that there are several deconvolution filters in the “itk Simple Filters” module such as:<br>
InverseDeconvolutionImageFilter<br>
LandweberDeconvolutionImageFilter<br>
ProjectedLandweberDeconvolutionImageFilter<br>
RichardsonLucyDeconvolutionImageFilter<br>
TikhonovDeconvolutionImageFilter<br>
WienerDeconvolutionImageFilter</p>
<p>When I use these filters with these image as input volume (with default settings), the output image is badly damaged.<br>
With this image and kenel, what solution you recommend to me?<br>
Please guide me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-12-16 13:27 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="5091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>It seems that deconvolution filters should be used to improve image quality</p>
</blockquote>
</aside>
<p>It is expected that the device manufacturer performs all possible image quality improvement filtering that optimizes overall signal-to-noise ratio in the image. This includes deconvolution filtering, if applicable. If you have doubts that the image quality is optimal then report this error to the manufacturer. If you work with images or features that the imaging device was not optimized for then you might be able to achieve further improvements by enhancing those specific features that you are interested in (at the cost of decreasing overall image quality).</p>
<p>Unsharp masking only improves image quality with optimal parameter settings but if the output image is completely off then you may need to convert the pixel type of the input image to float (using Cast Scalar Volume module). Some filters may not work on single-slice volumes, so you may need to resample it to have multiple slices (using Resample Scalar Volume, adjust Spacing parameters to have at least 10 slices). Make sure to also crop any black borders in the input image.</p>

---

## Post #3 by @Juicy (2019-11-24 22:27 UTC)

<p>I was looking at some papers about improving the accuracy of segmented models from CT scans. <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7284707" rel="noopener nofollow ugc">One paper</a> suggested that the slightly blurred edge between bone and soft tissue could be sharpened using a Richardson Lucy Deconvolution filter with some knowledge of the point spread function.</p>
<p>It would be good to experiment with this filter to see if edges could be un-blurred to potentially make more accurate bone surface models for modelling implants.</p>
<p>I was looking at the Richardson Lucy Filter in Simple Filters and was wondering if anyone knows how to use this filter? I couldn’t find much info on the ITK website either. Why are there two volume inputs? Also I was under the impression that this filter needed an estimate of the PSF? Where would this be input?</p>
<p>I haven’t had any luck using this filter. The output is always a greyed out volume with a black dot in the middle. I have tried playing with all the settings and different iterations. I have also tried converting the volume to float as well as double.</p>
<p>Thanks,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9ffe4d03d7faec7b42a02c8b54f9ad5bbbb4da0a.jpeg" alt="RichardsonLucy" data-base62-sha1="mPmKNB3JyEyhfESAlakgiUaaXOO" width="553" height="475"></p>

---

## Post #4 by @lassoan (2019-11-24 23:21 UTC)

<p>We worked on orbital bone reconstruction from CT images where segmentation of thin bones was very challenging. Deconvolution helped but simple unsharp masking worked about just as well in practice.</p>
<p>See these posts for some more details:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/high-quality-segmentation-of-the-orbital-walls/2345/5" class="inline-onebox">High quality segmentation of the orbital walls</a></li>
<li><a href="https://discourse.slicer.org/t/segmentation-of-thin-surfaces/2332" class="inline-onebox">Segmentation of thin surfaces</a></li>
</ul>
<p>I would recommend not to worry about achieve optimal results by preprocessing. If you oversample the volume (so that you can represent thinner walls) and apply some edge enhancement filter then it should help. You can take care of the remaining issues in further segmentation steps (e.g., you can create a continuous bone surface from segmented contours by using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">WrapSolidify</a> segment editor effect).</p>

---
