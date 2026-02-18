# General Registration (BRAINS) consistently reports the error “All samples map outside the moving image buffer,” even when the same image is used for both the fixed and moving volumes for a specific image

**Topic ID**: 45677
**Date**: 2026-01-05
**URL**: https://discourse.slicer.org/t/general-registration-brains-consistently-reports-the-error-all-samples-map-outside-the-moving-image-buffer-even-when-the-same-image-is-used-for-both-the-fixed-and-moving-volumes-for-a-specific-image/45677

---

## Post #1 by @ffr (2026-01-05 19:37 UTC)

<p>I am using Windows version 5.10.0</p>
<p>Please find the image here. It is a normal CT image, and I don’t know why BRAINS is not working for this specific case. Thank you very much for any help.</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1UxmIlAuSxNIINjQrV6-q-vSZcaxw1IYS/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1UxmIlAuSxNIINjQrV6-q-vSZcaxw1IYS/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1UxmIlAuSxNIINjQrV6-q-vSZcaxw1IYS/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1UxmIlAuSxNIINjQrV6-q-vSZcaxw1IYS/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">ct_sample.nii.gz</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4ed206ed98e434e52c12e842f1face350487b39.jpeg" data-download-href="/uploads/short-url/wFaU6gs8o2ZTHVz80XynNo3wGeZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4ed206ed98e434e52c12e842f1face350487b39_2_337x249.jpeg" alt="image" data-base62-sha1="wFaU6gs8o2ZTHVz80XynNo3wGeZ" width="337" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4ed206ed98e434e52c12e842f1face350487b39_2_337x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4ed206ed98e434e52c12e842f1face350487b39_2_505x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4ed206ed98e434e52c12e842f1face350487b39_2_674x498.jpeg 2x" data-dominant-color="444240"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1259×932 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-01-05 22:32 UTC)

<p>In general, using the same image as fixed and moving is not a good test case, as having exactly 0 intensity difference and gradients can cause numerical errors. For testing, always add some random perturbation in image pose and/or image content.</p>
<p>That said, after I’ve added some small initial random transformation to the moving image, I still got the same error:</p>
<blockquote>
<p>itk::ExceptionObject (0000007E693D76B0)<br>
Location: “unknown”<br>
File: C:\D\S\S-0-build\ITK\Modules\Registration\Metricsv4\include\itkMattesMutualInformationImageToImageMetricv4.hxx<br>
Line: 311<br>
Description: ITK ERROR: MattesMutualInformationImageToImageMetricv4(00000237B9A05CA0): All samples map outside moving image buffer. The images do not sufficiently overlap. They need to be initialized to have more overlap before this metric will work. For instance, you can align the image centers by translation.</p>
</blockquote>
<p>I debugged it a bit and it seems that after the first iteration the new transform moves the moving image so much that it no longer overlaps with the fixed volume. Rescaling the image intensity values (e.g., Simple Filters module, <code>RescaleIntensityImageFilter</code> set output minimum and maximum to 0 and 255) or changing the optimization parameters could solve this.</p>
<p>Instead of trying to tune these registration parameters, I would recommend to use a registration tool that does not require parameter tuning, such as Elastix or ANTs Slicer extensions.</p>

---

## Post #3 by @ffr (2026-01-06 21:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="45677">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>RescaleIntensityImageFilter</code></p>
</blockquote>
</aside>
<p>RescaleIntensityImageFilter fixed this issue. Thank you so much Dr. Lasso!</p>

---
