---
topic_id: 899
title: "Dwi Convent Errors"
date: 2017-08-19
url: https://discourse.slicer.org/t/899
---

# DWI convent errors

**Topic ID**: 899
**Date**: 2017-08-19
**URL**: https://discourse.slicer.org/t/dwi-convent-errors/899

---

## Post #1 by @Jin (2017-08-19 04:31 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.7.0<br>
Expected behavior: DTI datas convent<br>
Actual behavior: errors<br>
Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>The errors was described as follows:<br>
Can’t get vendor name from DICOM file<br>
itk::ExceptionObject (0000009DB1F4A828)<br>
Location: "unknown"<br>
File: C:\D\N\Slicer-0-build\ITKv4\Modules\IO\DCMTK\src\itkDCMTKFileReader.cxx<br>
Line: 464<br>
Description: itk::ERROR: Cant find tag 8 70</p>

---

## Post #2 by @ljod (2017-08-22 17:42 UTC)

<p>Hi it looks like there is an issue with your DWI dataset. Are you able to load this dataset as regular DICOM into Slicer or any other program? Is it definitely a DWI dataset?</p>

---

## Post #3 by @Jin (2017-08-24 12:38 UTC)

<p>Thank you very much! The dataset got from the PACS system in my hospital! But I download this dataset from the department computer. I’m sure its a DWI dataset, maybe some information loss during the download?</p>

---

## Post #4 by @ljod (2017-08-24 13:05 UTC)

<p>There could be a download issue. I recommend testing if the DICOM is ok to load in Slicer or any other program, in order to see if it is valid DICOM. Then take a look at the data to see if it’s DWI (it should have multiple DWI images at each location in the brain, that look different due to different diffusion-sensitizing gradients that were applied). Also the size of the DWI file (or directory if several files) should be larger than the file size of other images you have like T1 or T2 (at least 7 times larger due to at least 6 diffusion-encoding gradients).</p>
<p>Also you should report the very first error encountered by Slicer during DWIConvert. Please check if the reported error was the first error.</p>

---

## Post #5 by @cecile_Muller (2017-08-24 13:24 UTC)

<p>Hello! I had the very same issues. You can’t download from any computer of the hospital. The PACS or the other system you use in your hospital to archive and visualize the dataset compress datas like the b-values you need from DWI dataset to use it properly in Slicer . You have to download it from the MRI itself. No other solution, trust me I tried very long;)))</p>

---

## Post #6 by @cecile_Muller (2017-08-24 13:28 UTC)

<p>Moreover, if your data are too old, and have been suppressed from the MRI console, you can push it again from the server ( here we have AW Server from General Electrics) on the MRI console and then download it ….</p>

---

## Post #7 by @Jin (2017-08-24 14:31 UTC)

<p>thank you very much! I will try the next time. In our hospital, the server or workstation, can’t remain the original dataset for long.</p>

---

## Post #8 by @Jin (2017-08-24 14:39 UTC)

<p>Thank you so much! The DTI dataset contain 1 DWI b-values=0 and 25 different diffusion-sensitizing gradients, the file size is about 130K. It’s small than other MRI sequence, so I think the dataset should be compressed.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4396bfc2b3fd9784f67ec74d242ba791223d8d53.jpeg" data-download-href="/uploads/short-url/9DUY4snKbH9LZqPhWHpIzzgsUcb.JPG?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4396bfc2b3fd9784f67ec74d242ba791223d8d53_2_461x500.JPG" alt="捕获" data-base62-sha1="9DUY4snKbH9LZqPhWHpIzzgsUcb" width="461" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/4396bfc2b3fd9784f67ec74d242ba791223d8d53_2_461x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4396bfc2b3fd9784f67ec74d242ba791223d8d53.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/4396bfc2b3fd9784f67ec74d242ba791223d8d53.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">690×747 69.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @cecile_Muller (2017-08-24 14:55 UTC)

<p>Sorry, in fact, you push it from the pacs on the server, then re-push it on the MRI console, and then download it. Pretty much complicated, so either you download from the console as soon as the MRI has been performed, either you have to do that each time. PACS is not research-friendly;)<br>
Be carefull all the images has been pushed each time, some time you have to do it manually 100 by 100 images…otherwise won’t work either;)</p>
<p>Cecile Muller</p>

---

## Post #10 by @Jin (2017-08-24 15:02 UTC)

<p>Thanks a lot, I will try the next time, and tell you  if the issue is settled.</p>

---
