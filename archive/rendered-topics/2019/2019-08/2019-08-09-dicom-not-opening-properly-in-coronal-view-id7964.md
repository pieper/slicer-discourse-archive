---
topic_id: 7964
title: "Dicom Not Opening Properly In Coronal View"
date: 2019-08-09
url: https://discourse.slicer.org/t/7964
---

# DICOM not opening properly in coronal view

**Topic ID**: 7964
**Date**: 2019-08-09
**URL**: https://discourse.slicer.org/t/dicom-not-opening-properly-in-coronal-view/7964

---

## Post #1 by @Ricardo (2019-08-09 14:06 UTC)

<p>Hi everybody.</p>
<p>While opening a DICOM folder, I can’t make Coronal view to be shown properly. Let me explain you:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a4117b4dfeea177199fb44bc16cd912bd3b735c.jpeg" data-download-href="/uploads/short-url/1sIezcFcLmVVB7zxMTYiiMWM2vO.jpeg?dl=1" title="Image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a4117b4dfeea177199fb44bc16cd912bd3b735c_2_690x134.jpeg" alt="Image1" data-base62-sha1="1sIezcFcLmVVB7zxMTYiiMWM2vO" width="690" height="134" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a4117b4dfeea177199fb44bc16cd912bd3b735c_2_690x134.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a4117b4dfeea177199fb44bc16cd912bd3b735c_2_1035x201.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a4117b4dfeea177199fb44bc16cd912bd3b735c_2_1380x268.jpeg 2x" data-dominant-color="D2DDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image1</span><span class="informations">1911×373 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the previous picture you can see the series I chose to open. When I try to load them, I get the following message:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba3fdcbe6b190d76b46c4bce684bcffc64559ad0.jpeg" alt="Image2" data-base62-sha1="qzDDimkzNmV0nawfBUoGfQFeblK" width="507" height="100"></p>
<p>In “advance mode” I get this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf9dfa7ff3280bff199df9a9ed7050db04d8ff23.jpeg" data-download-href="/uploads/short-url/tCFiPLFMDA4rzcLKhLHuyNM7Fuj.jpeg?dl=1" title="Image3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9dfa7ff3280bff199df9a9ed7050db04d8ff23_2_690x45.jpeg" alt="Image3" data-base62-sha1="tCFiPLFMDA4rzcLKhLHuyNM7Fuj" width="690" height="45" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9dfa7ff3280bff199df9a9ed7050db04d8ff23_2_690x45.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9dfa7ff3280bff199df9a9ed7050db04d8ff23_2_1035x67.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf9dfa7ff3280bff199df9a9ed7050db04d8ff23_2_1380x90.jpeg 2x" data-dominant-color="F1F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image3</span><span class="informations">1697×111 37.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>“apply regularization transform” is checked on DICOM settings:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d90d4de3a8fd871aa8532f712909105631b12402.jpeg" alt="Image5" data-base62-sha1="uY879izwf5OxUi1Su7vZsa5xcSS" width="662" height="294"></p>
<p>Now, when loading is finished, I get the right series for the Axial view, but not as so for Sagital and Coronal views. As you can see, the image quality is good for the Axial view, but really choppy for the other two, making it really hard for a decent segmentation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af6e474397e76772d19d67ddc101bbed974245ec.jpeg" data-download-href="/uploads/short-url/p1VPjvZH31brf9IkDHQOj1Wb4Nm.jpeg?dl=1" title="Image4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af6e474397e76772d19d67ddc101bbed974245ec_2_690x477.jpeg" alt="Image4" data-base62-sha1="p1VPjvZH31brf9IkDHQOj1Wb4Nm" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af6e474397e76772d19d67ddc101bbed974245ec_2_690x477.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af6e474397e76772d19d67ddc101bbed974245ec_2_1035x715.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af6e474397e76772d19d67ddc101bbed974245ec.jpeg 2x" data-dominant-color="5E5D69"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image4</span><span class="informations">1336×925 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After I manually pick the right series for each view, I get a stretched bar for the Coronal view. Quality image is now good for Axial and Sagital:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09ba04c9637e0f74d46528e3c78ae3a0d36ebea5.jpeg" data-download-href="/uploads/short-url/1o2Q6Ih8BtAIfRJuQpB1YAZfYi1.jpeg?dl=1" title="Image6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09ba04c9637e0f74d46528e3c78ae3a0d36ebea5_2_690x476.jpeg" alt="Image6" data-base62-sha1="1o2Q6Ih8BtAIfRJuQpB1YAZfYi1" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09ba04c9637e0f74d46528e3c78ae3a0d36ebea5_2_690x476.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09ba04c9637e0f74d46528e3c78ae3a0d36ebea5_2_1035x714.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09ba04c9637e0f74d46528e3c78ae3a0d36ebea5.jpeg 2x" data-dominant-color="52535E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image6</span><span class="informations">1338×924 92.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I solve this issue?</p>
<p>Regards,<br>
Ricardo</p>

---

## Post #2 by @pieper (2019-08-09 21:17 UTC)

<p>Hi Ricardo -</p>
<p>How were these coronal and sagittal views created?  It looks like they might have been resampled into the space of the MR (the sagittal is rotated), and as reported in the DICOM browser it seems there is an inconsistency in the geometry information.</p>
<p>Also, I’ve noticed a trend latestly that some software will take an original CT, perhaps with 1mm or smaller isotropic spacing and generate three series with good in-plane resolution but thick out-of-plane spacing.  This kind of makes sense if you are looking with a slice-oriented viewer but it’s not good for volumetric purposes, like segmentation.  If you have any control over the scanning process you should request a single high-res CT series.</p>

---

## Post #3 by @Ricardo (2019-08-13 08:59 UTC)

<p>Hi Steve,</p>
<p>unfortunately, I have zero influence over the scanning process, at least for this particular case.</p>
<p>What I find odd, is the fact that they were able to get a 3d model with decent resolution and detail, as you can see in the picture below (this 3d image is shown by the inbuilt software in the DVD):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc54910c5f5284ca8c6ea4c603b13721b7dd9727.jpeg" data-download-href="/uploads/short-url/qS2WKkZVIJMaJwlCEFXcRq98cUn.jpeg?dl=1" title="Capturar" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc54910c5f5284ca8c6ea4c603b13721b7dd9727_2_690x497.jpeg" alt="Capturar" data-base62-sha1="qS2WKkZVIJMaJwlCEFXcRq98cUn" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bc54910c5f5284ca8c6ea4c603b13721b7dd9727_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc54910c5f5284ca8c6ea4c603b13721b7dd9727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc54910c5f5284ca8c6ea4c603b13721b7dd9727.jpeg 2x" data-dominant-color="3B3028"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capturar</span><span class="informations">817×589 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Form your words, I can assume there’s not much to do with the current data I have (in terms of fixing the Coronary view), am I right?</p>
<p>Thank you for helping,<br>
Ricardo.</p>

---

## Post #4 by @pieper (2019-08-13 13:40 UTC)

<aside class="quote no-group" data-username="Ricardo" data-post="3" data-topic="7964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a6a055/48.png" class="avatar"> Ricardo:</div>
<blockquote>
<p>Form your words, I can assume there’s not much to do with the current data I have (in terms of fixing the Coronary view), am I right?</p>
</blockquote>
</aside>
<p>It’s a little hard to tell, since you have several series in your database, but did you try loading number 3?  The numbering is not definitive, but a common convention is that single digit series numbers are data produced by the scanner and numbers in the hundreds or thousands are derived data.  Number 3 might be the full res volume and Slicer can make the sagittal and coronal slices on the fly (instead of using the low-res precomputed ones).</p>

---

## Post #5 by @lassoan (2019-08-13 15:39 UTC)

<aside class="quote no-group" data-username="Ricardo" data-post="3" data-topic="7964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a6a055/48.png" class="avatar"> Ricardo:</div>
<blockquote>
<p>What I find odd, is the fact that they were able to get a 3d model with decent resolution and detail</p>
</blockquote>
</aside>
<p>The image you show above is displayed using volume rendering. Have you tried visualizing your series using volume rendering?</p>
<p>Can you rotate this volume around using the software and data on the DVD? If not, then it may be just a screenshot - based on data that might have not written to your DVD.</p>
<p>You may still have a chance to get the full-resolution image from the CT console or PACS by writing a new DVD with export options that preserve the original 3D image better.</p>

---

## Post #6 by @Ricardo (2019-08-19 10:17 UTC)

<p>I’ve tried loading all series, but the best Coronary view I can get is the one showed in the 4th picture in the first message.</p>
<p>Will have to do for this one.</p>

---

## Post #7 by @Ricardo (2019-08-19 10:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="7964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you tried visualizing your series using volume rendering?</p>
</blockquote>
</aside>
<p>Yes, the best I can get is showed in the next picture (the “noise” around the spine is the minimum possible using just the “Shift” bar (for preset CT-AA2), so spine bone doesn’t get removed from model. Also, this is without any kind of work, just straight volume rendering):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14d1364a6ca973c9362d9525a86d34ee1b76d203.jpeg" data-download-href="/uploads/short-url/2Y9MCuP60MvbsuhrJkOjI51On5h.jpeg?dl=1" title="Captura" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14d1364a6ca973c9362d9525a86d34ee1b76d203_2_538x500.jpeg" alt="Captura" data-base62-sha1="2Y9MCuP60MvbsuhrJkOjI51On5h" width="538" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14d1364a6ca973c9362d9525a86d34ee1b76d203_2_538x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/14d1364a6ca973c9362d9525a86d34ee1b76d203_2_807x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14d1364a6ca973c9362d9525a86d34ee1b76d203.jpeg 2x" data-dominant-color="ABA2A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura</span><span class="informations">872×809 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="7964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you rotate this volume around using the software and data on the DVD? If not, then it may be just a screenshot - based on data that might have not written to your DVD.</p>
</blockquote>
</aside>
<p>I can. It’s a 3D rendering of 19 pictures. Here it is from another angle (close to the one I got with Volume Rendering in Slicer):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ced1d05ecc8c64539d882edbfb6f9bbd7948dc6.jpeg" data-download-href="/uploads/short-url/dg3WiEFNmq2XOcPIcfKMOXeFF9Y.jpeg?dl=1" title="Captura" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ced1d05ecc8c64539d882edbfb6f9bbd7948dc6_2_548x500.jpeg" alt="Captura" data-base62-sha1="dg3WiEFNmq2XOcPIcfKMOXeFF9Y" width="548" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ced1d05ecc8c64539d882edbfb6f9bbd7948dc6_2_548x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ced1d05ecc8c64539d882edbfb6f9bbd7948dc6_2_822x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ced1d05ecc8c64539d882edbfb6f9bbd7948dc6.jpeg 2x" data-dominant-color="423830"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura</span><span class="informations">901×821 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="7964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may still have a chance to get the full-resolution image from the CT console or PACS by writing a new DVD with export options that preserve the original 3D image better.</p>
</blockquote>
</aside>
<p>And I guess that’s the best option I have right now. I’ll try to reach the medical unit and try to get a new set of images. Any advice on what to explain that went wrong?</p>
<p>Thank you so much.</p>

---

## Post #8 by @lassoan (2019-08-21 16:44 UTC)

<aside class="quote no-group" data-username="Ricardo" data-post="7" data-topic="7964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a6a055/48.png" class="avatar"> Ricardo:</div>
<blockquote>
<p>I can. It’s a 3D rendering of 19 pictures.</p>
</blockquote>
</aside>
<p>I guess you mean that it is a pre-recorded video (so you cannot rotate the model arbitrarily, just replay the video of a rotation). If this is the case then indeed you do not have the full-resolution image on the DVD.</p>
<aside class="quote no-group" data-username="Ricardo" data-post="7" data-topic="7964">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/a6a055/48.png" class="avatar"> Ricardo:</div>
<blockquote>
<p>Any advice on what to explain that went wrong?</p>
</blockquote>
</aside>
<p>Each PACS and image viewers are different. If you can provide the list of export options then we may give advice about which one sounds the most appropriate.</p>

---
