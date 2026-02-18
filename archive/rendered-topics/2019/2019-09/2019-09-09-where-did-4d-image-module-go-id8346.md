# Where did 4D image module go?

**Topic ID**: 8346
**Date**: 2019-09-09
**URL**: https://discourse.slicer.org/t/where-did-4d-image-module-go/8346

---

## Post #1 by @KTakahiro1729 (2019-09-09 13:56 UTC)

<p><a href="https://www.slicer.org/wiki/Modules:FourDImage-Documentation-3.6" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Modules:FourDImage-Documentation-3.6</a></p>
<p>In the link above, I found that 3DSlicer has a module to load 4D images(xyz+time).<br>
However, I cannot find it in the latest Slicer(4.11.00, 20190219 daily build). Where did it go?</p>
<p>(I tried MulitvolumeImport but didn’t work for my DICOM data)</p>

---

## Post #2 by @pieper (2019-09-11 19:02 UTC)

<p>You can try the Sequences extension.  We are working to make that the core infrastructure for multidimensional data.  Let us know if it doesn’t work for your data.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/Sequences" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Extensions/Sequences</a></p>

---

## Post #3 by @KTakahiro1729 (2019-09-13 02:38 UTC)

<p>Thank you for your reply.<br>
The sequences extension worked completely fine (and removed other problems I was facing)</p>
<p>Is there any reason why the Sequences extension does not appear in the nightly builds? (I could only find them in the stable versions)</p>

---

## Post #4 by @Sam_Horvath (2019-09-13 13:42 UTC)

<p>We have had some instability in the preview builds over the past week.  The preview is constantly undergoing changes, and so is susceptible to daily build / etc errors.</p>

---
