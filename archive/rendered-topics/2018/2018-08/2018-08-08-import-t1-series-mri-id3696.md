# Import T1 series MRI

**Topic ID**: 3696
**Date**: 2018-08-08
**URL**: https://discourse.slicer.org/t/import-t1-series-mri/3696

---

## Post #1 by @DIM (2018-08-08 05:39 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.8.0<br>
Expected behavior: Import multi series from MRI,<br>
Actual behavior: Import only one series (coronal) the other slices are distortionated</p>

---

## Post #2 by @lassoan (2018-08-08 05:43 UTC)

<p>Please try import using latest nightly version. If you still have problems then enable advanced mode in the DICOM loading window and try selecting different items in the list at the bottom. If you still not get the results you expect, give us more information about the data (what software generated it, what does it contain, how do you expect it to be loaded, etc. and the application log - menu: Help / Report a bug).</p>

---

## Post #3 by @DIM (2018-08-08 17:16 UTC)

<p>Thank you for your attention<br>
I am using version 4.9.0, try to import the series according to the different advanced options. When viewing the master volume of the series, only one cut is defined. the others are blurred, the same happens when I import different series from the same patient.<br>
Can you please guide me?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5c366555b9359dca9409ea0d51a784049f321dd.png" data-download-href="/uploads/short-url/sduHCZab4gT1Wjuqn1kOxnB0yaV.png?dl=1" title="3d%20slicer%202" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5c366555b9359dca9409ea0d51a784049f321dd.png" alt="3d%20slicer%202" data-base62-sha1="sduHCZab4gT1Wjuqn1kOxnB0yaV" width="690" height="414" data-dominant-color="D0E0ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d%20slicer%202</span><span class="informations">1353×813 46.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-08-09 08:53 UTC)

<p>This is normal. MRI acquisitions are often highly anisotropic (much larger spacing between slices than pixel size within a slice). If this is a problem then you need to change your image acquisition protocol.</p>

---
