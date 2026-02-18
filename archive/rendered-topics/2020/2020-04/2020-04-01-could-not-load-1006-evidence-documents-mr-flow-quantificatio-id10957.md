# Could not load: 1006: Evidence Documents MR Flow Quantification as a Scalar Volume

**Topic ID**: 10957
**Date**: 2020-04-01
**URL**: https://discourse.slicer.org/t/could-not-load-1006-evidence-documents-mr-flow-quantification-as-a-scalar-volume/10957

---

## Post #1 by @Andre_Mourato (2020-04-01 13:33 UTC)

<p>Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hey, im trying to analise results of an 4D MRI but when i try to load some of the documents this messagem appears.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4f6623c898c02ae7d59b851b52b2431c638b905.png" alt="image" data-base62-sha1="nxkb9r0jke5PakNQsbNW118esyF" width="509" height="103"></p>
<p>and if i try to load anyway this appears</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13bc49fc34dca22316ae550b6c8ebca0cd745380.png" alt="image" data-base62-sha1="2OAtIjyR1QtefraExZQjwkqLR28" width="482" height="107"></p>
<p>I also tryed to examine the particular file i wanted to open and this is what the examination says.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90eb72ae2229a30408aa0d5438555eeb18e44e33.png" data-download-href="/uploads/short-url/kG1crsKWzvpnPGZ893lNZFAimeD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90eb72ae2229a30408aa0d5438555eeb18e44e33.png" alt="image" data-base62-sha1="kG1crsKWzvpnPGZ893lNZFAimeD" width="690" height="72" data-dominant-color="F5F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×143 7.28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In one of my trys to make this work i install the SlicerHeart extension and this message started to appear.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4abc8f83d311d372b13a8b0595b0cb195181e2f.png" data-download-href="/uploads/short-url/ulngPzBhDuuPPj2FpAGpwuEaKTR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4abc8f83d311d372b13a8b0595b0cb195181e2f.png" alt="image" data-base62-sha1="ulngPzBhDuuPPj2FpAGpwuEaKTR" width="689" height="42" data-dominant-color="FFF5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1344×83 3.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i wonder if this problem is related with that strange caracter that appears in metadata<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bebadd767686c439c752921f71d634c54c07867.png" data-download-href="/uploads/short-url/hGfFtp4W73IMCQ8jb4Oo9jNKcbd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bebadd767686c439c752921f71d634c54c07867.png" alt="image" data-base62-sha1="hGfFtp4W73IMCQ8jb4Oo9jNKcbd" width="690" height="138" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1319×264 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I really don’t know how to solve this and i would really appreciate some help. Thanks!</p>
<p>Best regards,</p>
<p>André Mourato</p>

---

## Post #2 by @lassoan (2020-04-01 14:18 UTC)

<p>“Reference image does not contain geometry information” message means that the image is just a screenshot or screen capture video - there is no information about image scale or position. The image is probably rejected in the end because it is a color image with burnt-in annotations.</p>
<p>You can probably bypass DICOM checks by drag-and-dropping a single file of the series to the application window, check “Options”, and uncheck “Single file” option.</p>
<p>What would you like to do with these images in Slicer?</p>

---

## Post #3 by @Andre_Mourato (2020-04-01 16:21 UTC)

<p>Hey again, thanks for the tip but i’m afraid it didn’t worked. After unchecking “Single File” and press “OK” a box appears and dissappears vey quickly but nothing else happens.</p>
<p>Im trying to develop a numeral model to acess the hemodynamics inside the ascending aorta. In this case i wanted to consult the initial conditions of the flow.</p>

---

## Post #4 by @lassoan (2020-04-01 19:19 UTC)

<p>Probably the flow information is stored in private tags and all that is stored in standard DICOM fields is a single screenshot. If you can share an anonymized sample data set then we can give more specific details.</p>

---

## Post #5 by @Andre_Mourato (2020-04-02 14:35 UTC)

<p>Sorry i’m just an engineering student and i really don’t know how anonymate my sample but i will try to do that and come ask for help again.</p>
<p>Anyway, thank you so much fot the help.</p>

---

## Post #6 by @lassoan (2020-04-04 20:16 UTC)

<p><a href="https://mircwiki.rsna.org/index.php?title=The_CTP_DICOM_Anonymizer">CTP Anonymizer</a> is a quite good tool. You can usually get good results (patient information is removed but information that is needed to interpret the data set is preserved) with default settings.</p>

---
