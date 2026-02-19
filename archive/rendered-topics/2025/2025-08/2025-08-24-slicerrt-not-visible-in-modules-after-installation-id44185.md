---
topic_id: 44185
title: "Slicerrt Not Visible In Modules After Installation"
date: 2025-08-24
url: https://discourse.slicer.org/t/44185
---

# SlicerRT not visible in modules after installation

**Topic ID**: 44185
**Date**: 2025-08-24
**URL**: https://discourse.slicer.org/t/slicerrt-not-visible-in-modules-after-installation/44185

---

## Post #1 by @Mahrukh_Tariq (2025-08-24 01:20 UTC)

<p>Hi. Can you please help to resolve the issue I‘m facing with SlicerRT extension not being visible in the Modules even after it has been installed and visible in Extensions Manager.</p>
<p>3D Slicer version 5.8.1</p>

---

## Post #2 by @cpinter (2025-08-25 09:31 UTC)

<p>First of all, I suggest uninstalling the extension and installing it again. If you still experience the problem, please give us more information: your operating system, the error log, anything else that comes to mind.</p>

---

## Post #3 by @Mahrukh_Tariq (2025-08-26 16:04 UTC)

<p>Thank you.</p>
<p>I uninstalled and then installed the extension, but it is still not showing up in the modules.</p>
<p>Operating System: Windows 10</p>
<p>Slicer version: 5.8.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d55c2eb315f39541ddc488b53a9dc1b45709eca.png" data-download-href="/uploads/short-url/kaj46OjdFVEaVZqxyV4V9cLH9s6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d55c2eb315f39541ddc488b53a9dc1b45709eca.png" alt="image" data-base62-sha1="kaj46OjdFVEaVZqxyV4V9cLH9s6" width="377" height="500" data-dominant-color="E5E8EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">557×738 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2025-08-27 10:35 UTC)

<p>Thanks! The module directories are included, there is no error about DLL loading… I don’t see any issues. I don’t know if it could be a problem that you use Windows 10, but it works on Windows 11.</p>
<p>A very basic question but sometimes people miss things: Is there a Radiotherapy category in the module list? Can you make me a screenshot of the module list? Also, if you import an RT structure set in the DICOM database and load it, does the segmentation show up in the views?</p>

---

## Post #5 by @cpinter (2025-08-27 10:39 UTC)

<p>I see one potential issue. From your log it seems that you installed the extension in that session. You need to restart Slicer to see it.</p>

---

## Post #6 by @cpinter (2025-08-27 10:40 UTC)

<p>It works for me on Windows 11 and Slicer 5.8.1 (fresh install):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46e9d6fbcdca875f024d9426bfabeb60538bc541.png" data-download-href="/uploads/short-url/a7kqbvzjr1o8PSI1z7nqvvBhrd7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46e9d6fbcdca875f024d9426bfabeb60538bc541_2_416x500.png" alt="image" data-base62-sha1="a7kqbvzjr1o8PSI1z7nqvvBhrd7" width="416" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46e9d6fbcdca875f024d9426bfabeb60538bc541_2_416x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46e9d6fbcdca875f024d9426bfabeb60538bc541_2_624x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46e9d6fbcdca875f024d9426bfabeb60538bc541.png 2x" data-dominant-color="C3C3C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">632×759 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2025-08-29 17:18 UTC)

<p>Do you use any third-party antivirus? It may be an issue with the antivirus software putting into quarantine all files that are downloaded from the internet. You can verify this by opening <code>"C:\ProgramData\slicer.org\Slicer 5.8.1\slicer.org\Extensions-33241\SlicerRT\lib\Slicer-5.8\cli-modules"</code> folder and check if you see .dll and .exe files there. You can also open your antivirus software and if you see Slicer extension files in quarantine then mark them as safe.</p>

---

## Post #8 by @lassoan (2025-08-29 17:22 UTC)

<p>I’ve also noticed that your application installation path is unusual. It should be installed in your user folder (something like <code>c:\Users\yourusername\AppData\Local\slicer.org\Slicer 5.8.1\bin</code>) and not the shared <code>ProgramData</code> folder (<code>C:\ProgramData\slicer.org\Slicer 5.8.1\bin</code>). Do you have write access in the <code>C:\ProgramData\slicer.org\Slicer 5.8.1</code> folder? Does everything work well if you install Slicer in the location that the installer offers by default (in your user folder)?</p>

---

## Post #9 by @Mahrukh_Tariq (2025-08-30 02:51 UTC)

<p>Thanks a lot! I wasn’t looking at the Radiotherapy category in the first place (thinking the module would be named as the extension), as this is my first time using Slicer. Now, I got it!</p>

---

## Post #10 by @Mahrukh_Tariq (2025-08-30 03:00 UTC)

<p>There is no antivirus. I have write access to both but Slicer by default offered to be installed in the <code>ProgramData. </code></p>
<p>The issue has now been resolved. Thanks!</p>

---

## Post #11 by @cpinter (2025-09-01 08:51 UTC)

<p>OK great, the important part is that now you have it! SlicerRT is one of the largest extensions with more than a dozen modules, and some of them are not even listed. For example when you import DICOM-RT data to the DICOM database, then a hidden module gets activated that examines and loads the data (also can export).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I wanted to check the documentation but the Documentation link from <a href="http://slicerrt.org">slicerrt.org</a> leads to a 502 error. I can (and will) simply update the link, but we should really move the SlicerRT documentation out from the old Slicer wiki. Do you have a suggestion where? We have some capacity to work on this. Thanks!</p>
<p>Update: Wow, now the same link works… Anyway, the question remains valid <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @Mahrukh_Tariq (2025-09-01 15:25 UTC)

<p>Thank you for guiding! I’ll make sure about this and will ask if there’s any issue!</p>

---
