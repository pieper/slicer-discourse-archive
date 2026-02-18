# Cannot save DICOM to NRRD files

**Topic ID**: 32609
**Date**: 2023-11-05
**URL**: https://discourse.slicer.org/t/cannot-save-dicom-to-nrrd-files/32609

---

## Post #1 by @maiseld (2023-11-05 17:43 UTC)

<p>After loading in all of the DICOM files into Slicer, I click to save but do not have the option of saving into NRRD files. I was following this guide:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.embodi3d.com/blogs/entry/345-a-ridiculously-easy-way-to-convert-ct-scans-to-3d-printable-bone-stl-models-for-free-in-minutes/">
  <header class="source">

      <a href="https://www.embodi3d.com/blogs/entry/345-a-ridiculously-easy-way-to-convert-ct-scans-to-3d-printable-bone-stl-models-for-free-in-minutes/" target="_blank" rel="noopener nofollow ugc">embodi3D.com</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://content.invisioncic.com/r248939/monthly_2019_05/large.57f1cd457cd65_Covershot.JPG.07e4fff571d0dbf21f75a34a5ec4ecf5.JPG.25a410a9e45085bd78881426a84c81de.JPG" class="thumbnail">

<h3><a href="https://www.embodi3d.com/blogs/entry/345-a-ridiculously-easy-way-to-convert-ct-scans-to-3d-printable-bone-stl-models-for-free-in-minutes/" target="_blank" rel="noopener nofollow ugc">A Ridiculously Easy Way to Convert CT Scans to 3D Printable Bone STL Models...</a></h3>

  <p>Please note the democratiz3D service was previously named "Imag3D" In this tutorial you will learn how to quickly and easily make 3D printable bone models from medical CT scans using the free online service democratiz3D®. The method described here...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I just downloaded Slicer as of today so I should have the current version. What do I need to configure to <strong>save in NRRD filetype</strong>?</p>

---

## Post #2 by @maiseld (2023-11-06 02:45 UTC)

<p>To demonstrate what is going on. First I load to DICOM data into Slicer (redacting my name in the url):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e74ab4509845669081285fb8a8c2a3c312cefcec.jpeg" data-download-href="/uploads/short-url/x06lDCd4eo5Dqqq8Z30pxKLZ03G.jpeg?dl=1" title="A" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e74ab4509845669081285fb8a8c2a3c312cefcec_2_617x500.jpeg" alt="A" data-base62-sha1="x06lDCd4eo5Dqqq8Z30pxKLZ03G" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e74ab4509845669081285fb8a8c2a3c312cefcec_2_617x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e74ab4509845669081285fb8a8c2a3c312cefcec_2_925x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e74ab4509845669081285fb8a8c2a3c312cefcec_2_1234x1000.jpeg 2x" data-dominant-color="A5A4AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">A</span><span class="informations">1281×1038 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Once the upload finishes and I click done, then I click the save icon (at the top left) and this window opens. I click the drop down list in this save window, and I get these options for saving:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/624ebfa1fae7e219a3650b0317d7d88c3c1104eb.png" alt="B" data-base62-sha1="e1FvCVAOAwTdeybkMVLYP7bQPSr" width="634" height="332"></p>
<p>As you can see there is no option to save into NRRD. How do I enable this option?</p>

---

## Post #3 by @maiseld (2023-11-06 03:52 UTC)

<p>So  I found one forum post relating to my issue :</p><aside class="quote" data-post="6" data-topic="540">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ccd318/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-convert-dicom-files-to-nrrd/540/6">How to convert dicom files to nrrd</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Do you know of anywhere I can go to learn how to use SlicerRadiomics? I now 
have it installed, but I cannot find how to use the extension.
  </blockquote>
</aside>

<p>After reading this and trying something - I did manage to make some progress…</p>
<p>After freshly booting up Slicer and uploading the DICOM data, I then clicked “Load” on the bottom of the Slicer interface and it loaded the DICOM files (which I think allows me to view their contents) and each scan appeared under the “Loaded Data” window in the left sidebar.</p>
<p>After that, when I clicked “Save” (from under “File” or Ctrl + S) I had the option of saving multiple files as .nrrd. (But not the whole of the data). I was able to find the files in the directory I saved them to.</p>
<p>So maybe I was running into difficulties because the DICOM data I was importing was from multiple different CT scans, and I had to load them first so it recognized them as multiple scans to be saved as multiple .nrrd files?</p>
<p>I just want to make sure I did this correctly in accordance with the tutorial I linked in my first post, so let me know.</p>

---

## Post #4 by @muratmaga (2023-11-06 05:45 UTC)

<p>All your issues are related to your DICOM import. If you can successfully import DICOMs, you can save them as NRRD.</p>
<p>From the screenshot it appears you are trying to load every single dicom file as a separate volume.</p>
<p>Go to File-&gt;Add DICOM to switch to the DICOM module then click Import DICOM Files and navigate to the folder where you have your files and click import. If you have more than one study, it may take a few minutes to import them all. Then from the database click the study you wish to load into the scene. After that you can use the File As to save your imported volume as NRRD.</p>
<p>For more information see the <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#dicom-data">documentation on DICOMs.</a></p>

---
