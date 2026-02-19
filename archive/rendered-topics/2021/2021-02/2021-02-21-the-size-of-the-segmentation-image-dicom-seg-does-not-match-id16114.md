---
topic_id: 16114
title: "The Size Of The Segmentation Image Dicom Seg Does Not Match"
date: 2021-02-21
url: https://discourse.slicer.org/t/16114
---

# The size of the segmentation image (DICOM-SEG) does not match the size of the main image (DICOM)

**Topic ID**: 16114
**Date**: 2021-02-21
**URL**: https://discourse.slicer.org/t/the-size-of-the-segmentation-image-dicom-seg-does-not-match-the-size-of-the-main-image-dicom/16114

---

## Post #1 by @cnhwl (2021-02-21 05:41 UTC)

<p>hello everyone!</p>
<p>As shown in the figure, I downloaded the LIDC-IDRC dataset (<a href="https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI#1966254f633413761b746ff9e49dd8f0d5b679d" class="inline-onebox" rel="noopener nofollow ugc">LIDC-IDRI - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki</a>) and the corresponding annotation data (<a href="https://wiki.cancerimagingarchive" rel="noopener nofollow ugc">https://wiki.cancerimagingarchive</a>) from TICA .net/display/DOI/Standardized+representation+of+the+TCIA+LIDC-IDRI+annotations+using+DICOM), and then use the plug-in to convert DICOM-SEG format files to nrrd format files.<br>
They can be opened and feature extraction well in 3D-Slicer, but I want to use the python library radiomics programming for feature extraction, and the dimensionality does not match when reading the data. Similarly, when reading ITK-snap The same problem also appeared at the time, is there any way to solve it?</p>

---

## Post #2 by @cnhwl (2021-02-21 05:41 UTC)

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

## Post #3 by @lassoan (2021-02-21 05:49 UTC)

<p>It seems that in the TCIA data set segmentation is only specified for those 8 frames. This is completely normal and should not cause any problem, as both the segmentation and the reference image are correctly specified in physical space.</p>
<p>If ITK-Snap cannot deal with this then you can resample the segmentation by choosing a reference image when you export the segmentation. Alternatively, you can segment the image in Slicer, which you need to use anyway, and that can handle any segmentation and master volume dimensions and have much more segmentation tools than ITK-Snap (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">this page</a> to get started).</p>

---

## Post #4 by @cnhwl (2021-02-21 07:20 UTC)

<p>Thank you very much for your answer! It is indeed a good way to choose a reference image when exporting. In addition, because I have too many data, I need to use a python script to achieve it. Specifically, I achieved it by resampling the mask from (512<em>512</em>8) to (512<em>512</em>133) through the nibabel library of python.</p>

---

## Post #5 by @lassoan (2021-02-21 13:45 UTC)

<p>All Slicer features are available in Python, so you can do the entire import, conversion, export with reference volume in a single script. See examples in the <a href="https://www.slicer.org/w/index.php?title=Documentation/Nightly/ScriptRepository#Segmentations">script repository</a> and you can ask here for details/advice.</p>

---
