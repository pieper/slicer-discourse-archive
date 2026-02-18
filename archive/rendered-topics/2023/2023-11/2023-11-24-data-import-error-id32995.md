# Data Import Error

**Topic ID**: 32995
**Date**: 2023-11-24
**URL**: https://discourse.slicer.org/t/data-import-error/32995

---

## Post #1 by @Lilyana (2023-11-24 04:04 UTC)

<p>why when converting data from IMA type to DICOM type the description display is volume? so I have to change the VOLUME descriptions one by one to DICOM (screenshot 1).<br>
and when I succeeded in changing it to DICOM, but the data was not input in 3D Slicer (screenshot 2).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d2f83a803766b09da10adb7e0a1d3b3e7e57556.jpeg" data-download-href="/uploads/short-url/6rJhFJAOQdhdZITJUexuBP2LLJI.jpeg?dl=1" title="Screenshot (1623)_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2f83a803766b09da10adb7e0a1d3b3e7e57556_2_690x388.jpeg" alt="Screenshot (1623)_LI" data-base62-sha1="6rJhFJAOQdhdZITJUexuBP2LLJI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2f83a803766b09da10adb7e0a1d3b3e7e57556_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2f83a803766b09da10adb7e0a1d3b3e7e57556_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d2f83a803766b09da10adb7e0a1d3b3e7e57556_2_1380x776.jpeg 2x" data-dominant-color="EBF0F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (1623)_LI</span><span class="informations">1920×1080 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e03f961cd12e857c22b6cf598bf6e46430d48a87.png" data-download-href="/uploads/short-url/vZNbz9M3fE4AlfGEcPdxWaUbZrx.png?dl=1" title="Screenshot (1622)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03f961cd12e857c22b6cf598bf6e46430d48a87_2_690x388.png" alt="Screenshot (1622)" data-base62-sha1="vZNbz9M3fE4AlfGEcPdxWaUbZrx" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03f961cd12e857c22b6cf598bf6e46430d48a87_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03f961cd12e857c22b6cf598bf6e46430d48a87_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e03f961cd12e857c22b6cf598bf6e46430d48a87_2_1380x776.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (1622)</span><span class="informations">1920×1080 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-11-24 14:27 UTC)

<p>It is better to use the 'Import DICOM files" button in the DICOM module and point to a directory containing valid dicom data.  This avoids using the Add Data dialog that is better for other data formats.</p>
<p>It looks in your second screenshot that 0 files were imported, indicating that maybe your .IMA files are not actually DICOM.  There is no official file extension for DICOM, but .dcm is often used.  .IMA is also used sometimes, but it doesn’t always indicate that the files are DICOM.  Even if the files are supposed to be DICOM, there are many things that could make them impossible to load without extra effort.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---
