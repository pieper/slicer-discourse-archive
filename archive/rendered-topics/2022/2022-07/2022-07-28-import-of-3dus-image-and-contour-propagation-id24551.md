# Import of 3DUS image and contour propagation

**Topic ID**: 24551
**Date**: 2022-07-28
**URL**: https://discourse.slicer.org/t/import-of-3dus-image-and-contour-propagation/24551

---

## Post #1 by @erpoul (2022-07-28 20:08 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.0.3 revision 30893<br>
Expected behavior: loading of a 3DUS image as a volume and export of the deform MRI with the ultrasound<br>
Actual behavior: loading of the images individually and export only one image with an RT struc with missing data</p>
<p>The goal is to use the MRI contour propagation extension to register US and MRI so we can export the deformed MR structure on the US volume. The US volume are actually loaded as individual instead of a volume. The registration is performed correctly but when I export the deformed MR structure on the ultrasound only one individual image is exported with an RT struct which is missing data.</p>
<p>[INFO][Stream] 28.07.2022 14:04:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Imported a DICOM directory, checking for extensions<br>
[CRITICAL][Stream] 28.07.2022 14:05:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
[CRITICAL][Stream] 28.07.2022 14:05:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - W: OperatorsName (0008,1070) absent in RTSeriesModule (type 2)<br>
[WARNING][Python] 28.07.2022 14:05:17 [Python] (C:\tmp\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\DICOMLib\DICOMBrowser.py:555) - Warning in DICOM plugin Image sequence when examining loadable 1: US Oncentra Prostate Image Series [0]: Image spacing may need to be calibrated for accurate size measurements.<br>
[WARNING][Python] 28.07.2022 14:05:17 [Python] (C:\tmp\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\DICOMLib\DICOMBrowser.py:555) - Warning in DICOM plugin Image sequence when examining loadable 1: US Oncentra Prostate Image Series [1]: Image spacing may need to be calibrated for accurate size measurements.<br>
[WARNING][Python] 28.07.2022 14:05:17 [Python] (C:\tmp\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\DICOMLib\DICOMBrowser.py:555) - Warning in DICOM plugin Image sequence when examining loadable 1: US Oncentra Prostate Image Series [2]: Image spacing may need to be calibrated for accurate size measurements.<br>
[WARNING][Python] 28.07.2022 14:05:17 [Python] (C:\tmp\NA-MIC\Slicer 5.0.3\lib\Slicer-5.0\qt-scripted-modules\DICOMLib\DICOMBrowser.py:555) - Warning in DICOM plugin Image sequence when examining loadable 1: US Oncentra Prostate Image Series [3]: Image spacing may need to be calibrated for accurate size measurements.<br>
[INFO][Python] 28.07.2022 14:05:17 [Python] (C:\tmp\NA-MIC\Slicer 5.0.3\bin\Python\slicer\util.py:2695) - Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?<br>
[CRITICAL][Stream] 28.07.2022 14:05:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Warning in DICOM plugin Image sequence when examining loadable 1: US Oncentra Prostate Image Series [0]: Image spacing may need to be calibrated for accurate size measurements.<br>
[CRITICAL][Stream] 28.07.2022 14:05:17 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Warning in DICOM plugin Image sequence when examining loadable 1: US Oncentra Prostate Image Series [1]: Image spacing may need to be calibrated for accurate size measurements.</p>

---

## Post #2 by @lassoan (2022-08-03 17:14 UTC)

<p>You can enable the “Advanced” option in DICOM module and try all the loadables (check the checkboxes next to them) to see if any of them produce a 3D ultrasound image.</p>
<p>Have you loaded such 3D ultrasound images successfully into Slicer before?</p>

---

## Post #3 by @erpoul (2022-08-03 18:54 UTC)

<p>We were able to import them in Slicer 4.7.0-2017-10-05 r26425 and earlier version but can’t say when it stop working. However, I think the loading was working in version 4.11.20200930, but for sure since 4.13.0-2020-12-17 it is not working. In advanced mode it clearly shows that the images will be loaded in sequence, individually (even with all the checkbox to on)</p>

---

## Post #4 by @lassoan (2022-08-03 21:45 UTC)

<p>Each checkbox loads one node. Please check all of them - if Slicer loaded the series correctly then one of the loaded nodes should be a 3D volume. Probably the only change is which loadable is selected by default. You can enable the “Advanced” option in the old Slicer version (that loaded the series as a 3D image) to see which loadable was the one that worked well.</p>

---

## Post #5 by @erpoul (2022-08-04 16:08 UTC)

<p>Found the issue, in the older version the US scalar volume was check automatically and loaded. Now in the new version it is the image individually which are loaded (if 153 slices there is 153 image sequence loaded; see joined picture). However the scalar volume is created and in the advanced mode we can go at the bottom of the page and actually select only the scalar volume, then everything is working. Is there a fix possible so that it actually select automatically the scalar volume ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16c40183e8bf1eb16bafa27aa2c2bc13cc4e172c.png" data-download-href="/uploads/short-url/3forAWvZiTJOjjNzyoCthoNhAhS.png?dl=1" title="Capture_3DUSload_v4.7.0-2017-10-05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16c40183e8bf1eb16bafa27aa2c2bc13cc4e172c.png" alt="Capture_3DUSload_v4.7.0-2017-10-05" data-base62-sha1="3forAWvZiTJOjjNzyoCthoNhAhS" width="690" height="104" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture_3DUSload_v4.7.0-2017-10-05</span><span class="informations">1225×185 6.75 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8faa8ad6a762b55976332a1764377884c65f2b9.jpeg" data-download-href="/uploads/short-url/o6Rfs5J63tosgb4rjADANvQjmul.jpeg?dl=1" title="Capture_v5.0.3_image_sequence" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8faa8ad6a762b55976332a1764377884c65f2b9_2_690x87.jpeg" alt="Capture_v5.0.3_image_sequence" data-base62-sha1="o6Rfs5J63tosgb4rjADANvQjmul" width="690" height="87" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8faa8ad6a762b55976332a1764377884c65f2b9_2_690x87.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8faa8ad6a762b55976332a1764377884c65f2b9_2_1035x130.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8faa8ad6a762b55976332a1764377884c65f2b9_2_1380x174.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture_v5.0.3_image_sequence</span><span class="informations">1893×239 51.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60ed2977cdea44747726b2c0f3fc0167e712af56.jpeg" data-download-href="/uploads/short-url/dPrXaBm4q9ixMwe3bqVZwgkSiZU.jpeg?dl=1" title="Capture_v5.0.3_scalar_volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ed2977cdea44747726b2c0f3fc0167e712af56_2_690x103.jpeg" alt="Capture_v5.0.3_scalar_volume" data-base62-sha1="dPrXaBm4q9ixMwe3bqVZwgkSiZU" width="690" height="103" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ed2977cdea44747726b2c0f3fc0167e712af56_2_690x103.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ed2977cdea44747726b2c0f3fc0167e712af56_2_1035x154.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60ed2977cdea44747726b2c0f3fc0167e712af56_2_1380x206.jpeg 2x" data-dominant-color="F9F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture_v5.0.3_scalar_volume</span><span class="informations">1907×286 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2022-08-05 16:47 UTC)

<p>Sure, it should be no problem to adjust the DICOM importers to recognize this specific image type. There is no commonly used DICOM standard for 3D/4D ultrasound storage, so we need to add such custom import rule for each manufacturer.</p>
<p>We just need an example image (preferably of a phantom or animal case, but an anonymized patient case works, too). Please upload it to somewhere and post the link here.</p>

---

## Post #7 by @erpoul (2022-08-05 18:52 UTC)

<p>There is only 2 compagnies in brachytherapy/radiotherapy which are performing 3DUS scan, Elekta and Varian, the current data is for Elekta:</p>
<p><a href="https://drive.google.com/drive/folders/1IDJnRUv2teXZPVOiT4FaqC0SFSP6wtoq?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1IDJnRUv2teXZPVOiT4FaqC0SFSP6wtoq?usp=sharing</a></p>

---
