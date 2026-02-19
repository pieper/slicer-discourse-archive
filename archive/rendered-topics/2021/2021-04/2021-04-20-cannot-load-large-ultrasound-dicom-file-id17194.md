---
topic_id: 17194
title: "Cannot Load Large Ultrasound Dicom File"
date: 2021-04-20
url: https://discourse.slicer.org/t/17194
---

# Cannot load large Ultrasound DICOM file

**Topic ID**: 17194
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/cannot-load-large-ultrasound-dicom-file/17194

---

## Post #1 by @ZHENZC (2021-04-20 05:29 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a240120079ed98cd55e4430455bc2afc06122e7e.jpeg" alt="mmexport1618880832319" data-base62-sha1="n9kCscvbbicXXbcVwF5GVZQjhca" width="492" height="329"><br>
Cannon Ultrasound DICOM</p>
<p>small file can be loaded(approximately 5Mb for a 30s video)</p>
<p>However larger file cannot be loaded(approximately 100Mb for a 3min video).<br>
The error is showed in the attached screenshot.</p>
<p>How tosolve this problem? Is there anyway can I load the 3min video in 3Dslicer?</p>
<p>Is there any software can cut the long video into several shorter video?</p>
<p>Will exporting files in nrrd format from the ultrasound machine help?</p>

---

## Post #2 by @lassoan (2021-04-20 05:38 UTC)

<p>The application has run out of memory while trying to load this long sequence. 100MB compressed video can be several GB when uncompressed. If you want to make sure that the application does not run out of memory, allocate 10x larger memory space than than your data size.</p>
<p>I would recommend to set the virtual memory size to 30GB and see how big the sequence is when loaded successfully.</p>
<p>You may also have a look at the log to see if there is any useful error or warning message.</p>
<p>If you can upload an example video somewhere and post the link here then we can have a look why the sequence requires a lot of memory and if there is an easy way to reduce it.</p>

---

## Post #3 by @ZHENZC (2021-04-20 11:28 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb850fbfce05b9f6ba92be5bdd7b31e0627b9f2e.png" alt="WeChat Image_20210420192316" data-base62-sha1="qKSmW9rfNCZUHCmlzfSXADp4T5c" width="502" height="266"><br>
I have set virtual memory to 50G and mechanical memory is 16G, still can’t load. And I noticed in the task manager that 3Dslicer only takes up 6G of memory when loading.</p>
<p>I have also tried in the other computer, it shows a different error as the picture attached. And I can’t search any useful information about this error on the Internet.</p>
<p>Thank you anyway<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51039c17abf2e9c4c7ef4e347447c8d9df4551a2.png" data-download-href="/uploads/short-url/byGplVAHPnL2HdAdqccLaGouubM.png?dl=1" title="WeChat Screenshot_20210420193033" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51039c17abf2e9c4c7ef4e347447c8d9df4551a2.png" alt="WeChat Screenshot_20210420193033" data-base62-sha1="byGplVAHPnL2HdAdqccLaGouubM" width="690" height="98" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WeChat Screenshot_20210420193033</span><span class="informations">743×106 2.16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-04-20 12:57 UTC)

<p>Did you use the DICOM module to load the image? You may try to set the DICOM reader to DCMTK (in menu: Edit / Application settings).</p>
<p>The DICOM image may be incorrect, which is not uncommon for ultrasound images. If you can share an anonymized or phantom image (upload somewhere and post the link here) then we can investigate.</p>

---
