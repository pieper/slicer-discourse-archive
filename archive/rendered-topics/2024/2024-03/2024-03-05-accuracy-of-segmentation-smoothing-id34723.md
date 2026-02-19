---
topic_id: 34723
title: "Accuracy Of Segmentation Smoothing"
date: 2024-03-05
url: https://discourse.slicer.org/t/34723
---

# Accuracy of segmentation smoothing

**Topic ID**: 34723
**Date**: 2024-03-05
**URL**: https://discourse.slicer.org/t/accuracy-of-segmentation-smoothing/34723

---

## Post #1 by @vikas26 (2024-03-05 20:26 UTC)

<p>Hello,</p>
<p>I am healthcare professional, a general and orthopedic surgeon with over 24 years of active experience. We have been using an FDA approved software for complex surgical planning for the past 8 years.</p>
<p>However, due to its increasing cost per seat, we were looking for alternative and free solutions and came across 3D Slicer. I appreciate what Slicer’s existing features provide, and we started evaluating it just a couple of months ago. Besides the great functionalities, I have found subtle differences between these two.</p>
<p>In 3D Slicer, I applied threshold and island effect and exported the STL(s), then loaded it back into to the FDA approved software. In the FDA approved software, the same effects are applied, and we found a significant difference in contour of both the STL(s). Please find the comparison images below:</p>
<p><strong>Contour Deviations:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6041c6fe52c4452dd1d7adc8d328f9bfeb20f6d7.png" data-download-href="/uploads/short-url/dJwLoq3iXRNMtaWLEq9DffLdScL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6041c6fe52c4452dd1d7adc8d328f9bfeb20f6d7_2_345x166.png" alt="image" data-base62-sha1="dJwLoq3iXRNMtaWLEq9DffLdScL" width="345" height="166" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6041c6fe52c4452dd1d7adc8d328f9bfeb20f6d7_2_345x166.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6041c6fe52c4452dd1d7adc8d328f9bfeb20f6d7_2_517x249.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6041c6fe52c4452dd1d7adc8d328f9bfeb20f6d7_2_690x332.png 2x" data-dominant-color="8A8885"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×347 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0357418dee4b1fe18e0575457acbbb3b3c34ef66.png" data-download-href="/uploads/short-url/tynpOvn19JHT0y9AdxQ9p56wQe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0357418dee4b1fe18e0575457acbbb3b3c34ef66.png" alt="image" data-base62-sha1="tynpOvn19JHT0y9AdxQ9p56wQe" width="345" height="230" data-dominant-color="545453"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1061×708 5.72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7ffed6a583eef52cc486e566aada3f54cd96e4b7.png" data-download-href="/uploads/short-url/igiCUDfsU2vPfwJLKXRlz4N34wL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7ffed6a583eef52cc486e566aada3f54cd96e4b7.png" alt="image" data-base62-sha1="igiCUDfsU2vPfwJLKXRlz4N34wL" width="345" height="233" data-dominant-color="575756"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">985×666 4.06 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6e058ec3cc73159ffe005c0c284ee066d6c5909.png" data-download-href="/uploads/short-url/nOfVauIBQQVvpULmOcGpplWULyh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6e058ec3cc73159ffe005c0c284ee066d6c5909_2_345x135.png" alt="image" data-base62-sha1="nOfVauIBQQVvpULmOcGpplWULyh" width="345" height="135" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6e058ec3cc73159ffe005c0c284ee066d6c5909_2_345x135.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6e058ec3cc73159ffe005c0c284ee066d6c5909_2_517x202.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6e058ec3cc73159ffe005c0c284ee066d6c5909_2_690x270.png 2x" data-dominant-color="686767"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×283 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3224750ac8ccd9d8ddea5a45c212a4f833060fa.jpeg" data-download-href="/uploads/short-url/wpjPi8ETCZEYUnpzDKlYYKN4fzk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3224750ac8ccd9d8ddea5a45c212a4f833060fa_2_345x151.jpeg" alt="image" data-base62-sha1="wpjPi8ETCZEYUnpzDKlYYKN4fzk" width="345" height="151" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3224750ac8ccd9d8ddea5a45c212a4f833060fa_2_345x151.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3224750ac8ccd9d8ddea5a45c212a4f833060fa_2_517x226.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3224750ac8ccd9d8ddea5a45c212a4f833060fa_2_690x302.jpeg 2x" data-dominant-color="4E4B49"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">719×316 63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88a3c6ec4a9ec1099ea46f9f4ba75626ba507780.png" data-download-href="/uploads/short-url/juLPfKnQ7Tjz4aGRLNiJGkbvngc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a3c6ec4a9ec1099ea46f9f4ba75626ba507780_2_302x250.png" alt="image" data-base62-sha1="juLPfKnQ7Tjz4aGRLNiJGkbvngc" width="302" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a3c6ec4a9ec1099ea46f9f4ba75626ba507780_2_302x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a3c6ec4a9ec1099ea46f9f4ba75626ba507780_2_453x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88a3c6ec4a9ec1099ea46f9f4ba75626ba507780_2_604x500.png 2x" data-dominant-color="565350"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×596 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd545af2b3081995ae28f5fef46543f659f737ea.png" data-download-href="/uploads/short-url/tiqBVCQIbr9klOGiXVdgD2OpRWO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd545af2b3081995ae28f5fef46543f659f737ea_2_345x208.png" alt="image" data-base62-sha1="tiqBVCQIbr9klOGiXVdgD2OpRWO" width="345" height="208" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd545af2b3081995ae28f5fef46543f659f737ea_2_345x208.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd545af2b3081995ae28f5fef46543f659f737ea_2_517x312.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd545af2b3081995ae28f5fef46543f659f737ea_2_690x416.png 2x" data-dominant-color="565453"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×435 38.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The yellow contour is from the FDA approved software STL, and the red contour is from 3D slicer STL</p>
<p>I am not a technical person but from the above image, we can see that there is an approximately 1-pixel difference between the two contours or we can say the contours are shifting from each other.</p>
<p>Here are the properties for the two different tested STL(s):</p>
<p><strong>FDA approved software STL properties</strong>:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/778b5c8fbb6018bbf61461a073cda6a20d145a2f.png" alt="image" data-base62-sha1="h3xoMHtSSNpZWRcHBwrXV4XQOWb" width="446" height="470"></p>
<p><strong>Slicer STL properties:</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f4b5db709564ffeffa96aaf36f68b9cb8cc8ba7.png" alt="image" data-base62-sha1="mJbo6OKF9Xc1emZgHKRUPDia4g7" width="215" height="235"></p>
<p><strong>STL ‘Conversion setting’ of the FDA approved software:</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a77b4637af717fcb138eddb9b27f9801691f7758.png" alt="image" data-base62-sha1="nTBQNc0KujRjE4iCC7zmR5R0RU4" width="311" height="221"></p>
<p>Based on the above geometry images, the bounding box and volume geometry estimation appear to be approximately the same.</p>
<p>So how can we have the same STL output as the FDA approved software so that slicer can fit in our protocol.</p>
<p>I’ve used slicer version 5.4.0 and also verified in the 5.6.1 &amp; 5.7.0 versions.<br>
Dataset link: <a href="https://drive.google.com/file/d/1a5qy3DUe80K30OhOBgnvS3CN-fBDfmnW/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">dataset.zip - Google Drive</a></p>

---

## Post #2 by @mau_igna_06 (2024-03-05 21:22 UTC)

<p>I would suggest to try exploring:</p>
<ul>
<li>margin tool from dynamic modeler module with a 3D model of the skull and a small positive value</li>
<li>using a very small up-scaling transform on the Transforms module</li>
<li>segment editor effect ‘margin’ inside segment editor module with your skull sementation and then cover to a model and check if you can get the overlay you want</li>
</ul>
<p>Last option is less likely to be your solution because it will change triangle count from your original segmentation</p>
<p>HIH</p>

---

## Post #3 by @pieper (2024-03-05 21:50 UTC)

<p>Thanks for reporting - are you able to share the STL files from both systems too?</p>
<p>It’s possible that the two systems use different algorithms or different interpretations of the parameters and care must be taken to make sure they provide results that are consistent with your needs.</p>
<p>One suggestion would be to scan a phantom with known dimensions and confirm what the accuracy of any particular method will be.  As <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> points out, there may be several ways of approximating the surface.  It may also be important to consider the CT scan protocol and reconstruction options as they may influence the estimation of the surface.</p>
<p>Also, these CT pixels are about .5 mm so the differences appear in most cases to be about .1 or .2 mm or less.  It would be interesting to hear your thoughts on the accuracy you need to achieve.</p>
<p>Also note the <a href="https://github.com/Slicer/Slicer/blob/main/License.txt#L147-L156">disclaimer</a> that while the 3D Slicer community strives for accuracy, it is not an FDA approved application and you need to use consistent with the laws and any institutional policies that govern your work.</p>

---

## Post #4 by @mikebind (2024-03-05 22:30 UTC)

<p>The red contour, from Slicer, looks more aggressively smoothed than the yellow contour, and that may be the main difference between them.  You might explore reducing the smoothing that Slicer applies when converting from binary labelmap representation (the direct result of the threshold) to the closed surface representation (what is shown in the 3D view, and what is created as the exported surface model representation).  You can change this smoothing factor by clicking on the dropdown on the “Show 3D” button in segment editor, and then changing the slider value between 0 and 1 (default is 0.5, and 0 means no smoothing).  More conversion settings (such as a decimation factor) are accessible in the Segmentations module, if you click the “Update” button next to the “Closed Surface” line in the “Representations” section, and then click the ‘Binary labelmap → Closed surface’ path in the window that pops up.</p>
<p>If you can load your FDA STL into Slicer, you can see if you can get a better match by iteratively changing the Smoothing factor on the Slicer segmentation and directly comparing.  To get some of the sharp features visible in the FDA STL, you may need to turn off smoothing entirely.  I would also suggest considering what representation you feel is most faithful to the surgical reality.  Does the skull have small sharp features more like the yellow line? I would also second <a class="mention" href="/u/pieper">@pieper</a> 's suggestion to consider what level of accuracy you expect from an image with a voxel resolution of 0.5 mm.</p>

---

## Post #5 by @lassoan (2024-03-06 16:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="34723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Also, these CT pixels are about .5 mm so the differences appear in most cases to be about .1 or .2 mm or less. It would be interesting to hear your thoughts on the accuracy you need to achieve.</p>
</blockquote>
</aside>
<p>Yes, the the segmentation results look about the same to me, with the difference being smaller than a single voxel.</p>
<p>See intensity profile along a line orthogonal to the bone surface. The width of the transition zone from soft tissue to bone is about 2mm. It would be hard to tell where is the exact boundary: at the peak intensity, where the peak starts, at half maximum, …? Each definition could be valid and the difference between them can be up to a millimeter.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d508b7aa76c1445d8287fa016f98f460d4f72b57.jpeg" data-download-href="/uploads/short-url/uoAnrYnQiK4UIjpToIRGSMyV4Pl.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d508b7aa76c1445d8287fa016f98f460d4f72b57_2_690x205.jpeg" alt="image" data-base62-sha1="uoAnrYnQiK4UIjpToIRGSMyV4Pl" width="690" height="205" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d508b7aa76c1445d8287fa016f98f460d4f72b57_2_690x205.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d508b7aa76c1445d8287fa016f98f460d4f72b57_2_1035x307.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d508b7aa76c1445d8287fa016f98f460d4f72b57_2_1380x410.jpeg 2x" data-dominant-color="9E9E9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×571 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/vikas26">@vikas26</a> What is the accuracy requirement for your clinical application?</p>
<aside class="quote no-group" data-username="mikebind" data-post="4" data-topic="34723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>More conversion settings (such as a decimation factor) are accessible in the Segmentations module, if you click the “Update” button next to the “Closed Surface” line in the “Representations” section, and then click the ‘Binary labelmap → Closed surface’ path in the window that pops up.</p>
</blockquote>
</aside>
<p>I would specifically recommend to try the surfacenet smoothing filter:</p>
<ul>
<li>Conversion method: 1 (vtkSurfaceNets3D)</li>
<li>SurfaceNets smoothing: 1 (smoothing done in surfacenets filter)</li>
</ul>

---

## Post #6 by @lassoan (2024-03-08 14:35 UTC)

<p><a class="mention" href="/u/vikas26">@vikas26</a> I’ve analyzed your report very thoroughly and could reproduce a scaling inaccuracy of up to about 0.7% when not using “surface nets” smoothing (<code>Conversion method: 0</code> or <code>SurfaceNets smoothing: 0</code>). This error typically means subpixel size, but we take any unnecessary processing inaccuracies very seriously and do everything to avoid them.</p>
<p>I’ve submitted a detailed report to VTK developers, who maintain the affected smoothing filter (vtkWindowedSincPolyDataFilter). Hopefully we’ll hear from them soon:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676/8?u=lassoan">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676/8?u=lassoan" target="_blank" rel="noopener" title="02:25PM - 08 March 2024">VTK – 8 Mar 24</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:652/499;"><img src="https://discourse.vtk.org/uploads/default/original/2X/7/73f5037cd6ec13d4a7caab32d34234e86ef486d8.jpeg" class="thumbnail" width="652" height="499"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/slight-offset-in-vtkwindowedsincpolydatafilter-if-normalization-is-enabled/7676/8?u=lassoan" target="_blank" rel="noopener">Slight offset in vtkWindowedSincPolyDataFilter if normalization is enabled</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Support</span>
        </span>
      </span>
  </div>
</div>

  <p>This issue has come up again. This time, it is very simple and clear case and it is hard to justify the error.  Example use case: We have a head CT, we create a binary image using thresholding to segment the bone, convert to polydata - everything...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Until then, you can use <code>Conversion method: 1</code> and <code>SurfaceNets smoothing: 1</code> to avoid this processing inaccuracy.</p>

---

## Post #7 by @lassoan (2024-03-13 01:01 UTC)

<p>We have found that by using a different window function in the low-pass filter in vtkWindowedSincPolyDataFilter in VTK, we can avoid this slight change in the smoothed surface. The change has been integrated into VTK library and Slicer will be updated within a few days to use this improved filtering.</p>

---

## Post #8 by @vikas26 (2024-04-01 10:22 UTC)

<p>Thank you mau_igna_06, pieper, mikebind, lassoan for the invaluable solution provided.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="34723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is the accuracy requirement for your clinical application?</p>
</blockquote>
</aside>
<ul>
<li>We aim for a stringent standard, adhering closely to FDA-approved software guidelines, with an error rate maintained below 0.01%.</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="34723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>. The change has been integrated into VTK library and Slicer will be updated within a few days to use this improved filtering.</p>
</blockquote>
</aside>
<p>We extend our heartfelt appreciation to <a class="mention" href="/u/lassoan">@lassoan</a> for the diligent integration of improvements into the VTK library. Following our thorough testing, we are pleased to report that the previously noted contour shift appears to be resolved satisfactorily.</p>
<p>However, we wish to address another concern regarding the presence of step-like structures on the object’s surface.</p>
<ul>
<li>Red represents the slicer with Zero smoothing.</li>
<li>Green represents the FDA approved software without any smoothing.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9372d33fc1d121da4dbb79c6fd038a7a69ef024.jpeg" data-download-href="/uploads/short-url/xh7sSQiXwmezREqxI7AiXl36nvC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9372d33fc1d121da4dbb79c6fd038a7a69ef024_2_411x500.jpeg" alt="image" data-base62-sha1="xh7sSQiXwmezREqxI7AiXl36nvC" width="411" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9372d33fc1d121da4dbb79c6fd038a7a69ef024_2_411x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9372d33fc1d121da4dbb79c6fd038a7a69ef024.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9372d33fc1d121da4dbb79c6fd038a7a69ef024.jpeg 2x" data-dominant-color="6F6818"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">596×725 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Upon activating the wireframe representation, it becomes apparent that the FDA-approved STL selectively stitches only the sharp edges, thereby mitigating the step-like structures, as illustrated in the accompanying image.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbab92de4b920a7b4e2a52b46d83b77d691eeee5.jpeg" data-download-href="/uploads/short-url/qMcSGb6g5bgyYof7kisqOOYoAp7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbab92de4b920a7b4e2a52b46d83b77d691eeee5_2_633x500.jpeg" alt="image" data-base62-sha1="qMcSGb6g5bgyYof7kisqOOYoAp7" width="633" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbab92de4b920a7b4e2a52b46d83b77d691eeee5_2_633x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbab92de4b920a7b4e2a52b46d83b77d691eeee5_2_949x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbab92de4b920a7b4e2a52b46d83b77d691eeee5.jpeg 2x" data-dominant-color="56551D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1117×881 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your attention to this matter. I eagerly await your response.</p>

---

## Post #9 by @lassoan (2024-04-01 20:29 UTC)

<aside class="quote no-group" data-username="vikas26" data-post="8" data-topic="34723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/3ab097/48.png" class="avatar"> vikas26:</div>
<blockquote>
<p>We aim for a stringent standard, adhering closely to FDA-approved software guidelines, with an error rate maintained below 0.01%</p>
</blockquote>
</aside>
<p>0.01% error is not even remotely feasible in anything related to clinical 3D medical imaging.</p>
<p>For example, if you work with images of 0.5mm voxel size then you could not possibly reach less than 1% error on a 50mm distance measurement.</p>
<p>If you work with any automated clinical image processing algorithm then the success rate is acceptable if it is about 1-5% (of course you need to make sure that you can detect error and make corrections, so this error will not be the final success rate of the procedure).</p>
<p>If you 3D print a part then you would have trouble going below 0.1mm error, which means 0.2% error for a 50mm part size.</p>
<p>We could say that a single basic software processing step (e.g., store a mesh in file and read it back) should work with less than 0.01% error, which should be very easy to satisfy as floating-point computations can be performed with magnitudes less error.</p>
<aside class="quote no-group" data-username="vikas26" data-post="8" data-topic="34723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/3ab097/48.png" class="avatar"> vikas26:</div>
<blockquote>
<ul>
<li>Red represents the slicer with Zero smoothing.</li>
<li>Green represents the FDA approved software without any smoothing.</li>
</ul>
</blockquote>
</aside>
<p>In Slicer, disabling smoothing means that the original continuous signal is not reconstructed at all, you just display the discrete sampling points. You must enable smoothing to get the correct surface. It is not some user preference that some people like it smoothed others prefer without smoothing, but if you don’t smooth then you get incorrect results.</p>
<p>Probably the other software just does not let you disable smoothing (lowest smoothing setting still applies some smoothing). It is hard to even tell which software works better, maybe inspecting zoomed-in cross-sectional views could help. However, validation should be always done with a reasonable tolerance for clinical use (not  0.01% but more like 1%) and with that the two software should produce equivalent results.</p>

---

## Post #10 by @MJamal (2024-04-05 10:04 UTC)

<p>I was looking into this question and decided to give it a shot.</p>
<p>From what I’ve seen, it seems like 3D Slicer uses a method based on right angle triangles to create meshes, while the FDA software mentioned earlier might use a different method called tetrahedral meshing.</p>
<p>Do you think these different ways of calculating meshes could affect how smooth and accurate the final results are?</p>
<p>I think, since these software use different algorithms for meshing, it’s important to understand how this might affect the quality and accuracy of the meshes they produce.</p>
<p>I’m particularly interested in how the choice of meshing method might affect things like how smooth the surfaces are, how accurate the shapes are, and how fast the software can do its calculations.</p>
<p>If you have any insights or corrections on any of this, I’d really appreciate it. What is your opinion on this <a class="mention" href="/u/lassoan">@lassoan</a>?</p>

---

## Post #11 by @lassoan (2024-04-05 14:51 UTC)

<aside class="quote no-group" data-username="MJamal" data-post="10" data-topic="34723">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d26b3c/48.png" class="avatar"> MJamal:</div>
<blockquote>
<p>Do you think these different ways of calculating meshes could affect how smooth and accurate the final results are?</p>
</blockquote>
</aside>
<p>The used algorithm should not matter much, because the differences should be all smaller than a voxel and you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">choose the voxel size for your segmentation</a>.</p>

---
