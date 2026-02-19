---
topic_id: 1109
title: "How To Open Telemed Ultrasound Images With Vol Format"
date: 2017-09-24
url: https://discourse.slicer.org/t/1109
---

# How to open Telemed Ultrasound images with .vol format

**Topic ID**: 1109
**Date**: 2017-09-24
**URL**: https://discourse.slicer.org/t/how-to-open-telemed-ultrasound-images-with-vol-format/1109

---

## Post #1 by @Fatemeh_Salehi (2017-09-24 09:49 UTC)

<p>hello<br>
I have a telemed system that its output is .vol and i need to convert these images.<br>
when i drag and drop  my file and click Ok to loading nothing happens.<br>
if somebody had this problem i would be thankful if help me to solve it.</p>
<p>I have uploaded an example of our 3D imagesRegards<br>
<a href="https://drive.google.com/file/d/0B2z7D55qZUFQTUQ0UlVPQldReFk/view?usp=sharingRegards" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/file/d/0B2z7D55qZUFQTUQ0UlVPQldReFk/view?usp=sharingRegards</a></p>

---

## Post #2 by @lassoan (2017-09-24 15:02 UTC)

<p>Unfortunately, this .vol file contains data compressed with an unknown algorithm. Can you save data as DICOM or some other format or get specification of the file format from the manufacturer?</p>

---

## Post #3 by @Fatemeh_Salehi (2017-10-08 09:13 UTC)

<p>hello dear Lassoan<br>
unfortunately we can save just with this format… do you know about converter for example .vol to DICOME?</p>

---

## Post #4 by @lassoan (2017-10-08 13:09 UTC)

<p>I think only Telemed can help you to convert your existing 3D files.</p>
<p>If attaching an external tracker (such as a webcam that track 2D barcodes that you print and attach to the probe) is acceptable then you can use Plus toolkit (<a href="http://www.plustoolkit.org">www.plustoolkit.org</a>) and SlicerIGT extension to show live images in Slicer and reconstruct 3D ultrasound volumes from freehand sweeps. See more information at <a href="http://www.slicerigt.org">www.slicerigt.org</a>.</p>

---

## Post #5 by @Fatemeh_Salehi (2017-11-14 08:08 UTC)

<p>Hello<br>
We tied fcal but we have problem with transfer calibration in slicer, any way i really need 3d ultrasound of liver…Do you have some sample size?<br>
I have some 3d ultrasound data (not liver) of GE system…but i couldn’t open them too…would you please help me?This is on of this images:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/j514jx0q9kpm1u0/gyn_polycystic_ovary.vol?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/j514jx0q9kpm1u0/gyn_polycystic_ovary.vol?dl=0" target="_blank" rel="nofollow noopener">gyn_polycystic_ovary.vol</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
