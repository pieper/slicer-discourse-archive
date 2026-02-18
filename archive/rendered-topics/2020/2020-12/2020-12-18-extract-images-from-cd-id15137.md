# Extract images from CD

**Topic ID**: 15137
**Date**: 2020-12-18
**URL**: https://discourse.slicer.org/t/extract-images-from-cd/15137

---

## Post #1 by @Valentina_Mejia_Gall (2020-12-18 22:36 UTC)

<p>Hello,<br>
I have a CD with all the information of a ct scan and x-ray, there is a carpet that says DICOM so when i tried to upload this carpet to 3dSlicer it appears desorganized or like this (images attached). How can i organized it ? or how to uppload images in 3dSlicer so it appears correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/498a3e2f903c85de0a1501bca2664b270ae0a9c2.png" data-download-href="/uploads/short-url/auz2rwwktRbinsex7lqtWfMEmv8.png?dl=1" title="Screen Shot 2020-12-18 at 5.35.18 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498a3e2f903c85de0a1501bca2664b270ae0a9c2_2_690x486.png" alt="Screen Shot 2020-12-18 at 5.35.18 PM" data-base62-sha1="auz2rwwktRbinsex7lqtWfMEmv8" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498a3e2f903c85de0a1501bca2664b270ae0a9c2_2_690x486.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/498a3e2f903c85de0a1501bca2664b270ae0a9c2_2_1035x729.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/498a3e2f903c85de0a1501bca2664b270ae0a9c2.png 2x" data-dominant-color="4B4A56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-12-18 at 5.35.18 PM</span><span class="informations">1045×737 76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2020-12-19 00:09 UTC)

<p>Did you try the steps in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">dicom troubleshooting section</a>?</p>

---

## Post #3 by @lassoan (2020-12-19 02:35 UTC)

<p>Also make sure you load using DICOM module (not using “Add data” window). See instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#dicom-data">here</a>.</p>

---

## Post #4 by @Valentina_Mejia_Gall (2020-12-19 20:39 UTC)

<p>the problem is that i already did that, i loaded using the DICOM module but it appears that the sagital, coronal and all views are in different files and mixed up. I don’t understand much about it.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8556303f850518dc678c8b5b88c775768467ca30.jpeg" data-download-href="/uploads/short-url/j1ya0RazL2G5KZv8S72p4apnNm0.jpeg?dl=1" title="Screen Shot 2020-12-19 at 3.37.13 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8556303f850518dc678c8b5b88c775768467ca30_2_690x312.jpeg" alt="Screen Shot 2020-12-19 at 3.37.13 PM" data-base62-sha1="j1ya0RazL2G5KZv8S72p4apnNm0" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8556303f850518dc678c8b5b88c775768467ca30_2_690x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8556303f850518dc678c8b5b88c775768467ca30_2_1035x468.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8556303f850518dc678c8b5b88c775768467ca30_2_1380x624.jpeg 2x" data-dominant-color="89898F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-12-19 at 3.37.13 PM</span><span class="informations">1659×751 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2020-12-19 20:57 UTC)

<p>What you show in the screenshot looks perfect. This is how an imaging study should look like. It typically starts with a few low-quality large-field-of-view scans (commonly referred to as survey or scout scans). The purpose of these is to provide allow the technologist to define region of interest and determine optimal imaging parameters. These images are usually saved but you can just ignore them. What you are untreated in are the diagnostic images that are acquired after the scout scans.</p>
<p>Did you expect to find something different in this imaging study?</p>

---

## Post #6 by @lassoan (2020-12-21 17:43 UTC)

<p>Based on further discussions with <a class="mention" href="/u/valentina_mejia_gall">@Valentina_Mejia_Gall</a>, the problem turns out to be the usual issue that MRI images are often acquired with highly anisotropic spacing: having high resolution in one plane and large gaps between the planes (see <a href="https://discourse.slicer.org/t/3d-model-from-dicoms/5478/2" class="inline-onebox">3D model from dicoms</a> and related topics).</p>

---
