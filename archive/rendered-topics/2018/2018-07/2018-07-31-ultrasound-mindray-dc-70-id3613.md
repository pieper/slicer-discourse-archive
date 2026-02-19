---
topic_id: 3613
title: "Ultrasound Mindray Dc 70"
date: 2018-07-31
url: https://discourse.slicer.org/t/3613
---

# Ultrasound Mindray DC-70

**Topic ID**: 3613
**Date**: 2018-07-31
**URL**: https://discourse.slicer.org/t/ultrasound-mindray-dc-70/3613

---

## Post #1 by @Ezequiel (2018-07-31 05:37 UTC)

<p>Good morning, I need to make a printable STL file using the Ultrasound Mindray DC-70.<br>
Is it possible to do this with 3D Slicer?<br>
Thank you very much.</p>

---

## Post #2 by @lassoan (2018-07-31 05:41 UTC)

<p>You can certainly make 3D-printable STL models in 3D Slicer. You can find step-by-step tutorials here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>
<p>Were you able to import the 3D ultrasound volume into Slicer?</p>

---

## Post #3 by @Ezequiel (2018-07-31 06:01 UTC)

<p>I wanted to know if the Mindray DC-70 ultrasound is used to export a file that importing it in 3D Slicer can make the printable STL file.<br>
Thanks for your time.</p>

---

## Post #4 by @lassoan (2018-07-31 06:49 UTC)

<p>What file formats you can export from your ultrasound system? DICOM, nrrd, vtk, raw? Are there any export settings that you can configure? If you don’t know the answers to these questions then you may have to contact Mindray support.</p>

---

## Post #5 by @Ezequiel (2018-07-31 19:51 UTC)

<p>I already contacted, they sent me several files exported in the Mindray DC-70 ultrasound, 3 .DCM files, 1 .CIN file and 2 .FRM files<br>
I could not do anything with any.<br>
If you want, I can send them to you in private.<br>
They told me that in case these files do not work, they contact the factory to analyze other alternatives.</p>

---

## Post #6 by @lassoan (2018-08-01 06:29 UTC)

<p>If you send me link to the files in a private message then I can take a look.</p>

---

## Post #7 by @Ezequiel (2018-08-02 19:53 UTC)

<p>I have already sent the files through wetransfer to <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> is it ok?</p>

---

## Post #8 by @lassoan (2018-08-02 21:58 UTC)

<p>I don’t know what this email address is. You need to get a link and post it here or send it to me in a private message.</p>

---

## Post #9 by @Ezequiel (2018-08-02 23:41 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/qm4i33m0scvd9pa/AAAk7pW8AUrZiQ2r_V5yy6c-a?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/qm4i33m0scvd9pa/AAAk7pW8AUrZiQ2r_V5yy6c-a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/qm4i33m0scvd9pa/AAAk7pW8AUrZiQ2r_V5yy6c-a?dl=0" target="_blank" rel="noopener nofollow ugc">Mindray DC-70</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @Ezequiel (2018-08-03 02:31 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/sh/qm4i33m0scvd9pa/AAAk7pW8AUrZiQ2r_V5yy6c-a?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/sh/qm4i33m0scvd9pa/AAAk7pW8AUrZiQ2r_V5yy6c-a?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/sh/qm4i33m0scvd9pa/AAAk7pW8AUrZiQ2r_V5yy6c-a?dl=0" target="_blank" rel="noopener nofollow ugc">Mindray DC-70</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @Josualos (2018-12-20 10:07 UTC)

<p>Good morning, in the end you could get how to export them with mindray dc-70. I am in the same situation and they do not give me an answer.<br>
regards</p>

---

## Post #12 by @lassoan (2018-12-20 16:27 UTC)

<p>The folder that are shared at the dropbox link above contain:</p>
<ul>
<li>3 DICOM files (*.DCM): you can load them by drag-and-dropping each file to the application window (not via the DICOM module), but they only contain screenshots (two of them a singe screenshot, the third one is a short sequence).</li>
<li>3 subfolders: two of them contain uncompressed (therefore relatively easily accessible) voxel data in in BC_CinePartition0.bin files; one of them is probably a single 3D volume, the other is a 4D volume. To be able to read them, someone would need to spend some time figuring out how to interpret these files (they seem to contain a variable-length header before each 2D frame; x dimension is 317, pixel type is unsigned char).</li>
</ul>
<p>To get 3D volumes, you need to either save 3D volumes in DICOM format and not just screenshots (you could ask Mindray how to do that); or ask Mindray for cine file specification (find someone who would be willing to reverse-engineer the cine file format for you) and implement a reader for that in Slicer (probably it would be 1-2 weeks of work for an experienced software developer).</p>

---

## Post #13 by @MartinNA (2023-06-19 20:56 UTC)

<aside class="quote no-group" data-username="Josualos" data-post="11" data-topic="3613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c57346/48.png" class="avatar"> Josualos:</div>
<blockquote>
<p>in the end you could get how to export them with mindray dc-70. I am in the same situation and they do not give me an answer.<br>
regards</p>
</blockquote>
</aside>
<p>in the end someone could get how to export them with mindray dc-70. I am in the same situation and they do not give me an answer.<br>
regards</p>

---

## Post #14 by @fili_S_S (2024-04-23 18:43 UTC)

<p>me too<br>
i own a dc40,  a renewa i9<br>
and im still unable to extract geometry from the DCM  FILES</p>

---

## Post #15 by @lassoan (2024-04-23 21:43 UTC)

<p>Ultrasound imaging device manufacturers are not interested in making image data accessible to users, because it would mean more work for them (to implement and support these features), it would bring more competition (third-party software could compete with the vendor’s proprietary software), and users keep buying their systems anyway.</p>
<p>So, unfortunately there is no good short-term solution (you need to use the workarounds described above). You can change things in the long term by pressuring your clinicians and hospital administrators to refuse buying devices that does not give users full access to image data.</p>

---
