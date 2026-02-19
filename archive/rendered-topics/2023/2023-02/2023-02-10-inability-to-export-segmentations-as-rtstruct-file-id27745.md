---
topic_id: 27745
title: "Inability To Export Segmentations As Rtstruct File"
date: 2023-02-10
url: https://discourse.slicer.org/t/27745
---

# Inability to export segmentations as RTStruct File

**Topic ID**: 27745
**Date**: 2023-02-10
**URL**: https://discourse.slicer.org/t/inability-to-export-segmentations-as-rtstruct-file/27745

---

## Post #1 by @KSC_IA (2023-02-10 15:07 UTC)

<p>Slicer Version: 5.2.1 (Stable Release)<br>
OS: MacOS Big Sur 11.7.3 (Intel i7)<br>
Expected Behaviour: ‘Export as DICOM’ in Export Data converts scene to DICOM files and segmentations to RT Structure file<br>
Actual Behaviour: DICOM files are created but RT structure file is not created</p>
<p>Hello.</p>
<p>I am a radiation oncologist and just beginning to explore 3DSlicer for integration into our research workflow.</p>
<p>I saw the video by Dr <a class="mention" href="/u/lassoan">@lassoan</a> on exporting segmentations to DICOM and RT Structure files (<a href="https://youtu.be/nzWf4xHy1BM" class="inline-onebox" rel="noopener nofollow ugc">Create DICOM files from CT volume and segmentation - YouTube</a>). I have the SlicerRT and QuantitativeReporting modules installed as well. Following along the video step-by-step, unfortunately after hitting ‘Export’, the output folder contains the DICOM files, but not the RT Structure File.</p>
<p>Before posting here, I scanned through all posts related to this topic, but most dealt with problems with RT Structure files, rather than the process of exporting it. At present, I am performing a clean install of Slicer, using the nightly release (v5.3.0) and also attempting to recreate the problem on a Windows machine. [Update: Tried this step, but no luck. DICOM files are still exporting, but no RT Structure file.]</p>
<p>I am also aware that as a format, RT Structure, is considered a legacy format. But its a core component of Radiation Oncology workflows.</p>
<p>Thank you for your help in advance.</p>

---

## Post #3 by @cpinter (2023-02-13 12:10 UTC)

<p>Can you please make a screenshot of your Data module (Subject hierarchy tab) before starting DICOM export?</p>

---

## Post #4 by @KSC_IA (2023-02-17 06:48 UTC)

<p>Thank you for your reply &amp; apologies for my delayed response.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ea4ab0bfe70a82be265b31b17113a0e68840fae.jpeg" data-download-href="/uploads/short-url/25xu2jNFciceMlY3Z63d64RKaxE.jpeg?dl=1" title="Screenshot 2023-02-17 at 12.13.26 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ea4ab0bfe70a82be265b31b17113a0e68840fae_2_690x346.jpeg" alt="Screenshot 2023-02-17 at 12.13.26 PM" data-base62-sha1="25xu2jNFciceMlY3Z63d64RKaxE" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ea4ab0bfe70a82be265b31b17113a0e68840fae_2_690x346.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ea4ab0bfe70a82be265b31b17113a0e68840fae_2_1035x519.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ea4ab0bfe70a82be265b31b17113a0e68840fae.jpeg 2x" data-dominant-color="3F3E3C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-02-17 at 12.13.26 PM</span><span class="informations">1365×685 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is the subject hierarchy screen</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27097cb47c9e87b179e7dcddeb6bd8d8b69c9c7b.png" data-download-href="/uploads/short-url/5zkWJUxE2iJ2yMMjMdBUF1iMvpN.png?dl=1" title="Screenshot 2023-02-17 at 12.14.13 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27097cb47c9e87b179e7dcddeb6bd8d8b69c9c7b_2_690x344.png" alt="Screenshot 2023-02-17 at 12.14.13 PM" data-base62-sha1="5zkWJUxE2iJ2yMMjMdBUF1iMvpN" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27097cb47c9e87b179e7dcddeb6bd8d8b69c9c7b_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27097cb47c9e87b179e7dcddeb6bd8d8b69c9c7b_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27097cb47c9e87b179e7dcddeb6bd8d8b69c9c7b.png 2x" data-dominant-color="323232"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-02-17 at 12.14.13 PM</span><span class="informations">1364×681 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Here is the export selection screen after I have selected ‘Export to DICOM’</p>
<p>Am I doing something wrong?</p>

---

## Post #5 by @KSC_IA (2023-02-18 07:33 UTC)

<p>I can also confirm that this is not an issue on Windows-based systems. The RT structure file is created as expected.</p>

---

## Post #6 by @cpinter (2023-02-19 12:27 UTC)

<p>Please attach the log after export fails on Mac. Maybe it contains some pointers.</p>

---

## Post #7 by @KSC_IA (2023-02-20 07:36 UTC)

<p>Thank you for your reply <a class="mention" href="/u/cpinter">@cpinter</a>. I’m not sure when you say ‘log file’. I actually don’t get an ‘export failed’ message. The DICOM files are generated successfully, but the RT structure file is not!</p>

---

## Post #8 by @cpinter (2023-02-20 14:45 UTC)

<p>You can find the log in <code>View / Error Log</code> or <code>Help / Report a Bug</code>. Basic information such as what is the log file can be found easily in the forum or the <a href="https://slicer.readthedocs.io/en/latest/index.html">Slicer documentation</a>, so I encourage consulting these material for help.</p>

---

## Post #9 by @KSC_IA (2023-02-23 04:38 UTC)

<p>Thank you for your suggestion <a class="mention" href="/u/cpinter">@cpinter</a>. I did as you suggested and discovered that I need  to save all my data into an MRML scene first, quit the scene and then reload the MRML scene. Then after exporting as RT structure set, it creates an RT_Struct file.<br>
My next task will be check the compatibility of these RT_Struct files with our manufacturers’ Treatment Planning Software (TPS).<br>
Thank you for all your responses.</p>

---

## Post #10 by @KSC_IA (2023-02-23 11:18 UTC)

<p>I can also confirm that the RT_Struct file from Slicer imports perfectly into Varian Eclipse TPS.</p>
<p>Will add to this list in the future.</p>

---

## Post #11 by @cpinter (2023-02-24 15:16 UTC)

<p>I think it would be much better to fix this issue rather than do the save/load workaround. Can you please help with this by sharing the error log that you get after a failed export attempt?</p>

---

## Post #12 by @KSC_IA (2023-02-25 04:22 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f15f555b6fba71c1f68fc1ef8b92e67cc519757f.png" data-download-href="/uploads/short-url/yrhjV5ms1x9rinWoPMOe517ukLJ.png?dl=1" title="Error Log for Export as RT_Struct" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15f555b6fba71c1f68fc1ef8b92e67cc519757f_2_690x181.png" alt="Error Log for Export as RT_Struct" data-base62-sha1="yrhjV5ms1x9rinWoPMOe517ukLJ" width="690" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15f555b6fba71c1f68fc1ef8b92e67cc519757f_2_690x181.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f15f555b6fba71c1f68fc1ef8b92e67cc519757f_2_1035x271.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f15f555b6fba71c1f68fc1ef8b92e67cc519757f.png 2x" data-dominant-color="2F2F2F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error Log for Export as RT_Struct</span><span class="informations">1247×328 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The last step in this sequence was when I switched to the Data Module and rearranged the hierarchy as demonstrated in your video. Upon hitting export, nothing gets logged and I got only DICOM files (no RT_Struct file).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad5f51e855a0a8948a59d60f959b7b277b3c7d70.png" data-download-href="/uploads/short-url/oJIP79xkbx6jEQBVrrCV2KI3lOo.png?dl=1" title="Screenshot 2023-02-25 at 9.49.18 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad5f51e855a0a8948a59d60f959b7b277b3c7d70_2_690x198.png" alt="Screenshot 2023-02-25 at 9.49.18 AM" data-base62-sha1="oJIP79xkbx6jEQBVrrCV2KI3lOo" width="690" height="198" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad5f51e855a0a8948a59d60f959b7b277b3c7d70_2_690x198.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad5f51e855a0a8948a59d60f959b7b277b3c7d70_2_1035x297.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad5f51e855a0a8948a59d60f959b7b277b3c7d70.png 2x" data-dominant-color="363636"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-02-25 at 9.49.18 AM</span><span class="informations">1247×358 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I then closed the previous scene. I next loaded a scene, which I had already worked upon, and repeated the export procedure and it behaved as expected.</p>

---

## Post #13 by @cpinter (2023-02-28 09:49 UTC)

<p>I find it very strange that there is no error or warning in the log. Do you have access to a Windows or Linux machine to try the same thing? To see if it’s OS specific or not. Also is there any special data involved? Can you reproduce it with data from the Sample Data module? Thanks!</p>

---

## Post #14 by @KSC_IA (2023-03-01 03:52 UTC)

<p>It does appear to be OS Specific. I tried the same steps on Windows, with no issues whatsoever.<br>
All of the above was performed on the datasets from the sample data module. No special data was used.<br>
Thank you for you help <a class="mention" href="/u/cpinter">@cpinter</a>!</p>

---
