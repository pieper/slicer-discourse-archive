---
topic_id: 12560
title: "Importing Pacs Anonymised Data Into 3D Slicer"
date: 2020-07-15
url: https://discourse.slicer.org/t/12560
---

# Importing PACs anonymised data into 3D Slicer

**Topic ID**: 12560
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/importing-pacs-anonymised-data-into-3d-slicer/12560

---

## Post #1 by @David_Nahabedian (2020-07-15 17:45 UTC)

<p>Hello slicer community. I am trying to import MRI’s and CT scans from a client into 3D sclicer form a PACs based system. I am familiar with importing DICOM data but this is very new to me. THe PACs system can be viewed in a web browser but i cannot seem to find direction on how to import a PACs based scan into slicer. Pardon me if my jargon isn’t perfect. <a class="mention" href="/u/pieper">@pieper</a> seems to be an authority on this and i would love some guidance on this. I noticed some screenshots and other references by him but I am very new and require a touch more guidance.  I could pull the jpeg sequences out of the PACs but this would be very time consuming and im not sure it would even work…</p>
<p>I have 13 anonymized  patient data sets, from a disk from my client. I can access the PACs and images online…just need to get them into slicer for volumetric rendering. Thank you for your help and time</p>
<p>Operating system: Mac OS Catalina<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2020-07-15 18:06 UTC)

<p>Hi <a class="mention" href="/u/david_nahabedian">@David_Nahabedian</a> -</p>
<p>If you have the dicom files on a disk, then this tutorial should get you going:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_3D_Visualization_of_DICOM_images_for_Radiology_Applications" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_3D_Visualization_of_DICOM_images_for_Radiology_Applications</a></p>
<p>Definitely avoid the jpeg route, as that would be very lossy.  But it’s not clear to my why you need to access the pacs if you have them on disk?</p>
<p>Also you should try the latest nightly builds, since there have been lots of improvements since 4.10.2.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @David_Nahabedian (2020-07-15 18:33 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> i am extremely grateful for your reply and resources. Here’s some more info. I <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b4fd2881d46865dc6e29392b9115a3e1910cad0.jpeg" data-download-href="/uploads/short-url/fjk6HdSwICUqA9JNxQfiif3BeF2.jpeg?dl=1" title="Screen Shot 2020-07-15 at 2.31.26 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b4fd2881d46865dc6e29392b9115a3e1910cad0_2_690x125.jpeg" alt="Screen Shot 2020-07-15 at 2.31.26 PM" data-base62-sha1="fjk6HdSwICUqA9JNxQfiif3BeF2" width="690" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b4fd2881d46865dc6e29392b9115a3e1910cad0_2_690x125.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b4fd2881d46865dc6e29392b9115a3e1910cad0_2_1035x187.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b4fd2881d46865dc6e29392b9115a3e1910cad0_2_1380x250.jpeg 2x" data-dominant-color="F8FAFB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-15 at 2.31.26 PM</span><span class="informations">2832×516 77.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My client has them on a disk but it is all different than what i am used to seeing in regard to normal DICOM data. He is a physician from the uk and his radiology team said this to me:</p>
<p>“We don’t save or send images in the jpeg format as a rule. All images stored in PACS are stored in DICOM format. These studies were anonymised in PACS and sent straight from there to the CD. As well as this our CD burner does not accept any other image format other than DICOM (.dcm).”</p>
<p>but the files have no .dcm extension and can only be viewed in the pacs online server. I attached a picture of the file structure of the information from the disk. Does this give you any insight to my problem? I am exploring the resource you posted now to see if there is a solution there as well. Thank you</p>

---

## Post #4 by @pieper (2020-07-15 19:29 UTC)

<p>Yes, that all looks pretty normal.  Systems have been making this kind of CD for decades so you can find lots of general information about it online in the dicom standard itself or just by searches.  It’s normal that they don’t have .dcm extensions since that is optional.</p>
<p>Probably all you need to do is drop the directory called “IMAGES” onto the slicer app and it should load all your subjects into the database and you can load them from there.</p>

---
