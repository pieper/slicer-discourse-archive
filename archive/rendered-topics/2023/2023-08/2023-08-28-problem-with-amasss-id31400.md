---
topic_id: 31400
title: "Problem With Amasss"
date: 2023-08-28
url: https://discourse.slicer.org/t/31400
---

# Problem with AMASSS

**Topic ID**: 31400
**Date**: 2023-08-28
**URL**: https://discourse.slicer.org/t/problem-with-amasss/31400

---

## Post #1 by @user2828 (2023-08-28 10:28 UTC)

<p>Hi everyone,</p>
<p>I am trying to use the AMASSS (part of Automated dental tools extension) and every time I try to run the segmentation the program is freezing. I am trying to segment a CBCT file saves as a GIPL file. At the bottom of the one section, it lists the time it takes to run but no matter what I try it always freezes and won’t continue. I was wondering if anyone is experiencing this issue or knows how to combat it. I don’t have too much experience using this program! Thank you in advance</p>

---

## Post #2 by @YOU_DDS (2023-08-28 11:40 UTC)

<p>Hello,</p>
<p>I have try using it for a few weeks ago. I do not have much experience in using it as well. However, it work as normal for my case but it take very long time to run and complete the process. It took me around 2 hours to run the segmentation. To be clear, could you share how you do it by screenshot your working tab. so that I might have suggest what I have done.</p>

---

## Post #3 by @user2828 (2023-08-28 12:27 UTC)

<p>Hello,</p>
<p>I am using the newest slicer version: 5.4.0 (I’ve also tried some of the slightly older ones as well).</p>
<p>I load my CBCT scan as a .gpl file.</p>
<p>Click on modules → AMASSS<br>
The node is selected as the scan I uploaded<br>
Model’s Folder: I clicked on “download latest models” and after those are downloaded I place them into one folder and upload that for the model’s folder section</p>
<p>I am running segmentation on the Maxilla, Mandible, and cranial base and select them in the options.</p>
<p>I click select “separated + merged” for generated files<br>
-click check box for “generate surface file”<br>
-I have been keeping my GPU usage set to 1 and I don’t touch any other setting<br>
-then i click “run prediction”</p>
<p>the time at the bottom left will run and then reach a certain point and stop.<br>
I notice usually the first bar “scans ready for segmentation 0/1” gets 100% completed by my computer freezes before any segmentations are done.</p>
<p>I am using a MacBook Pro 2020, running on MacOS Monterey</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6deb2b148c82f802cd74ae472ffb3245abc972a.jpeg" data-download-href="/uploads/short-url/wWmWGmMEpy68SFATyB9u9yThGQ2.jpeg?dl=1" title="Screen Shot 2023-08-28 at 8.26.21 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6deb2b148c82f802cd74ae472ffb3245abc972a_2_690x396.jpeg" alt="Screen Shot 2023-08-28 at 8.26.21 AM" data-base62-sha1="wWmWGmMEpy68SFATyB9u9yThGQ2" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6deb2b148c82f802cd74ae472ffb3245abc972a_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6deb2b148c82f802cd74ae472ffb3245abc972a_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6deb2b148c82f802cd74ae472ffb3245abc972a_2_1380x792.jpeg 2x" data-dominant-color="404248"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-08-28 at 8.26.21 AM</span><span class="informations">1920×1103 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In this case if you see the bottom left: Time is stuck at 75.01 seconds. I’ve tried to leave the program on for awhile but i never see it advance. If you have any tips/tricks on what you do differently I’d really appreciate any help!</p>

---

## Post #4 by @YOU_DDS (2023-08-29 01:40 UTC)

<p>Hello Jess,</p>
<p>Ah Did you set the direction of where to save the file? For my case the segmentation does not appear in slicer but it was save in the directory location that I intended to save it. After the time keep running and stop since the process was already finished. The file will automatically save in the directory file you choose. And you can drag and drop it in slicer to see whether it is the segmentation you want or not.</p>
<p>I actually face the same problem when I first started it.</p>

---

## Post #5 by @user2828 (2023-08-29 01:53 UTC)

<p>Hi Thank you for getting back to me. I have checked and I do see the new folder created in the directory after I hit “run prediction” but no file is loaded in the file. I will try to keep the program running overnight tonight to see if there is a change. Did you notice that the file would appear in that folder even if the Slicer program appeared to be frozen?</p>
<p>Thank you for your help! I am hoping that I can get AMASSS to work for me</p>

---

## Post #6 by @YOU_DDS (2023-08-29 02:11 UTC)

<p>After the the process complete, the file will be there in that file. I think you did the right process. I am sure it will work. and after many try and error you will understand how it work.</p>

---

## Post #7 by @user2828 (2023-08-29 11:48 UTC)

<p>I tried again but didn’t see the file but I will keep trying different settings. Thank you for all of your help! Could I ask if you are using a desktop computer or laptop? I’m not sure if that matters or not</p>

---

## Post #8 by @YOU_DDS (2023-08-29 11:59 UTC)

<p>Oh I am using MSI laptop. I also experience a few time of the program not running well because I am trying to run the DICOM file, But after that it work as normal. Follow the video tutorial and give yourself time. Keep trying after a ew trial you will figure it out.</p>
<p>But for me the AMASSS is not that accurate compare to normal segments. May I know what you intended to do with that segmentation?</p>

---

## Post #9 by @YOU_DDS (2023-08-29 12:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df9a74338ec980d3b8044a62fe103a2d9df7f54.jpeg" data-download-href="/uploads/short-url/1ZD5ooTsVSLVJDACB1Y53Ybc7li.jpeg?dl=1" title="IMG_2073" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df9a74338ec980d3b8044a62fe103a2d9df7f54_2_690x396.jpeg" alt="IMG_2073" data-base62-sha1="1ZD5ooTsVSLVJDACB1Y53Ybc7li" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df9a74338ec980d3b8044a62fe103a2d9df7f54_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df9a74338ec980d3b8044a62fe103a2d9df7f54_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0df9a74338ec980d3b8044a62fe103a2d9df7f54_2_1380x792.jpeg 2x" data-dominant-color="484A4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_2073</span><span class="informations">1920×1103 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Base on my experiences if the 2 points that I circled keep running until it reach 100% and all the 3/3 segments are showing. Then the “Cancel prediction” turn into “complete” (I forget what word will appear). The the segmentation you want will appear in the directory location you want it to be stored.</p>

---

## Post #10 by @user2828 (2023-08-29 12:26 UTC)

<p>Ok thank you for your insights!</p>

---

## Post #11 by @Alexander_Suchanek (2023-12-12 11:51 UTC)

<p>Hello, did you solve your problem? I’m having exactly same issue. I tried different kinds of versions but all of them get me quite similar results which is stopping time after completing bar with scans ready for segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56a11b2bb14cc494a564cbf35cfe17d30503563.png" data-download-href="/uploads/short-url/pSRFNHTGbpl8HCcXigHiaGJ1h4v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56a11b2bb14cc494a564cbf35cfe17d30503563.png" alt="image" data-base62-sha1="pSRFNHTGbpl8HCcXigHiaGJ1h4v" width="335" height="500" data-dominant-color="EFF3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">574×855 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @user2828 (2023-12-13 11:39 UTC)

<p>No unfortunately I never got it to work for me. I’m still trouble shooting.</p>

---

## Post #13 by @Esteban_Barreiro (2025-01-11 13:35 UTC)

<p>Hi! AMASS module works fine if you save the 3dslicer scene before you run the module, and use the folder where you save it (it will contain the .nrrd file now) with NRRD Input Modality, selecting that folder you create  as Directory.</p>

---
