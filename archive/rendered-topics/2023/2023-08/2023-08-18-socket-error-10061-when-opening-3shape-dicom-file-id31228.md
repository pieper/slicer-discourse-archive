---
topic_id: 31228
title: "Socket Error 10061 When Opening 3Shape Dicom File"
date: 2023-08-18
url: https://discourse.slicer.org/t/31228
---

# Socket Error #10061 when opening 3Shape DICOM file

**Topic ID**: 31228
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/socket-error-10061-when-opening-3shape-dicom-file/31228

---

## Post #1 by @Ripanjit (2023-08-18 17:13 UTC)

<p>While opening 3Shape DCM file abutment 3D model file, I am getting error on the clients associated with the server</p>

---

## Post #2 by @Ripanjit (2023-08-18 17:14 UTC)

<p>This is happening only in client machines not server</p>

---

## Post #3 by @lassoan (2023-08-18 20:16 UTC)

<aside class="quote no-group" data-username="Ripanjit" data-post="1" data-topic="31228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/839c29/48.png" class="avatar"> Ripanjit:</div>
<blockquote>
<p>While opening 3Shape DCM file abutment 3D model file</p>
</blockquote>
</aside>
<p>What do you mean by 3D model DICOM file? 3D surface segmentation DICOM information object? Can you share a sample data set that reproduces the behavior? (make sure it does not contain any patient information)</p>

---

## Post #4 by @Ripanjit (2023-08-20 15:29 UTC)

<p>Is there a way I can share the file which has an issue ? 3Shape team can open that file… but I am unable to open that file.</p>

---

## Post #5 by @lassoan (2023-08-20 16:57 UTC)

<p>You can upload the file anywhere (dropbox, OneDrive, etc) and post the link here.</p>

---

## Post #6 by @Ripanjit (2023-08-20 17:28 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fi/6tjuv78j1szwfyopdsgt5/I-790453-6112-1.dcm?rlkey=j402inxf42elehct0yphbmfms&amp;dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fi/6tjuv78j1szwfyopdsgt5/I-790453-6112-1.dcm?rlkey=j402inxf42elehct0yphbmfms&amp;dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-file-unknown-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/scl/fi/6tjuv78j1szwfyopdsgt5/I-790453-6112-1.dcm?rlkey=j402inxf42elehct0yphbmfms&amp;dl=0" target="_blank" rel="noopener nofollow ugc">I-790453-6112 1.dcm</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Ripanjit (2023-08-20 17:28 UTC)

<p>Please try opening this file …</p>

---

## Post #8 by @issakomi (2023-08-20 18:37 UTC)

<p>The file is <strong>not</strong>  a DICOM file. Some HPS (?) format (XML).</p>
<pre><code class="lang-auto">&lt;HPS version="1.1"&gt;
  &lt;Packed_geometry&gt;
    &lt;Schema&gt;CE&lt;/Schema&gt;
    &lt;Binary_data&gt;
      &lt;CE version="1.0"&gt;
</code></pre>

---

## Post #9 by @Ripanjit (2023-08-20 18:42 UTC)

<p>From 3-Shape , I exported the CAD … and in that folder I got three files</p>
<p>DentalDesignerOutput.3ml<br>
I-790453-6112 0.dcm<br>
I-790453-6112 1.dcm</p>
<p>I am able to open “I-790453-6112 0.dcm”</p>
<p>Q1 Were you able to open “I-790453-6112 1.dcm” file ?<br>
Q2 Is there any viewer for HPS format</p>

---

## Post #10 by @Ripanjit (2023-08-20 18:49 UTC)

<p>Both files have same tags… HPS … But one opens and other does not</p>

---
