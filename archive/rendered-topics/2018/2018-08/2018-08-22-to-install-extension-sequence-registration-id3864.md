# To install extension "Sequence registration"

**Topic ID**: 3864
**Date**: 2018-08-22
**URL**: https://discourse.slicer.org/t/to-install-extension-sequence-registration/3864

---

## Post #1 by @Kyu_Sung_Choi (2018-08-22 01:47 UTC)

<p>Dear Dr. <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I want to use the extension “Sequence registration” to register 4D DSC images.<br>
<strong>However, buttons on the panel look different from the manual</strong> (<a href="https://github.com/moselhy/SlicerSequenceRegistration" rel="noopener nofollow ugc">https://github.com/moselhy/SlicerSequenceRegistration</a>).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c234e08773af4e0f1b8acbe5e6c5dd5aee06eac1.jpeg" data-download-href="/uploads/short-url/rI1UUfOwjTFd0qWQ2CAPv7BrLln.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c234e08773af4e0f1b8acbe5e6c5dd5aee06eac1_2_690x359.jpeg" alt="image" data-base62-sha1="rI1UUfOwjTFd0qWQ2CAPv7BrLln" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c234e08773af4e0f1b8acbe5e6c5dd5aee06eac1_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c234e08773af4e0f1b8acbe5e6c5dd5aee06eac1_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c234e08773af4e0f1b8acbe5e6c5dd5aee06eac1_2_1380x718.jpeg 2x" data-dominant-color="8A8A92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1787×932 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here’s mine.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce621c504c19a8813a04278f33d9e6abecf0afc8.png" data-download-href="/uploads/short-url/trKyIgOOUcGyEMGAcffRMewqH8Y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce621c504c19a8813a04278f33d9e6abecf0afc8_2_690x379.png" alt="image" data-base62-sha1="trKyIgOOUcGyEMGAcffRMewqH8Y" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce621c504c19a8813a04278f33d9e6abecf0afc8_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce621c504c19a8813a04278f33d9e6abecf0afc8_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce621c504c19a8813a04278f33d9e6abecf0afc8_2_1380x758.png 2x" data-dominant-color="77767D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1850×1017 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Moreover, Input volume sequence seems to be not activated.</strong><br>
My Slicer is Slicer-4.9.0-2018-08-20-linux-amd64 version (latest nightly build),and Stable release (Slicer-4.8.1) shows also the same screen.<br>
<em>How can I fix it?</em><br>
Thank you in advance!</p>
<p>BR,<br>
Kyu Sung</p>

---

## Post #2 by @lassoan (2018-08-22 12:23 UTC)

<aside class="quote no-group" data-username="Kyu_Sung_Choi" data-post="1" data-topic="3864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b77776/48.png" class="avatar"> Kyu_Sung_Choi:</div>
<blockquote>
<p>However, buttons on the panel look different from the manual</p>
</blockquote>
</aside>
<p>We continuously improve the module, but we don’t always update illustrative screenshots.</p>
<aside class="quote no-group" data-username="Kyu_Sung_Choi" data-post="1" data-topic="3864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/b77776/48.png" class="avatar"> Kyu_Sung_Choi:</div>
<blockquote>
<p>Moreover, Input volume sequence seems to be not activated.</p>
</blockquote>
</aside>
<p>You need to load volume in a Sequence node. You may have loaded your 4D data set as MultiVolume node. To convert a Multivolume node, save it to a file and when you load it again, choose “Volume sequence” in the “Add data” dialog.</p>

---
