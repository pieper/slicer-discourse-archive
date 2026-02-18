# Accessing data from an Orthanc PACS server

**Topic ID**: 1985
**Date**: 2018-01-31
**URL**: https://discourse.slicer.org/t/accessing-data-from-an-orthanc-pacs-server/1985

---

## Post #1 by @stevenagl12 (2018-01-31 15:19 UTC)

<p>Hi, I am collaborating with another lab that exclusively uses the Orthanc PACS server for their DICOM data and I was wondering fi someone can tell me how to properly connect to the server to access the data through Slicer, and whether there is a way for slicer to access the data without having to download a complete copy of the file onto the computer? Right now I am using Slicer 4.9.0-2017-11-06.</p>

---

## Post #2 by @pieper (2018-01-31 16:53 UTC)

<p>You should be able to do DICOM query retrieve from orthanc using Slicer’s DICOM Module.  See the Query dialog and networking information here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>
<p>With that you could pull down individual studies to Slicer’s database and then delete them when you are finished.</p>

---

## Post #3 by @stevenagl12 (2018-02-04 14:50 UTC)

<p>Thank you. Is there any more clear directions for establishing the connection to the PACS server? The site you directed me to only has an image of the DICOM browser query dialogue box and a brief mention of it. It didn’t have any directions.</p>

---

## Post #4 by @pieper (2018-02-04 20:55 UTC)

<p>No, I don’t think there’s anything more written up - but it uses pretty standard dicom networking terminology and concepts so if you need background there are resources linked at the bottom of the page.  The topic can get pretty deep quickly.  Often the hard part is finding out the right ports and AETITLE info for your local system.  That’s why you may want to use the dcmtk command line utilities I pointed to in the CTK test program comments to debug and then enter the info to Slicer once you know they work.</p>
<p>Also the folks at <a href="http://dicomserver.co.uk/">Medical Connections</a> are nice enough to run a public PACS for testing and Slicer comes pre-configured to query/retrieve from that.  So you can see if you can just copy that over to your setup.</p>
<p>Basic steps:</p>
<p>Enable the medical connections server, pick a search option and click Query:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eadb7a5dc63a088819e8e9c7ca7a84cca45db67f.png" data-download-href="/uploads/short-url/xvDXmHafIwBKtaCraMQcgnmuKWH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eadb7a5dc63a088819e8e9c7ca7a84cca45db67f_2_505x500.png" alt="image" data-base62-sha1="xvDXmHafIwBKtaCraMQcgnmuKWH" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eadb7a5dc63a088819e8e9c7ca7a84cca45db67f_2_505x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eadb7a5dc63a088819e8e9c7ca7a84cca45db67f_2_757x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eadb7a5dc63a088819e8e9c7ca7a84cca45db67f.png 2x" data-dominant-color="EFF1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">855×845 56.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Select a patient and click Retrieve, data is put in Slicer dicom database:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea0a822ecbba6de0cd87391d46ef757a108c086.png" data-download-href="/uploads/short-url/klK0ov1Mab1nIyRTGXI5mWWFwAS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ea0a822ecbba6de0cd87391d46ef757a108c086_2_690x435.png" alt="image" data-base62-sha1="klK0ov1Mab1nIyRTGXI5mWWFwAS" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ea0a822ecbba6de0cd87391d46ef757a108c086_2_690x435.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ea0a822ecbba6de0cd87391d46ef757a108c086_2_1035x652.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea0a822ecbba6de0cd87391d46ef757a108c086.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1361×859 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Load result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3e01dc31682d81eaa0d0bd8c746e1396ee6df00.jpeg" data-download-href="/uploads/short-url/pFfDjoIN28HSXQ8bHIU8XAlNZoQ.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3e01dc31682d81eaa0d0bd8c746e1396ee6df00_2_690x443.jpg" alt="image" data-base62-sha1="pFfDjoIN28HSXQ8bHIU8XAlNZoQ" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3e01dc31682d81eaa0d0bd8c746e1396ee6df00_2_690x443.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3e01dc31682d81eaa0d0bd8c746e1396ee6df00_2_1035x664.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3e01dc31682d81eaa0d0bd8c746e1396ee6df00_2_1380x886.jpg 2x" data-dominant-color="98989E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1973×1267 376 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @stevenagl12 (2018-02-05 19:21 UTC)

<p>Thank you very much.</p>

---

## Post #6 by @pieper (2018-02-05 19:35 UTC)

<p>Oh, and I remember now there was some info too on the orthanc list that may<br>
be just what you are looking for:</p>
<p><a href="https://groups.google.com/forum/#!topic/orthanc-users/BZSbsksrMVA" class="onebox" target="_blank">https://groups.google.com/forum/#!topic/orthanc-users/BZSbsksrMVA</a></p>

---

## Post #7 by @stevenagl12 (2018-06-06 17:16 UTC)

<p>Is there a way to set up the PACS server with security details such as the username and password for the server?</p>

---

## Post #8 by @pieper (2018-06-06 19:08 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="7" data-topic="1985" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>Is there a way to set up the PACS server with security details such as the username and password for the server?</p>
</blockquote>
</aside>
<p>Not with regular DICOM networking in Slicer.  I don’t think username/passwords are a widely used feature.  More common in DICOMweb, but we don’t support that currently in Slicer.</p>

---

## Post #9 by @lassoan (2018-06-06 20:23 UTC)

<p>Usually you control access by configuring in the PACS what client connections it accepts. You accept a connection if port number, AE title, client’s IP address, host name, etc. are matching. If you are on a different network then probably you can use standard secure network access techniques (VPN, SSH tunneling, etc.).</p>

---
