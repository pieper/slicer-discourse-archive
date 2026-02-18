# DICOM browser does not show the count of images in a series

**Topic ID**: 33506
**Date**: 2023-12-23
**URL**: https://discourse.slicer.org/t/dicom-browser-does-not-show-the-count-of-images-in-a-series/33506

---

## Post #1 by @chir.set (2023-12-23 09:54 UTC)

<p>Hi,</p>
<p>I built Slicer 66a424d on Linux and recreated the DICOM database. The number of images in the series are not available in the DICOM browser.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/251f0defbd121b997f185f1edd544930df3c714e.png" alt="dicom_browser_no_count" data-base62-sha1="5iocpHS6L1MAjwULp7qhM3ek8nY" width="329" height="146"></p>
<p>Thanks for having a look.</p>

---

## Post #2 by @pieper (2023-12-23 18:25 UTC)

<p>It would help fi you could point to the most recent version where you know the counts are present for the same dataset.</p>

---

## Post #3 by @chir.set (2023-12-23 18:49 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="33506">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>the most recent version where you know the counts are present</p>
</blockquote>
</aside>
<p>The counts were available in eccb98c, that was my previous build. I agree it’s relatively old for a development process.</p>

---

## Post #4 by @rbumm (2023-12-23 22:56 UTC)

<p>3D Slicer 5.6.1 (the latest stable) shows the count in my installation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e015fda20e4f557051e28472f10558fd1a0db1cc.png" data-download-href="/uploads/short-url/vYm4eKCGMaO0ELVkqV9eH11Mkyg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e015fda20e4f557051e28472f10558fd1a0db1cc.png" alt="image" data-base62-sha1="vYm4eKCGMaO0ELVkqV9eH11Mkyg" width="690" height="60" data-dominant-color="95C2DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×112 2.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The data were imported from a SECTRA IDS-7 DICOM export.</p>

---
