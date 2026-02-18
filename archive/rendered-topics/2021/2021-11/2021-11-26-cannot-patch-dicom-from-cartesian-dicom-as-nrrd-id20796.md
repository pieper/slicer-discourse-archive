# Cannot patch dicom from cartesian dicom as NRRD

**Topic ID**: 20796
**Date**: 2021-11-26
**URL**: https://discourse.slicer.org/t/cannot-patch-dicom-from-cartesian-dicom-as-nrrd/20796

---

## Post #1 by @Rodrigo_Visconti (2021-11-26 03:23 UTC)

<p>I used to load 3d cartesian files by patching into nrrd in dicom patch module slicerheart. When i try now the module doesn’t create any file. How to fix it?</p>

---

## Post #2 by @lassoan (2021-11-26 03:52 UTC)

<p>I’ve just tested “Philips 4D US DICOM Patcher” module on Windows with the latest Slicer Preview Release and it still works well. Both the patched DICOM and the exported NRRD files can be read correctly.</p>
<p>Make sure you use the “Philips 4D US DICOM Patcher” module in SlicerHeart and not the general-purpose DICOM patcher.</p>
<p>If you still have problems then please provide more information (OS, Slicer version, exact steps that you do, application log, etc.).</p>

---

## Post #3 by @Rodrigo_Visconti (2021-11-26 03:56 UTC)

<p>I’m using the windows 8 with latest version from 4d Phillips dicom patcher using only export as only nrrd export.</p>

---

## Post #4 by @Rodrigo_Visconti (2021-11-26 03:57 UTC)

<p>Doesn’t give any log but the folder stays empty</p>

---

## Post #5 by @lassoan (2021-11-26 04:08 UTC)

<p>Have you converted your images to Cartesian DICOM in QLab? See instructions <a href="https://github.com/SlicerHeart/SlicerHeart/blob/4b9ad82d8e58c8445173f9b72046eed124e13028/Docs/ImageImportExport.md#import-philips-4d-cardiac-images">here</a>.</p>
<p>If you did, then please test using this data set: <a href="https://github.com/SlicerHeart/SlicerHeart/releases/download/TestingData/PhilipsCartesianElephantUnpatched.dcm">https://github.com/SlicerHeart/SlicerHeart/releases/download/TestingData/PhilipsCartesianElephantUnpatched.dcm</a></p>

---

## Post #6 by @Rodrigo_Visconti (2021-11-26 04:13 UTC)

<p>Same thing<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efeca270a7071da6c591a2dc5af1739045274b60.jpeg" data-download-href="/uploads/short-url/yet6mkkWOZRgpumpPbAkkjWsj2U.jpeg?dl=1" title="20211126_011225" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efeca270a7071da6c591a2dc5af1739045274b60_2_375x500.jpeg" alt="20211126_011225" data-base62-sha1="yet6mkkWOZRgpumpPbAkkjWsj2U" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efeca270a7071da6c591a2dc5af1739045274b60_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efeca270a7071da6c591a2dc5af1739045274b60_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efeca270a7071da6c591a2dc5af1739045274b60_2_750x1000.jpeg 2x" data-dominant-color="747171"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211126_011225</span><span class="informations">1920×2560 770 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de5cd2de14cf9cb91a3af80c241775febd83b631.jpeg" data-download-href="/uploads/short-url/vJ6S583P6dz3eN1YCwzThBkRVPX.jpeg?dl=1" title="20211126_011210" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de5cd2de14cf9cb91a3af80c241775febd83b631_2_375x500.jpeg" alt="20211126_011210" data-base62-sha1="vJ6S583P6dz3eN1YCwzThBkRVPX" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de5cd2de14cf9cb91a3af80c241775febd83b631_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de5cd2de14cf9cb91a3af80c241775febd83b631_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de5cd2de14cf9cb91a3af80c241775febd83b631_2_750x1000.jpeg 2x" data-dominant-color="7D7A7A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211126_011210</span><span class="informations">3468×4624 2.04 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Rodrigo_Visconti (2021-11-26 04:26 UTC)

<p>In 4.10 version appears this code<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/596c672c8525249f50058717953b24bcdacdcfa7.jpeg" data-download-href="/uploads/short-url/cL4KkwJKCM2GMYxR2P7kkJd5KJ1.jpeg?dl=1" title="20211126_012516" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/596c672c8525249f50058717953b24bcdacdcfa7_2_375x500.jpeg" alt="20211126_012516" data-base62-sha1="cL4KkwJKCM2GMYxR2P7kkJd5KJ1" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/596c672c8525249f50058717953b24bcdacdcfa7_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/596c672c8525249f50058717953b24bcdacdcfa7_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/596c672c8525249f50058717953b24bcdacdcfa7_2_750x1000.jpeg 2x" data-dominant-color="636061"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211126_012516</span><span class="informations">1920×2560 446 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-11-26 04:27 UTC)

<p>You need to remove special characters from the folder name and file name or use a recent Windows10 version.</p>

---

## Post #9 by @Rodrigo_Visconti (2021-11-26 04:35 UTC)

<p>Thanks! It worked now</p>

---
