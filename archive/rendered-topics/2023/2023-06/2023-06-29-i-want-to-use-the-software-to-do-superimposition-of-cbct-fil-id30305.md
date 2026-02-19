---
topic_id: 30305
title: "I Want To Use The Software To Do Superimposition Of Cbct Fil"
date: 2023-06-29
url: https://discourse.slicer.org/t/30305
---

# I want to use the software to do superimposition of CBCT files. but when I insert my CBCT in nrrd format, it apear only black and white black not the whole image. as in the picture i attached. what should I do?

**Topic ID**: 30305
**Date**: 2023-06-29
**URL**: https://discourse.slicer.org/t/i-want-to-use-the-software-to-do-superimposition-of-cbct-files-but-when-i-insert-my-cbct-in-nrrd-format-it-apear-only-black-and-white-black-not-the-whole-image-as-in-the-picture-i-attached-what-should-i-do/30305

---

## Post #1 by @YOU_DDS (2023-06-29 16:16 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f163b6261666055578b2b25773c634a450549976.png" data-download-href="/uploads/short-url/yrqHtSBiJWFm8z70F40tqvcNfEO.png?dl=1" title="스크린샷(12)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f163b6261666055578b2b25773c634a450549976_2_690x439.png" alt="스크린샷(12)" data-base62-sha1="yrqHtSBiJWFm8z70F40tqvcNfEO" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f163b6261666055578b2b25773c634a450549976_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f163b6261666055578b2b25773c634a450549976_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f163b6261666055578b2b25773c634a450549976_2_1380x878.png 2x" data-dominant-color="2E2F3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷(12)</span><span class="informations">1451×925 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @gcsharp (2023-06-29 16:58 UTC)

<p>It may be that the image was converted incorrectly, or it could be a display issue.</p>
<p>In the Volumes module, you can look at “Scalar Type” and “Scalar Range.”  You can also look at the histogram.  Further, the data probe will show you the intensity at the position of the cursor.  Do these values make sense for your image?</p>

---

## Post #3 by @YOU_DDS (2023-08-01 00:40 UTC)

<p>Thank for your help!!</p>

---
