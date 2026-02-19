---
topic_id: 2803
title: "Shift Rt Dose Gamma Comparison With Differents Ct Cbct Isoce"
date: 2018-05-11
url: https://discourse.slicer.org/t/2803
---

# Shift RT dose gamma comparison with differents CT - CBCT isocenter acquisition

**Topic ID**: 2803
**Date**: 2018-05-11
**URL**: https://discourse.slicer.org/t/shift-rt-dose-gamma-comparison-with-differents-ct-cbct-isocenter-acquisition/2803

---

## Post #1 by @Aurelien_Badey (2018-05-11 11:22 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1</p>
<p>Hello,</p>
<p>I have questions about gamma comparison module (slicer 4.8.1), I have a shift between two image series CT and cone beam CT (with different acquisition isocenter). I tried to import online registration from our TPS, but it doesn’t work…is it possible to import registration from ARIA ?</p>
<p>Have you a specific advice for this situation ? How can I do to obtain gamma comparison with right shift ?</p>
<p>I’m trying to realize a manual registration with Transform module, by selecting CT images, RT dose, and RT struct to make my comparison but that’s not really precise. I have always in my opinion a shift between dose matrices (cf. printscreen in attachments)(<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f714a30140b4a3d8e1aef68d75fd2fe49edae2d1.jpeg" data-download-href="/uploads/short-url/zfM9fypLOTXWRkaSvQk5xOlSNEZ.JPG?dl=1" title="Screen%20slicer%20shift%20gamma%20comparison" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f714a30140b4a3d8e1aef68d75fd2fe49edae2d1_2_690x370.JPG" alt="Screen%20slicer%20shift%20gamma%20comparison" data-base62-sha1="zfM9fypLOTXWRkaSvQk5xOlSNEZ" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f714a30140b4a3d8e1aef68d75fd2fe49edae2d1_2_690x370.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f714a30140b4a3d8e1aef68d75fd2fe49edae2d1_2_1035x555.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f714a30140b4a3d8e1aef68d75fd2fe49edae2d1.jpeg 2x" data-dominant-color="8BB391"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen%20slicer%20shift%20gamma%20comparison</span><span class="informations">1361×730 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks a lot for your help,</p>

---

## Post #2 by @gcsharp (2018-05-11 12:55 UTC)

<p>Hi Aurelien,</p>
<p>If you can’t import the registration object, you can create it manually.  In Transforms module, there is a combo box labeled “Active Transform”.  Choose “Create new LinearTransform”, type in your shifts, and then in the “Apply transform” section, choose the dose volume you wish to transform.</p>
<p>One detail that I can’t remember: you might need to click “Harden Transform” before running Gamma.  But I would try without first.</p>
<p>DICOM (linear) registration import is supposed to work, I’m surprised that it doesn’t.  If you could please send log details of import failure or anonymize and provide the example SRO file it is appreciated.</p>
<p>Greg</p>

---

## Post #3 by @Aurelien_Badey (2018-05-18 14:50 UTC)

<p>Hello,</p>
<p>thanks for your return, you’ll find in attachments compressed files with CT-CBCT images (with RP, RD, RS DICOM object) and registration in DICOM format.</p>
<p>Thanks for your help ++</p>
<p>Aurélien BADEY​​</p>

---

## Post #4 by @gcsharp (2018-05-18 21:43 UTC)

<p>Hi Aurelien,<br>
I didn’t get any attachment.  Is it possible to share a download link (dropbox, box, google, onedrive, etc.)?<br>
Greg</p>

---

## Post #5 by @Aurelien_Badey (2018-05-22 11:40 UTC)

<p>Greg,</p>
<p>I send you an email from Dropbox, tell me if it’s ok for you.</p>
<p>Aurélien</p>

---

## Post #6 by @Aurelien_Badey (2018-05-29 09:22 UTC)

<p>Hi Greg,</p>
<p>could you download data transferred from dropbox (CT CBCT images) ?</p>
<p>Regards,</p>
<p>Aurélien</p>

---

## Post #7 by @gcsharp (2018-05-29 14:20 UTC)

<p>Hi Aurelien,</p>
<p>Sorry, I didn’t receive any e-mail.  If you don’t want to post a link in the forum, you can e-mail to <a href="mailto:gcsharp@partners.org">gcsharp@partners.org</a>.</p>
<p>Greg</p>

---

## Post #8 by @gcsharp (2018-05-30 20:20 UTC)

<p>Hi Aurelien,</p>
<p>Thank you, I could download the data.</p>
<p>My initial finding is that the registration maps from two frames of reference (UID = 1.2.246.352.62.3.5468625514681278990.7951560648237656234 and UID = 1.3.6.1.4.1.5962.99.1.2407451348.214665615.1522825906900.5.0), but the CT images have frame of reference (UID = 1.2.246.352.62.3.4782682682985951499.3939753861484204422 and UID =<br>
1.3.6.1.4.1.5962.99.1.2407451348.214665615.1522825906900.5.0).</p>
<p>Notice that they are a little different.</p>
<p>Also, the Referenced SOP Instance UIDs in the Registration object do not match the UIDs in the CT.</p>
<p>Based on this, my conclusion is that you somehow have the wrong Registration object, or maybe there are two Registration objects composed in sequence.</p>
<p>Greg</p>

---
