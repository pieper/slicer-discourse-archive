# DICOM data not visible in DICOM browser, only loads in axial view,thin slice views in sagittal/coronal

**Topic ID**: 6635
**Date**: 2019-04-28
**URL**: https://discourse.slicer.org/t/dicom-data-not-visible-in-dicom-browser-only-loads-in-axial-view-thin-slice-views-in-sagittal-coronal/6635

---

## Post #1 by @Dexter777 (2019-04-28 14:43 UTC)

<p>Operating system:Windows10<br>
Slicer version:4.10.1<br>
Expected behavior:Data to load as volumes in all views,scroll wheel to work in all views<br>
Actual behavior: Data only visible in axial view, scrolling between views does not work. 2nd- sagittal and coronal views are only represented by a thin line,scroll wheel does work. No data visible in DICOM browser.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36e2812ee886c336058673c54c982b258c27b0aa.jpeg" data-download-href="/uploads/short-url/7Px4aLXkxvXYepB09gbD4CseKbU.jpeg?dl=1" title="Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36e2812ee886c336058673c54c982b258c27b0aa_2_690x372.jpeg" alt="Slicer" data-base62-sha1="7Px4aLXkxvXYepB09gbD4CseKbU" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36e2812ee886c336058673c54c982b258c27b0aa_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36e2812ee886c336058673c54c982b258c27b0aa_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36e2812ee886c336058673c54c982b258c27b0aa_2_1380x744.jpeg 2x" data-dominant-color="6F6F77"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer</span><span class="informations">1915×1033 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-04-28 19:13 UTC)

<p>Have you loaded the data set using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" rel="nofollow noopener">DICOM module</a>?</p>
<p>If just use “Add data” module and leave the default “single slice” option enabled then only the selected slice will be loaded.</p>

---

## Post #3 by @Dexter777 (2019-04-30 21:46 UTC)

<p>Hi Andras,</p>
<p>I was using the drag and drop the DICOM folder into the Slicer window to open data. I saw it on a video.</p>
<p>What finally worked was hitting the DCM button on the upper left and then hitting Import. It allowed me to import the DICOM folder and select files once imported.</p>
<p>I’m now trying to figure out, when segmenting a brain and meningioma from a MRI and CT, how to get a more realistic looking brain/meningioma. My parts are very smooth or if I turn the smoothing function down, the</p>
<p>brain looks like segmented planes. I’ll look through the Slicer Forum for suggestions.</p>
<p>Thanks again for responding.</p>
<p>Richard</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/5/52d5f1c08649212fe6768d2cacdcf8df711810d9.jpeg" width="100" height="100"></p>

---
