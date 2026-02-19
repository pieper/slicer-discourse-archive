---
topic_id: 36740
title: "Open Dcm File Fail"
date: 2024-06-13
url: https://discourse.slicer.org/t/36740
---

# Open .dcm file fail

**Topic ID**: 36740
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/open-dcm-file-fail/36740

---

## Post #1 by @lili-yu22 (2024-06-13 01:25 UTC)

<p>when I drag a .dcm file,the image is nomal at x axis，but longer at y and z axis<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abbae8cdd4db99441fdae4a70926fc6f67864064.jpeg" data-download-href="/uploads/short-url/ovc68rdPb1qHtDhmnZOKEiUMw4I.jpeg?dl=1" title="IMG_20240613_092318" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbae8cdd4db99441fdae4a70926fc6f67864064_2_666x500.jpeg" alt="IMG_20240613_092318" data-base62-sha1="ovc68rdPb1qHtDhmnZOKEiUMw4I" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbae8cdd4db99441fdae4a70926fc6f67864064_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbae8cdd4db99441fdae4a70926fc6f67864064_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbae8cdd4db99441fdae4a70926fc6f67864064_2_1332x1000.jpeg 2x" data-dominant-color="8B878F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20240613_092318</span><span class="informations">1920×1440 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
can you help me</p>

---

## Post #2 by @lili-yu22 (2024-06-13 02:18 UTC)

<p>please help me ，online waiting urgently</p>

---

## Post #3 by @muratmaga (2024-06-13 04:56 UTC)

<p>Try importing your dcm via the DICOM module. Do not drag and drop.<br>
M</p>

---

## Post #4 by @lili-yu22 (2024-06-14 01:26 UTC)

<p>thank you for your reply.but When I follow your instructions，i can’t found my dcm file.my dcm file are as show in the figure.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ab169b59a20cf7a380c0e15504256971b626aa6.jpeg" data-download-href="/uploads/short-url/1wASzhWS2rcoNAckuyFEOVbqFIq.jpeg?dl=1" title="IMG_20240614_091827" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ab169b59a20cf7a380c0e15504256971b626aa6_2_375x500.jpeg" alt="IMG_20240614_091827" data-base62-sha1="1wASzhWS2rcoNAckuyFEOVbqFIq" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ab169b59a20cf7a380c0e15504256971b626aa6_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ab169b59a20cf7a380c0e15504256971b626aa6_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ab169b59a20cf7a380c0e15504256971b626aa6_2_750x1000.jpeg 2x" data-dominant-color="A49FA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20240614_091827</span><span class="informations">1920×2560 764 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2024-06-14 17:22 UTC)

<p>You mean you can’t navigate to this folder and see it is contents in DICOM module?</p>

---

## Post #6 by @lili-yu22 (2024-06-14 23:48 UTC)

<p>thank you very much .when i navigate to this folder"sample"there is nothing，but this folder contain these dcm,I don’t know why</p>

---

## Post #7 by @muratmaga (2024-06-15 01:43 UTC)

<p>It might be related to an issue with chinese characters. What is the version of Slicer you are using?</p>

---

## Post #8 by @lili-yu22 (2024-06-15 01:51 UTC)

<p>I tried to change the Chinese character but when open the folder， no dcm file. i use version5.6.2</p>

---

## Post #9 by @muratmaga (2024-06-15 01:54 UTC)

<p>Is this a folder synced to a cloud provider (dropbox, onedrive, google drive etc). If so try copying the contents to an another folder and retry the dicom module. Otherwise I am not sure what might be issue.</p>

---
