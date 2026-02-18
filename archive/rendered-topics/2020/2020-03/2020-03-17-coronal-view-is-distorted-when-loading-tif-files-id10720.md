# Coronal view is distorted when loading .tif Files

**Topic ID**: 10720
**Date**: 2020-03-17
**URL**: https://discourse.slicer.org/t/coronal-view-is-distorted-when-loading-tif-files/10720

---

## Post #1 by @Stephan_R (2020-03-17 14:12 UTC)

<p>Operating system:Win10<br>
Slicer version:4.10.2<br>
Expected behavior: Normal View<br>
Actual behavior: Coronal View is distorted</p>
<p>Hello,<br>
I am new to evaluation of CT-Scans. When i import my tiff-files from a CT-scan to Slicer, the coronal view is distorted as shown in the picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fd0b074baff2ae6ba1be3946e54142da322e827.png" data-download-href="/uploads/short-url/2fUh9WjNHA91z1xCiTxDNzpgK47.png?dl=1" title="twisted" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd0b074baff2ae6ba1be3946e54142da322e827_2_641x500.png" alt="twisted" data-base62-sha1="2fUh9WjNHA91z1xCiTxDNzpgK47" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd0b074baff2ae6ba1be3946e54142da322e827_2_641x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd0b074baff2ae6ba1be3946e54142da322e827_2_961x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0fd0b074baff2ae6ba1be3946e54142da322e827_2_1282x1000.png 2x" data-dominant-color="91919A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">twisted</span><span class="informations">1382×1077 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure how to avoid this behavior.</p>
<p>Thank you in advance!</p>

---

## Post #2 by @pieper (2020-03-17 15:35 UTC)

<p>That appears to be a set of projection images, not a volume.  You need reconstruct, either with the scanner itself or with another program.</p>
<p><a href="https://www.openrtk.org/" class="onebox" target="_blank">https://www.openrtk.org/</a></p>

---
