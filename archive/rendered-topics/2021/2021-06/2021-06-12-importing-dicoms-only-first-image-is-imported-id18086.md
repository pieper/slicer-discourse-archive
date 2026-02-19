---
topic_id: 18086
title: "Importing Dicoms Only First Image Is Imported"
date: 2021-06-12
url: https://discourse.slicer.org/t/18086
---

# Importing dicoms only first image is imported

**Topic ID**: 18086
**Date**: 2021-06-12
**URL**: https://discourse.slicer.org/t/importing-dicoms-only-first-image-is-imported/18086

---

## Post #1 by @Hello (2021-06-12 01:32 UTC)

<p>When I try to import a DICOM file only the first image uploads. I can only see the first slice. How can I get the entire file to upload, I only recently started having this problem.</p>
<p>Here is a link to one of the folders with the DICOM files.</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflY996NT.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/sh/v1o5j9b8e7pse1m/AACKJ07-qELdBv0R01HGYuoSa?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/v1o5j9b8e7pse1m/AACKJ07-qELdBv0R01HGYuoSa?dl=0" target="_blank" rel="noopener nofollow ugc">PAB_W5_Cap</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2021-06-12 03:16 UTC)

<p>Try the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">troubleshooting guide</a>.   If you don’t sort it out, let us know how you import the images and what version worked and what version stopped working for you.</p>

---

## Post #3 by @lassoan (2021-06-12 04:03 UTC)

<p>I had a look at the files and they are not valid DICOM images many mandatory fields are missing and those that are set are not correct.</p>
<p>If you want to generate valid DICOM images then you can look for a Matlab toolbox that can write valid DICOM files, save into a simpler file format (and convert that to DICOM with other tools), or learn how to do it yourself (read about DICOM, check what fields are typically used in the kind of images that you want to create, check the DICOM standard to ensure that you add all required fields, etc.), .</p>
<p>Probably the simplest is to save the volume as nrrd using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite.m</a>. You can readily load this nrrd file into Slicer and many other software. In case you need the image in DICOM format then you can load it into Slicer and then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-files">export it to DICOM</a>.</p>

---
