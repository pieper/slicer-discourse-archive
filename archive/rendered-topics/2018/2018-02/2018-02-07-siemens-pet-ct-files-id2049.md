---
topic_id: 2049
title: "Siemens Pet Ct Files"
date: 2018-02-07
url: https://discourse.slicer.org/t/2049
---

# Siemens PET/CT files

**Topic ID**: 2049
**Date**: 2018-02-07
**URL**: https://discourse.slicer.org/t/siemens-pet-ct-files/2049

---

## Post #1 by @Hamburgerfinger (2018-02-07 20:36 UTC)

<p>Can Slicer directly load Siemens PET/CT images? (.img and .hdr files) I can get them into Slicer by exporting them from Siemens’ software in dicom format, but it would be much more convenient to import them into Slicer directly.</p>
<p>Thanks!!</p>

---

## Post #2 by @lassoan (2018-02-07 22:31 UTC)

<p>Have you tried loading the .hdr file into Slicer?</p>
<p>Is the .hdr file a text file? Can you copy its contents here? (make sure to remove any patient information, if any)</p>

---

## Post #3 by @Hamburgerfinger (2018-02-11 21:53 UTC)

<p>I’ve tried loading in the .hdr to no avail.  The .hdr file is a text file; I’ve pasted an example header below.  Thanks!</p>

---

## Post #4 by @lassoan (2018-02-11 22:51 UTC)

<p>I don’t see the header here. If it is too long for copying here as a message then you can upload it to somewhere (Dropbox, OneDrive, etc.) and post the link here.</p>

---

## Post #5 by @Hamburgerfinger (2018-02-12 19:28 UTC)

<p>The link is below, and contains the header and image:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/qiv9kx5tmuqzj8n/AAC4XtV0-c1UtDPq-a7L-s_ua?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/qiv9kx5tmuqzj8n/AAC4XtV0-c1UtDPq-a7L-s_ua?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/qiv9kx5tmuqzj8n/AAC4XtV0-c1UtDPq-a7L-s_ua?dl=0" target="_blank" rel="noopener nofollow ugc">PET Image</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks!!</p>

---

## Post #6 by @Sammy (2020-02-19 21:38 UTC)

<p>Was there any conclusion to whether Siemens hdr and img files can be added directly?</p>

---

## Post #7 by @lassoan (2020-02-20 04:29 UTC)

<p>Since the header file contains pixel type, dimensions, and spacing, you can load the image file using RawImageGuess extension. If you need to load a lot of these then you can create a simple text converter script, which loads fields from the .hdr file and saves them as a .nhdr file</p>

---
