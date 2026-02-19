---
topic_id: 13493
title: "Loading Stopped At Autostru"
date: 2020-09-15
url: https://discourse.slicer.org/t/13493
---

# Loading stopped at AutoStru

**Topic ID**: 13493
**Date**: 2020-09-15
**URL**: https://discourse.slicer.org/t/loading-stopped-at-autostru/13493

---

## Post #1 by @Eyck_Blank (2020-09-15 17:18 UTC)

<p>Hi,<br>
I cannot load pation DICOM files into 3D Slicer, independent od AdvanceMode is checked. .<br>
I use version 4.10.2<br>
The loading process will stopped at AutoStru.<br>
Could someone help me?</p>

---

## Post #2 by @lassoan (2020-09-15 17:26 UTC)

<p>Please use latest Slicer Preview Release and install SlicerRT extension. Let us know if you still have trouble loading the data.</p>

---

## Post #3 by @cpinter (2020-09-15 17:55 UTC)

<p>Hi Eyck,<br>
Please see what I wrote you in email. The answer is there. You need to uncheck Advanced because the way you set up the loadables the Scalar Volume plugin tries to load the structure set instead of RT, and it fails because of that.<br>
Also make sure you use a Slicer preview version.</p>

---

## Post #4 by @Eyck_Blank (2020-09-16 07:01 UTC)

<p>Thank you!<br>
Where can I get the latest Version?<br>
The latest Version, I found, is 4.10.2.</p>
<p>Many thanks<br>
Mit freundlichen Grüßen<br>
Dr.rer.nat. Eyck Blank</p>

---

## Post #5 by @cpinter (2020-09-16 07:28 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://download.slicer.org/">
  <header class="source">
      <img src="https://slicer.org/assets/favicons/favicon-32x32.png?v=Gv63MLlwnz" class="site-icon" width="" height="">

      <a href="https://download.slicer.org/" target="_blank" rel="noopener">3D Slicer</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://slicer.org/assets/img/3d-slicer-128x128.png" class="thumbnail">

<h3><a href="https://download.slicer.org/" target="_blank" rel="noopener">Download 3D Slicer</a></h3>

  <p>3D Slicer is a free, open source software for visualization, processing, segmentation, registration, and analysis of medical, biomedical, and other 3D images and meshes; and planning and navigating image-guided procedures.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a5d5ddc2ba69b6ca3142b8f26d9c88e09884e7d.png" data-download-href="/uploads/short-url/8kjJhCIf53Olzv6iGWCJCW0mCjX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a5d5ddc2ba69b6ca3142b8f26d9c88e09884e7d.png" alt="image" data-base62-sha1="8kjJhCIf53Olzv6iGWCJCW0mCjX" width="690" height="238" data-dominant-color="F7F6F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">894×309 13.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Eyck_Blank (2020-09-17 09:44 UTC)

<p>Thank you, Mr. Lasso,<br>
I have installed the Version 4.11.0, I had found.<br>
This Version stopped the loading process at the structures too.<br>
Mr. Pinter told me about the Version 4.12, I have not found unfortunately.<br>
Can I get the possibility to install Version 4.12 anymore?</p>
<p>Many thanks to you!</p>
<p>Mit freundlichen Grüßen<br>
Dr.rer.nat. Eyck Blank</p>

---

## Post #7 by @Eyck_Blank (2020-09-17 09:46 UTC)

<p>Of corse, I have installed SlicerRT</p>
<p>Mit freundlichen Grüßen<br>
Dr.rer.nat. Eyck Blank</p>

---
