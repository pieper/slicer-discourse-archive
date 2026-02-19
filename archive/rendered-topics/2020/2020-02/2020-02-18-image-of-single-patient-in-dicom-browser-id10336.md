---
topic_id: 10336
title: "Image Of Single Patient In Dicom Browser"
date: 2020-02-18
url: https://discourse.slicer.org/t/10336
---

# Image of single patient in dicom browser

**Topic ID**: 10336
**Date**: 2020-02-18
**URL**: https://discourse.slicer.org/t/image-of-single-patient-in-dicom-browser/10336

---

## Post #1 by @ruthra_priya (2020-02-18 15:04 UTC)

<p>how to load the image of single patient in dicom browser</p>

---

## Post #2 by @manjula (2020-02-18 15:51 UTC)

<p>Select folders that contain DICOM files</p>
<ul>
<li>Option A: Drag-and-drop the folder that contains DICOM files to the Slicer application window. Slicer displays a popup, asking what to do - click OK (“Load directory in DICOM database”). After import is completed, go to DICOM module.</li>
<li>Option B: Go to DICOM module. Click “Import” button in the top-left corner of the DICOM browser. Select folder that contains DICOM files.</li>
</ul>

---

## Post #3 by @ruthra_priya (2020-02-18 16:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46fa896cb0451d4c80cea282a5eacbfcfed3e816.jpeg" data-download-href="/uploads/short-url/a7Uc7Ow43HL3BGl2as9ioEy3vHE.jpeg?dl=1" title="15820430178601405492352" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fa896cb0451d4c80cea282a5eacbfcfed3e816_2_666x500.jpeg" alt="15820430178601405492352" data-base62-sha1="a7Uc7Ow43HL3BGl2as9ioEy3vHE" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fa896cb0451d4c80cea282a5eacbfcfed3e816_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fa896cb0451d4c80cea282a5eacbfcfed3e816_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46fa896cb0451d4c80cea282a5eacbfcfed3e816_2_1332x1000.jpeg 2x" data-dominant-color="717477"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">15820430178601405492352</span><span class="informations">2064×1548 751 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>     the loaded is not displaying in the screen sir</p>

---

## Post #4 by @lassoan (2020-02-18 16:53 UTC)

<p>The selected study only contains “OT” = other data, something non-image. Use latest Slicer Preview Release and after the patient is imported, double-click on the patient in the DICOM browser to load all data that can be loaded for that patient.</p>

---

## Post #5 by @ruthra_priya (2020-02-19 03:58 UTC)

<p>i tried sir. but it didn’t work out</p>

---

## Post #6 by @ruthra_priya (2020-02-19 04:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d940918ea94d1d55f4ab6356339c6102a37c7dd.jpeg" data-download-href="/uploads/short-url/hUUQByAIxhUMZ57GCcYrtPyKL0h.jpeg?dl=1" title="pic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d940918ea94d1d55f4ab6356339c6102a37c7dd_2_690x477.jpeg" alt="pic" data-base62-sha1="hUUQByAIxhUMZ57GCcYrtPyKL0h" width="690" height="477" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d940918ea94d1d55f4ab6356339c6102a37c7dd_2_690x477.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d940918ea94d1d55f4ab6356339c6102a37c7dd_2_1035x715.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d940918ea94d1d55f4ab6356339c6102a37c7dd_2_1380x954.jpeg 2x" data-dominant-color="E8EDF0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic</span><span class="informations">1920×1330 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>this is the error we got after loading the images</p>

---

## Post #7 by @manjula (2020-02-19 07:16 UTC)

<p>That error i get usually when there is spacing errors. In that case I load the data and inspect and i use dicom patcher to fix it. It has worked for me all the time. How ahead and look at the metadata and then load and see in the volume information whhere the problem is.</p>

---

## Post #8 by @ruthra_priya (2020-02-19 14:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8863350f202a275299f6c356ab13d252ad34ff2.jpeg" data-download-href="/uploads/short-url/qknnpUDlne5W5gnPa4yq5Vd2LhU.jpeg?dl=1" title="158212380726058468778" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8863350f202a275299f6c356ab13d252ad34ff2_2_375x500.jpeg" alt="158212380726058468778" data-base62-sha1="qknnpUDlne5W5gnPa4yq5Vd2LhU" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8863350f202a275299f6c356ab13d252ad34ff2_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8863350f202a275299f6c356ab13d252ad34ff2_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8863350f202a275299f6c356ab13d252ad34ff2_2_750x1000.jpeg 2x" data-dominant-color="777678"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">158212380726058468778</span><span class="informations">1548×2064 697 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How to use it sir…</p>

---

## Post #9 by @ruthra_priya (2020-02-19 14:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b1da9513f8ffabe497f7e7079c004376cfd48ae.jpeg" data-download-href="/uploads/short-url/69q4ZlXtohEIIujvEY9HRQH88fY.jpeg?dl=1" title="1582123902380447812625" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1da9513f8ffabe497f7e7079c004376cfd48ae_2_666x500.jpeg" alt="1582123902380447812625" data-base62-sha1="69q4ZlXtohEIIujvEY9HRQH88fY" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1da9513f8ffabe497f7e7079c004376cfd48ae_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1da9513f8ffabe497f7e7079c004376cfd48ae_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b1da9513f8ffabe497f7e7079c004376cfd48ae_2_1332x1000.jpeg 2x" data-dominant-color="727478"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1582123902380447812625</span><span class="informations">2064×1548 534 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The patient name is not created for me sir…when i drag and drop the folder into the dicom browser…it shows 41 patients…like it sir…how to display the image in the screen of the 3d slicer software</p>

---

## Post #10 by @lassoan (2020-02-19 15:43 UTC)

<p>These data sets have their modality set to “OT”, which means “other”. These might not images at all, or maybe they have an associated color image (a screenshot, a rendered image of a report, etc.). None of these are usable for visualization or analaysis.</p>
<p>Where do these files come from? What do you expect to have in them?</p>

---

## Post #11 by @ruthra_priya (2020-02-20 08:41 UTC)

<p>sir… our concept is that we are using the set of single patient mri brain images to convert into 3d reconstruction to identify the volume of the tumor.</p>

---

## Post #12 by @lassoan (2020-02-20 19:05 UTC)

<p>The file that you showed the metadata content of appears to be a single 8-bit RGB screenshot without any geometry information (ConversionType=WSD means that “The equipment that captured the image from the screen, or placed the modified image into a DICOM SOP Instance”). Such images are not usable for any kind of analysis.</p>
<p>You need to export your data sets from the workstation as proper DICOM MR image series.</p>

---

## Post #13 by @ruthra_priya (2020-02-21 08:52 UTC)

<p>Thank you sir…i am final year student of kamaraj college of engineering and technology …i am doing final year project with the help of your software,which type of images can be used in 3d slicer software?please send sample mri brain image for our reference sir or send me any link  to download images.</p>

---

## Post #14 by @manjula (2020-02-21 11:08 UTC)

<p>You have sample data that you can download within 3D Slicer. Just go to Sample Data module and you have sample data. MRI, CT etc…</p>
<p>Also when you start the 3D Slicer in the welcome screen you can see the link “Download Sample Data”</p>
<p>As for supported image/data formats can be found at</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat</a></p>

---

## Post #15 by @ruthra_priya (2020-03-15 15:20 UTC)

<p>sir, how to calculate the volume of a 3d reconstructed mri brain image in 3d slicer software</p>

---

## Post #16 by @manjula (2020-03-16 19:59 UTC)

<p>First Segment the area you want to calculate. Use “segment editor” module for this,</p>
<p>You can find many tutorials online for this. Some common segmentation recipes can be found at<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <a href="https://lassoan.github.io/SlicerSegmentationRecipes/" target="_blank">3D Slicer segmentation recipes</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://lassoan.github.io/SlicerSegmentationRecipes/" target="_blank">Segmentation recipes for 3D Slicer</a></h3>

<p>Recipes for common medical image segmentation tasks using 3D Slicer</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>you can just apply the technique to your area of interest.</p>
<p>then you can use “segment statistics” module to to calculate volume and many other data.</p>

---
