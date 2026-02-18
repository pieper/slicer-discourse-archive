# The size of the segmentation image (DICOM-SEG) does not match the size of the main image (DICOM)

**Topic ID**: 16115
**Date**: 2021-02-21
**URL**: https://discourse.slicer.org/t/the-size-of-the-segmentation-image-dicom-seg-does-not-match-the-size-of-the-main-image-dicom/16115

---

## Post #1 by @cnhwl (2021-02-21 05:41 UTC)

<p>Operating system: win 10<br>
Slicer version: Slicer 4.11</p>
<p>Hi Everyone,</p>
<p>As shown in the figure, I downloaded the LIDC-IDRC dataset  and standardized representation of the TCIA LIDC-IDRI annotations using from TICA , and then use the dcmqi to convert DICOM-SEG format files to nrrd format files.<br>
They can be opened and feature extraction well in 3D-Slicer, but I want to use the python library radiomics with programming to do feature extraction, and the dimension does not match when reading the data. Similarly, when reading those data with ITK-snap the same problem also appeared at the time, is there any way to solve it? Or, is there any way to change the dimension of the 512<em>512</em>8 annotation file to be the same as the 512<em>512</em>133 of the source image?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62dc654afb5bb0ab1dff3c581140e811a38f3271.png" data-download-href="/uploads/short-url/e6yZezdpNmepiPJs644Wsuh1qUN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62dc654afb5bb0ab1dff3c581140e811a38f3271.png" alt="image" data-base62-sha1="e6yZezdpNmepiPJs644Wsuh1qUN" width="690" height="49" data-dominant-color="5B2F2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1301×94 6.75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c88f9500cffe0b16e67d49d120e59bf993c0d0.png" data-download-href="/uploads/short-url/ne335M1avg7qdehirRVJRNNw6RO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2c88f9500cffe0b16e67d49d120e59bf993c0d0_2_690x459.png" alt="image" data-base62-sha1="ne335M1avg7qdehirRVJRNNw6RO" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2c88f9500cffe0b16e67d49d120e59bf993c0d0_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2c88f9500cffe0b16e67d49d120e59bf993c0d0_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c88f9500cffe0b16e67d49d120e59bf993c0d0.png 2x" data-dominant-color="939293"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1093×728 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6ccda3cdc542e851436f356e2461285ab2fa4d2.jpeg" data-download-href="/uploads/short-url/wVKIbopgaXbiyOCfgoDrOubpou6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6ccda3cdc542e851436f356e2461285ab2fa4d2_2_690x376.jpeg" alt="image" data-base62-sha1="wVKIbopgaXbiyOCfgoDrOubpou6" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6ccda3cdc542e851436f356e2461285ab2fa4d2_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6ccda3cdc542e851436f356e2461285ab2fa4d2_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6ccda3cdc542e851436f356e2461285ab2fa4d2_2_1380x752.jpeg 2x" data-dominant-color="A0A0A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1048 306 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ae0f982b3f76dd0c9c218b0cea1c69099a2dcce.jpeg" data-download-href="/uploads/short-url/hx2fXigTJiDxTnSumJ0L0tKObD0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae0f982b3f76dd0c9c218b0cea1c69099a2dcce_2_690x374.jpeg" alt="image" data-base62-sha1="hx2fXigTJiDxTnSumJ0L0tKObD0" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae0f982b3f76dd0c9c218b0cea1c69099a2dcce_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae0f982b3f76dd0c9c218b0cea1c69099a2dcce_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ae0f982b3f76dd0c9c218b0cea1c69099a2dcce_2_1380x748.jpeg 2x" data-dominant-color="A2A2AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1041 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you all !!!</p>

---

## Post #2 by @lassoan (2021-02-21 05:41 UTC)

<p>A post was merged into an existing topic: <a href="/t/the-size-of-the-segmentation-image-dicom-seg-does-not-match-the-size-of-the-main-image-dicom/16114">The size of the segmentation image (DICOM-SEG) does not match the size of the main image (DICOM)</a></p>

---

## Post #3 by @lassoan (2021-02-21 05:41 UTC)



---
